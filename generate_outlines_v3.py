import os

# --- BUTTON HTML ---
EXPORT_HEADER = """
<div class="export-controls" style="margin-bottom: 30px; border-bottom: 1px solid #333; padding-bottom: 20px;">
    <button onclick="window.print()" style="background: #00ff41; color: black; border: none; padding: 10px 20px; font-family: 'Fira Code', monospace; font-weight: bold; cursor: pointer; margin-right: 10px;">[ SAVE AS PDF ]</button>
    <a href="Attack_Outline.md" download="Attack_Outline.md" style="color: #00f3ff; text-decoration: none; font-family: 'Fira Code', monospace; font-weight: bold;">[ DOWNLOAD MARKDOWN ]</a>
</div>
"""

# --- CONTENT: THE MAGNA CARTA ---
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
* **Strict Liability:** No intent required. (Statutory Rape).

## II. HOMICIDE
* **Common Law Murder:** Unlawful killing + Malice Aforethought.
* **Felony Murder:** Killing during BARRK felony (Burglary, Arson, Rape, Robbery, Kidnapping).
* **Voluntary Manslaughter:** Heat of Passion + Provocation.

## III. INCHOATE OFFENSES
* **Conspiracy:** Agreement + Overt Act. (Pinkerton Liability applies).
* **Attempt:** Substantial Step + Specific Intent.
""",

    "Property_Law": """---
layout: default
title: Property Law Attack Outline
---
# // PROPERTY: THE FINAL ATTACK
### STATUS: COMPREHENSIVE_MODE

""" + EXPORT_HEADER + """

