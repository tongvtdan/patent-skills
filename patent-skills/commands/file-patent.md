---
description: End-to-end guided patent filing workflow — from invention idea to a filing-ready application with prior art search, jurisdiction strategy, and complete draft
argument-hint: "<invention description or topic>"
---

# /file-patent — End-to-End Patent Filing

Go from raw invention idea to a complete, filing-ready patent application. Combines prior art search → jurisdiction strategy → full application draft in one guided workflow.

## Invocation

```
/patent-skills:file-patent
/patent-skills:file-patent biodegradable packaging made from cassava starch
/patent-skills:file-patent provisional  (→ fast priority-date filing only)
/patent-skills:file-patent VN  (→ targets NOIP Vietnam filing)
```

## Workflow

### Step 1 — Invention Disclosure Interview
Conduct a structured interview to fully capture the invention:
- What problem does it solve?
- How does it work (key technical mechanism)?
- What's novel vs. existing solutions?
- What field / IPC class?
- Any prior art already known?
- Target markets and jurisdictions?

### Step 2 — Prior Art Search
Apply the `patent-research` skill to:
- Search Google Patents, Espacenet, PATENTSCOPE, NOIP IP Library
- Identify IPC classification
- Assess novelty and inventive step
- Check freedom-to-operate in target markets

### Step 3 — Jurisdiction & Filing Route Decision
Based on business situation and budget, recommend:

| Route | When to Use | Cost Level |
|-------|-------------|-----------|
| Vietnam NOIP only | Vietnam market focus | Low |
| Vietnam + PCT | Global ambitions, need time | Medium |
| US Provisional → PCT | Startup raising funds | Medium |
| Multi-jurisdictional | Scale stage, investor-ready | High |

### Step 4 — Urgency Check
- Upcoming public disclosure, conference, or product launch?
- Competitor activity spotted in this space?
→ If urgent: go directly to provisional filing to lock priority date

### Step 5 — Draft the Application
Apply `provisional-claims` skill (fast priority-date filing) or `application-writer` skill (full utility application):
- Complete specification: field, background, summary, detailed description
- Independent + dependent claims in English and Vietnamese
- Abstract (≤150 words)
- Drawings guidance

### Step 6 — Deliver Filing Package
- Complete patent application document (.docx)
- Filing checklist per jurisdiction
- Official fee schedule (VND / USD)
- Prosecution timeline with key deadlines
- 12-month action plan

## Notes
- Vietnam: file as sáng chế (utility patent) or giải pháp hữu ích (utility solution — lower inventive step required)
- First-to-file system: priority date is everything — file before any public disclosure
- After the provisional expires at 12 months, a full application must be filed to maintain priority
