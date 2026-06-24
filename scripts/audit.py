#!/usr/bin/env python3
import os
import sys
import re
import xml.etree.ElementTree as ET

# ANSI Colors for console output
COLOR_RESET = "\033[0m"
COLOR_BOLD = "\033[1m"
COLOR_RED = "\033[91m"
COLOR_YELLOW = "\033[93m"
COLOR_GREEN = "\033[92m"
COLOR_BLUE = "\033[94m"

def print_header(title):
    print(f"\n{COLOR_BOLD}{COLOR_BLUE}=== {title} ==={COLOR_RESET}")

def print_success(message):
    print(f"  {COLOR_GREEN}[OK] {message}{COLOR_RESET}")

def print_warning(title, desc):
    print(f"  {COLOR_YELLOW}[WARN] {COLOR_BOLD}{title}{COLOR_RESET}")
    print(f"    {desc}")

def print_error(title, desc):
    print(f"  {COLOR_RED}[FAIL] {COLOR_BOLD}{title}{COLOR_RESET}")
    print(f"    {desc}")

class ComplianceAuditor:
    def __init__(self, project_dir):
        self.project_dir = os.path.abspath(project_dir)
        self.manifests = []
        self.gradles = []
        self.net_configs = []
        self.violations_count = 0
        self.warnings_count = 0
        self.passes_count = 0
        
        # Lists to store findings for markdown generation
        self.violations = []
        self.warnings = []
        self.passes = []

    def log_success(self, title):
        self.passes_count += 1
        self.passes.append(title)
        print_success(title)

    def log_warning(self, title, desc):
        self.warnings_count += 1
        self.warnings.append((title, desc))
        print_warning(title, desc)

    def log_error(self, title, desc):
        self.violations_count += 1
        self.violations.append((title, desc))
        print_error(title, desc)

    def scan_files(self):
        """Scans the directory for manifest, gradle, and network security files."""
        for root, dirs, files in os.walk(self.project_dir):
            if any(p in root.replace(self.project_dir, "") for p in [".gradle", ".git", "build", "app/build", "bin", "obj", "mock_project"]):
                continue
            for file in files:
                full_path = os.path.join(root, file)
                if file == "AndroidManifest.xml":
                    self.manifests.append(full_path)
                elif file in ("build.gradle", "build.gradle.kts"):
                    self.gradles.append(full_path)
                elif file == "network_security_config.xml":
                    self.net_configs.append(full_path)

    def audit(self):
        print(f"{COLOR_BOLD}Scanning directory: {self.project_dir}{COLOR_RESET}")
        self.scan_files()
        
        if not self.manifests and not self.gradles:
            print_error("No Android Files Found", "Could not find any AndroidManifest.xml or build.gradle files in this folder. Make sure you point to the Android project root.")
            return False

        self.audit_gradle()
        self.audit_manifests()
        self.audit_network_security()

        # Generate local markdown checklist file
        self.generate_markdown_report()

        # Print final summary
        print_header("AUDIT SUMMARY")
        print(f"  Passed Checks:  {COLOR_GREEN}{self.passes_count}{COLOR_RESET}")
        print(f"  Warnings:       {COLOR_YELLOW}{self.warnings_count}{COLOR_RESET}")
        print(f"  Critical Risks: {COLOR_RED}{self.violations_count}{COLOR_RESET}")

        if self.violations_count > 0:
            print(f"\n{COLOR_RED}{COLOR_BOLD}[FAIL] COMPLIANCE FAIL: Your app has critical risk factors that may lead to Play Store rejection or legal fines.{COLOR_RESET}")
            return False
        elif self.warnings_count > 0:
            print(f"\n{COLOR_YELLOW}{COLOR_BOLD}[WARN] COMPLIANCE WARNING: Review the warning flags above before publishing your app.{COLOR_RESET}")
            return True
        else:
            print(f"\n{COLOR_GREEN}{COLOR_BOLD}[PASS] COMPLIANCE PASS: No critical compliance or security risks detected!{COLOR_RESET}")
            return True

    def audit_gradle(self):
        print_header("Gradle Configuration Audit")
        
        target_sdk = None
        has_ads = False
        has_auth = False
        
        for gradle_path in self.gradles:
            try:
                with open(gradle_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    
                    # Regex for targetSdk or targetSdkVersion
                    match_sdk = re.search(r"targetSdk(?:Version)?\s*=?\s*(\d+)", content)
                    if match_sdk:
                        target_sdk = int(match_sdk.group(1))
                        
                    # Check for SDK dependencies
                    if "play-services-ads" in content or "google-mobile-ads" in content:
                        has_ads = True
                    if "firebase-auth" in content or "play-services-auth" in content:
                        has_auth = True
            except Exception as e:
                self.log_error(f"Failed to read Gradle: {os.path.basename(gradle_path)}", str(e))

        if target_sdk:
            if target_sdk < 34:
                self.log_error(
                    f"Outdated Target SDK Level (API {target_sdk})",
                    "Google Play requires apps to target at least API 34 (Android 14) for updates in 2026. Target API 35/36 for late 2026 updates.\n"
                    "Action: Update targetSdk to 34 or higher in build.gradle."
                )
            else:
                self.log_success(f"Target SDK Version is API {target_sdk} (Compliant)")
        else:
            self.log_warning("Target SDK Version Not Found in Gradle", "Could not verify targetSdkVersion programmatically. Ensure it is set to API 34+.")

        if has_ads:
            self.log_warning(
                "Ad Network Detected (AdMob)",
                "Your Gradle config contains AdMob dependencies. Under EEA GDPR rules, you MUST implement Google's User Messaging Platform (UMP) SDK for certified consent.\n"
                "Action: Verify that UMP SDK consent flows are integrated and active in EEA countries."
            )
            
        if has_auth:
            self.log_warning(
                "Authentication Detected",
                "Your Gradle config contains sign-in / authentication libraries. Google Play requires a working in-app account deletion path AND an external web deletion link.\n"
                "Action: Implement both deletion channels and configure them in Play Console under App Content."
            )

    def audit_manifests(self):
        print_header("Manifest & Permissions Audit")
        
        for manifest_path in self.manifests:
            try:
                ET.register_namespace('android', 'http://schemas.android.com/apk/res/android')
                tree = ET.parse(manifest_path)
                root = tree.getroot()
                
                # Fetch all declared permissions
                permissions = []
                for perm in root.findall("uses-permission"):
                    name = perm.attrib.get("{http://schemas.android.com/apk/res/android}name")
                    if name:
                        permissions.append(name)
                        
                # 1. Contacts Permission Check
                if "android.permission.READ_CONTACTS" in permissions or "android.permission.WRITE_CONTACTS" in permissions:
                    self.log_error(
                        "Dangerous Contacts Permission Declared",
                        "The READ/WRITE_CONTACTS permissions are heavily restricted under Google Play's 2026/2027 policies.\n"
                        "Action: Migrate to the Android Contact Picker (using ActivityResultContracts.PickContact) which does not require permission declarations."
                    )
                else:
                    self.log_success("No broad Contacts read/write permissions declared (Compliant)")

                # 2. Location Permissions
                if "android.permission.ACCESS_FINE_LOCATION" in permissions:
                    self.log_warning(
                        "Precise Location Access",
                        "Your app requests ACCESS_FINE_LOCATION. Ensure that you request ACCESS_COARSE_LOCATION concurrently.\n"
                        "Also note that geofencing is restricted from foreground services; use the Google Play Services Geofence API."
                    )
                if "android.permission.ACCESS_BACKGROUND_LOCATION" in permissions:
                    self.log_error(
                        "Background Location Access Requested",
                        "Background location is subject to severe Play Store reviews, high rejection rates, and strict privacy scrutiny.\n"
                        "Action: Ensure you submit a detailed Prominent Disclosure video to Play Console or remove background access."
                    )

                # 3. Storage Permissions
                if "android.permission.READ_EXTERNAL_STORAGE" in permissions or "android.permission.WRITE_EXTERNAL_STORAGE" in permissions:
                    self.log_warning(
                        "Legacy Storage Permissions",
                        "Your app declares legacy external storage permissions. Modern Android versions enforce Scoped Storage.\n"
                        "Action: Migrate to Scoped Storage, Media Store API, or Android Photo Picker."
                    )

                # 4. Cleartext Traffic Checks
                apps = root.findall("application")
                for app in apps:
                    cleartext = app.attrib.get("{http://schemas.android.com/apk/res/android}usesCleartextTraffic")
                    if cleartext == "true":
                        self.log_error(
                            "Cleartext Traffic Permitted in Manifest",
                            "android:usesCleartextTraffic=\"true\" is set. This allows insecure HTTP connections, which is a major security vulnerability.\n"
                            "Action: Remove this attribute or set it to \"false\". Enforce HTTPS everywhere."
                        )
                    else:
                        self.log_success("Cleartext HTTP traffic is disabled in Manifest (Compliant)")
                        
            except Exception as e:
                self.log_error(f"Failed to audit manifest: {os.path.basename(manifest_path)}", str(e))

    def audit_network_security(self):
        print_header("Network Security Configurations")
        
        if not self.net_configs:
            self.log_warning(
                "No Network Security Configuration Found",
                "Your project does not have a network_security_config.xml file. This is recommended to restrict cleartext traffic.\n"
                "Action: Create a network security config file and reference it in your AndroidManifest.xml application tag."
            )
            return

        for config_path in self.net_configs:
            try:
                tree = ET.parse(config_path)
                root = tree.getroot()
                
                # Check base-config cleartext settings
                base_config = root.find("base-config")
                if base_config is not None:
                    cleartext = base_config.attrib.get("cleartextTrafficPermitted")
                    if cleartext == "true":
                        self.log_error(
                            "Cleartext Traffic Allowed in Network Security Config",
                            f"Base config allows cleartext traffic in {os.path.basename(config_path)}.\n"
                            "Action: Set cleartextTrafficPermitted=\"false\" for production release builds."
                        )
                    else:
                        self.log_success(f"Network config blocks cleartext traffic base: {os.path.basename(config_path)}")
            except Exception as e:
                self.log_error(f"Failed to audit network config: {os.path.basename(config_path)}", str(e))

    def generate_markdown_report(self):
        """Generates a local markdown checklist file of the audit results."""
        report_path = os.path.join(self.project_dir, "COMPLIANCE_REPORT.md")
        try:
            with open(report_path, "w", encoding="utf-8") as f:
                f.write("# Android Application Compliance Checklist\n\n")
                f.write("This checklist was automatically generated based on the compliance audit scan of your project files.\n\n")
                
                f.write("## Status Summary\n\n")
                f.write(f"- Critical Risks: {self.violations_count}\n")
                f.write(f"- Warnings: {self.warnings_count}\n")
                f.write(f"- Passed Checks: {self.passes_count}\n\n")
                
                if self.violations_count > 0:
                    f.write("Status: FAIL\n")
                    f.write("Resolve the critical issues below before submitting the application to Google Play.\n\n")
                elif self.warnings_count > 0:
                    f.write("Status: WARNING\n")
                    f.write("Review the warnings below before release.\n\n")
                else:
                    f.write("Status: PASS\n")
                    f.write("All checked items conform to the baseline compliance standards.\n\n")
                
                f.write("## Compliance Action Items\n\n")
                
                if self.violations:
                    f.write("### Critical Risks\n\n")
                    for title, desc in self.violations:
                        clean_desc = desc.replace("\n", "\n  ")
                        f.write(f"- [ ] **{title}**\n")
                        f.write(f"  {clean_desc}\n\n")
                        
                if self.warnings:
                    f.write("### Warnings and Recommendations\n\n")
                    for title, desc in self.warnings:
                        clean_desc = desc.replace("\n", "\n  ")
                        f.write(f"- [ ] **{title}**\n")
                        f.write(f"  {clean_desc}\n\n")
                        
                if self.passes:
                    f.write("### Completed / Compliant Items\n\n")
                    for title in self.passes:
                        f.write(f"- [x] {title}\n")
                    f.write("\n")
            print(f"\nGenerated compliance checklist file at: {report_path}")
        except Exception as e:
            print(f"Failed to write compliance report file: {e}")

if __name__ == "__main__":
    target_dir = "."
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
    
    # Initialize Windows Terminal Color support
    if os.name == 'nt':
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

    auditor = ComplianceAuditor(target_dir)
    success = auditor.audit()
    sys.exit(0 if success else 1)
