# GitHub Pages Launch Countdown Page — AI Agent Reference & Lessons Learned
# Project: SpaceX CRS-34 Launch Countdown (jasondmackey/crs34)
# Generated: 2026-05-13 | Last updated: 2026-05-13 (post-launch-day session)

---

## PROJECT OVERVIEW

A single-file static GitHub Pages site (index.html) serving as a real-time
launch countdown dashboard. All logic, styles, and markup live in one file.
Hosted at: https://jasondmackey.github.io/crs34/

## CRITICAL PROJECT INVENTORY

- **Primary IDs:**
  - `#missionStatus`: Main header for launch clock/status
  - `#chatMessages`: Container for the CRS34Bot feed
  - `#mocclockFrame`: LASP MOC Clock iframe
  - `#weatherFrame`: 45th Weather Squadron forecast iframe
- **External Dependencies:**
  - SpaceX API/RSS: `https://api.spacexdata.com/v4/launches/next`
  - RSS Proxy: `https://corsproxy.io/?https://www.nitter.net/SpaceX/rss`
  - Clock Source: `https://lasp.colorado.edu/atoc/clock/`
- **LocalStorage Keys:**
  - `crs34_last_update`: Prevents bot duplication on refresh
  - `launch_scrubbed`: Boolean flag to suppress post-scrub messages

---

## Layout & Structural Rules

- **Two-Column Grid:** Keep a clear separation between the left content column (Mission Status, Payload) and the right media/tracker column.
- **Parent Container Integrity:** Never move panels outside their original parent containers. This prevents layout breaks on different viewport sizes.
- **Collapsible Sections:** Wrap secondary details (Payload Highlights) in `<details>` tags with clear `<summary>` labels to keep the initial view compact.

## Surgical Modification Rules (CRITICAL)

- **NO Structural Regex:** Never use global or multi-line regex for structural HTML changes. It is prone to "greedy" matching that deletes entire page sections.
- **Grep & Sed Methodology:**
  i. Identify target lines using `grep -n` or `sed -n 'X,Yp'`.
  ii. Use Python string slicing or exact line-by-line `sed` operations.
  iii. Verify the final line count matches expectations before pushing.
- **CDN Propagation:** GitHub Pages takes 1-3 minutes to update. Always perform a "Hard Refresh" (Cmd+Shift+R) before evaluating changes.

## Feature Implementation Lessons

- **RSS Proxying:** Use `https://corsproxy.io/?` for reliable CORS-safe fetching of SpaceX RSS feeds. `allorigins.win` proved unstable during high-traffic windows.
- **MOC Clock Embedding:** Embed as an iframe with a specific height (e.g., 500px) to accommodate the full TDRS schedule without internal scrollbars.
- **45 WS Forecast:** Embed the direct page URL (not just the PDF link) in an iframe so users can click the PDF buttons directly from the dashboard.
- **Launch Probability:** Always label as "N/A" with a footnote until the official 45 WS L-3/L-2/L-1 forecasts are issued.

## Bot Logic (CRS34Bot)

- **Scrub Detection:** Use a `LAUNCH_SCRUBBED` flag to prevent the bot from posting contradictory "T-minus" messages after a confirmed scrub or rescheduling.
- **API Polling:** Poll the SpaceX API/RSS feed for `date_utc` changes to automatically update the countdown timer on the dashboard.
- **Deduplication:** Use a unique message ID (e.g., `timestamp + type`) to prevent the bot from re-posting the same status update on page refresh.

---

## RECOVERY & ROLLBACK

- **Known-Good Commit:** `7276afd` (Final pre-launch baseline)
- **Hard Reset:** `git reset --hard 7276afd && git push --force` (Only as a last resort)
