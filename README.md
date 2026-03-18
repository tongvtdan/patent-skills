# Patent Skills — AI-Powered IP Protection for Inventors & Entrepreneurs

> 7 patent and IP skills. 4 slash commands. Built for Vietnamese inventors, startups, and entrepreneurs. Covers Vietnamese IP Law (Luật SHTT 2022), PCT, and USPTO.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

---

## What This Does

Patent Skills gives Claude the knowledge of a Vietnamese patent attorney. It handles the full IP lifecycle — from idea to protected asset:

| Skill | Trigger Phrases | What It Does |
|-------|----------------|-------------|
| `patent-research` | "Is this patentable?", "search prior art", "can I patent X?" | Prior art search across 6 databases, IPC classification, patentability verdict, FTO analysis |
| `provisional-claims` | "Quick filing", "secure priority date", "before I launch" | Draft provisional application to lock filing date fast |
| `application-writer` | "Write my patent", "full patent application", "draft patent spec" | Complete filing-ready utility patent application |
| `patent-strategy` | "IP strategy", "patent roadmap", "patent moat", "VC due diligence" | Portfolio audit, jurisdiction roadmap, budget plan, competitor IP landscape |
| `claims-analyzer` | "Review my claims", "are my claims strong?", "broaden claims" | Claim critique, prior art differentiation, scope rating, revised claim set |
| `office-action` | "Got a rejection", "NOIP rejected", "respond to examiner" | Analyzes rejection, drafts complete office action response |
| `patent-valuation` | "Patent worth?", "licensing deal", "royalty rate", "IP due diligence" | IP valuation, licensing term sheets, Vietnamese technology transfer law |

---

## Commands

| Command | What It Does |
|---------|-------------|
| `/patent-skills:file-patent` | Full guided workflow from invention → filing-ready application |
| `/patent-skills:search-prior-art` | Quick patentability check + prior art search |
| `/patent-skills:build-ip-strategy` | Complete IP strategy and portfolio roadmap |
| `/patent-skills:respond-to-rejection` | Office action analysis + response draft |

---

## Jurisdictions Covered

- 🇻🇳 **Vietnam (NOIP)** — Luật Sở hữu trí tuệ 2005, amended 2022 (Law 07/2022/QH15)
- 🌍 **PCT (WIPO)** — International filing, 30-month national phase strategy
- 🇺🇸 **USPTO** — US patent law (35 USC §§ 101-112)
- 🌏 **ASEAN** — ASPEC cooperation, regional strategy

---

## Installation

### Claude Cowork

1. Open **Claude Settings → Plugins → Add Marketplace**
2. Enter the GitHub repo URL: `https://github.com/YOUR_USERNAME/patent-skills`
3. Install the `patent-skills` plugin
4. Start a new chat — commands are ready

### Claude Code

```bash
/plugin install patent-skills@patent-skills
```

---

## Quick Start

```
/patent-skills:file-patent I invented a new water purification method using biochar
```

```
/patent-skills:search-prior-art AI-powered traffic signal optimization
```

```
/patent-skills:build-ip-strategy Vietnamese healthtech startup, raising Series A
```

---

## Works Best With

This plugin pairs with [inventor-skills](https://github.com/tongvtdan/inventor-skills) (TRIZ + SIT innovation methodology):
- Use **inventor-skills** to *generate* breakthrough inventions
- Use **patent-skills** to *protect* them

---

## Disclaimer

This plugin provides strategic guidance and drafting assistance for educational and productivity purposes. It does not constitute legal advice and does not create an attorney-client relationship. For official filings, have a licensed patent attorney in the relevant jurisdiction review before submission.

Vietnamese IP Law guidance is based on Luật SHTT as amended through 2022. Verify current NOIP requirements at [noip.gov.vn](https://www.noip.gov.vn).

---

## Author

**Dan Tong** — Inventor, entrepreneur, and IP strategy enthusiast
[tongvtdan@gmail.com](mailto:tongvtdan@gmail.com)

---

## License

MIT — see [LICENSE](LICENSE)
