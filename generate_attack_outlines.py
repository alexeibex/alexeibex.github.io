import os

# --- DATA: ATTACK OUTLINES ---
# High-level checklists for issue spotting.

ATTACK_OUTLINES = {
    "Civil_Procedure": """---
layout: default
title: Civil Procedure Attack Outline
---

# // CIVIL_PROCEDURE_ATTACK_OUTLINE
### STATUS: ACTIVE_PROTOCOL

> **MISSION:** Determine if the court has power over the parties and the case.

## 1. PERSONAL JURISDICTION (PJ)
**Can the court talk to this defendant?**
- [ ] **Statutory Basis:** Does the state long-arm statute authorize jurisdiction?
- [ ] **Constitutional Basis (Due Process):**
    - [ ] **General PJ:** Is D "at home" (domiciled/incorp/HQ)?
    - [ ] **Specific PJ:** Does the claim arise from D's contacts?
        - [ ] **Purposeful Availment:** Did D reach out to the forum?
        - [ ] **Foreseeability:** Was suit foreseeable?
    - [ ] **Fairness Factors:** Burden on D, State's interest, Plaintiff's interest.

## 2. SUBJECT MATTER JURISDICTION (SMJ)
**Can the court hear this type of case?**
- [ ] **Diversity (1332):** Complete diversity + >$75k?
- [ ] **Federal Question (1331):** "Arising under" federal law (Well-Pleaded Complaint Rule).
- [ ] **Supplemental Jur (1367):** Common nucleus of operative fact?

## 3. VENUE
**Is this the correct courthouse?**
- [ ] **1391(b)(1):** Where any D resides (if all in same state).
- [ ] **1391(b)(2):** Substantial part of events occurred.

## 4. ERIE DOCTRINE
**Federal judge in diversity case.**
- [ ] **Federal Rule?** If yes -> Apply it (Supremacy Clause).
- [ ] **No Rule?** Apply State Substantive Law, Federal Procedural Law.
- [ ] **Outcome Determinative Test:** Would ignoring state law change the outcome?

## 5. PRECLUSION
- [ ] **Claim Preclusion (Res Judicata):** Same Parties, Same Claim, Final Judgment on Merits.
- [ ] **Issue Preclusion (Collateral Estoppel):** Same Issue, Actually Litigated, Essential to Judgment.
""",

    "Torts": """---
layout: default
title: Torts Attack Outline
---

# // TORTS_ATTACK_OUTLINE
### STATUS: ACTIVE_PROTOCOL

> **MISSION:** Identify the wrong, the harm, and the remedy.

## 1. INTENTIONAL TORTS
**Did D intend the act?**
- [ ] **Battery:** Harmful/offensive contact + Intent + Causation.
- [ ] **Assault:** Reasonable apprehension of immediate battery + Intent.
- [ ] **False Imprisonment:** Confinement + Awareness/Harm.
- [ ] **IIED:** Extreme/Outrageous conduct + Severe distress.

## 2. NEGLIGENCE
**The Big Four.**
- [ ] **Duty:** To foreseeable plaintiffs in the zone of danger (Standard: Reasonable Person).
- [ ] **Breach:** Failure to meet standard (B < PL / Custom / Negligence Per Se).
- [ ] **Causation:**
    - [ ] **Actual (Factual):** "But for" test.
    - [ ] **Proximate (Legal):** Was the harm a foreseeable result of the breach?
- [ ] **Damages:** Actual harm required (Eggshell Skull Rule applies).

## 3. STRICT LIABILITY
**Liability without fault.**
- [ ] **Wild Animals:** Strict liability for dangerous propensities.
- [ ] **Abnormally Dangerous Activities:** High risk, cannot be made safe, not common.
- [ ] **Products Liability:** Commercial seller + Defective product + Unaltered since sale.

## 4. DEFENSES
- [ ] **Contributory/Comparative Negligence.**
- [ ] **Assumption of Risk.**
""",

    "Contracts": """---
layout: default
title: Contracts Attack Outline
---

# // CONTRACTS_ATTACK_OUTLINE
### STATUS: ACTIVE_PROTOCOL

> **MISSION:** Determine enforceability of the promise.

## 1. APPLICABLE LAW
- [ ] **UCC Art. 2:** Sale of Goods (tangible, movable).
- [ ] **Common Law:** Services, Real Estate.

## 2. FORMATION
**Is there a deal?**
- [ ] **Offer:** Intent to be bound + Definite terms + Communicated.
- [ ] **Acceptance:** Mirror Image Rule (CL) vs. Battle of Forms 2-207 (UCC).
- [ ] **Consideration:** Bargained-for exchange (Benefit/Detriment).

## 3. DEFENSES TO FORMATION
**Can we kill the deal?**
- [ ] **Statute of Frauds (MYLEGS):** Marriage, Year+, Land, Executor, Goods >$500, Surety.
- [ ] **Mistake / Misrepresentation / Duress / Unconscionability.**

## 4. PERFORMANCE & BREACH
- [ ] **Parol Evidence Rule:** Final writing blocks prior/contemporaneous terms.
- [ ] **Conditions:** Precedent, Subsequent, Concurrent.
- [ ] **Discharge:** Impossibility, Impracticability, Frustration of Purpose.
- [ ] **Breach:** Material vs. Minor.

## 5. REMEDIES
- [ ] **Expectation:** Put P in position as if contract performed.
- [ ] **Reliance:** Put P in position as if contract never happened.
- [ ] **Restitution:** Prevent unjust enrichment.
- [ ] **Specific Performance:** Only for unique goods/land (not services).
""",

    "Criminal_Law": """---
layout: default
title: Criminal Law Attack Outline
---

# // CRIMINAL_LAW_ATTACK_OUTLINE
### STATUS: ACTIVE_PROTOCOL

> **MISSION:** Determine criminal liability and punishment.

## 1. ELEMENTS OF A CRIME
- [ ] **Actus Reus:** Voluntary physical act.
- [ ] **Mens Rea:** Mental state (Specific Intent, General Intent, Malice, Strict Liability).
- [ ] **Concurrence:** Act + Mental State at same time.
- [ ] **Causation:** Actual + Proximate.

## 2. HOMICIDE
- [ ] **Murder:** Unlawful killing + Malice Aforethought.
    - [ ] Intent to kill.
    - [ ] Intent to inflict great bodily harm.
    - [ ] Depraved Heart (Reckless indifference).
    - [ ] Felony Murder (BARRK).
- [ ] **Voluntary Manslaughter:** "Heat of Passion" + Provocation.
- [ ] **Involuntary Manslaughter:** Criminal Negligence.

## 3. INCHOATE OFFENSES
- [ ] **Solicitation:** Asking another to commit crime.
- [ ] **Conspiracy:** Agreement + Overt Act.
- [ ] **Attempt:** Specific Intent + Substantial Step.

## 4. DEFENSES
- [ ] **Insanity (M'Naghten / MPC).**
- [ ] **Intoxication (Voluntary vs. Involuntary).**
- [ ] **Self-Defense.**
""",

    "Property_Law": """---
layout: default
title: Property Attack Outline
---

# // PROPERTY_ATTACK_OUTLINE
### STATUS: ACTIVE_PROTOCOL

> **MISSION:** Define rights over land and chattels.

## 1. OWNERSHIP & POSSESSION
- [ ] **Adverse Possession:** Continuous, Open/Notorious, Actual, Hostile (COAH).
- [ ] **Estates:** Fee Simple, Life Estate, Fee Tail.

## 2. LANDLORD / TENANT
- [ ] **Tenancies:** Years, Periodic, At Will, Sufferance.
- [ ] **Duties:** Pay rent, Habitability, Quiet Enjoyment.
- [ ] **Assignment vs. Sublease.**

## 3. LAND USE
- [ ] **Easements:** Grant, Prescription, Implication, Necessity.
- [ ] **Covenants:** Writing, Intent, Touch & Concern, Notice, Privity.
- [ ] **Zoning & Takings (5th Am):** Public use + Just compensation.
""",

    "Constitutional_Law": """---
layout: default
title: Con Law Attack Outline
---

# // CON_LAW_ATTACK_OUTLINE
### STATUS: ACTIVE_PROTOCOL

> **MISSION:** Check government power against the Constitution.

## 1. JUDICIAL REVIEW
- [ ] **Standing:** Injury + Causation + Redressability.
- [ ] **Ripeness / Mootness.**
- [ ] **Political Question.**

## 2. SEPARATION OF POWERS
- [ ] **Congress:** Commerce Clause, Taxing/Spending.
- [ ] **Executive:** Veto, Commander in Chief, Treaties/Exec Agreements.
- [ ] **10th Amendment:** Commandeering state officials.

## 3. INDIVIDUAL RIGHTS
- [ ] **Due Process (5th/14th):**
    - [ ] Procedural: Life, Liberty, Property -> Hearing.
    - [ ] Substantive: Fundamental Rights (Strict Scrutiny).
- [ ] **Equal Protection (14th):**
    - [ ] Strict Scrutiny: Race, National Origin.
    - [ ] Intermediate Scrutiny: Gender.
    - [ ] Rational Basis: Everything else.
- [ ] **First Amendment:** Speech, Religion (Establishment/Free Exercise).
""",

    "Evidence": """---
layout: default
title: Evidence Attack Outline
---

# // EVIDENCE_ATTACK_OUTLINE
### STATUS: ACTIVE_PROTOCOL

> **MISSION:** Determine admissibility.

## 1. RELEVANCE
- [ ] **Rule 401:** Any tendency to make fact more/less probable.
- [ ] **Rule 403:** Probative value substantially outweighed by prejudice.

## 2. HEARSAY
**Out of court statement offered for truth of matter asserted.**
- [ ] **Non-Hearsay:** Effect on listener, State of mind.
- [ ] **Exclusions (Not Hearsay):** Opposing Party Statement, Prior inconsistent statement (under oath).
- [ ] **Exceptions (Declarant Unavailable):** Dying Declaration, Former Testimony.
- [ ] **Exceptions (Availability Irrelevant):** Present Sense Impression, Excited Utterance, Business Records.

## 3. WITNESSES & IMPEACHMENT
- [ ] **Competency:** Personal knowledge + Oath.
- [ ] **Impeachment:** Bias, Prior Convictions, Bad Acts (probative of truthfulness).

## 4. PRIVILEGES
- [ ] **Attorney-Client.**
- [ ] **Spousal Immunity / Marital Comms.**
"""
}

