# Claim Drafting Guide — Rules, Patterns & Common Mistakes

## The Golden Rules

1. **A claim is a single sentence.** No periods until the final period after the last claim element.
2. **"Comprising" is open. "Consisting of" is closed.** Always use "comprising" unless the inventor needs absolute exclusivity.
3. **Claim what you invent, not what you sell.** The broadest version of what's novel, not the preferred product.
4. **Every element in a claim must be in the description.** Courts invalidate claims that lack written description support.
5. **Use functional claiming thoughtfully.** "configured to" or "adapted to" is fine; pure result claiming ("a device that causes X") is weak.

---

## Claim Anatomy

### Independent Product Claim
```
A [preamble — category], comprising:
  [element A] having [structural feature];
  [element B] operably connected to [A]; and
  [element C] configured to [function] in response to [condition].
```

### Independent Method Claim
```
A method for [achieving result], the method comprising:
  providing [input/element];
  [performing action] on [element] to produce [intermediate];
  [applying action] to [intermediate]; and
  obtaining [output] characterized by [property].
```

### Dependent Claim — Adding an Element
```
The [noun] of claim 1, further comprising [additional element] configured to [function].
```

### Dependent Claim — Narrowing a Feature
```
The [noun] of claim 1, wherein [element A] comprises [more specific structure].
```

### Dependent Claim — Adding a Step
```
The method of claim 3, further comprising [verb]-ing [element] after [step reference].
```

---

## Common Claim Mistakes

### Mistake 1: Too Narrow Too Soon
**Bad:**
> A smartphone case made of polycarbonate with a 2mm shock-absorbing rim for iPhone 14 Pro...

**Better:**
> A protective cover for a portable electronic device, comprising: a body formed of impact-resistant material; and a peripheral rim extending from the body configured to absorb impact forces...

*You own the concept, not just one material or one phone model.*

### Mistake 2: Missing Elements in Description
**Bad:** Claim mentions "the sensor module" but description never explains what the sensor module is or does.

**Fix:** Every noun in a claim must be introduced and described in the specification.

### Mistake 3: Antecedent Basis Problems
**Bad:**
> Claim 1: A system comprising a processor...
> Claim 2: The system of claim 1, wherein the memory...

*"The memory" has no antecedent — memory was never introduced in claim 1.*

**Fix:** If claim 2 references memory, claim 1 must also mention "a memory."

### Mistake 4: Negative Limitations Without Basis
**Bad:** "wherein the composition is free of preservatives"
**Fix:** Only use negative limitations if the specification explains WHY the absence matters and what happens when the element is absent.

### Mistake 5: Vague Relative Terms
**Bad:** "a substantially large opening"
**Fix:** Define quantitatively: "an opening having a diameter of at least 5 mm" or define "substantially" in the specification.

### Mistake 6: Method Claims for Products
**Bad:** Trying to claim a device by the method of making it when you mean to claim the device itself.
**Fix:** Write both a product claim AND a method claim — they have different scope.

---

## Claim Sets Strategy

For a strong patent application, aim for:

| Claim Type | Number | Purpose |
|------------|--------|---------|
| Independent product claim | 1–2 | Core ownership — broadest scope |
| Independent method claim | 1–2 | Covers manufacturing, use process |
| Independent system claim | 0–1 | For system-level inventions |
| Dependent claims (narrowing) | 8–15 | Fallback positions if independent claim is rejected |

### The "Russian Dolls" Principle
Each dependent claim should be narrower than the one it depends from:
- Independent: The invention's core concept (broadest)
- Dep. 1: Adds preferred material/structure
- Dep. 2: Adds preferred dimension/range
- Dep. 3: Adds optional sub-feature
- Dep. 4: Specific preferred embodiment (narrowest)

If the independent claim is rejected/invalidated, the dependent claims survive as fallbacks.

---

## Vietnamese-Specific Claim Drafting Notes

**Claims in Vietnamese (Yêu cầu bảo hộ):**
- Must be in Vietnamese for NOIP filing
- Use formal legal Vietnamese, not casual language
- Key phrase: "Yêu cầu bảo hộ độc lập" = independent claim
- Key phrase: "Yêu cầu bảo hộ phụ thuộc" = dependent claim

**Vietnamese claim format:**
```
1. [Category] đặc trưng bởi chỗ [it] bao gồm:
   - [element 1] được cấu hình để [function];
   - [element 2] được kết nối với [element 1]; và
   - [element 3] để [purpose].

2. [Category] theo yêu cầu 1, trong đó [specific limitation].
```

**Translation strategy:**
- Draft in English first for conceptual clarity
- Translate to Vietnamese with native legal translator for filing
- Keep English version as internal working document
