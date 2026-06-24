# android-legal-compliance

A Claude **Skill** (and plain reference doc) that walks an AI coding agent — or a human — through every legal/privacy/store-policy obligation an Android (or cross-platform) app needs before going live: GDPR, India's DPDP Act, CCPA/US state laws, COPPA, Google Play Developer Program Policy, Apple App Store rules, AdMob/ad-consent, children's privacy, accessibility law, and a security baseline.

Built for solo/indie developers shipping fast with AI coding tools who still need to not get an app rejected, fined, or banned.

## What's inside

```
android-legal-compliance/
├── SKILL.md                              # orchestrator: data inventory → decision tree → universal baseline
└── references/
    ├── global-privacy-laws.md            # GDPR, CCPA/CPRA + 20-state US patchwork, India DPDP, LGPD, PIPEDA
    ├── play-store-policy.md              # Data Safety form, account deletion, permissions, Families, target API
    ├── app-store-policy.md               # Apple Privacy Nutrition Label, ATT, 2026 review focus areas
    ├── ad-monetization.md                # AdMob UMP SDK, GDPR/CCPA consent signals, TFUA for children
    ├── children-accessibility.md         # COPPA 2025 amendments, Families Policy, EAA/WCAG
    ├── security-baseline.md              # secrets, encrypted storage, network security config, logging
    ├── legal-documents.md                # required Privacy Policy / ToS clauses + hosting
    └── prelaunch-audit-checklist.md      # final mechanical checklist before every Play Console submission
```

## How to use it

### As a Claude Skill
Drop the `android-legal-compliance/` folder into your Claude Skills directory (or upload the packaged `.skill` file). Claude will automatically consult it whenever you're building an app, adding a permission/SDK, writing a privacy policy, or about to submit to Play Console.

### As a plain checklist
Just read `SKILL.md` top to bottom, then jump into whichever `references/*.md` file your app's Decision Tree (Step 2) flags as relevant.

### With any other AI coding agent (Cursor, Windsurf, Antigravity, etc.)
Paste `SKILL.md` (and the relevant reference file) into the agent's context before asking it to wire up Data Safety answers, a privacy policy page, or a `network_security_config.xml`.

## Status / maintenance

Laws and platform policies in here are accurate as compiled in **mid-2026** — thresholds, deadlines, and required SDK versions shift roughly every 6–12 months (Google Play policy alone updates 2–4 times a year). Each reference file ends with a **Source note** pointing to where the facts came from — re-verify against the live source before relying on a specific number, date, or threshold in a real dispute.

## Disclaimer

This is engineering/compliance guidance, **not legal advice**. For anything high-stakes — health/biometric data at scale, an active regulator inquiry, cross-border fintech, or drafting a contract — talk to an actual lawyer in the relevant jurisdiction.

## License

MIT — see `LICENSE`. Use it, fork it, send a PR if a policy/law in here has changed.
