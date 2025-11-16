import os

# --- BUTTON HTML ---
EXPORT_HEADER = """
<div class="export-controls" style="margin-bottom: 30px; border-bottom: 1px solid #333; padding-bottom: 20px;">
    <button onclick="window.print()" style="background: #00ff41; color: black; border: none; padding: 10px 20px; font-family: 'Fira Code', monospace; font-weight: bold; cursor: pointer; margin-right: 10px;">[ SAVE AS PDF ]</button>
    <a href="Attack_Outline.md" download="Attack_Outline.md" style="color: #00f3ff; text-decoration: none; font-family: 'Fira Code', monospace; font-weight: bold;">[ DOWNLOAD MARKDOWN ]</a>
</div>
"""

# --- CONTENT: DEEP DIVE OUTLINES WITH LINKS ---
DETAILED_OUTLINES = {
    "Civil_Procedure": """---
layout: default
title: Civil Procedure Attack Outline
---
# // CIVIL PROCEDURE: THE FINAL ATTACK
### STATUS: COMPREHENSIVE_MODE

""" + EXPORT_HEADER + """

## I. PERSONAL JURISDICTION (PJ)
**THE ISSUE:** Can this specific court exercise power over this specific defendant?

### A. The Two-Step Analysis
1.  **Statutory Step:** Does the state's "Long Arm Statute" allow it?
2.  **Constitutional Step (Due Process):** Does D have "such minimum contacts with the forum so that jurisdiction does not offend traditional notions of fair play and substantial justice"? ([*Int'l Shoe v. Washington*](https://supreme.justia.com/cases/federal/us/326/310/)).

### B. General Jurisdiction ("At Home")
* **Rule:** D can be sued for *anything* in this state.
* **Human:** Domicile (Presence + Intent to remain).
* **Corporation:** State of Incorporation OR Principal Place of Business (PBB/Nerve Center). ([*Daimler AG v. Bauman*](https://supreme.justia.com/cases/federal/us/571/117/)).

### C. Specific Jurisdiction (The Analysis)
**1. Purposeful Availment (The Contact)**
* Did D reach out to the forum? (Marketing, selling, driving).
* **Stream of Commerce:** Merely putting a product in the stream is likely *not* enough without "targeting" the specific state. ([*McIntyre v. Nicastro*](https://supreme.justia.com/cases/federal/us/564/873/)).
* **Internet:** *Zippo* Sliding Scale (Active vs. Passive websites).

**2. Relatedness (The Nexus)**
* Does the Plaintiff's claim *arise from* or *relate to* D's contact?

**3. Fairness (The 5 Factors)**
* Burden on D, State's Interest, Plaintiff's Interest, Interstate Efficiency, Social Policy. ([*World-Wide Volkswagen*](https://supreme.justia.com/cases/federal/us/444/286/)).

---

## II. SUBJECT MATTER JURISDICTION (SMJ)
**THE ISSUE:** Can federal courts hear this *type* of case?

### A. Diversity Jurisdiction (§ 1332)
1.  **Complete Diversity:** No P is a citizen of the same state as any D. ([*Strawbridge v. Curtiss*](https://supreme.justia.com/cases/federal/us/7/267/)).
2.  **Amount in Controversy:** Must **exceed** $75,000.

### B. Federal Question (§ 1331)
* **Rule:** The claim must "arise under" federal law.
* **Well-Pleaded Complaint Rule:** The federal question must appear on the face of the P's complaint, not as a defense. ([*Mottley*](https://supreme.justia.com/cases/federal/us/211/149/)).

### C. Supplemental Jurisdiction (§ 1367)
* **The Test:** "Common Nucleus of Operative Fact" (CNOF). ([*Gibbs*](https://supreme.justia.com/cases/federal/us/383/715/)).

---

## III. ERIE DOCTRINE
**THE ISSUE:** Federal Judge in Diversity Case - Which law applies?

1.  **Federal Rule on Point?** YES -> Apply Federal Rule. ([*Hanna v. Plumer*](https://supreme.justia.com/cases/federal/us/380/460/)).
2.  **No Rule?** Apply State Substantive Law, Federal Procedural Law. ([*Erie R.R. v. Tompkins*](https://supreme.justia.com/cases/federal/us/304/64/)).

---

## IV. PRECLUSION
* **Claim Preclusion (Res Judicata):** Same Parties, Same Claim, Valid Final Judgment.
* **Issue Preclusion (Collateral Estoppel):** Same Issue, Actually Litigated, Essential to Judgment.
""",

    "Torts": """---
layout: default
title: Torts Attack Outline
---
# // TORTS: THE FINAL ATTACK
### STATUS: COMPREHENSIVE_MODE

""" + EXPORT_HEADER + """

## I. NEGLIGENCE (THE BIG FOUR)
**Prima Facie Case:** Duty, Breach, Causation, Damages.

### A. DUTY
**To whom do you owe a duty?**
* **Cardozo (Majority):** Foreseeable plaintiffs in the "Zone of Danger." ([*Palsgraf v. Long Island RR*](https://casetext.com/case/palsgraf-v-long-island-rr-co)).
* **Andrews (Minority):** Everyone. If you hurt someone, you owe them a duty.

### B. BREACH
* **Hand Formula:** B < PL (Burden < Probability x Loss). ([*United States v. Carroll Towing*](https://law.justia.com/cases/federal/appellate-courts/f2/159/169/)).
* **Res Ipsa Loquitur:** "The thing speaks for itself."

### C. CAUSATION
**1. Actual Cause (Factual)**
* **"But For" Test:** But for D's act, injury wouldn't have happened.

**2. Proximate Cause (Legal)**
* **Foreseeability:** Was the harm a foreseeable consequence?
* **Intervening Causes:** Independent acts (Acts of God) supersede D's liability.

### D. DAMAGES
* **Eggshell Skull Rule:** You take your victim as you find them.

---

## II. STRICT LIABILITY
### A. Abnormally Dangerous Activities
* **Rule:** High risk + Cannot be made safe + Not common. ([*Rylands v. Fletcher*](https://www.law.cornell.edu/wex/rylands_v_fletcher)).

### B. Products Liability
* **Defects:** Manufacturing, Design, Warning.

---

## III. INTENTIONAL TORTS
* **Battery:** Harmful/Offensive contact + Intent.
* **Assault:** Reasonable apprehension of immediate battery.
* **IIED:** Extreme & Outrageous conduct + Severe Distress.
""",

    "Contracts": """---
layout: default
title: Contracts Attack Outline
---
# // CONTRACTS: THE FINAL ATTACK
### STATUS: COMPREHENSIVE_MODE

""" + EXPORT_HEADER + """

## I. FORMATION
### A. Offer
* **Rule:** Manifestation of willingness to enter a bargain.
* **Ads:** Generally invitations to deal, unless specific/limiting. ([*Lefkowitz*](https://law.justia.com/cases/minnesota/supreme-court/1957/36-988.html)).

### B. Acceptance
* **Mirror Image Rule (CL):** Must match offer exactly.
* **UCC 2-207 (Battle of the Forms):** New terms may become part of the K between merchants.

### C. Consideration
* **Rule:** Bargained-for exchange. ([*Hamer v. Sidway*](https://casebriefs.com/blog/law/contracts/contracts-keyed-to-farnsworth/policing-the-bargain/hamer-v-sidway/)).
* **Promissory Estoppel:** Reliance can substitute for consideration.

---

## II. REMEDIES
* **Expectation Damages:** Put P in position as if K was performed. ([*Hawkins v. McGee*](https://en.wikipedia.org/wiki/Hawkins_v._McGee)).
* **Specific Performance:** Only for unique items (Land).
""",

    "Criminal_Law": """---
layout: default
title: Criminal Law Attack Outline
---
# // CRIMINAL LAW: THE FINAL ATTACK
### STATUS: COMPREHENSIVE_MODE

""" + EXPORT_HEADER + """

## I. MENS REA (THE GUILTY MIND)
* **Specific Intent:** D wanted the specific result. (Theft, First Degree Murder).
* **Malice:** Reckless disregard of high risk. (Arson, Common Law Murder).

## II. FOURTH AMENDMENT
**Did the police need a warrant?**
1.  **Gov't Conduct?**
2.  **Reasonable Expectation of Privacy (REP)?**
    * **Yes:** Home, Phone Booth ([*Katz*](https://supreme.justia.com/cases/federal/us/389/347/)).
    * **No:** Open Fields, Garbage.
3.  **Exceptions (ESCAPIST):** Exigent Circumstances, Search Incident to Arrest, Consent, Automobile, Plain View, Inventory, Stop & Frisk ([*Terry v. Ohio*](https://supreme.justia.com/cases/federal/us/392/1/)).
""",

    "Internet_Privacy_AI": """---
layout: default
title: Internet & AI Law Attack Outline
---
# // INTERNET, PRIVACY & AI: THE FUTURE SHOCK
### STATUS: ACTIVE_PROTOCOL

""" + EXPORT_HEADER + """

> **MISSION:** Analyze liability and rights in the digital frontier.

## I. INTERNET LAW (THE PLATFORM LAYER)
### A. Section 230 (CDA)
* **The Shield:** "No provider or user of an interactive computer service shall be treated as the publisher or speaker of any information provided by another information content provider."
* **Key Case:** [*Zeran v. AOL*](https://law.justia.com/cases/federal/appellate-courts/F3/129/327/622664/). (Platforms are immune from defamation suits for user content).
* **Exceptions:** Federal Crimes, IP violations (FOSTA-SESTA).

### B. DMCA Section 512 (Copyright Safe Harbor)
* **The Bargain:** Platforms are not liable for user copyright infringement **IF** they:
    1.  Have no actual knowledge.
    2.  Receive financial benefit? No.
    3.  **Notice & Takedown:** Must remove content expeditiously upon notice.
* **Key Case:** [*Viacom v. YouTube*](https://en.wikipedia.org/wiki/Viacom_International_Inc._v._YouTube,_Inc.).

---

## II. PRIVACY (THE DATA LAYER)
### A. Fourth Amendment in the Digital Age
* **Thermal Imaging:** Police need warrant to scan heat of home. ([*Kyllo v. US*](https://supreme.justia.com/cases/federal/us/533/27/)).
* **GPS Tracking:** 28-day GPS monitoring constitutes a search. ([*US v. Jones*](https://supreme.justia.com/cases/federal/us/565/400/)).
* **Cell Phones:** Police need warrant to search phone contents incident to arrest. ([*Riley v. California*](https://supreme.justia.com/cases/federal/us/573/373/)).
* **Cell Site Location Info (CSLI):** Third-Party Doctrine does not apply to long-term location data; warrant required. ([*Carpenter v. US*](https://supreme.justia.com/cases/federal/us/585/16-402/)).

### B. Consumer Privacy (Statutory)
* **GDPR (EU):** Extraterritorial reach. Rights: Access, Erasure ("Right to be Forgotten"), Portability.
* **CCPA/CPRA (California):** Right to Know, Right to Delete, Right to Opt-Out of Sale.

---

## III. ARTIFICIAL INTELLIGENCE (THE ALGORITHMIC LAYER)
### A. Copyright & Generative AI
* **Training Data:** Is scraping the web "Fair Use"?
    * *Analogy:* [*Authors Guild v. Google*](https://www.copyright.gov/fair-use/summaries/authorsguild-google-2dcir2015.pdf) (Book scanning was fair use because it was transformative/searchable).
    * *Current Issue:* Does GenAI replace the market for the original art?
* **Output:** Can AI-generated work be copyrighted?
    * *USCO Position:* No. Copyright requires "human authorship." (*Thaler v. Perlmutter*).

### B. Algorithmic Bias & Liability
* **Disparate Impact:** Algorithms in housing/hiring that unintentionally discriminate.
* **Black Box Problem:** Liability when the AI's decision logic is unexplainable.

---

## IV. BLOCKCHAIN & CRYPTO (THE TRUST LAYER)
### A. Securities Regulation
* **The Test:** Is the token an "Investment Contract"?
* **Howey Test** ([*SEC v. W.J. Howey Co.*](https://supreme.justia.com/cases/federal/us/328/293/)):
    1.  Investment of money.
    2.  In a common enterprise.
    3.  With expectation of profits.
    4.  Derived solely from the efforts of others.

### B. Smart Contracts
* **Enforceability:** "Code is Law" vs. "Law is Law."
* **The DAO Hack:** Can the code be "forked" (overruled) by consensus?
"""
}

