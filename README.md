# 🏛️ News Article Text Analyzer

<div align="left">
  <img src="https://img.shields.io/badge/Moringa_School-Summative_Lab-800020?style=for-the-badge&logoColor=white" alt="School" />
  <img src="https://img.shields.io/badge/LANGUAGE-Python3.12-1a1a1a?style=for-the-badge&logoColor=white" alt="Environment" />
  <img src="https://img.shields.io/badge/Author-Oliver Kiplagat-2c003e?style=for-the-badge&logoColor=white" alt="Theme" />
</div>

---

### 📋 Project Overview
Imagine cracking open a massive news article. To the human eye, it’s just rows of paragraphs. But to a developer, it is a playground of patterns, hidden trends, and data insights waiting to be uncovered.

This repository houses pythonAssessment.py , a lightweight, intelligent News Text Analysis Engine built entirely from the ground up using pure Python. Instead of forcing you to manually skim through endless lines of copy, this application acts as your automated digital editor. It instantly breaks down raw articles to map out their DNA, calculating everything from structural counts to word popularity in real time.

### How It Works: The Interactive Experience
We didn’t want a boring script that just runs once and shuts down. Instead, the application boots up into a live, interactive terminal command center. Driven by a continuous control loop, it lets you seamlessly query the text and run deep analytics with simple menu choices:

 >(i): Smart Word Tracker – Lock onto any specific word (like "ACME" or "Apple") and see exactly how many times the author used it, completely ignoring capitalization or trick punctuation.

 >(ii): The Frequency Champion – Automatically sifts through the entire article to locate the single most heavily used word, ignoring distracting punctuation clutter.

 >(iii): Text Readability Metric – Computes the true mathematical average length of the words used, giving you an instant feel for the article's reading complexity.

 >(iv): Layout Parser – Scans the visual structure of the document to count genuine paragraphs while filtering out accidental white space and "ghost lines."

>(v): Structural Sentence Counter – Intelligently tracks punctuation boundaries to tally every full sentence across the narrative.

---

### ⚙️ Data Pipeline & Storage Framework

The program processes data through a structured pipeline, streaming content from physical disk architecture directly into short-term execution memory (RAM).

```text
📁 Physical Disk (article.txt) ──[ Safe UTF-8 Stream ]──> 🧠 Python RAM Canvas (article_text)
                                                                 │
                                                    ┌────────────┴────────────┐
                                             [ File Found ]             [ File Missing ]
                                                    │                         │
                                            Read Raw Content            Load Hardcoded
                                              From Storage              Backup Dataset