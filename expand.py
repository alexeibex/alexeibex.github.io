import os
import yaml

# --- DATA: THE COMPREHENSIVE CURRICULUM ---
# This defines the "Ideal" Law School Archive.
# The script will create folders and 'Topic Checklists' for all of these.

CURRICULUM = {
    "1L_Core_Kernel": {
        "Civil_Procedure": ["Jurisdiction", "Erie Doctrine", "Pleadings", "Joinder", "Discovery", "Preclusion"],
        "Torts": ["Intentional Torts", "Negligence", "Strict Liability", "Products Liability", "Defamation"],
        "Criminal_Law": ["Actus Reus/Mens Rea", "Homicide", "Inchoate Crimes", "Defenses", "Theft Offenses"],
        "Contracts": ["Offer & Acceptance", "Consideration", "Defenses to Formation", "Performance & Breach", "Remedies"],
        "Property_Law": ["Adverse Possession", "Estates in Land", "Landlord/Tenant", "Easements", "Takings"],
        "Constitutional_Law": ["Judicial Review", "Separation of Powers", "Federalism", "Individual Rights", "Due Process"]
    },
    "Advanced_Protocols": {
        "Evidence": ["Relevance", "Hearsay", "Character Evidence", "Impeachment", "Expert Testimony"],
        "Administrative_Law": ["Agency Power", "Rulemaking", "Adjudication", "Judicial Review (Chevron)"],
        "Corporations": ["Formation", "Fiduciary Duties", "Shareholder Rights", "M&A", "Securities Basics"],
        "Criminal_Procedure": ["4th Amendment (Search/Seizure)", "5th Amendment (Miranda)", "6th Amendment (Counsel)"],
        "Professional_Responsibility": ["Client Confidentiality", "Conflicts of Interest", "Duties to the Court"],
        "Intellectual_Property": ["Copyright", "Trademarks", "Patents", "Trade Secrets"]
    },
    "Future_Vision": {
        "Future_Law_Tech": ["Artificial Intelligence Policy", "Blockchain & Smart Contracts", "Cyber Rights", "Algorithmic Bias"]
    }
}

# --- CONTENT: THE MANIFESTO ---
# A starter paper to establish the Cyberpunk Lawyer persona.

MANIFESTO_TEXT = """---
layout: default
title: The Algorithmic Social Contract
---

# // THE_ALGORITHMIC_SOCIAL_CONTRACT
### RE: CODE_AS_LAW // VERSION 1.0

**Status:** DRAFT_PROTOCOL  
**Author:** AlexeiBex

## 01. The New Precedent
The rigid structures of traditional jurisprudence are colliding with the fluid, decentralized reality of the digital frontier. We are no longer just governed by statutes and case law; we are governed by algorithms, terms of service, and immutable ledger entries.

## 02. The Mission
As a legal professional operating at this intersection, my mission is not merely to interpret the law but to debug it. We must ensure that the "smart contracts" of the future adhere to the equitable principles of the past.

## 03. Focus Areas
* **AI Liability:** Who is responsible when the black box hallucinates?
* **Data Sovereignty:** Establishing property rights in the digital self.
* **Decentralized Justice:** Dispute resolution on the blockchain.

> "The code is the law? No. The law must govern the code."
"""

# --- LOGIC: GENERATORS ---

def create_subject_readme(path, subject, topics):
    """Generates a Cyberpunk-themed Syllabus/Checklist for a subject."""
    content = f"""---
layout: default
title: {subject.replace('_', ' ')}
---

# // MODULE: {subject.upper()}
### STATUS: ARCHIVE_ACTIVE

> **SYSTEM NOTE:** This module contains raw data logs and analysis derived from legal training protocols.

## // TOPIC_CHECKLIST
The following sub-routines are covered in this archive:

"""
    for topic in topics:
        content += f"- [ ] **{topic}**\n"
    
    content += "\n\n---\n*End of Log. Return to [Main Console](/)*"
    
    with open(os.path.join(path, 'README.md'), 'w') as f:
        f.write(content)

