#!/usr/bin/env python3
import os
import sys
import shutil

# ANSI Colors
COLOR_RESET = "\033[0m"
COLOR_BOLD = "\033[1m"
COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"
COLOR_BLUE = "\033[94m"

def print_success(message):
    print(f"{COLOR_GREEN}[OK] {message}{COLOR_RESET}")

def print_error(message):
    print(f"{COLOR_RED}[ERROR] {message}{COLOR_RESET}")

def install(dest_dir):
    dest_path = os.path.abspath(dest_dir)
    print(f"{COLOR_BOLD}{COLOR_BLUE}Installing Legal & Compliance Guard into: {dest_path}{COLOR_RESET}")

    if not os.path.isdir(dest_path):
        print_error(f"Target directory '{dest_path}' does not exist.")
        sys.exit(1)

    # Locate source files relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, ".."))

    source_cursorrules = os.path.join(repo_root, ".cursorrules")
    source_audit = os.path.join(script_dir, "audit.py")

    # Verify source files exist
    if not os.path.isfile(source_cursorrules):
        print_error(f"Source file '.cursorrules' not found at '{source_cursorrules}'. Make sure you are running from the original repo.")
        sys.exit(1)
    if not os.path.isfile(source_audit):
        print_error(f"Source file 'audit.py' not found at '{source_audit}'.")
        sys.exit(1)

    # Copy .cursorrules to target project root
    dest_cursorrules = os.path.join(dest_path, ".cursorrules")
    try:
        shutil.copy2(source_cursorrules, dest_cursorrules)
        print_success("Copied '.cursorrules' to project root.")
    except Exception as e:
        print_error(f"Failed to copy '.cursorrules': {e}")
        sys.exit(1)

    # Create target scripts/ directory
    dest_scripts_dir = os.path.join(dest_path, "scripts")
    try:
        os.makedirs(dest_scripts_dir, exist_ok=True)
    except Exception as e:
        print_error(f"Failed to create directory '{dest_scripts_dir}': {e}")
        sys.exit(1)

    # Copy audit.py to target scripts/ folder
    dest_audit = os.path.join(dest_scripts_dir, "audit.py")
    try:
        shutil.copy2(source_audit, dest_audit)
        print_success("Copied 'audit.py' scanner to 'scripts/' folder.")
    except Exception as e:
        print_error(f"Failed to copy 'audit.py': {e}")
        sys.exit(1)

    # Final Instructions
    print(f"\n{COLOR_BOLD}{COLOR_GREEN}[OK] Installation Successful!{COLOR_RESET}")
    print(f"Now, any AI agent reading your project root will automatically enforce compliance guidelines.")
    print(f"To scan your app for compliance, run the following command in the target directory:")
    print(f"{COLOR_BOLD}{COLOR_BLUE}    python scripts/audit.py .{COLOR_RESET}\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python install.py <path_to_android_project>")
        sys.exit(1)
    
    # Initialize Windows Terminal Color support
    if os.name == 'nt':
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

    install(sys.argv[1])
