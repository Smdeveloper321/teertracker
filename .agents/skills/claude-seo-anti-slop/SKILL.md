---
name: claude-seo-anti-slop
description: Claude-style SEO & Anti-AI-Slop content generation and audit skill. Eliminates AI fluff, filler phrases, fake promises, overused AI clichés/patterns, and robotic UI slop to produce high-EEAT, human-sounding, search-intent driven content that ranks and avoids Google AI spam penalties.
---

# Claude SEO & Anti-AI-Slop Framework

A systematic guide and toolkit to produce human-grade, high-ranking SEO content while eradicating AI-generated fluff, repetitive filler, empty promises, robotic UI layouts, and overused AI buzzwords.

---

## The Core Philosophy (Claude / Anthropic Approach)

> **"If a sentence does not deliver new information, answer a direct question, or provide specific proof, cut it."**

Standard AI outputs suffer from a predictable fingerprint: breathlessness, generic throat-clearing intros, symmetrical bullet points, and empty cheerleading. Google's Search Quality Rater guidelines and post-leak ranking algorithms aggressively penalize these patterns for lack of **Information Gain** and low **E-E-A-T** (Experience, Expertise, Authoritativeness, Trustworthiness).

---

## The 6 Anti-Slop Pillars

### 1. Zero Filler & Throat-Clearing Intros
* **Never use preamble openings:**
  * ❌ *"In today's fast-paced digital world..."*
  * ❌ *"Whether you are a seasoned expert or just starting out..."*
  * ❌ *"Have you ever wondered how XYZ works? Well, you're in the right place!"*
* **The Rule:** Begin immediately with the direct answer or core finding (Inverted Pyramid style). The first two sentences must directly address the target search query for Google Snippet capture.

### 2. Strict Exclusion of Fake Promises
* **Never make empty hype claims:**
  * ❌ *"Read on to discover the ultimate secret that will blow your mind."*
  * ❌ *"In this comprehensive, step-by-step master guide, we will unlock everything you need to know."*
  * ❌ *"Prepare to transform your entire workflow forever."*
* **The Rule:** State exactly what is covered without theatrical suspense:
  * ✔️ *"Here is the exact cost breakdown and step-by-step method to calculate net hourly wage in Germany for 2026."*

### 3. Elimination of AI UI Slop (Clean UX / Layout)
When designing web pages, affiliate landing pages, or tools:
* **No meaningless decorative cards:** Avoid 4 identical boxes with stock-like icons ("Fast", "Secure", "Reliable", "24/7").
* **No fake social proof:** Remove arbitrary counter bars or meaningless percentages (*"99.8% customer satisfaction rating"* with no source).
* **Prioritize content density:** Put the primary functional element (the calculator, the coupon table, the translator, the answer) **above the fold**.
* **Clean typography over widget bloat:** High readability, fast DOM load, zero obstructive popups or aggressive floating ads during initial inspection.

### 4. Breaking Robotic AI Formatting Patterns
AI models default to repetitive visual rhythms. You must actively break them:
* **No Symmetrical Bullet Trains:** Do NOT produce 5 bullet points that all follow the exact formula: `**[Adjective] [Noun]**: [Two lines of generic explanation].`
* **Vary Sentence Lengths (Rhythm):** Mix punchy 4-word sentences with longer technical explanations. Never keep every sentence between 15-20 words.
* **No Redundant Conclusion Sections:**
  * ❌ Avoid sections titled `## In Conclusion`, `## Final Thoughts`, `## Wrapping Up` that merely repeat the preceding headings.
  * ✔️ End with actionable next steps, a downloadable checklist, or a comparison table.
* **No Transition Signposts:** Eliminate *"Furthermore"*, *"Moreover"*, *"In addition to this"*, *"Last but not least"*. Just start the sentence.

### 5. Blocked Words & AI Cliché Blacklist
Never use these flagged words in SEO or content generation. Use human alternatives:

| Category | Banned AI Words | Direct Human Replacement |
| :--- | :--- | :--- |
| **Fluff Verbs** | *delve, embark, unleash, harness, foster, elevate, revolutionize, navigate, demystify, transcend* | look at, test, use, build, check, examine, improve |
| **Fluff Nouns** | *tapestry, beacon, testament, landscape, realm, paradigm, synergy, plethora, game-changer, powerhouse* | system, market, area, collection, tool, big change, proof |
| **Overused Adjectives** | *crucial, pivotal, paramount, bustling, vibrant, multifaceted, seamless, cutting-edge, groundbreaking* | key, vital, important, fast, direct (or state the actual benefit) |
| **Empty Transitions** | *furthermore, moreover, needless to say, it is worth noting, first and foremost, with that being said* | also, plus, and, or omit completely |
| **Fake Suspense** | *look no further, we've got you covered, buckle up, dive right in* | Delete entirely. Jump straight into the facts. |

---

## 6. Information Gain & E-E-A-T Optimization

To rank under Google's modern Search API signals, every piece of content must contain at least **three Information Gain elements**:
1. **Specific Real-World Data:** Real pricing ($), exact dates, statutory law citations, or tax brackets (not approximations).
2. **Edge Cases & Disclaimers:** Explain when a solution fails or who it is *not* suitable for. Pure AI writes cheerleading; human experts mention caveats.
3. **Structured Comparison Tables:** Present attributes side-by-side rather than in vague paragraphs.

---

## How to Audit Any Content with the Built-in Script

Run the automated validator to scan any text or markdown file for AI slop score:

```powershell
python "C:\Users\AJ Developer\.gemini\config\skills\claude-seo-anti-slop\scripts\audit_anti_slop.py" "<file-path-or-text>"
```

### Interpretation of Results:
* **0% Slop Density (Clean):** 100% human voice, safe from AI pattern filters.
* **< 0.8% Slop Density:** Minor cleanup required.
* **> 1.5% Slop Density:** Rejected. High risk of search demotion and AI detection flags.

---

## Prompt Template for Writing Anti-Slop SEO Content

Whenever generating articles or web copy, prepend this directive:

```markdown
Write in a direct, authoritative, human voice. 
- Answer the search query in the first 2 sentences without throat-clearing.
- Never use the words: delve, tapestry, testament, crucial, pivotal, landscape, realm, furthermore, moreover, seamless.
- No fake promises or clickbait suspense.
- Do not use symmetrical bold bullet lists; use natural paragraphs and tables.
- Include specific numbers, real constraints, and edge cases to maximize Google Information Gain.
- End with actionable next steps, NOT an "In conclusion" summary.
```
