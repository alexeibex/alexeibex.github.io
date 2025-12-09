import os

# Files that historically contained API Credentials or are now obsolete
SENSITIVE_FILES = [
    # Upgrade Scripts (API Keys were here)
    "upgrade_to_terminal.py",
    "upgrade_to_ai_terminal.py",
    "upgrade_to_gemini_terminal.py",
    "upgrade_to_gemini_2_5.py",
    "upgrade_to_gatekeeper_terminal.py",
    "upgrade_legal_os_v8.py",
    "upgrade_legal_os_v9.py",
    "upgrade_legal_os_v10.py",
    "upgrade_legal_os_v11.py",
    "upgrade_legal_os_v12.py",
    "upgrade_legal_os_v13.py",
    "upgrade_legal_os_v14.py",
    "upgrade_legal_os_v15.py",
    "upgrade_legal_os_v16.py",
    "upgrade_legal_os_v17.py",
    "upgrade_legal_os_v18.py",
    
    # Fix Scripts (API Keys were here)
    "fix_gatekeeper_and_docs.py",
    "fix_gatekeeper_prompt.py",
    "fix_mailto_behavior.py",
    "fix_mailto_popup.py",
    
    # Single-Use Utilities (Clutter)
    "remove_gemini_integration.py",
    "repair_portfolio.py",
    "move_resume.py",
    "update_resume.py",
    "update_identity.py",
    "update_identity_v2.py"
]

def main():
    print("--- INITIATING SECURITY PURGE ---")
    count = 0
    for f in SENSITIVE_FILES:
        if os.path.exists(f):
            try:
                os.remove(f)
                print(f" [x] DELETED: {f}")
                count += 1
            except Exception as e:
                print(f" [!] ERROR DELETING {f}: {e}")
        else:
            pass # File already gone
            
    print(f"--- PURGE COMPLETE. {count} FILES REMOVED. ---")
    print("Remember to run: git add . && git commit -m 'Cleanup' && git push")

if __name__ == "__main__":
    main()