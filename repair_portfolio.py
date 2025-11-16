import os

def repair_notes_structure():
    print("--- SCANNING NEURAL ARCHIVE FOR BROKEN LINKS ---")
    base_dir = 'notes'
    
    if not os.path.exists(base_dir):
        print(" ! ALERT: 'notes' directory not found.")
        return

    # Walk through all note folders
    count = 0
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            # If we find a README.md in a subject folder, rename it to index.md
            # This forces GitHub Pages to render it as the "Home" of that folder.
            if file.lower() == 'readme.md':
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, 'index.md')
                os.rename(old_path, new_path)
                print(f" > REPAIRED LINK: {old_path} -> {new_path}")
                count += 1
    
    print(f"--- REPAIR COMPLETE. {count} MODULES OPTIMIZED. ---")

def update_resume_pointer():
    print("--- UPDATING RESUME POINTER ---")
    index_file = 'index.html'
    
    # The target filename we WANT the user to use
    target_resume = "Alexei_Furs_Resume.pdf"
    
    if os.path.exists(index_file):
        with open(index_file, 'r') as f:
            content = f.read()
        
        # Replace the old placeholder with the new specific file link
        # We accept either the generic one I made before or just force the update
        if "Alexei_Resume.pdf" in content:
            new_content = content.replace("Alexei_Resume.pdf", target_resume)
            with open(index_file, 'w') as f:
                f.write(new_content)
            print(f" > SUCCESS: Homepage now links to '/assets/{target_resume}'")
        elif target_resume in content:
             print(" > SYSTEM NOTE: Resume link is already correct.")
        else:
            print(" ! WARNING: Could not find resume link anchor. Please check index.html manually.")
    else:
        print(" ! ERROR: index.html not found.")

if __name__ == "__main__":
    repair_notes_structure()
    update_resume_pointer()