def main():
    print("--- INITIATING ATTACK OUTLINE GENERATION ---")
    
    # Ensure base directory exists
    base_dir = 'notes'
    if not os.path.exists(base_dir):
        print(" ! ERROR: 'notes' directory not found. Run setup script first.")
        return

    count = 0
    # Iterate through defined outlines
    for subject, content in ATTACK_OUTLINES.items():
        # 1. Construct Path
        subject_dir = os.path.join(base_dir, subject)
        
        # Ensure directory exists (if not, create it to be safe)
        if not os.path.exists(subject_dir):
            os.makedirs(subject_dir)
            print(f" > Created missing directory: {subject_dir}")
        
        # 2. Write Attack Outline File
        outline_path = os.path.join(subject_dir, 'Attack_Outline.md')
        with open(outline_path, 'w') as f:
            f.write(content)
        print(f" > Generated: {outline_path}")
        
        # 3. Link in Index (Syllabus)
        # We look for index.md (or README.md if legacy) to append the link
        index_path = os.path.join(subject_dir, 'index.md')
        if not os.path.exists(index_path):
            # Check for README fallback
            readme_path = os.path.join(subject_dir, 'README.md')
            if os.path.exists(readme_path):
                index_path = readme_path
        
        if os.path.exists(index_path):
            with open(index_path, 'r') as f:
                current_content = f.read()
            
            # Only append if not already linked
            if "Attack_Outline.md" not in current_content:
                with open(index_path, 'a') as f:
                    f.write(f"\n\n### [>> ACCESS ATTACK OUTLINE <<](Attack_Outline.md)\n")
                print(f"   - Linked in syllabus: {index_path}")
        else:
            # If no index exists, create a basic one
            with open(index_path, 'w') as f:
                f.write(f"""---
layout: default
title: {subject}
---
# {subject}
- [Access Attack Outline](Attack_Outline.md)
""")
            print(f"   - Created new index: {index_path}")

        count += 1

    print(f"--- PROCESS COMPLETE. {count} OUTLINES DEPLOYED. ---")

if __name__ == "__main__":
    main()