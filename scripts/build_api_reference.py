"""Generate docs/integrations/developer-api/reference.md from the API contract.

Reads developer-api-worker/src/openapi.json and writes one Markdown page with
every endpoint grouped by tag: method and path, permission, parameters,
request body fields, response fields and a curl example. Run it before the
docs build so the reference always matches the contract the Worker serves.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = ROOT / "developer-api-worker" / "src" / "openapi.json"
OUT = ROOT / "docs-site" / "docs" / "integrations" / "developer-api" / "reference.md"

PERMISSION_LABEL = {
    "visibility:read": "Read visibility data (every key)",
    "tracking:write": "Manage tracking",
    "runs:execute": "Start runs",
}

PLACEHOLDERS = {
    "projectId": "PROJECT_ID",
    "promptId": "PROMPT_ID",
    "answerId": "ANSWER_ID",
    "requestId": "REQUEST_ID",
    "webhookId": "WEBHOOK_ID",
}


def load_spec() -> dict:
    return json.loads(SPEC.read_text(encoding="utf-8"))


class Ref:
    def __init__(self, spec: dict):
        self.spec = spec

    def resolve(self, node):
        seen = 0
        while isinstance(node, dict) and "$ref" in node and seen < 10:
            parts = node["$ref"].lstrip("#/").split("/")
            target = self.spec
            for part in parts:
                target = target[part]
            node = target
            seen += 1
        return node


def type_label(schema: dict, ref: Ref) -> str:
    schema = ref.resolve(schema)
    if "allOf" in schema:
        return "object"
    if "oneOf" in schema or "anyOf" in schema:
        options = schema.get("oneOf") or schema.get("anyOf")
        return " or ".join(type_label(o, ref) for o in options)
    t = schema.get("type")
    if isinstance(t, list):
        nullable = "null" in t
        base = [x for x in t if x != "null"]
        label = base[0] if base else "any"
    else:
        nullable = False
        label = t or ("object" if "properties" in schema else "any")
    if label == "array":
        items = schema.get("items", {})
        label = f"array of {type_label(items, ref)}"
    if schema.get("format") in ("date-time",):
        label = "string (RFC 3339 time)"
    elif schema.get("format") == "date":
        label = "string (YYYY-MM-DD)"
    elif schema.get("format") == "uri":
        label = "string (URL)"
    if schema.get("enum"):
        values = [v for v in schema["enum"] if v is not None]
        label += ": " + ", ".join(f"`{v}`" for v in values)
    if nullable:
        label += ", or null"
    return label


def merged_properties(schema: dict, ref: Ref) -> tuple[dict, set]:
    """Flatten allOf into one property map and required set."""
    schema = ref.resolve(schema)
    props: dict = {}
    required: set = set()
    if "allOf" in schema:
        for part in schema["allOf"]:
            p, r = merged_properties(part, ref)
            props.update(p)
            required |= r
        return props, required
    props.update(schema.get("properties", {}))
    required |= set(schema.get("required", []))
    return props, required


def clean(text: str | None) -> str:
    if not text:
        return ""
    return " ".join(text.strip().split()).replace("|", "\\|")


DEFAULT_DESC = {
    "data": "The rows on this page.",
    "from": "The first day included, UTC.",
    "to": "The last day included, UTC.",
    "deleted": "True when the item was removed.",
    "host": "The project's host computer.",
    "nextCursor": "Pass it back as cursor for the next page. Null on the last page.",
}


def field_rows(schema: dict, ref: Ref, prefix: str = "", depth: int = 0) -> list[str]:
    rows: list[str] = []
    props, required = merged_properties(schema, ref)
    for name, prop in props.items():
        resolved = ref.resolve(prop)
        label = type_label(prop, ref)
        req = "yes" if name in required else "no"
        desc = clean(resolved.get("description")) or (DEFAULT_DESC.get(name, "") if depth == 0 else "")
        if "default" in resolved and resolved["default"] is not None:
            desc = (desc + " " if desc else "") + f"Default `{json.dumps(resolved['default'])}`."
        if "maxLength" in resolved:
            desc = (desc + " " if desc else "") + f"At most {resolved['maxLength']} characters."
        if "maxItems" in resolved:
            desc = (desc + " " if desc else "") + f"At most {resolved['maxItems']} items."
        rows.append(f"| `{prefix}{name}` | {label} | {req} | {desc} |")
        if depth < 2:
            inner = resolved
            child_prefix = f"{prefix}{name}."
            if inner.get("type") == "array" or (isinstance(inner.get("type"), list) and "array" in inner["type"]):
                item = ref.resolve(inner.get("items", {}))
                if item.get("properties") or item.get("allOf"):
                    rows.extend(field_rows(item, ref, f"{prefix}{name}[]." , depth + 1))
            elif inner.get("properties") or inner.get("allOf"):
                rows.extend(field_rows(inner, ref, child_prefix, depth + 1))
    return rows


def fields_table(schema: dict, ref: Ref) -> str:
    rows = field_rows(schema, ref)
    if not rows:
        return ""
    header = "| Field | Type | Required | Description |\n|---|---|---|---|\n"
    return header + "\n".join(rows) + "\n"


def array_body_table(schema: dict, ref: Ref) -> str:
    schema = ref.resolve(schema)
    if schema.get("type") == "array":
        item = ref.resolve(schema.get("items", {}))
        note = "The body is a JSON array."
        if "maxItems" in schema:
            note += f" At most {schema['maxItems']} items."
        return note + " Each item:\n\n" + fields_table(item, ref)
    return fields_table(schema, ref)


def params_table(params: list, ref: Ref) -> str:
    rows = []
    for raw in params:
        p = ref.resolve(raw)
        schema = p.get("schema", {})
        label = type_label(schema, ref)
        desc = clean(p.get("description"))
        if "default" in schema:
            desc = (desc + " " if desc else "") + f"Default `{schema['default']}`."
        if "maximum" in schema:
            desc = (desc + " " if desc else "") + f"At most {schema['maximum']}."
        req = "yes" if p.get("required") else "no"
        rows.append(f"| `{p['name']}` | {p.get('in')} | {label} | {req} | {desc} |")
    if not rows:
        return ""
    return "| Name | In | Type | Required | Description |\n|---|---|---|---|---|\n" + "\n".join(rows) + "\n"


def permission_for(path: str, method: str, tags: list) -> str:
    tag = tags[0] if tags else ""
    if tag == "Tracking" and method != "get":
        return "tracking:write"
    if tag == "Runs" and method == "post":
        return "runs:execute"
    if tag == "Webhooks" and method in ("post", "delete"):
        return "tracking:write"
    return "visibility:read"


def example_path(path: str) -> str:
    for key, value in PLACEHOLDERS.items():
        path = path.replace("{" + key + "}", value)
    return path


def curl_example(path: str, method: str, op: dict, ref: Ref) -> str:
    lines = [f"curl https://api.himoose.com/v1{example_path(path)} \\"]
    if method != "get":
        lines[0] = f"curl -X {method.upper()} https://api.himoose.com/v1{example_path(path)} \\"
    lines.append('  -H "Authorization: Bearer hmk_live_..."')
    body = op.get("requestBody")
    if body:
        schema = ref.resolve(body["content"]["application/json"]["schema"])
        sample = sample_body(schema, ref)
        if sample is not None:
            lines[-1] += " \\"
            lines.append('  -H "Content-Type: application/json" \\')
            lines.append("  -d '" + json.dumps(sample, ensure_ascii=False) + "'")
    for raw in op.get("parameters", []):
        p = ref.resolve(raw)
        if p.get("in") == "header":
            lines[-1] += " \\"
            sample = "nightly-2026-10-15" if p["name"] == "Idempotency-Key" else "VALUE"
            lines.append(f'  -H "{p["name"]}: {sample}"')
    return "```bash\n" + "\n".join(lines) + "\n```\n"


def sample_value(name: str, schema: dict, ref: Ref):
    schema = ref.resolve(schema)
    if "example" in schema:
        return schema["example"]
    if schema.get("enum"):
        values = [v for v in schema["enum"] if v is not None]
        return values[0] if values else None
    t = schema.get("type")
    if isinstance(t, list):
        t = [x for x in t if x != "null"][0] if [x for x in t if x != "null"] else "string"
    if t == "array":
        item = sample_value(name, schema.get("items", {}), ref)
        return [item] if item is not None else []
    if t == "object" or "properties" in schema or "allOf" in schema:
        return sample_body(schema, ref)
    if t == "integer":
        return schema.get("minimum", 1)
    if t == "boolean":
        return True
    if schema.get("format") == "uri" or name.lower().endswith("url"):
        return "https://example.com/page"
    if schema.get("format") == "date":
        return "2026-10-01"
    if schema.get("format") == "date-time":
        return "2026-10-01T09:00:00Z"
    return {
        "name": "Acme",
        "text": "What are the best SAST tools?",
        "websiteUrl": "https://acme.example",
        "timezone": "America/Chicago",
        "timeOfDay": "09:00",
        "description": "Nightly dashboard refresh",
        "domain": "example.com",
    }.get(name, "string")


def sample_body(schema: dict, ref: Ref):
    schema = ref.resolve(schema)
    if schema.get("type") == "array":
        item = ref.resolve(schema.get("items", {}))
        return [sample_body(item, ref)]
    props, required = merged_properties(schema, ref)
    if not props:
        return None
    out = {}
    for name, prop in props.items():
        resolved = ref.resolve(prop)
        if name in required or len(props) <= 3:
            out[name] = sample_value(name, resolved, ref)
    if not out:
        first = next(iter(props))
        out[first] = sample_value(first, ref.resolve(props[first]), ref)
    return out


def response_sections(op: dict, ref: Ref) -> str:
    out = []
    shown: dict[str, str] = {}
    for status, raw in op.get("responses", {}).items():
        resp = ref.resolve(raw)
        desc = clean(resp.get("description"))
        content = resp.get("content", {})
        schema = None
        for ctype in ("application/json", "application/problem+json"):
            if ctype in content:
                schema = content[ctype].get("schema")
                break
        out.append(f"**{status}** {desc}")
        if schema is not None and status.startswith("2"):
            table = fields_table(schema, ref)
            if table:
                key = json.dumps(schema, sort_keys=True)
                if key in shown:
                    out.append(f"Same fields as the {shown[key]} response.")
                else:
                    shown[key] = status
                    out.append("")
                    out.append(table.rstrip())
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def anchor(text: str) -> str:
    keep = []
    for ch in text.lower():
        if ch.isalnum():
            keep.append(ch)
        elif ch in " -_/":
            keep.append("-")
    slug = "".join(keep)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")


def build(spec: dict) -> str:
    ref = Ref(spec)
    version = spec["info"]["version"]
    lines = []
    lines.append("<!-- Generated by scripts/build_api_reference.py from developer-api-worker/src/openapi.json. Do not edit by hand. -->")
    lines.append("")
    lines.append("# Endpoint reference")
    lines.append("")
    lines.append(f"Every endpoint of the Hi, Moose API, contract version {version}, generated from the same OpenAPI file the API serves at [api.himoose.com/v1/openapi.json](https://api.himoose.com/v1/openapi.json). That file imports into Postman, Insomnia, Bruno and code generators.")
    lines.append("")
    lines.append("All requests go to `https://api.himoose.com/v1` and carry the key as a Bearer token, see [Keys and authentication](keys-and-auth.md). Responses are JSON. Errors use the Problem Details format described in [Errors and limits](errors-and-limits.md). Lists return `data` and `nextCursor`, see [Reading data](reading-data.md#pages).")
    lines.append("")
    lines.append("Permissions: **Read visibility data** is on every key. **Manage tracking** and **Start runs** are chosen when the key is created.")
    lines.append("")

    tag_order = [t["name"] for t in spec.get("tags", [])]
    tag_desc = {t["name"]: t.get("description", "") for t in spec.get("tags", [])}
    grouped: dict[str, list] = {t: [] for t in tag_order}
    for path, ops in spec["paths"].items():
        for method, op in ops.items():
            if method not in ("get", "post", "put", "patch", "delete"):
                continue
            tag = (op.get("tags") or ["Other"])[0]
            grouped.setdefault(tag, []).append((path, method, op))

    lines.append("## Contents")
    lines.append("")
    for tag in grouped:
        if not grouped[tag]:
            continue
        lines.append(f"- **{tag}**")
        for path, method, op in grouped[tag]:
            title = op.get("summary") or f"{method.upper()} {path}"
            lines.append(f"    - [{title}](#{anchor(title)}) `{method.upper()} {path}`")
    lines.append("")

    for tag, items in grouped.items():
        if not items:
            continue
        lines.append(f"## {tag}")
        lines.append("")
        if tag_desc.get(tag):
            lines.append(tag_desc[tag])
            lines.append("")
        for path, method, op in items:
            title = op.get("summary") or f"{method.upper()} {path}"
            lines.append(f"### {title}")
            lines.append("")
            lines.append("```")
            lines.append(f"{method.upper()} {path}")
            lines.append("```")
            lines.append("")
            perm = permission_for(path, method, op.get("tags", []))
            lines.append(f"Permission: **{PERMISSION_LABEL[perm]}**")
            lines.append("")
            if op.get("description"):
                lines.append(" ".join(op["description"].split()))
                lines.append("")
            params = params_table(op.get("parameters", []), ref)
            if params:
                lines.append("**Parameters**")
                lines.append("")
                lines.append(params)
            body = op.get("requestBody")
            if body:
                schema = body["content"]["application/json"]["schema"]
                lines.append("**Request body**" + ("" if body.get("required", True) else " (optional)"))
                lines.append("")
                table = array_body_table(schema, ref)
                lines.append(table if table else "No fields.\n")
            lines.append("**Example**")
            lines.append("")
            lines.append(curl_example(path, method, op, ref))
            lines.append("**Responses**")
            lines.append("")
            lines.append(response_sections(op, ref))
            lines.append("")

    lines.append("## Webhook event payload")
    lines.append("")
    lines.append("The JSON body Hi, Moose posts to a webhook endpoint. See [Webhooks](webhooks.md) for signing and delivery rules.")
    lines.append("")
    payload = spec["components"]["schemas"].get("WebhookEventPayload")
    if payload:
        lines.append(fields_table(payload, ref))
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    spec = load_spec()
    text = build(spec)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    previous = OUT.read_text(encoding="utf-8") if OUT.exists() else None
    if previous != text:
        OUT.write_text(text, encoding="utf-8", newline="\n")
        print(f"wrote {OUT.relative_to(ROOT)} ({len(text.splitlines())} lines)")
    else:
        print(f"{OUT.relative_to(ROOT)} unchanged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