def update_index_html():
    """Rewrites the index.html to visually group the new curriculum."""
    html_content = """---
layout: default
title: Home
---

<section id="identity">
    <p>
        <span style="color: #666;">> SYSTEM_USER:</span> <strong>AlexeiBex</strong><br>
        <span style="color: #666;">> ROLE:</span> <strong>Tech-Focused Legal Counsel</strong><br>
        <span style="color: #666;">> MISSION:</span> <strong>Decoding the Future of Law</strong>
    </p>
</section>

<section id="future-tech">
    <h2>// SECTOR_01: FUTURE_OF_LAW_&_TECH</h2>
    <p>Research protocols on AI, Blockchain, and Cyber Rights.</p>
    <div class="grid">
        {% for file in site.static_files %}
            {% if file.path contains 'papers/Future_Law_Tech' %}
             <div class="card" style="border-color: #ff00ff;">
                <span class="label" style="color: #ff00ff;">PRIORITY_DOC</span>
                <a href="{{ file.path }}" class="title">{{ file.name | replace: '.md', '' | replace: '_', ' ' }}</a>
            </div>
            {% endif %}
        {% endfor %}
    </div>
</section>

<section id="core-kernel">
    <h2>// SECTOR_02: CORE_KERNEL (JD_FOUNDATIONS)</h2>
    <p>The fundamental operating system of American Jurisprudence.</p>
    <div class="grid">
        {% for item in site.data.curriculum.1L_Core_Kernel %}
        <div class="card">
            <span class="label">MODULE: CORE</span>
            <a href="/notes/{{ item[0] }}/" class="title">{{ item[0] | replace: '_', ' ' }}</a>
        </div>
        {% endfor %}
    </div>
</section>

<section id="advanced-protocols">
    <h2>// SECTOR_03: ADVANCED_PROTOCOLS</h2>
    <p>Specialized modules and regulatory frameworks.</p>
    <div class="grid">
        {% for item in site.data.curriculum.Advanced_Protocols %}
        <div class="card">
            <span class="label">MODULE: ADVANCED</span>
            <a href="/notes/{{ item[0] }}/" class="title">{{ item[0] | replace: '_', ' ' }}</a>
        </div>
        {% endfor %}
    </div>
</section>

<section id="contact">
    <h2>// ESTABLISH_UPLINK</h2>
    <p>> <a href="https://github.com/alexeibex">GITHUB_REPO</a></p>
</section>
"""
    with open('index.html', 'w') as f:
        f.write(html_content)

def main():
    print("--- INITIATING PHASE 2: EXPANSION ---")
    
    # 1. Save Curriculum Data for Jekyll
    if not os.path.exists('_data'): os.makedirs('_data')
    with open('_data/curriculum.yml', 'w') as f:
        yaml.dump(CURRICULUM, f)
    print(" > Curriculum Data Indexed.")

    # 2. Create Folders & Readmes
    base_notes = 'notes'
    if not os.path.exists(base_notes): os.makedirs(base_notes)

    for category, subjects in CURRICULUM.items():
        # Handle Future Tech separately as it goes in 'papers'
        if category == "Future_Vision":
            path = 'papers/Future_Law_Tech'
            if not os.path.exists(path): os.makedirs(path)
            # specific manifesto creation
            with open(os.path.join(path, 'The_Algorithmic_Social_Contract.md'), 'w') as f:
                f.write(MANIFESTO_TEXT)
            print(f" > Created Future Tech Module: {path}")
            continue

        # Handle Standard Subjects
        for subject, topics in subjects.items():
            # Check if folder exists (from previous script), if not create
            # Note: We normalized names in previous script, we try to match or create new
            folder_path = os.path.join(base_notes, subject)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f" > Created Module: {subject}")
            
            # Always generate the README "Checklist"
            create_subject_readme(folder_path, subject, topics)

    # 3. Update Index
    update_index_html()
    print(" > Interface Upgraded (index.html).")
    
    print("--- EXPANSION COMPLETE. DEPLOY NOW. ---")

if __name__ == "__main__":
    main()