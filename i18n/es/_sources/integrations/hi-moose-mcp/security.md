# Security and data handling

This page is for the people who review a connector before a team connects it. It describes how Hi, Moose MCP works today, in the order a security review usually asks. Last checked against the running server on 2026-10-19.

## Short answers

| Question | Answer |
|---|---|
| Who runs the server? | Hi, Moose, the maker of the app. Not a third party. |
| Can the tool list change after we connect? | No. Tools are fixed code. The exact list is published with a hash at [mcp.himoose.com/tools.json](https://mcp.himoose.com/tools.json). |
| How do people sign in? | OAuth 2.1, the standard remote MCP flow, with their existing Hi, Moose account. No API keys. |
| How long do tokens live? | Access tokens one hour. Refresh tokens expire after 30 days without use, 90 days at most. |
| Can we revoke access? | Yes, per app, in Hi, Moose under **Settings → Hi, Moose MCP**. |
| What can a connected app change? | Content work and reads inside the signed-in account's projects. It cannot publish, delete, or change settings, team members or tracking. |
| Does it reach anything outside Hi, Moose? | No. It never sees the chats, files, repositories or other connectors of the app it is used from. |
| Where does the work run? | In the Hi, Moose app on a device you choose, the host device. |
| Is outside text in results marked? | Yes. Page passages and AI engine answers come back between markers labelled as data, not instructions. |
| Where do we report a problem? | [legal@himoose.com](mailto:legal@himoose.com), or the [contact page](https://himoose.com/contact/). |

## Who runs the server

Hi, Moose MCP is built and run by Hi, Moose. It is the only MCP server that reaches a Hi, Moose account, and it is not a community or third-party server. The server address is:

```text
https://mcp.himoose.com/mcp
```

The server itself is small. It handles sign-in and tokens, offers the tool list, and passes each request to Hi, Moose's cloud, which hands it to the host device. The work, such as reading the site crawl or writing a brief, runs in the Hi, Moose app on that device, the same way it runs when someone clicks the button in the app.

## The tool list is published and does not change

An MCP server can, in principle, change its tool descriptions after you connect, or hide instructions for the AI agent inside them. The OWASP name for this is tool poisoning.

Hi, Moose MCP's tools are fixed code in the server. The names, descriptions and input schemas do not change between calls, and no user content is ever written into them. A new tool means a new server release.

The exact list the server serves is published at:

```text
https://mcp.himoose.com/tools.json
```

It carries the server version, the date the tool list last changed, the number of tools, the full text of every tool, the instructions text the server gives the agent, and a SHA-256 hash. The hash covers the compact JSON of the `instructions` and `tools` fields, so you can recompute it from the file or compare it with what your MCP client received. Pin the hash in your review notes and compare it on a schedule. The same hash is the file's `ETag` header.

Before anyone signs in, the consent page shows the same tool list in plain words, under "This app will be able to" and "It will not be able to".

## Sign-in and tokens

Every client runs the same flow: Claude on the web, the Claude desktop app, Claude Code, ChatGPT and any other MCP app. There is no shortcut, no shared token and no API key.

- OAuth 2.1 as the current MCP authorization specification describes it: protected resource metadata (RFC 9728) with a `WWW-Authenticate` challenge, authorization server metadata (RFC 8414), PKCE required for every client, resource indicators (RFC 8707) so a token for this server cannot be replayed elsewhere, dynamic client registration (RFC 7591) and Client ID Metadata Documents, and token revocation (RFC 7009).
- Sign-in happens on `console.himoose.com`, with the person's existing Hi, Moose account, by email and password or with Google. The MCP app never sees the password. Hi, Moose MCP learns only the account id and email, and which projects the account can see.
- The consent page names the app that is asking. When the app publishes its identity, the page shows its publisher domain. When it does not, the page says "Name not verified".
- Access tokens live one hour. Refresh tokens live at most 90 days and expire after 30 days without use. Tokens, codes and secrets are stored only as hashes.
- One connection belongs to one person. Team members connect with their own accounts.

To disconnect an app, open Hi, Moose and go to **Settings → Hi, Moose MCP**. The **Connected apps** table lists every app signed in to the account, with the publisher domain and the time it connected. **Revoke** signs that app out within a minute. The app can only connect again by going through sign-in.

## What a connected app can and cannot do

Everything a connected app can do is listed in the [setup guide](../hi-moose-mcp.md#what-a-connected-app-can-do) and described tool by tool in the [tool reference](tools.md). It is content and research work inside the account's projects: briefs, drafts, images, FAQs, key points, AEO audits, internal link plans, audio episodes, coverage checks, and reads of stored AI search results.

It cannot:

- Publish to a website, or change anything on one
- Delete anything
- Change settings, team members, billing or the host device
- Change what Hi, Moose tracks, or start a visibility run
- Reach any account other than the one that signed in
- Reach anything in the app it is used from: no chats, files, repositories, memory or other connectors

Every request names a project. Before any work starts, Hi, Moose checks that the signed-in account has access to that project. A request for a project the account cannot see fails at once.

## Where the work runs and what data moves

Hi, Moose MCP never has a copy of the site crawl, the Brand Truth profile or the Library. Those live in the Hi, Moose app on the host device, the one computer or server you pick in Settings. The host runs each job the same way the app runs it from a button.

Here is the path a request takes:

1. The MCP app sends the tool name and its input to the server.
2. The server checks the token and asks Hi, Moose's cloud to create a job record for the project. The cloud checks project access and writes the record.
3. The host device, which watches for jobs on its projects, picks the job up and runs it.
4. The host writes the result to the job record and saves it in the Library. The server returns the result to the MCP app.

What that means for your data:

- The request and the result travel through Hi, Moose's cloud (Google Cloud, United States region) as a job record. The job record stays with the project so the **Recent agent jobs** table in Settings can show what was asked, by which app and account, and whether it finished.
- Generated images are stored in the account's Hi, Moose cloud storage and returned as a link.
- Model calls use the same path as the app: the managed models of your plan, your own model keys if you brought them, or a local model if you run one. Connecting an MCP app does not change which models see your content.
- The server's own logs hold the tool name, how long the call took and whether the client streamed. They never hold the input or the result.

## Outside text in results

Some results contain text Hi, Moose did not write: passages from pages of your site, anchor text quoted from a page, short excerpts of what an AI engine answered, or the full text of a stored answer. Text like that could carry instructions aimed at an AI agent. The OWASP name for this is indirect prompt injection.

Every result that carries outside text marks it. The text comes back between a start marker and an end marker, with a line in front naming where it came from and saying that everything between the markers is data, not instructions. The structured form of the same result carries a `dataNotice` field saying the same thing. This applies to `check_site_coverage`, `run_aeo_audit`, `find_internal_links`, `visibility_check_topic`, `visibility_get_answer` and `visibility_list_opportunities`.

Briefs, drafts, FAQs, key points and audio scripts are written by Hi, Moose for you. The research behind them is read on the host device and is not passed through to the agent.

Markers help an agent treat the text as data. They do not make an agent immune to instructions in content it reads, and no tool vendor can promise that. Keep the permissions of the agent you connect as narrow as its job needs, the same way you would for any connector.

## Reporting a security issue

Write to [legal@himoose.com](mailto:legal@himoose.com) or use the [contact page](https://himoose.com/contact/). Tell us what you found and how to reproduce it. We answer every report, and we will tell you what we changed.
