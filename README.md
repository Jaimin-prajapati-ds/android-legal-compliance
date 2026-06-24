# Android Legal and Compliance Guard

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: Android](https://img.shields.io/badge/Platform-Android-3DDC84.svg?style=flat&logo=android)](https://developer.android.com)
[![AI Rules: Ready](https://img.shields.io/badge/AI%20Rules-Ready-blueviolet.svg)](#universal-ai-rules)
[![DPDP: 2026/2027 Compliant](https://img.shields.io/badge/India%20DPDP-2027%20Compliant-FF9933.svg)](#global-jurisdictions-covered)
[![GDPR: Compliant](https://img.shields.io/badge/EEA%20GDPR-Compliant-003399.svg)](#global-jurisdictions-covered)

The developer compliance shield for solo and indie Android developers. This toolkit helps you ship applications that avoid regulatory rejection, fines, or store bans globally.

This repository compiles public regulator guidelines, platform developer policies, and security baselines into a pure Markdown-based compliance skill and AI guardrails updated for the 2026/2027 compliance landscape.

---

## Key Features

Android developers face strict, extraterritorial laws. Fines can reach significant amounts (such as 20 million EUR or 4 percent of global turnover under GDPR, and 250 crore INR under India DPDP), and platform policies are enforced automatically.

This repository resolves compliance at the codebase level, providing:
*   **Universal AI Rules (.airules)** - Instruct Cursor, Windsurf, Copilot, Aider, or other AI agents to generate compliant code.
*   **Claude / MCP Skill (SKILL.md)** - A packaged skill folder for Claude Desktop or local LLM assistants.
*   **2026/2027 Global Updates** - Updated for India DPDP Rules, the European Accessibility Act (EAA), and recent Play Store identity verification deadlines.

---

## Directory Structure

```
Repository Root
├── README.md (Landing)
├── .airules (Universal AI Guidelines)
├── SKILL.md (Claude Skill Orchestrator)
└── references/ (Detailed compliance files)
    ├── ad-monetization.md
    ├── app-store-policy.md
    ├── children-accessibility.md
    ├── global-privacy-laws.md
    ├── legal-documents.md
    ├── play-store-policy.md
    ├── prelaunch-audit-checklist.md
    └── security-baseline.md
```

---

## 1. Universal AI Rules (.airules)

Enforce compliance and accessibility by default during AI generation. Drop the `.airules` file into the root of your project:
*   **Automates** permission audits before they are added to AndroidManifest.xml.
*   **Enforces** safe data handling and storage encryption.
*   **Ensures** TalkBack/VoiceOver compatibility in Compose and XML UIs.
*   **Supports Slash Commands:** Type `/privacypolicy` or `/terms` in the chat for dynamic, customized document generation.

---

## 2. Packaged Claude Skill (SKILL.md)

For AI assistants using the Claude desktop app, Antigravity IDE, or similar platforms, you can load this repository folder as a local skill. It uses a core orchestrator SKILL.md and detailed reference modules:

*   [SKILL.md](SKILL.md) - The data inventory checklist and global decision tree.
*   [references/global-privacy-laws.md](references/global-privacy-laws.md) - GDPR, India DPDP, California CCPA/CPRA, LGPD, PIPEDA.
*   [references/play-store-policy.md](references/play-store-policy.md) - Play Store Developer Verification, Contacts Picker Policy, Geofencing.
*   [references/app-store-policy.md](references/app-store-policy.md) - Apple Privacy Nutrition Label and ATT rules.
*   [references/ad-monetization.md](references/ad-monetization.md) - Google UMP SDK, consent parameters, COPPA tags.
*   [references/children-accessibility.md](references/children-accessibility.md) - Families Policy, Age Signals API, European Accessibility Act (EAA).
*   [references/security-baseline.md](references/security-baseline.md) - Secure storage, redacted logging, network config.
*   [references/legal-documents.md](references/legal-documents.md) - Privacy policy and ToS clause reference.
*   [references/prelaunch-audit-checklist.md](references/prelaunch-audit-checklist.md) - Submission audit checklist.

---

## Global Jurisdictions Covered

*   **European Union and UK:** GDPR / ePrivacy Directive. Mandates strict consent, cookie banners, and user deletion rights.
*   **India:** IT Act + Digital Personal Data Protection (DPDP) Act, 2023 and Rules, 2025. Extraterritorial scope. Mandates consent forms, a designated Grievance Officer, and 1-year log retention.
*   **United States:** CCPA/CPRA + patchwork of over 20 state privacy laws (TX, VA, CO, UT, CT, etc.). Mandates "Do Not Sell My Info" and Universal Opt-Out signals.
*   **Brazil:** LGPD. South American equivalent to GDPR.
*   **Canada:** PIPEDA + Quebec Law 25.
*   **Accessibility:** European Accessibility Act (EAA) (enforceable since June 28, 2025). Mandates WCAG 2.1 Level AA compliance for consumer-facing apps in the EU market.

---

## Disclaimer

This project is engineering-focused compliance reference material, not legal advice. Laws, developer terms, and enforcement thresholds evolve constantly. Always cross-reference facts with official government or platform resources. For high-risk applications (e.g. handling biometric data, healthcare, or financial payments), consult a qualified legal professional.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
