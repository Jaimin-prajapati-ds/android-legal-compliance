# Security Baseline — Reference

Most global privacy laws require "reasonable security safeguards" without defining exact technical controls. This reference details the practical, Android-specific security baseline that satisfies GDPR, CCPA/CPRA, and India DPDP simultaneously.

---

## 1. Network Communications & HTTPS

You must secure all data in transit. On Android 9 (API 28) and higher, cleartext HTTP traffic is blocked by default.
- **The Rule**: Never permit cleartext HTTP traffic (`cleartextTrafficPermitted="true"`) in production.
- **Action**: Create a production Network Security Config file and link it in your `AndroidManifest.xml` application tag:
  ```xml
  <application
      android:networkSecurityConfig="@xml/network_security_config"
      ... >
  ```
- **network_security_config.xml (Production)**:
  ```xml
  <?xml version="1.0" encoding="utf-8"?>
  <network-security-config>
      <!-- Force HTTPS for all domains -->
      <base-config cleartextTrafficPermitted="false" />
  </network-security-config>
  ```
- **Local Development**: If you need to test local APIs on localhost or an emulator:
  - Create a separate config for debug builds or use specific domain overrides:
    ```xml
    <network-security-config>
        <base-config cleartextTrafficPermitted="false" />
        <!-- Permit cleartext traffic ONLY for local debugging -->
        <domain-config cleartextTrafficPermitted="true">
            <domain includeSubdomains="true">localhost</domain>
            <domain includeSubdomains="true">10.0.2.2</domain> <!-- Android Emulator loopback -->
        </domain-config>
    </network-security-config>
    ```

---

## 2. Secure Local Storage

Never store access tokens, Firebase API keys (that are sensitive), or user personal data in plain text.
- **Jetpack Security**: Use `EncryptedSharedPreferences` for basic key-value data:
  ```kotlin
  import androidx.security.crypto.EncryptedSharedPreferences
  import androidx.security.crypto.MasterKeys

  val masterKeyAlias = MasterKeys.getOrCreate(MasterKeys.AES256_GCM_SPEC)
  val sharedPreferences = EncryptedSharedPreferences.create(
      "secure_prefs",
      masterKeyAlias,
      context,
      EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
      EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
  )

  // Write securely
  sharedPreferences.edit().putString("auth_token", token).apply()
  ```
- **Android Keystore**: For large files or databases, use SQLite encryption (SQLCipher) backed by keys managed in the Android Keystore.

---

## 3. Redacted Logging & Crash Reports

Leakage of personal data (PII) or credentials into Logcat or crash reporting systems is a common compliance violation.
- **Rules**:
  - Strip authorization tokens, passwords, and PII (email, location) from debug logs.
  - Wrap your logging library (e.g., Timber) to disable logging completely in release builds:
    ```kotlin
    if (BuildConfig.DEBUG) {
        Timber.plant(Timber.DebugTree())
    }
    ```
  - Ensure ProGuard / R8 rules strip out log calls and class metadata from release builds to prevent reverse engineering.

---

## 4. Play SDK Index Verification

Third-party libraries are a primary source of data leakage.
- **Action**: Before importing any library or SDK into your `build.gradle`, search the **Play SDK Index** (developer.android.com/distribute/sdk-index).
- **Checks**: Verify that the SDK does not contain active policy warnings or outdated SDK versions that continue to fetch non-compliant device identifiers (like MAC addresses or IMEI numbers).

---

## 5. India DPDP Log Retention Rule

- **The Rule**: Under India's DPDP Rules 2025, data fiduciaries must retain **processing logs, transaction details, and traffic data for at least 1 year** from the date of processing for regulatory audit purposes.
- **Backend Setup**: Ensure your backend databases, hosting providers (e.g. Firebase Cloud Functions, AWS CloudWatch, Supabase), or server infrastructure maintain secure access logs for a minimum of 1 year, even if the user's primary personal profile is deleted upon request.
