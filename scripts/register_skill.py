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

def register_global_skill():
    # Identify source directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, ".."))
    source_skill_dir = os.path.join(repo_root, "android-legal-compliance")

    if not os.path.isdir(source_skill_dir):
        print_error(f"Source skill folder not found at '{source_skill_dir}'.")
        sys.exit(1)

    # Determine global config directory
    home_dir = os.path.expanduser("~")
    target_skill_root = os.path.join(home_dir, ".gemini", "config", "skills")
    target_skill_dir = os.path.join(target_skill_root, "android-legal-compliance")

    print(f"{COLOR_BOLD}{COLOR_BLUE}Registering Android Legal & Compliance Skill Globally...{COLOR_RESET}")
    print(f"Target location: {target_skill_dir}")

    # Remove existing global install if present
    if os.path.exists(target_skill_dir):
        try:
            shutil.rmtree(target_skill_dir)
        except Exception as e:
            print_error(f"Failed to remove existing global registration: {e}")
            sys.exit(1)

    # Ensure parent folders exist
    try:
        os.makedirs(target_skill_root, exist_ok=True)
    except Exception as e:
        print_error(f"Failed to create config directories: {e}")
        sys.exit(1)

    # Copy files
    try:
        shutil.copytree(source_skill_dir, target_skill_dir)
        print_success("Global registration complete.")
    except Exception as e:
        print_error(f"Failed to register global skill: {e}")
        sys.exit(1)

    # Final verification
    skill_file = os.path.join(target_skill_dir, "SKILL.md")
    if os.path.isfile(skill_file):
        print(f"\n{COLOR_BOLD}{COLOR_GREEN}[OK] Global Skill Registered Successfully!{COLOR_RESET}")
        print("Your AI assistant will now automatically consult these compliance guidelines for all active workspaces.\n")
    else:
        print_error("Verification failed: SKILL.md was not found in the target directory.")
        sys.exit(1)

if __name__ == "__main__":
    # Initialize Windows Terminal Color support
    if os.name == 'nt':
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

    register_global_skill()
