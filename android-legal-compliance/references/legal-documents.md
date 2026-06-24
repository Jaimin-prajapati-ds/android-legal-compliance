# Legal Documents — AI-Driven Policy Generation Guide

To comply with the user request to avoid static templates and support AI-driven generation, this document serves as the guide for the AI (and developers) to dynamically draft **Privacy Policies** and **Terms of Service** tailored specifically to the app's configuration.

---

## 📄 Privacy Policy Dynamic Generation

When creating a Privacy Policy, the AI must collect the app's metadata (from the Data Inventory step) and compile the following mandatory sections:

### 1. Developer Identity & Contact
- **Format**: Must specify the developer or entity name *exactly as it appears on the Google Play Console / Apple App Store listing*.
- **Contact**: Provide a dedicated email for privacy inquiries.
- **India DPDP Grievance Officer**: For Indian users, include the name, designation, and contact details of the Grievance Officer.

### 2. Data Collected & Specific Mappings
- Do not write a generic statement like "we collect some data to improve the app."
- Instead, map each permission/identifier to a concrete function:
  - *Example*: "Precise location data (GPS) is processed locally on your device to calculate running speed. We do not upload location coordinates to our servers."
  - *Example*: "Google Advertising ID (AAID) is shared with Google AdMob to serve contextual and personalized ads (based on user consent choices)."

### 3. Third-Party Data Sharing Table
- Explicitly list the third-party SDKs integrated into the codebase:
  - Analytics (e.g., Firebase Analytics)
  - Ads (e.g., Google AdMob, AppLovin)
  - Crash Reporting (e.g., Crashlytics)
- Provide links to each partner's privacy policy.

### 4. User Rights & Choices (Cross-Border Compliance)
- Detail rights based on region:
  - **GDPR (Europe)**: Right to access, correct, delete, port, and withdraw consent.
  - **CCPA/CPRA (US)**: Right to know, delete, correct, and opt-out of the "sale or sharing" of personal information (including supporting Global Privacy Control signals).
  - **DPDP (India)**: Right to access summary of data, correct, erase, and register grievances.

### 5. Data Retention & Deletion Instructions
- Specify the retention period for each data type.
- Include the **India DPDP 2025 requirement of 1-year log retention** (retaining server logs for a minimum of 1 year).
- Provide a clear instruction on how users can request account and data deletion (including the mandatory web deletion link).

### 6. Children's Data Policy
- Explicitly state whether the app is directed to children or if it collects data from minors. If mixed-audience, explain how parental consent or age gating is handled.

---

## 📄 Terms of Service / EULA Dynamic Generation

When generating the Terms of Service, the AI must ensure the following clauses are drafted:

### 1. License Grant & Restrictions
- Grant the user a non-exclusive, non-transferable, revocable license to use the app for personal, non-commercial purposes.
- Restrict reverse engineering, copying, or distributing the app binary.

### 2. Intellectual Property (IP)
- State that you (the developer) own all intellectual property rights, trademarks, source code, and design assets.

### 3. Subscription & In-App Purchases (If Applicable)
- Detail subscription auto-renewals, trial terms, and link billing/refund disputes to the respective platform store policies (Google Play or Apple App Store).

### 4. Critical Warranty Disclaimers
- State that the app is provided "as is" and "as available," without any warranties of any kind.
- **Health & Fitness Apps Disclaimer**: Disclaim medical advice. State that the app is for general fitness purposes and users should consult a physician before starting any training program.
- **Financial/Information Apps Disclaimer**: Disclaim financial liability. State that the data provided is for informational purposes only.

### 5. Governing Law & Jurisdiction
- Define the legal jurisdiction (typically the developer's home country/state, e.g., India, California, etc.).
