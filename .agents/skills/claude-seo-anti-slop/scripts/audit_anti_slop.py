#!/usr/bin/env python3
"""
AI Slop & Anti-Cliché SEO Auditor
Scans content (Markdown, Plain Text, or HTML) for AI clichés, filler phrasing,
fake promises, robotic patterns, and blocked words.
"""

import sys
import re
import json
import os
from pathlib import Path

# Ensure UTF-8 output encoding for Windows command line compatibility
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

RESOURCE_DIR = Path(__file__).resolve().parent.parent / "resources"
BANNED_WORDS_FILE = RESOURCE_DIR / "banned_words.json"

def load_banned_data():
    if BANNED_WORDS_FILE.exists():
        with open(BANNED_WORDS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def strip_html_tags(text):
    clean = re.compile(r'<.*?>')
    return re.sub(clean, ' ', text)

def audit_content(text):
    banned_data = load_banned_data()
    all_categories = banned_data.get("banned_words_and_phrases", {})
    replacements = banned_data.get("replacements", {})

    clean_text = strip_html_tags(text)
    lower_text = clean_text.lower()
    total_words = len(re.findall(r'\b\w+\b', clean_text)) or 1

    findings = {}
    total_slop_hits = 0

    for category, phrases in all_categories.items():
        matched = []
        for phrase in phrases:
            # Word boundary regex for single words or exact phrases
            pattern = r'\b' + re.escape(phrase.lower()) + r'\b'
            matches = list(re.finditer(pattern, lower_text))
            if matches:
                count = len(matches)
                matched.append({"phrase": phrase, "count": count})
                total_slop_hits += count
        if matched:
            findings[category] = matched

    # Check structural AI patterns
    structural_issues = []
    
    # 1. Preamble sentences before lists
    list_preambles = re.findall(r'(here are (?:a few|some|the|several) key (?:points|benefits|steps|takeaways)[\s\S]{0,10}:)', lower_text)
    if list_preambles:
        structural_issues.append(f"AI List Preamble detected ({len(list_preambles)} occurrences): e.g., '{list_preambles[0]}'. Direct answers preferred.")
        total_slop_hits += len(list_preambles) * 2

    # 2. Robotic symmetrical bold lists: e.g. - **Title**: Description
    symmetrical_bullets = len(re.findall(r'^\s*[-*]\s+\*\*[^*]+\*\*:', text, re.MULTILINE))
    if symmetrical_bullets >= 4:
        structural_issues.append(f"Heavy symmetrical bullet structure detected ({symmetrical_bullets} items). High AI-fingerprint.")
        total_slop_hits += 2

    # 3. Fluff conclusions
    conclusions = re.findall(r'#+\s*(?:in conclusion|final thoughts|wrapping up|summary|wrapping it up)\b', lower_text)
    if conclusions:
        structural_issues.append("Generic conclusion heading ('In Conclusion / Final Thoughts'). Replace with clear action steps or summary table.")
        total_slop_hits += 3

    # Calculate Slop Score
    # Slop Density per 100 words
    slop_density = (total_slop_hits / total_words) * 100
    if slop_density == 0:
        score_label = "CLEAN (100% Human Feel)"
        verdict = "PASSED: Content is crisp, direct, and free from AI clichés."
    elif slop_density < 0.8:
        score_label = "LOW AI SLOP (Minor cleanup recommended)"
        verdict = "WARNING: Few AI filler phrases found."
    elif slop_density < 2.0:
        score_label = "MODERATE AI SLOP (Obvious AI fingerprint)"
        verdict = "REJECTED: Contains noticeable AI filler, transitions, or clichés."
    else:
        score_label = "HEAVY AI SLOP (Critical Google Spam/E-E-A-T Risk)"
        verdict = "CRITICAL FAIL: Saturated with AI filler, fake promises, and fluff."

    return {
        "total_words": total_words,
        "total_slop_hits": total_slop_hits,
        "slop_density_pct": round(slop_density, 2),
        "score_label": score_label,
        "verdict": verdict,
        "findings": findings,
        "structural_issues": structural_issues,
        "replacements": replacements
    }

def print_report(res):
    print("\n" + "="*60)
    print(" 🛡️  CLAUDE SEO & ANTI-AI-SLOP AUDIT REPORT")
    print("="*60)
    print(f"Total Words Analyzed: {res['total_words']}")
    print(f"AI Slop Hits:        {res['total_slop_hits']}")
    print(f"Slop Density:        {res['slop_density_pct']}%")
    print(f"Overall Rating:      {res['score_label']}")
    print(f"Verdict:             {res['verdict']}")
    print("-" * 60)

    if res['structural_issues']:
        print("\n⚠️  STRUCTURAL AI PATTERNS:")
        for issue in res['structural_issues']:
            print(f"  • {issue}")

    if res['findings']:
        print("\n🚫 DETECTED CLICHÉS & BANNED PHRASES:")
        for cat, items in res['findings'].items():
            cat_name = cat.replace("_", " ").title()
            print(f"\n  [{cat_name}]:")
            for it in items:
                print(f"    - \"{it['phrase']}\" ({it['count']}x)")

    print("\n💡 RECOMMENDED REPLACEMENTS & FIXES:")
    for key, repl in res['replacements'].items():
        print(f"  • Replace '{key}' → {repl}")
    print("="*60 + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python audit_anti_slop.py <path-to-file-or-string>")
        sys.exit(1)

    target = sys.argv[1]
    if os.path.exists(target):
        with open(target, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    else:
        content = target

    result = audit_content(content)
    print_report(result)
