# Troubleshooting

What to do when Hi, Moose MCP does not answer the way you expect. Most problems come down to the host device: the computer where Hi, Moose stays open and does the work.

## "The host device for this project has not checked in"

The computer picked as the host device is off, asleep, offline, or Hi, Moose is closed or signed out there.

1. Open Hi, Moose on that computer and sign in.
2. Wait a minute and ask again. The host checks in every few minutes while Hi, Moose is open.
3. If the computer is gone for good, pick another one under **Settings → Hi, Moose MCP**. Only the account owner can change the host device.

Jobs wait up to 15 minutes for the host device. After that they expire and the app gets a message saying so; ask again once the host is back.

## "This project has no host device"

Nobody has chosen a host device for the project yet. Open Hi, Moose on the computer that should do the work, go to **Settings → Hi, Moose MCP**, and pick it. Each project has its own host device, so a new project needs one chosen too.

## The app says the work is still running

Briefs, drafts, audits and audio take minutes, and some apps stop waiting before the work is done. Ask the app to check again; it picks the result up with the job id it was given. The work is also saved in your [Library](../../library/overview.md) in Hi, Moose, so nothing is lost if the chat moves on.

Audio takes longest: about 5 minutes for a short episode, 9 for standard and 15 for deep. The host device works on nothing else meanwhile, so a second request waits behind it.

## The app picked the wrong project

Tools take the project by name. Say it in the request, for example "for the Acme project", or ask the app to list the projects first and then pick. If two projects have similar names, use the one shown in Hi, Moose exactly.

## The connector will not connect

- **The sign-in page never opens.** Check the server address is `https://mcp.himoose.com/mcp`, with no trailing characters, and that the app is using OAuth, not an API key.
- **The sign-in code expired.** The code is good for two minutes. Start the connection again from the app.
- **Claude Team or Enterprise.** An owner has to add the connector for the organization before members can connect.
- **ChatGPT.** Custom MCP servers need a paid plan, and on Business and Enterprise workspaces an owner may need to allow custom connectors or turn on Developer mode first. Menu names change; see [Connect in ChatGPT](../hi-moose-mcp.md#connect-in-chatgpt).

## The app was connected and now is not

Access expires on its own after 30 days without use, and the account owner can revoke an app under **Settings → Hi, Moose MCP**. Connect again from the app.

## Results look out of date

- **Site coverage and internal links** read the latest crawl of your site and name its date. Pages published since then are not included. Run a crawl in Hi, Moose and ask again.
- **Visibility and opportunities** read stored results only and never run new checks. They cover the tracked prompts on the tracked engines over the window named in the answer. To see a new topic, add a prompt for it on the Visibility screen and let a run happen.

## Something ran that you did not expect

The **Recent agent jobs** table under **Settings → Hi, Moose MCP** lists every job: what was asked, by which app, when, and whether it finished. Jobs run as the account signed in on the host device, so a connected app can only read and write that account's Library.

## Still stuck

Write to support with the project name, which app you were using, roughly when it happened, and what the app said. The agent jobs table helps too.
