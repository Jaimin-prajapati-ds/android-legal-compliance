# Google Play Developer Program Policy — Reference

Read this when submitting, updating, or auditing any app on the Google Play Store. These rules are enforced automatically by Google's automated scanners and manual reviewers.

---

## 1. Stricter Developer Identity Verification (2026–2027)

Google is implementing mandatory identity verification for developers to ensure security on Android devices.
- **Deadlines**:
  - **September 30, 2026**: Verification is mandatory for developers distributing apps in **Brazil, Indonesia, Singapore, and Thailand**.
  - **Throughout 2027**: Rolled out globally to all developers in all countries.
- **Impact**: Apps published by developers who fail to complete verification by the deadline will be **blocked from installation** on certified Android devices (affecting both Play Store and side-loaded distribution).
- **Exceptions**: Managed Work Profiles and private enterprise applications (via EMM/DPC) are temporarily exempt until September 2027, with certain Managed Google Play apps exempt indefinitely.

---

## 2. Contacts Permissions Policy (Effective October 28, 2026)

Google is restricting broad contact list access to protect user privacy.
- **The Rule**: Apps requiring contact access must use the system **Android Contact Picker** instead of requesting the broad `READ_CONTACTS` permission in the manifest, unless broad access is strictly necessary and justified.
- **Implementation**:
  - If your app needs a user to select a contact, do **NOT** request `android.permission.READ_CONTACTS`.
  - Instead, launch the contact picker using `ActivityResultContracts.PickContact` (which lets the user select a single contact securely without granting broad read permissions).
- **Justification**: If you believe your app requires full contact access (e.g., sync contacts feature in social apps), you must submit a declaration form to Google explaining the core feature.

---

## 3. Location Permissions & Geofencing (Effective October 28, 2026)

Google enforces strict limits on background and foreground location access.
- **Geofencing Limit**: Geofencing is **no longer approved** as a foreground service use case. If you need geofencing, you must use the official **Google Play Services Geofence API**.
- **Location Scope**: Google recommends using the standard in-app location buttons to request the minimum precise/coarse location scope necessary.
- **Background Location**: Background location (`ACCESS_BACKGROUND_LOCATION`) remains highly restricted. You must provide a prominent in-app disclosure video explaining why background access is essential to the core functionality.

---

## 4. Target SDK Version Requirements

Google Play requires apps to target recent Android API versions to ensure security.
- **Timeline**:
  - **August 31, 2026**: All new apps and app updates must target **API 35 (Android 15) or API 36 (Android 16)**.
  - **Existing Apps**: Apps already in the store must target within 2 years of the latest release (API 34/35) to remain visible and installable for new users on newer devices.
- **Action**: Check your `app/build.gradle` or `build.gradle.kts` and ensure `targetSdk` is set to the compliant level.

---

## 5. Account Deletion Policy

If your app allows users to create an account, you must provide a deletion path.
- **Requirements**:
  - **In-App Deletion**: A clear, easily accessible button or menu option within the app (e.g., in Settings or Profile) to delete the account and its associated personal data.
  - **Web Deletion**: A public, working URL where a user can request account and data deletion online (without needing to reinstall the app).
  - Both paths must be declared in the Play Console under **App Content → Account Deletion**.
- **Data Retention Exceptions**: If you must keep certain data for compliance, tax, or legal reasons (such as financial logs), disclose this clearly in your deletion flow and Privacy Policy.

---

## 6. Play Store Data Safety Form

Developers must accurately declare what data is collected and shared.
- **What is "Collected"?**: Data transmitted off the device and stored for longer than is necessary to service the request in real time.
- **What is "Shared"?**: Data transferred to a third party (including third-party SDKs) for their own purposes.
- **SDK Impact**: You are legally responsible for whatever data your third-party SDKs (AdMob, Firebase, analytics, etc.) collect. Check the **Play SDK Index** for the policies of the specific SDK versions you import.

---

## 7. Families Policy (App Targets Children)

If children under 13 (US) or under 18 (some EU/EEA countries) are part of your target audience:
- You must use **self-certified SDKs** listed on Google's approved list for Families.
- You must not collect precise location, identifiers, or show personalized ads to children.
- You must utilize the **Age Signals API** if the app has a mixed-age audience.
