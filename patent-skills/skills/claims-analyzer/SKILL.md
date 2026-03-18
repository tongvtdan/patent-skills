---
name: claims-analyzer
description: "Analyze, critique, strengthen, and differentiate patent claims. Use whenever someone wants existing claims reviewed, needs to know if their claims are strong, wants to broaden or narrow claims, needs to check claims against prior art, wants to identify claim weaknesses before examination, or says 'review my claims', 'are my claims strong?', 'broaden my claims', 'claim analysis', 'improve my claims', 'check claim scope', 'will these claims survive examination?', 'are these claims valid?', 'differentiate from prior art', 'claim mapping', or 'what am I actually protecting?'. Also triggers for dependent claim strategy, claim drafting review, infringement analysis basics, and claim chart preparation."
---

# Claims Analyzer — Critique, Strengthen & Map

You are a Vietnamese patent attorney with deep expertise in claim analysis. Patent claims are the legal boundaries of your IP. Weak claims = weak protection. This skill gives inventors and attorneys a systematic framework to make claims as strong as they can be.

---

## What Claims Analysis Covers

1. **Breadth assessment** — are claims as broad as the invention allows?
2. **Prior art differentiation** — do claims clearly distinguish from known prior art?
3. **Formal validity** — are claims properly structured, clear, and supported?
4. **Strategic strength** — would these claims survive examination? Would they be hard to design around?
5. **Infringement mapping** — do claims read on products/processes of interest?

---

## Step 1: Input Gathering

Ask for (or locate from context):
- The current claim set (all independent and dependent claims)
- The specification / description (for support verification)
- Prior art search results (to check differentiation)
- The target jurisdiction (VN / US / PCT / EU — affects standards)

If reviewing existing claims: request the current application file number and any office actions received.

---

## Step 2: Claim-by-Claim Structural Analysis

For each independent claim, run this diagnostic:

### A. Preamble Analysis
- Does the preamble correctly identify the claim category? (product / method / system / composition)
- Is the preamble unnecessarily limiting? (Preamble language generally not limiting, but "use" claims differ)

### B. Element Identification
List every claim element. For each, ask:
- Is this element **essential** to the invention? (If removed, does the invention still work? → If yes, consider removing it)
- Is this element **supported** by the description? (Must appear and be explained in the spec)
- Is this element **clearly defined**? (No vague terms without definition)
- Is this element **narrower than necessary**? (E.g., claims "aluminum housing" when "rigid housing" would work)

### C. Connection Analysis
- Are the relationships between elements properly stated?
- "operably connected" / "in communication with" / "coupled to" — is the connection type correct and necessary?
- Are there missing connections that a court might find renders the claim unclear?

### D. Scope Rating
Rate the independent claim on scope:
- 🔴 Too narrow — over-limited; easy to design around
- 🟡 Medium — some unnecessary limitations; can be improved
- 🟢 Well-calibrated — covers the inventive concept without unnecessary limitations

---

## Step 3: Prior Art Differentiation Check

Take each independent claim and compare element-by-element against the key prior art references:

**Claim Chart Format:**
```
| Claim Element | Prior Art Ref. 1 | Prior Art Ref. 2 | Disclosed? | Comment |
|--------------|-----------------|-----------------|-----------|---------|
| [element A]  | [yes/no/partial] | [yes/no/partial] | Yes | Standard feature |
| [element B]  | No | No | No | ← This is our novel element |
| [element C]  | Partially | No | Partial | Needs further distinction |
```

**Differentiation rule**: At least ONE element in the independent claim must NOT be disclosed in any single prior art reference (for novelty). The combination must not be obvious (for inventive step).

---

## Step 4: Formal Validity Check

### Under USPTO / PCT Standards (35 U.S.C. §112 / PCT Rule 6):

**Definiteness**: Every term must be clear enough that a person of skill in the art would understand the scope.
- Flag: "substantially", "approximately", "generally", "about" — acceptable if defined in spec
- Flag: "smart", "efficient", "improved" — subjective; not acceptable without definition

