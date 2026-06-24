# Pre-Launch Compliance Audit Checklist

Run this final checklist top to bottom before uploading your app bundle (.aab) to Google Play Console or Apple App Store Connect.

---

## 💻 Step 1: Run the Automated Scanner
- [ ] Run the compliance auditor in your project directory:
  ```bash
  python scripts/audit.py .
  ```
- [ ] Resolve all **Critical Risks** (violations) reported by the scanner.
- [ ] Review and address all **Warnings**.

---

## 🔒 Step 2: Security & Storage Checks
- [ ] Verify that `cleartextTrafficPermitted="false"` is set in the release Network Security Config.
- [ ] Confirm no secrets, API keys, keystores, or password strings are committed to your git history.
- [ ] Ensure `EncryptedSharedPreferences` is used for authentication tokens or user PII.
- [ ] Confirm that log streams (Logcat, Timber) redact PII and tokens in release builds.
- [ ] Check that all third-party SDKs have clean status indicators in the Play SDK Index.

---

## 🛠️ Step 3: Permissions & Features
- [ ] If you read contacts, confirm you use the **Android Contact Picker** instead of requesting `READ_CONTACTS`.
- [ ] If accessing location, ensure precise location requests are accompanied by coarse options, and geofencing uses the Google Play Geofencing API.
- [ ] If the app allows user sign-ups, confirm that the in-app account deletion button and the web deletion link are fully functional.

---

## 📄 Step 4: Legal & Policy Disclosures
- [ ] Ask the AI to write your customized Privacy Policy dynamically (using `/privacypolicy` command).
- [ ] Publish the Privacy Policy at a stable, public URL (e.g., GitHub Pages).
- [ ] Verify that the developer name in the Privacy Policy matches your console developer profile exactly.
- [ ] Verify that the Privacy Policy includes a section on **India's DPDP Rules 2025 (1-year log retention)** and names a Grievance Officer.
- [ ] Complete the **Data Safety Form** in the Google Play Console, declaring all data collected by your code and third-party SDKs.

---

## 🌍 Step 5: Global Minor & Accessibility Checks
- [ ] If targeting children under 13 (or under 18 in EEA/India), verify that all ad SDKs are configured with child-directed tags, location tracking is disabled, and social logins are hidden.
- [ ] Under EAA compliance, verify that all Jetpack Compose or XML layout images have `contentDescription` attributes (or are set to null if decorative).
- [ ] Verify that all text sizes use scale-independent pixels (`sp`) and layouts adapt gracefully to 200% font scaling.
- [ ] Confirm all touch targets meet the minimum `48.dp` x `48.dp` layout recommendation.