## I. POSSESSION & OWNERSHIP
### A. First Possession
* **Rule:** Pursuit alone is not enough; you must mortally wound or capture. ([*Pierson v. Post*](https://en.wikipedia.org/wiki/Pierson_v._Post)).

### B. Adverse Possession (ECHO)
**You can steal land if you are:**
1.  **E**xclusive.
2.  **C**ontinuous.
3.  **H**ostile (Claim of Right).
4.  **O**pen and Notorious.

---

## II. ESTATES IN LAND
* **Fee Simple Absolute:** "To A and his heirs." (Total ownership).
* **Life Estate:** "To A for life."
* **Joint Tenancy:** Four Unities (Time, Title, Interest, Possession) + Right of Survivorship.

---

## III. LANDLORD / TENANT
* **Implied Warranty of Habitability:** Residential rentals must be fit for human habitation. Non-waivable.
* **Covenant of Quiet Enjoyment:** L cannot constructively evict T (e.g., by failing to fix the heat).

---

## IV. TAKINGS (5th AMENDMENT)
**"Nor shall private property be taken for public use, without just compensation."**
* **Per Se Taking:** Permanent physical occupation. ([*Loretto*](https://supreme.justia.com/cases/federal/us/458/419/)).
* **Total Regulatory Taking:** Regulation leaves land with NO economic value. ([*Lucas v. South Carolina*](https://supreme.justia.com/cases/federal/us/505/1003/)).
* **Penn Central Test:** For partial takings, balance: 1) Economic impact, 2) Investment-backed expectations, 3) Character of gov't action.
""",

    "Constitutional_Law": """---
layout: default
title: Con Law Attack Outline
---
# // CON LAW: THE FINAL ATTACK
### STATUS: COMPREHENSIVE_MODE

""" + EXPORT_HEADER + """

## I. JUDICIAL REVIEW
* **Marbury v. Madison:** It is emphatically the province of the judicial department to say what the law is. ([*Marbury*](https://supreme.justia.com/cases/federal/us/5/137/)).

## II. FEDERALISM & POWERS
### A. Commerce Clause
* **Congress can regulate:** 1) Channels, 2) Instrumentalities, 3) Activities having substantial effect on interstate commerce. ([*US v. Lopez*](https://supreme.justia.com/cases/federal/us/514/549/)).

### B. Commandeering
* Congress cannot force states to enact federal programs. ([*New York v. US*](https://supreme.justia.com/cases/federal/us/505/144/)).

---

## III. INDIVIDUAL RIGHTS
### A. Equal Protection (14th Am)
* **Strict Scrutiny (Race/Origin):** Gov must show compelling interest + narrowly tailored. ([*Brown v. Board*](https://supreme.justia.com/cases/federal/us/347/483/)).
* **Intermediate Scrutiny (Gender):** Important interest + substantially related.
* **Rational Basis:** Legitimate interest + rational relation.

### B. Fundamental Rights (Substantive Due Process)
* Marriage, Privacy, Contraception. ([*Obergefell v. Hodges*](https://supreme.justia.com/cases/federal/us/576/14-556/)).
""",

    "Evidence": """---
layout: default
title: Evidence Attack Outline
---
# // EVIDENCE: THE FINAL ATTACK
### STATUS: COMPREHENSIVE_MODE

""" + EXPORT_HEADER + """

## I. RELEVANCE
* **Rule 401:** Evidence is relevant if it has ANY tendency to make a fact more/less probable.
* **Rule 403 (The Gatekeeper):** Relevant evidence may be excluded if probative value is **substantially outweighed** by prejudice/confusion.

## II. CHARACTER EVIDENCE
* **Rule:** You generally cannot argue "Once a thief, always a thief."
* **Exceptions (MIMIC):** Motive, Intent, Mistake (Absence of), Identity, Common Plan.

## III. HEARSAY
**"Out of court statement, offered for the truth of the matter asserted."**

### A. Not Hearsay (Exclusions)
* **Effect on Listener:** "I heard him say 'Fire'" (to show why I ran, not that there was a fire).
* **Party Opponent Admission:** Anything the defendant said.

### B. Exceptions (Declarant Unavailable)
* Dying Declaration.
* Former Testimony.

### C. Exceptions (Availability Irrelevant)
* **Excited Utterance:** "Oh my god, he shot him!"
* **Present Sense Impression:** "The car is running the red light."
* **Business Records.**

## IV. CONFRONTATION CLAUSE
* **Crawford:** In criminal cases, testimonial hearsay is barred unless D had prior opportunity to cross-examine. ([*Crawford v. Washington*](https://supreme.justia.com/cases/federal/us/541/36/)).
""",

    "Criminal_Procedure": """---
layout: default
title: Criminal Procedure Attack Outline
---
# // CRIM PRO: THE FINAL ATTACK
### STATUS: COMPREHENSIVE_MODE

""" + EXPORT_HEADER + """

## I. FOURTH AMENDMENT (SEARCH & SEIZURE)
* **Katz Test:** 1) Subjective expectation of privacy? 2) Is it objectively reasonable? ([*Katz v. US*](https://supreme.justia.com/cases/federal/us/389/347/)).
* **Warrant Requirement:** Police generally need a warrant based on Probable Cause.
* **Exclusionary Rule:** Evidence found illegally is "fruit of the poisonous tree" and excluded. ([*Mapp v. Ohio*](https://supreme.justia.com/cases/federal/us/367/643/)).

## II. FIFTH AMENDMENT (MIRANDA)
* **Trigger:** Custody + Interrogation.
* **Right:** To remain silent and to counsel. ([*Miranda v. Arizona*](https://supreme.justia.com/cases/federal/us/384/436/)).

## III. SIXTH AMENDMENT (COUNSEL)
* **Right to Counsel:** Attaches at all critical stages of prosecution.
* **Indigent Defendants:** Must be provided counsel in felony cases. ([*Gideon v. Wainwright*](https://supreme.justia.com/cases/federal/us/372/335/)).
""",

    "Corporations": """---
layout: default
title: Corporations Attack Outline
---
# // CORPORATIONS: THE FINAL ATTACK
### STATUS: COMPREHENSIVE_MODE

""" + EXPORT_HEADER + """

## I. DUTY OF CARE
* **Business Judgment Rule (BJR):** Courts presume directors acted on an informed basis, in good faith, and in the honest belief that the action was in the best interest of the company.
* **Van Gorkom:** Gross negligence (failure to inform oneself) overcomes BJR. ([*Smith v. Van Gorkom*](https://en.wikipedia.org/wiki/Smith_v._Van_Gorkom)).

## II. DUTY OF LOYALTY
* **Self-Dealing:** Director is on both sides of the transaction.
* **Safe Harbor:** Transaction is valid if approved by disinterested directors or shareholders after full disclosure.

## III. DERIVATIVE SUITS
* **Rule:** Shareholder sues *on behalf* of the corporation for harm done *to* the corporation.
* **Demand Requirement:** Must ask the board to sue first, unless demand is "futile."
""",

    "Administrative_Law": """---
layout: default
title: Admin Law Attack Outline
---
# // ADMIN LAW: THE FINAL ATTACK
### STATUS: COMPREHENSIVE_MODE

""" + EXPORT_HEADER + """

## I. AGENCY POWER
* **Non-Delegation Doctrine:** Congress must provide an "intelligible principle" when delegating power.

## II. JUDICIAL REVIEW
* **Chevron Deference (OVERTURNED):** Formerly, courts deferred to agency interpretation of ambiguous statutes.
* **Loper Bright:** Courts must now exercise independent judgment on legal questions. ([*Loper Bright Enterprises v. Raimondo*](https://www.supremecourt.gov/opinions/23pdf/22-451_7m58.pdf)).
* **Arbitrary & Capricious:** Agency action must be rational and based on the record. ([*Motor Vehicle Mfrs. Assn. v. State Farm*](https://supreme.justia.com/cases/federal/us/463/29/)).
""",

    "Professional_Responsibility": """---
layout: default
title: Professional Responsibility Attack Outline
---
# // PROFESSIONAL RESPONSIBILITY: THE FINAL ATTACK
### STATUS: COMPREHENSIVE_MODE

""" + EXPORT_HEADER + """

## I. DUTY OF CONFIDENTIALITY (Rule 1.6)
* **Rule:** Lawyer shall not reveal information relating to representation.
* **Exception:** To prevent reasonably certain death or substantial bodily harm.

## II. CONFLICTS OF INTEREST (Rule 1.7)
* **Direct Adversity:** Cannot represent Client A vs. Client B.
* **Material Limitation:** Cannot represent if representation is limited by responsibility to another client or self-interest.

## III. CANDOR TO THE TRIBUNAL (Rule 3.3)
* Cannot knowingly make a false statement of fact or law to a tribunal.
""",

    "Intellectual_Property": """---
layout: default
title: IP Law Attack Outline
---
# // INTELLECTUAL PROPERTY: THE FINAL ATTACK
### STATUS: COMPREHENSIVE_MODE

""" + EXPORT_HEADER + """

## I. COPYRIGHT
* **Scope:** Original works of authorship fixed in a tangible medium.
* **Feist:** Sweat of the brow is not enough; need "creative spark." ([*Feist v. Rural Telephone*](https://supreme.justia.com/cases/federal/us/499/340/)).
* **Fair Use (Four Factors):** 1) Purpose (Transformative?), 2) Nature of work, 3) Amount used, 4) Effect on market.

## II. PATENT
* **Scope:** New, useful, and non-obvious inventions.
* **Alice Test:** Abstract ideas (algorithms) are not patentable unless there is an "inventive concept." ([*Alice Corp. v. CLS Bank*](https://supreme.justia.com/cases/federal/us/573/208/)).

## III. TRADEMARK
* **Scope:** Source identifiers (Names, Logos).
* **Abercrombie Spectrum:** Fanciful (Strongest) -> Arbitrary -> Suggestive -> Descriptive -> Generic (No protection).
"""
}

def main():
    print("--- INITIATING COMPREHENSIVE OUTLINE GENERATION (v3.0) ---")
    
    base_dir = 'notes'
    if not os.path.exists(base_dir):
        print(" ! ERROR: 'notes' directory not found.")
        return

    # Ensure all directories exist
    for subject in DETAILED_OUTLINES.keys():
        subject_dir = os.path.join(base_dir, subject)
        if not os.path.exists(subject_dir):
            os.makedirs(subject_dir)
        
        # Write Attack Outline
        outline_path = os.path.join(subject_dir, 'Attack_Outline.md')
        with open(outline_path, 'w') as f:
            f.write(DETAILED_OUTLINES[subject])
        print(f" > Generated: {outline_path}")
        
        # Link in Index
        index_path = os.path.join(subject_dir, 'index.md')
        if not os.path.exists(index_path):
            with open(index_path, 'w') as f:
                f.write(f"---\nlayout: default\ntitle: {subject}\n---\n# {subject}\n")
        
        with open(index_path, 'r') as f:
            if "Attack_Outline.md" not in f.read():
                with open(index_path, 'a') as af:
                    af.write(f"\n\n### [>> ACCESS ATTACK OUTLINE <<](Attack_Outline.md)\n")

    print("--- ALL SUBJECTS DEPLOYED. ---")

if __name__ == "__main__":
    main()