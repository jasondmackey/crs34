# Agent Lessons Learned & Reference (CRS-34 Mission)

## Layout & Structural Rules
- **Two-Column Grid**: Keep a clear separation between the left content column (Mission Status, Payload) and the right media/tracker column.
- **Parent Container Integrity**: Never move panels outside their original parent containers. This prevents layout breaks on different viewport sizes.
- **Collapsible Sections**: Wrap secondary details (Payload Highlights) in `<details>` tags with clear `<summary>` labels to keep the initial view compact.

## Surgical Modification Rules (CRITICAL)
- **NO Structural Regex**: Never use global or multi-line regex for structural HTML changes. It is prone to "greedy" matching that deletes entire page sections.
- **Grep & Sed Methodology**:
  1. Identify target lines using `grep -n` or `sed -n 'X,Yp'`.
  2. Use Python string slicing or exact line-by-line `sed` operations.
  3. Verify the final line count matches expectations before pushing.
- **CDN Propagation**: GitHub Pages takes 1-3 minutes to update. Always waitUpdate AGENT_REFERENCE.md with formal project reference and lessons learned and perform a "Hard Refresh" (Cmd+Shift+R) before evaluating changes.

## Feature Implementation Lessons
- **RSS Proxying**: Use `https://corsproxy.io/?` for reliable CORS-safe fetching of SpaceX RSS feeds. `allorigins.win` proved unstable during high-traffic windows.
- **MOC Clock Embedding**: Embed as an iframe with a specific height (e.g., 500px) to accommodate the full TDRS schedule without internal scrollbars.
- **45 WS Forecast**: Embed the direct page URL (not just the PDF link) in an iframe so users can click the PDF buttons directly from the dashboard.
- **Launch Probability**: Always label as "N/A" with a footnote until the official 45 WS L-3/L-2/L-1 forecasts are issued.

## Bot Logic (CRS34Bot)
- **Scrub Detection**: Use a `LAUNCH_SCRUBBED` flag to prevent the bot from posting contradictory "T-minus" messages after a confirmed scrub or rescheduling.
- **API Polling**: Poll the SpaceX API/RSS feed for `date_utc` changes to automatically update the countdown timer on the dashboard.
- **Deduplication**: Use a unique message ID (e.g., `timestamp + type`) to prevent the bot from re-posting the same status update on page refresh.