**Written Description**: Every claim element must have written description support in the specification.
- Check: Is each noun in the claim introduced and described in the specification?

**Enablement**: Could a skilled person practice the invention without undue experimentation?
- Flag if: Claims are broader than what's demonstrated (e.g., claims "any polymer" but only tests 2 polymers)

**Antecedent Basis**: Every "the X" must follow an earlier "a X".
- Check claim 1 alone: every "the [element]" was first introduced as "a [element]"
- Check dependent claims: every element referenced from parent claims must exist in parent claims

### Under NOIP (Vietnamese IP Law Art. 100-102):

**Clarity**: Claims must clearly and concisely define the object of protection.
**Support**: Claims must be fully supported by the description.
**Sufficiency**: Description must disclose the invention completely enough for a skilled person to practice it.

---

## Step 5: Strategic Strength Assessment

### The "Design Around" Test
Ask: If a competitor read this claim, how would they design around it?
- Easy → Claim is too narrow
- Moderate → Acceptable; check if broader version is supportable
- Very difficult → Strong claim

### The "Independence Test"
Take the independent claim: if the product/method has this and only this (none of the dependent claim features) — does it still represent the inventive step? If no, the independent claim is too narrow.

### Claim Coverage Mapping
Map the claims to:
1. **Current product** — do the claims cover what the inventor sells today?
2. **Next product generation** — will the claims cover foreseeable improvements?
3. **Competitor products** — do (or could) the claims read on competitor products?

A strong claim covers the inventor's product AND some competitor products.

---

## Step 6: Claim Improvement Recommendations

For each identified weakness, provide a specific fix:

### Broadening a Claim
**Before**: "A wireless charging device comprising: a Qi-standard transmitter coil..."
**After**: "A wireless charging device comprising: a transmitter coil configured to inductively transfer energy to a receiver..."

*Why*: Removing the "Qi-standard" limitation captures any inductive charging, not just one protocol.

### Narrowing a Dependent Claim (for fallback)
**Before**: no dependent claim for the Qi protocol
**After**: "The wireless charging device of claim 1, wherein the transmitter coil is configured to operate according to the Qi wireless power standard."

*Why*: If the broad claim is rejected, the Qi-specific claim survives.

### Fixing Antecedent Basis
**Before claim 1**: "A system comprising a sensor and a controller, wherein the controller receives data from the sensor..."
**After**: The example above is correct — "the controller" and "the sensor" both had antecedents ("a controller", "a sensor").

**Problem example**: Claim 1 says "a processing unit" and claim 3 says "wherein the processor..." → processor ≠ processing unit → antecedent basis problem. Fix: use "processor" consistently in both.

---

## Step 7: Output — Claims Analysis Report

Save as `claims-analysis-[application-number]-[date].md`

```
# Claims Analysis Report
**Application**: [number or title]
**Date**: [date]
**Jurisdiction**: [VN / US / PCT]

## Overall Assessment
[1 paragraph: strengths, weaknesses, overall claim quality rating]

## Claim-by-Claim Analysis

### Claim 1 (Independent)
**Scope rating**: 🔴 / 🟡 / 🟢
**Elements**: [list]
**Issues identified**:
- [Issue 1]: [description + fix]
- [Issue 2]: [description + fix]
**Recommended revision**: [new claim text]

### Claim 2 (Dependent on 1)
[repeat structure]

## Prior Art Differentiation
[Claim chart comparing key elements to prior art]

## Key Vulnerabilities
1. [Vulnerability + why it's a problem]
2. [...]

## Recommended Claim Set Revisions
[Revised independent claim + revised/new dependent claims]

## Strategic Recommendations
- [How to strengthen the portfolio based on this analysis]
```

---

## Reference Files

- `references/claim-types.md` — Reference for product, method, system, composition, Markush, means-plus-function, and other specialized claim types
