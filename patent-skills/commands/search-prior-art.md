---
description: Search prior art databases and assess patentability for any invention — novelty check, IPC classification, freedom-to-operate, and filing recommendation
argument-hint: "<describe your invention>"
---

# /search-prior-art — Prior Art Search & Patentability Check

Rapid prior art search across Google Patents, Espacenet, PATENTSCOPE, USPTO, and NOIP Vietnam. Returns patentability verdict, closest prior art, IPC classification, and strategic filing recommendation.

## Invocation

```
/patent-skills:search-prior-art wearable blood glucose monitor using near-infrared spectroscopy
/patent-skills:search-prior-art FTO  (→ freedom-to-operate mode — checks if your product infringes active patents)
/patent-skills:search-prior-art landscape AI-powered crop disease detection  (→ full patent landscape overview)
```

## Workflow

Apply the `patent-research` skill:

### 1. IPC Classification
Identify the 1–3 most relevant IPC classes for the invention.

### 2. Multi-Database Search
Search in parallel:
- Google Patents (global, AI-assisted)
- Espacenet/EPO (IPC browsing + European)
- PATENTSCOPE/WIPO (PCT applications)
- NOIP IP Library (Vietnamese patents)
- USPTO (US patents)

### 3. Prior Art Mapping
For each significant result: patent number, title, date, assignee, relevance rating (🔴 Blocking / 🟡 Relevant / 🟢 Background)

### 4. Patentability Assessment
Evaluate against three criteria (Vietnamese IP Law Art. 60–62 + international):
- **Novelty** (Tính mới): Is it new worldwide?
- **Inventive step** (Trình độ sáng tạo): Non-obvious to skilled person?
- **Industrial applicability** (Khả năng áp dụng công nghiệp): Can it be made/used?

### 5. Strategic Output
- Filing recommendation (full patent / utility solution / don't file / design around)
- What the claims should focus on to be distinct from prior art
- Key risk areas to address in the application

## Output
Structured research report saved as `patent-research-[invention]-[date].md`
