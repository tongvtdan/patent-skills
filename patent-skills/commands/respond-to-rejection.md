---
description: Draft a complete response to a patent office action or rejection from NOIP Vietnam, USPTO, or PCT examiner — with claim amendments and legal arguments
argument-hint: "<paste rejection summary or application number>"
---

# /respond-to-rejection — Office Action Response

Turn a patent rejection into a path to grant. Analyzes the examiner's objections, maps prior art claims, and drafts a complete response with arguments and amendments.

## Invocation

```
/patent-skills:respond-to-rejection
/patent-skills:respond-to-rejection VN-2023-01234 novelty rejection
/patent-skills:respond-to-rejection paste the office action text here
```

## What to Provide
- The office action / rejection notice (text or key points)
- Application number and jurisdiction (NOIP / USPTO / PCT)
- Current claim set
- Prior art references cited by the examiner

## Workflow

Apply the `office-action` skill:

### 1. Classify the Rejection
- NOIP: thiếu tính mới / thiếu trình độ sáng tạo / không thuộc đối tượng bảo hộ
- USPTO: §101 / §102 anticipation / §103 obviousness / §112 indefiniteness
- PCT: written opinion objections

### 2. Prior Art Gap Analysis
Claim chart mapping every cited reference element-by-element against your claims — identify what the examiner got right and what they missed.

### 3. Choose Response Strategy
- Arguments only (examiner misread claims or prior art)
- Amend claims + argue (prior art is close; narrow to distinguish)
- Cancel weak claims / allow strong ones (faster grant path)

### 4. Draft Complete Response
Full prosecution response document with:
- Rebuttal arguments per rejection type
- Proposed claim amendments (tracked changes format)
- Support citations from specification
- Conclusion requesting allowance

## Output
Complete response document saved as `office-action-response-[app-number]-[date].docx`