def main():
    print("--- INITIATING DEEP DIVE OUTLINE GENERATION (v2.0) ---")
    
    base_dir = 'notes'
    if not os.path.exists(base_dir):
        print(" ! ERROR: 'notes' directory not found.")
        return

    # Create Internet Law directory if missing
    if "Internet_Privacy_AI" not in os.listdir(base_dir):
        os.makedirs(os.path.join(base_dir, "Internet_Privacy_AI"))

    for subject, content in DETAILED_OUTLINES.items():
        subject_dir = os.path.join(base_dir, subject)
        if not os.path.exists(subject_dir):
            os.makedirs(subject_dir)
        
        # Write File
        outline_path = os.path.join(subject_dir, 'Attack_Outline.md')
        with open(outline_path, 'w') as f:
            f.write(content)
        print(f" > Generated Deep Dive: {outline_path}")
        
        # Link in Syllabus
        index_path = os.path.join(subject_dir, 'index.md')
        # Create index if missing (for new modules)
        if not os.path.exists(index_path):
             with open(index_path, 'w') as f:
                f.write(f"---\nlayout: default\ntitle: {subject}\n---\n# {subject}\n")

        with open(index_path, 'r') as f:
            if "Attack_Outline.md" not in f.read():
                with open(index_path, 'a') as af:
                    af.write(f"\n\n### [>> ACCESS ATTACK OUTLINE <<](Attack_Outline.md)\n")

    print("--- OUTLINES DEPLOYED. ---")

if __name__ == "__main__":
    main()