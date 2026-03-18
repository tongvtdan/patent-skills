# Patent Database Search Guide

## Quick Reference: Which Database to Use

| Goal | Best Database | URL |
|------|--------------|-----|
| Quick global search | Google Patents | patents.google.com |
| IPC class browsing | Espacenet | worldwide.espacenet.com |
| US patents | USPTO | patents.uspto.gov |
| PCT applications | PATENTSCOPE | patentscope.wipo.int |
| Vietnamese patents | NOIP IP Library | iplib.noip.gov.vn |
| Japanese patents | J-PlatPat | j-platpat.inpit.go.jp |
| Korean patents | KIPRIS | patent.kipris.or.kr |

---

## Google Patents — Advanced Search Operators

```
# Boolean operators
wifi AND antenna NOT bluetooth
"machine learning" OR "artificial intelligence"

# Field-specific search
title:(wireless charging)
abstract:(polymer electrolyte)
inventor:(Nguyen Van A)
assignee:(Samsung)

# IPC class filter
cl:H04L (Communications digital data)
cl:A61K (Pharmaceutical preparations)

# Date filters
before:priority:20200101
after:filing:20180101

# Status filter
is:PATENT (granted patents only)
is:APPLICATION (published applications)

# Country
country:VN (Vietnamese patents)
country:US (US patents)
```

---

## NOIP Vietnam Search (iplib.noip.gov.vn)

**Searching Vietnamese patents:**
1. Go to iplib.noip.gov.vn
2. Select "Sáng chế / Giải pháp hữu ích" (Patent / Utility Solution)
3. Search by: Keyword (Vietnamese or English), IPC code, Applicant name, Filing number

**Vietnamese patent number format:**
- Filed applications: VN [year][sequence] (e.g., VN 2022-01234)
- Granted patents: VN [number] (e.g., VN 25678)

**Note**: NOIP database coverage is strongest from 2000 onwards. For older Vietnamese patents, consider requesting manual search from NOIP directly.

---

## WIPO PATENTSCOPE — PCT Search

```
# Simple keyword
EN_AB:(biodegradable plastic packaging)

# IPC search
IPC:B65D AND EN_AB:(sustainable)

# Applicant country
IA:(VN) — Vietnamese origin PCT applications
IA:(US) — US origin applications

# National phase entries in Vietnam
ENTERED:VN — PCT apps entering Vietnam national phase
```

---

## Espacenet IPC Classification Browser

### Common IPC Classes by Technology

**Electronics & Communications**
- H04L — Data transmission (WiFi, 5G, networking)
- H04W — Wireless communications
- H04B — Radio transmission
- G06F — Computing, data processing
- G06N — AI, machine learning
- H01L — Semiconductor devices

**Medical & Health**
- A61K — Pharmaceutical preparations
- A61P — Therapeutic activity of compounds
- A61B — Medical diagnosis devices
- A61M — Medical devices for introduction into body

**Agriculture & Food**
- A01N — Biocides, plant growth regulators
- A23L — Food products and preparation
- A01G — Horticulture, cultivation

**Materials & Chemistry**
- C08 — Organic macromolecular compounds (plastics, polymers)
- C01 — Inorganic chemistry
- B01 — Physical/chemical processes

**Mechanical**
- F16 — Engineering elements
- B23 — Metal cutting, working
- B29 — Working of plastics

**Energy**
- H01M — Electrochemical processes (batteries)
- F03D — Wind motors
- H02S — Solar energy systems
- H01G — Capacitors

---

## Search Strategy Tips

### Step 1: Start Broad
Use 3-5 key technical terms in plain language. Identify the best 10-15 hits.

### Step 2: Extract IPC Classes
From the best hits, note which IPC classes appear most frequently. These are your target classes.

### Step 3: Go Deep by IPC
Browse all recent patents in those IPC classes. This catches patents with unusual terminology.

### Step 4: Citation Chaining
Take your closest prior art hit → check:
- "Cited by" (forward citations) — find later developments
- "References cited" (backward citations) — find foundational patents

### Step 5: Assignee Search
Identify the top competitors/companies in the space and search all their patents in the relevant IPC classes.

### Step 6: Non-Patent Literature (NPL)
Check Google Scholar, arXiv, PubMed for academic papers — these count as prior art too.

---

## Red Flags in Prior Art

Stop and escalate analysis if you find:
- A single patent that discloses **all elements** of the invention (anticipation → not novel)
- A **recent filing** (< 18 months old) by a competitor in exactly this space (may be unpublished prior art)
- A **broad independent claim** in an active patent that could read on the invention
- An **expired patent** — note it as public domain background art (positive for freedom to operate)
