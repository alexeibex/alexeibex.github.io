import os
import yaml

# --- BUTTON HTML ---
EXPORT_HEADER = """
<div class="export-controls" style="margin-bottom: 30px; border-bottom: 1px solid #333; padding-bottom: 20px;">
    <button onclick="window.print()" style="background: #00ff41; color: black; border: none; padding: 10px 20px; font-family: 'Fira Code', monospace; font-weight: bold; cursor: pointer; margin-right: 10px;">[ SAVE AS PDF ]</button>
    <a href="Attack_Outline.md" download="Attack_Outline.md" style="color: #00f3ff; text-decoration: none; font-family: 'Fira Code', monospace; font-weight: bold;">[ DOWNLOAD MARKDOWN ]</a>
</div>
"""

# --- CONTENT: EXAM-GRADE OUTLINES ---
DETAILED_OUTLINES = {
    "Civil_Procedure": """---
layout: default
title: Civil Procedure Comprehensive Outline
---
# // CIVIL PROCEDURE: EXAM MASTER PROTOCOL
### STATUS: FINAL_REVIEW_MODE

""" + EXPORT_HEADER + """

## I. PERSONAL JURISDICTION (PJ)
**THE ISSUE:** Can *this* court (in this state) exercise power over *this* defendant?

### A. The Framework
1.  **Statutory Step:** Check the State Long-Arm Statute.
    * *California Type:* "Courts may exercise jurisdiction on any basis not inconsistent with the Constitution." (Go to Step 2).
    * *Enumerated Type:* List specific acts (tort, contract, property in state).
2.  **Constitutional Step (Due Process):** Does D have "such minimum contacts with the forum so that jurisdiction does not offend traditional notions of fair play and substantial justice"? ([*Int'l Shoe*](https://supreme.justia.com/cases/federal/us/326/310/)).

### B. General Jurisdiction ("At Home")
* **Rule:** D can be sued for *any* claim in this state, even unrelated ones.
* **Individuals:** Domicile (Physical presence + Intent to remain).
* **Corporations:**
    1.  State of Incorporation.
    2.  Principal Place of Business (PPB). *Hertz*: The "Nerve Center" (usually HQ).
    * *Daimler Rule:* Only "at home" in these two places. Being "essentially at home" elsewhere is exceptionally rare.

### C. Specific Jurisdiction (The 3-Prong Test)
**1. Purposeful Availment (The Contact)**
* Did D *reach out* to the forum? (Marketing, selling, driving, calling).
* **Stream of Commerce:** Merely placing a product in the stream is likely *not* enough. Needs "targeting" (advertising, customer service). (*McIntyre v. Nicastro*).
* **Effects Test:** Intentional torts aimed at the forum (libel) count. (*Calder v. Jones*).
* **Internet (*Zippo*):** Active (business) vs. Passive (info only). Interactive is the grey zone.

**2. Relatedness (The Nexus)**
* Does P's claim *arise from* or *relate to* D's contact?
* *Ford Motor Co.:* "Relate to" is broader than strict causation. If D sells cars in State A, and P gets hurt in State A by that model (even if bought elsewhere), there is a nexus.

**3. Fairness (The 5 Factors - *World-Wide Volkswagen*)**
* Burden on D (Must be "so gravely difficult and inconvenient" -> unconstitutional).
* State's Interest (Protecting citizens).
* Plaintiff's Interest (Suing at home).
* Interstate Efficiency.
* Substantive Social Policy.

---

## II. SUBJECT MATTER JURISDICTION (SMJ)
**THE ISSUE:** Can *federal* courts hear this *type* of case?

### A. Diversity Jurisdiction (§ 1332)
1.  **Complete Diversity:** No Plaintiff can be a citizen of the same state as any Defendant. (*Strawbridge*).
    * *Tested at time of filing.*
    * *Citizenship (Human):* Domicile.
    * *Citizenship (Corp):* Every state of incorp + The one PPB.
2.  **Amount in Controversy:** Must **exceed** $75,000.00.
    * *Aggregation:* 1 P can stack all claims against 1 D.

### B. Federal Question (§ 1331)
* **Rule:** The claim must "arise under" federal law (Constitution, Treaties, Statutes).
* **Well-Pleaded Complaint Rule:** The federal issue must appear in the *Plaintiff's* cause of action, not in an anticipated defense. (*Mottley* - P sued RR for breach of pass; RR's defense was federal law. No SMJ).

### C. Supplemental Jurisdiction (§ 1367)
* **Step 1:** Is there an "anchor claim" with original SMJ?
* **Step 2 (The Test):** Does the new claim share a "Common Nucleus of Operative Fact" (CNOF)? (Usually same transaction).
* **Step 3 (The Trap - § 1367(b)):** In *Diversity* cases only, P cannot use Supp Jur to sue new parties if it would destroy diversity.

---

## III. VENUE (§ 1391)
**THE ISSUE:** Which specific federal district?

1.  **Residential Venue:** Any district where *any* D resides (if all Ds reside in same state).
2.  **Transactional Venue:** Any district where a *substantial part* of events occurred.
3.  **Transfer:**
    * *1404 (Convenience):* Original venue was proper, but another is better.
    * *1406 (Improper):* Original venue was wrong. Court dismisses or transfers.

---

## IV. ERIE DOCTRINE
**THE ISSUE:** Federal Court + Diversity Case. Which law applies?

1.  **Hanna Prong:** Is there a valid Federal Rule (FRCP/Statute) on point?
    * YES -> Apply it. (Supremacy Clause).
2.  **Erie Prong:** If no federal rule:
    * **Substantive Issue?** Apply State Law. (Elements of crime, Statue of Limitations, Tolling).
    * **Procedural Issue?** Apply Federal Law. (Judge/Jury allocation).
3.  **Grey Areas (Tests):**
    * *Outcome Determinative:* Would federal law change the result? -> Use State.
    * *Balance of Interests:* Does feds have strong interest (e.g., jury system)? -> Use Federal.
    * *Twin Aims of Erie:* Avoid forum shopping + inequitable administration of laws.

---

## V. PRECLUSION
### A. Claim Preclusion (Res Judicata)
**"One bite at the apple."**
1.  **Same Parties:** Case 1 and Case 2 have same P and same D.
2.  **Valid Final Judgment on Merits:** Not dismissed for technicality (PJ, Venue).
3.  **Same Claim:** Arises from same Transaction/Occurrence. (Federal approach).

### B. Issue Preclusion (Collateral Estoppel)
**"Fact sticking."**
1.  **Same Issue:** Literal identical fact.
2.  **Actually Litigated:** Not a default judgment/settlement.
3.  **Essential to Judgment:** If the verdict didn't rely on it, it's not precluded.
4.  **Against Whom?** Can only be used *against* someone who was a party in Case 1 (Due Process).
""",

    "Constitutional_Law": """---
layout: default
title: Constitutional Law Comprehensive Outline
---
# // CON LAW: EXAM MASTER PROTOCOL
### STATUS: FINAL_REVIEW_MODE

""" + EXPORT_HEADER + """

## I. JUDICIAL POWER
* **Marbury v. Madison:** Established Judicial Review. The Constitution is supreme; courts say what the law is.
* **Justiciability (Article III Limits):**
    1.  **Standing:**
        * *Injury in Fact:* Concrete & Particularized (not ideological).
        * *Causation:* Traceable to D.
        * *Redressability:* Court ruling will fix it.
    2.  **Ripeness:** Too early? (No pre-enforcement review unless hardship).
    3.  **Mootness:** Too late? (Injury ended). Exception: "Capable of repetition yet evading review" (Roe v. Wade).
    4.  **Political Question:** Textually committed to another branch (Impeachment, Foreign Policy recognition).

---

## II. LEGISLATIVE POWER (CONGRESS)
* **Enumerated Powers Only:** Congress has NO general police power (except M.I.L.D. - Military, Indian lands, Lands (federal), DC).
* **Commerce Clause:** Congress can regulate:
    1.  **Channels:** Roads, rivers, internet.
    2.  **Instrumentalities:** Trucks, planes, phones.
    3.  **Substantial Effects:**
        * *Economic Activity:* Aggregation applies (*Wickard v. Filburn* - growing own wheat affects market).
        * *Non-Economic:* Cannot aggregate (*US v. Lopez* - gun in school zone is not commerce).
* **Taxing & Spending:** Extremely broad. Can condition funds to states if: related to general welfare, unambiguous, not coercive (*Sebelius*).
* **10th Amendment (Commandeering):** Congress cannot force states to pass laws or enforce federal programs. (*New York v. US*).

---

## III. EXECUTIVE POWER
* **Domestic:**
    * *Youngstown Sheet & Tube:*
        * Zone 1 (Max): Acts with Congress approval.
        * Zone 2 (Twilight): Congress silent.
        * Zone 3 (Lowest): Acts against Congress (Unconstitutional unless exclusive power).
* **Foreign:**
    * Commander in Chief: Broad power, but Congress declares war.
    * Treaties: Ratified by Senate (Supreme Law).
    * Exec Agreements: No Senate needed (Trumps state law, loses to federal statute).

---

## IV. INDIVIDUAL RIGHTS (14th AMENDMENT)
### A. State Action Doctrine
* Constitution only applies to Government conduct.
* **Exceptions:**
    * *Public Function:* Private entity doing exclusive gov task (company town).
    * *Entanglement:* Gov encourages/facilitates private discrimination.

### B. Equal Protection (EP)
**Step 1: What is the Classification?**
**Step 2: Apply Scrutiny Level.**

1.  **Strict Scrutiny:**
    * *Classes:* Race, National Origin, Alienage (State laws).
    * *Test:* Gov must show **Compelling Interest** + **Narrowly Tailored** (Necessary).
    * *Burden:* On Government. (Usually fatal).
2.  **Intermediate Scrutiny:**
    * *Classes:* Gender, Illegitimacy.
    * *Test:* Gov must show **Important Interest** + **Substantially Related**.
    * *Burden:* On Government.
3.  **Rational Basis:**
    * *Classes:* Age, Wealth, Disability, Sexual Orientation (though arguably higher).
    * *Test:* P must show law is **Not Rationally Related** to **Legitimate Interest**.
    * *Burden:* On Plaintiff. (Gov usually wins).

### C. Due Process (DP)
1.  **Procedural DP:** Life, Liberty, Property taken? Need Notice + Hearing. (*Mathews v. Eldridge* balance).
2.  **Substantive DP (Fundamental Rights):**
    * *Strict Scrutiny applied to:* Vote, Travel, Privacy (CAMPER: Contraception, Abortion*, Marriage, Procreation, Education-ish, Relations).
    * *Abortion:* *Dobbs* overruled *Roe*. Now Rational Basis test.

### D. First Amendment (Speech)
* **Content-Based:** Strict Scrutiny.
* **Content-Neutral (Time/Place/Manner):** Intermediate Scrutiny (Narrowly tailored to significant interest + alternative channels).
* **Unprotected Speech:**
    * *Incitement:* Imminent lawless action + likely to produce. (*Brandenburg*).
    * *Obscenity:* Prurient interest + offensive + no artistic value (*Miller*).
    * *True Threats* / *Fighting Words*.
""",

    "Contracts": """---
layout: default
title: Contracts Comprehensive Outline
---
# // CONTRACTS: EXAM MASTER PROTOCOL
### STATUS: FINAL_REVIEW_MODE

""" + EXPORT_HEADER + """

## I. APPLICABLE LAW
* **UCC Article 2:** Sale of Goods (movable, tangible).
* **Common Law:** Services, Real Estate, Employment.
* **Mixed Deals:** "Predominant Purpose Test" - what is the main reason for the K?

---

## II. FORMATION (O + A + C)
### A. Offer
* Manifestation of willingness to enter a bargain.
* **Ads:** Usually invitations to deal. Exception: "First 10 customers get X for $1" (Specific/leaving nothing to negotiation).
* **Termination:** Revocation (before acceptance), Rejection, Counteroffer, Death, Lapse of Time.
* **Irrevocable:**
    1.  Option K (paid).
    2.  UCC Firm Offer (Merchant + Signed Writing).
    3.  Detrimental Reliance.

### B. Acceptance
* **Common Law:** Mirror Image Rule. Must match offer exactly.
* **UCC 2-207 (Battle of Forms):**
    * Acceptance with new terms is VALID.
    * *Terms:* If both merchants, new terms enter unless material alteration or objection.

### C. Consideration
* Bargained-for exchange of legal value.
* **Past Consideration:** Invalid.
* **Pre-Existing Duty:** CL requires new consideration to modify. UCC allows modification in Good Faith (no new consideration).

---

## III. DEFENSES (Unenforceability)
* **Statute of Frauds (MYLEGS):** Marriage, Year (>1), Land, Executor, Goods (>$500), Surety.
    * *Exception:* Part performance, Specially manufactured goods.
* **Duress:** Physical or Economic (improper threat + no reasonable alternative).
* **Unconscionability:** Procedural (fine print) + Substantive (unfair terms).

---

## IV. PERFORMANCE & BREACH
### A. Parol Evidence Rule
* Final writing blocks prior oral terms.
* *Merger Clause:* "This is the complete agreement."

### B. Breach
* **Common Law:**
    * *Material Breach:* Excuses counter-performance. P can sue for total damages.
    * *Substantial Performance:* Non-material breach. P gets K price minus cost of defect.
* **UCC:** Perfect Tender Rule. If goods fail in ANY respect, buyer can reject all.

---

## V. REMEDIES
* **Expectation Damages:** Put P in position as if K performed. (K Price - Market Price).
* **Consequential Damages:** Foreseeable losses (lost profits) known to D at time of K. (*Hadley v. Baxendale*).
* **Mitigation:** P has duty to minimize damages.
* **Specific Performance:** Only for unique goods (Land, Art). Never services.
""",

    "Criminal_Law": """---
layout: default
title: Criminal Law Comprehensive Outline
---
# // CRIMINAL LAW: EXAM MASTER PROTOCOL
### STATUS: FINAL_REVIEW_MODE

""" + EXPORT_HEADER + """

## I. THE ELEMENTS
1.  **Actus Reus:** Voluntary Act (Bodily movement).
    * *Omission:* Liability only if duty exists (Statute, Contract, Relationship, Creation of Peril).
2.  **Mens Rea:** Guilty Mind.
    * *Specific Intent:* Goal-oriented. (Solicitation, Conspiracy, Attempt, First Degree Murder, Assault, Larceny, Robbery, Burglary, Forgery).
    * *General Intent:* Awareness of factors. (Battery, Rape, False Imprisonment).
    * *Malice:* Reckless disregard. (Arson, Common Law Murder).
    * *Strict Liability:* No mental state. (Statutory Rape, Public Welfare).
3.  **Causation:**
    * *Actual:* "But for".
    * *Proximate:* Foreseeable result. (Superseding cause breaks chain).

---

## II. HOMICIDE
* **Common Law Murder:** Unlawful killing of human with Malice Aforethought.
    1.  Intent to Kill.
    2.  Intent to Inflict Serious Bodily Harm.
    3.  Depraved Heart (Reckless indifference to human life).
    4.  Felony Murder (Death during BARRK felony).
* **First Degree (Statutory):** Premeditated + Deliberate.
* **Voluntary Manslaughter:** Murder + "Heat of Passion" (Adequate provocation + No cooling off).
* **Involuntary Manslaughter:** Criminal Negligence.

---

## III. INCHOATE CRIMES
* **Solicitation:** Asking another to commit crime. Merges into completed crime.
* **Conspiracy:** Agreement + Intent + Overt Act.
    * *Pinkerton:* Liable for ALL foreseeable crimes of co-conspirators.
    * *No Merger:* Can be convicted of Conspiracy AND Crime.
* **Attempt:** Specific Intent + Substantial Step (beyond mere prep).

---

## IV. DEFENSES
* **Insanity:**
    * *M'Naghten:* Didn't know wrongfulness OR didn't understand nature of act.
    * *MPC:* Lacked capacity to appreciate criminality or conform conduct.
* **Intoxication:**
    * *Voluntary:* Defense to SPECIFIC INTENT only.
    * *Involuntary:* Defense to ALL.
* **Self-Defense:** Reasonable force to protect self. Deadly force only if threat of death/serious harm.
""",

    "Property_Law": """---
layout: default
title: Property Law Comprehensive Outline
---
# // PROPERTY: EXAM MASTER PROTOCOL
### STATUS: FINAL_REVIEW_MODE

""" + EXPORT_HEADER + """

## I. ADVERSE POSSESSION (COAH)
**Goal:** Turn trespasser into owner.
1.  **Continuous:** Statutory period (e.g., 10 years).
2.  **Open & Notorious:** Visible use.
3.  **Actual & Exclusive:** Not sharing with owner.
4.  **Hostile:** Without permission.

---

## II. ESTATES & FUTURE INTERESTS
* **Fee Simple Absolute:** "To A." (Forever).
* **Life Estate:** "To A for life." (Reversion to Grantor).
* **Rule Against Perpetuities (RAP):** "No interest is good unless it must vest, if at all, not later than 21 years after some life in being at creation."
    * *Applies to:* Contingent remainders, Executory interests, Vested remainder subject to open.

---

## III. LANDLORD / TENANT
* **Types:** Term of Years (Fixed), Periodic (Month-to-month), At Will, Sufferance (Holdover).
* **Tenant Duties:** Pay rent, avoid waste.
* **Landlord Duties:**
    * *Possession:* Deliver keys.
    * *Implied Warranty of Habitability:* Basic human living standards (Heat, Water). Breach -> T can withhold rent.
    * *Quiet Enjoyment:* No constructive eviction (unlivable conditions forcing T out).

---

## IV. EASEMENTS
**Right to use land of another.**
* **Creation (PING):**
    * *Prescription:* Adverse use (like Adv Poss).
    * *Implication:* Prior use implied from division.
    * *Necessity:* Landlocked.
    * *Grant:* Writing (>1 year).
* **Termination (END CRAMP):** Estoppel, Necessity ends, Destruction, Condemnation, Release, Abandonment, Merger, Prescription.

---

## V. TAKINGS (5th Amendment)
* **Rule:** Private property shall not be taken for public use without just compensation.
* **Per Se Taking:** Physical occupation (*Loretto*).
* **Regulatory Taking:**
    * *Total:* Leaves NO economic value (*Lucas*).
    * *Partial:* Penn Central Balancing (Economic impact vs. Expectation vs. Character).
""",

    "Torts": """---
layout: default
title: Torts Comprehensive Outline
---
# // TORTS: EXAM MASTER PROTOCOL
### STATUS: FINAL_REVIEW_MODE

""" + EXPORT_HEADER + """

## I. NEGLIGENCE (Prima Facie Case)
1.  **Duty:** Owed to foreseeable P's in Zone of Danger (*Palsgraf*).
    * *Standard:* Reasonably Prudent Person (RPP).
    * *Special Duties:* Landowners (invitees vs trespassers), Professionals, Children.
2.  **Breach:** Failure to meet standard.
    * *Hand Formula:* B < PL.
    * *Negligence Per Se:* Statute violation.
    * *Res Ipsa:* "Barrel doesn't fall without negligence."
3.  **Causation:**
    * *Actual:* But-For Test.
    * *Proximate:* Foreseeability. (Intervening Superseding Acts break chain).
4.  **Damages:** Actual harm.

---

## II. INTENTIONAL TORTS
* **Battery:** Harmful/Offensive contact + Intent to contact.
* **Assault:** Reasonable apprehension of immediate battery.
* **False Imprisonment:** Confinement + Awareness.
* **IIED:** Outrageous conduct + Severe distress.
* **Trespass:** Physical invasion of land.

---

## III. STRICT LIABILITY
* **Animals:** Wild animals (always SL), Domestic (One bite rule).
* **Abnormally Dangerous:** Blasting, Chemicals. (*Rylands*).
* **Products Liability:**
    1.  Merchant seller.
    2.  Defective Product (Design, Manufacture, Warning).
    3.  Unaltered condition.
    4.  Harm.

---

## IV. DEFAMATION
1.  Defamatory Statement (Adversely affects rep).
2.  Publication (to 3rd party).
3.  Damage.
4.  **Constitutional Layer (NY Times v. Sullivan):**
    * *Public Figure:* Must prove **Actual Malice** (Knowledge of falsity or reckless disregard).
    * *Private Figure:* Negligence is enough.
""",

    "Administrative_Law": """---
layout: default
title: Admin Law Comprehensive Outline
---
# // ADMINISTRATIVE LAW: EXAM MASTER PROTOCOL
### STATUS: FINAL_REVIEW_MODE

""" + EXPORT_HEADER + """

## I. DELEGATION
* **Non-Delegation Doctrine:** Congress cannot delegate legislative power without an "Intelligible Principle." (Historically very loose).

## II. AGENCY ACTION
* **Rulemaking (Legislative):**
    * *Notice & Comment (553):* Publish draft, accept comments, publish final.
* **Adjudication (Judicial):** Hearings, ALJ decisions.

## III. JUDICIAL REVIEW
* **Standing:** Injury + Causation + Redressability.
* **Chevron Deference (HISTORICAL/OVERTURNED):** Used to defer to agency on ambiguous statutes.
* **Loper Bright (2024):** **MAJOR SHIFT.** Courts must exercise independent judgment on legal questions. No automatic deference to agency interpretation.
* **Arbitrary & Capricious (State Farm):** Agency must examine relevant data and articulate satisfactory explanation. Hard Look Review.
""",

    "Corporations": """---
layout: default
title: Corporations Comprehensive Outline
---
# // CORPORATIONS: EXAM MASTER PROTOCOL
### STATUS: FINAL_REVIEW_MODE

""" + EXPORT_HEADER + """

## I. FORMATION
* **De Jure:** File Articles of Incorporation with Secretary of State.
* **De Facto:** Good faith attempt to incorporate + act like corp.
* **Piercing Corporate Veil:** Court ignores limited liability if: Alter Ego / Undercapitalization / Fraud.

## II. FIDUCIARY DUTIES
### A. Duty of Care
* **Rule:** Act as prudent person in like position.
* **Business Judgment Rule (BJR):** Court will NOT second guess business decisions if: Informed + Good Faith + No Conflict.
* **Overcoming BJR:** Gross Negligence (*Van Gorkom*).

### B. Duty of Loyalty
* **Self-Dealing:** Director on both sides of deal. Voidable unless:
    1.  Approved by disinterested directors.
    2.  Approved by shareholders.
    3.  Fair to corp.
* **Corporate Opportunity:** Cannot usurp opportunity belonging to corp.

## III. SHAREHOLDER SUITS
* **Direct:** SH harmed personally (dividend denial).
* **Derivative:** Harm to Corp. (SH sues on behalf).
    * *Demand Requirement:* Must ask board to sue first (unless futile).
""",

    "Evidence": """---
layout: default
title: Evidence Comprehensive Outline
---
# // EVIDENCE: EXAM MASTER PROTOCOL
### STATUS: FINAL_REVIEW_MODE

""" + EXPORT_HEADER + """

## I. RELEVANCE
* **401:** Any tendency to make fact more/less probable.
* **403:** Probative value substantially outweighed by prejudice, confusion, waste of time.

## II. CHARACTER EVIDENCE
* **Civil:** Inadmissible to prove propensity. (Exceptions: Defamation, Custody).
* **Criminal:**
    * Pros cannot introduce bad character first.
    * D can "open door" with good character -> Pros can rebut.
* **MIMIC (Not Character):** Motive, Intent, Mistake, Identity, Common Plan.

## III. HEARSAY
**Definition:** Out of court statement + Offered for truth.

### A. Exclusions (Not Hearsay)
* Prior Statement of Witness (if subject to cross).
* **Party Opponent Admission:** Anything D said is admissible against D.

### B. Exceptions (Declarant Unavailable)
* Former Testimony.
* Dying Declaration (Homicide/Civil only).
* Statement Against Interest.

### C. Exceptions (Availability Irrelevant)
* Present Sense Impression.
* Excited Utterance.
* State of Mind.
* Business Records.

## IV. IMPEACHMENT
* Prior Inconsistent Statement.
* Bias.
* Prior Convictions (Crimen Falsi = Automatic; Felony = Balancing).
""",

    "Criminal_Procedure": """---
layout: default
title: Crim Pro Comprehensive Outline
---
# // CRIMINAL PROCEDURE: EXAM MASTER PROTOCOL
### STATUS: FINAL_REVIEW_MODE

""" + EXPORT_HEADER + """

## I. FOURTH AMENDMENT (Search & Seizure)
* **Step 1: Search?** Gov't conduct violating Reasonable Expectation of Privacy (Katz).
* **Step 2: Warrant?** Needs Probable Cause + Particularity.
* **Step 3: Exceptions?**
    * **S**earch Incident to Arrest.
    * **P**lain View.
    * **A**utomobile (if PC exists).
    * **C**onsent.
    * **E**xigent Circumstances.
    * **S**top & Frisk (*Terry* - RS).

## II. FIFTH AMENDMENT (Confessions)
* **Miranda:** Custody + Interrogation.
* **Waiver:** Must be Knowing, Voluntary, Intelligent.
* **Invocation:** Must be explicit ("I want a lawyer").

## III. SIXTH AMENDMENT
* **Right to Counsel:** Post-charge critical stages.
* **Ineffective Assistance:** 1) Deficient performance + 2) Prejudice (Outcome would be different).

## IV. EXCLUSIONARY RULE
* **Fruit of Poisonous Tree:** Evidence derived from illegality is out.
* *Exceptions:* Independent Source, Inevitable Discovery, Attenuation.
""",

    "Professional_Responsibility": """---
layout: default
title: Professional Responsibility Comprehensive Outline
---
# // PROFESSIONAL RESPONSIBILITY: EXAM MASTER PROTOCOL
### STATUS: FINAL_REVIEW_MODE

""" + EXPORT_HEADER + """

## I. DUTIES TO CLIENT
* **Competence:** Knowledge/skill reasonably necessary.
* **Confidentiality (1.6):** Keep info secret.
    * *Exceptions:* Prevent death/GBH, Prevent fraud (using lawyer's services), Fee dispute.
* **Loyalty (Conflicts 1.7):**
    * *Direct Adversity:* Cannot represent Client A v. Client B.
    * *Material Limitation:* Lawyer's own interest limits rep.

## II. DUTIES TO COURT
* **Candor:** Cannot lie / Must correct false statements.
* **Frivolous Claims:** Must have basis in law/fact.

## III. FEES
* Must be reasonable.
* **Contingency:** Writing required. Prohibited in Criminal/Domestic.
* **Splitting:** No splitting with non-lawyers.
""",

    "Intellectual_Property": """---
layout: default
title: IP Law Comprehensive Outline
---
# // INTELLECTUAL PROPERTY: EXAM MASTER PROTOCOL
### STATUS: FINAL_REVIEW_MODE

""" + EXPORT_HEADER + """

## I. COPYRIGHT
* **Subject Matter:** Original work of authorship + Fixed in tangible medium.
* **Rights:** Reproduce, Derivative Works, Distribute, Perform, Display.
* **Infringement:** Access + Substantial Similarity.
* **Fair Use (107):**
    1.  Purpose (Transformative?).
    2.  Nature of work.
    3.  Amount used.
    4.  Effect on Market (Most important).

## II. TRADEMARK
* **Goal:** Prevent consumer confusion.
* **Distinctiveness:**
    * *Inherently:* Fanciful ("Kodak"), Arbitrary ("Apple"), Suggestive ("Coppertone").
    * *Requires Secondary Meaning:* Descriptive ("Best Buy").
    * *Generic:* No protection ("Apple" for apples).
* **Infringement:** Likelihood of Confusion (Polaroid Factors).

## III. PATENT
* **Subject Matter:** Process, Machine, Manufacture, Composition.
* **Requirements:**
    1.  Patentable Subject Matter (No abstract ideas - *Alice*).
    2.  Novelty.
    3.  Non-Obviousness.
    4.  Utility.
""",

    "Internet_Privacy_AI": """---
layout: default
title: Internet & AI Law Comprehensive Outline
---
# // INTERNET, PRIVACY & AI: THE FUTURE SHOCK
### STATUS: FINAL_REVIEW_MODE

""" + EXPORT_HEADER + """

> **MISSION:** Analyze liability, rights, and regulation in the digital frontier. This module covers the intersection of code and statutes.

## I. INTERNET LAW (THE PLATFORM LAYER)
### A. Section 230 (CDA)
* **The Shield:** "No provider or user of an interactive computer service shall be treated as the publisher or speaker of any information provided by another information content provider."
* **Core Function:** Platforms are immune from liability for user-generated content (defamation, negligence, etc.).
* **Key Case:** [*Zeran v. AOL*](https://law.justia.com/cases/federal/appellate-courts/F3/129/327/622664/) (1997) - Distributor liability rejected. 230 is broad immunity.
* **Exceptions:** Federal Criminal Law, IP Law (DMCA), FOSTA-SESTA (Sex trafficking).
* **The Algorithm Debate:** Does recommendation = publishing? (*Gonzalez v. Google* - SCOTUS punted, but 230 generally protects algorithms).

### B. DMCA Section 512 (Copyright Safe Harbor)
* **The Trade-Off:** Platforms avoid copyright liability if they follow rules.
* **Requirements:**
    1.  No actual knowledge of infringement.
    2.  No financial benefit directly attributable to infringing activity (where platform controls).
    3.  **Notice & Takedown:** Must remove content "expeditiously" upon receipt of valid notice.
* **Key Case:** [*Viacom v. YouTube*](https://en.wikipedia.org/wiki/Viacom_International_Inc._v._YouTube,_Inc.) - "General knowledge" that YouTube has pirated clips isn't enough; need specific knowledge of specific clips.

---

## II. PRIVACY (THE DATA LAYER)
### A. Fourth Amendment in the Digital Age
**"The Reasonable Expectation of Privacy" (REP)**
* **Thermal Imaging:** [*Kyllo v. US*](https://supreme.justia.com/cases/federal/us/533/27/) - Using tech not in general public use to see inside home = Search.
* **GPS Tracking:** [*US v. Jones*](https://supreme.justia.com/cases/federal/us/565/400/) - Physical attachment of GPS to car = Trespass/Search.
* **Cell Phones:** [*Riley v. California*](https://supreme.justia.com/cases/federal/us/573/373/) - Police need warrant to search phone incident to arrest. Digital data is different from physical pockets.
* **CSLI (Location):** [*Carpenter v. US*](https://supreme.justia.com/cases/federal/us/585/16-402/) - Third-Party Doctrine exception. People have REP in long-term physical movements. Warrant required for historical cell site data.

### B. Consumer Privacy (Statutory)
* **GDPR (EU):** Gold standard.
    * *Principles:* Consent, Minimization, Purpose Limitation.
    * *Rights:* Access, Erasure ("Right to be Forgotten"), Portability.
* **CCPA/CPRA (California):**
    * *Rights:* Know, Delete, Opt-Out of Sale/Sharing.
    * *Definition of Sale:* Exchange for "monetary or other valuable consideration" (Broad).

---

## III. ARTIFICIAL INTELLIGENCE (THE ALGORITHMIC LAYER)
### A. Copyright & Generative AI
**1. The Input Side (Training)**
* **The Issue:** Is scraping billions of images/text to train a model "Fair Use"?
* **Arguments:**
    * *Pro-AI:* It's transformative. It learns patterns, doesn't collage. Similar to [*Authors Guild v. Google*](https://en.wikipedia.org/wiki/Authors_Guild,_Inc._v._Google,_Inc.) (Book scanning).
    * *Anti-AI:* It competes in the same market. It's commercial scale copying.
* **Current Status:** Heavily litigated (*NYT v. OpenAI*, *Andersen v. Stability AI*).

**2. The Output Side (Authorship)**
* **Rule:** Copyright requires **Human Authorship**.
* **USCO Position:** Images generated solely by Midjourney/DALL-E are NOT copyrightable. (*Thaler v. Perlmutter*).

### B. Algorithmic Bias & Liability
* **Disparate Impact:** AI in hiring/housing/lending that discriminates against protected classes.
* **Section 230 Defense?** If the AI *generates* the discriminatory content (e.g., a chatbot writing hate speech), is the platform the creator? 230 might not apply to *created* content.

---

## IV. BLOCKCHAIN & CRYPTO (THE TRUST LAYER)
### A. Securities Regulation
* **The Question:** Is a token a "security"?
* **The Howey Test** ([*SEC v. W.J. Howey Co.*](https://supreme.justia.com/cases/federal/us/328/293/)):
    1.  Investment of money.
    2.  In a common enterprise.
    3.  With expectation of profits.
    4.  Derived solely from the efforts of others.
* **Application:** Bitcoin (Commodity) vs. ICOs (Likely Securities).

### B. Smart Contracts
* **Concept:** Self-executing code on blockchain.
* **Legal Status:** Generally enforceable if contract elements (Offer/Acceptance/Consideration) met.
* **The Problem:** "Code is Law" vs. "Law is Law." If code allows a hack (The DAO), is it legal theft? (Courts say no, unjust enrichment applies).
"""
}

# --- CURRICULUM DATA (YAML) ---
CURRICULUM_YAML = """1L_Core_Kernel:
  - ["Civil_Procedure"]
  - ["Constitutional_Law"]
  - ["Contracts"]
  - ["Criminal_Law"]
  - ["Property_Law"]
  - ["Torts"]

Advanced_Protocols:
  - ["Administrative_Law"]
  - ["Corporations"]
  - ["Evidence"]
  - ["Criminal_Procedure"]
  - ["Professional_Responsibility"]
  - ["Intellectual_Property"]
  - ["Internet_Privacy_AI"]
"""

def main():
    print("--- INITIATING COMPREHENSIVE CONTENT GENERATION (v4.0) ---")
    
    base_dir = 'notes'
    if not os.path.exists(base_dir):
        print(" ! ERROR: 'notes' directory not found.")
        return

    # 1. Update Curriculum Data
    if not os.path.exists('_data'): os.makedirs('_data')
    with open('_data/curriculum.yml', 'w') as f:
        f.write(CURRICULUM_YAML)
    print(" > Updated _data/curriculum.yml (Added Internet_Privacy_AI)")

    # 2. Generate Outlines
    for subject, content in DETAILED_OUTLINES.items():
        subject_dir = os.path.join(base_dir, subject)
        if not os.path.exists(subject_dir):
            os.makedirs(subject_dir)
        
        # Write File
        outline_path = os.path.join(subject_dir, 'Attack_Outline.md')
        with open(outline_path, 'w') as f:
            f.write(content)
        print(f" > Generated Exam Outline: {outline_path}")
        
        # Link in Syllabus (Index)
        index_path = os.path.join(subject_dir, 'index.md')
        if not os.path.exists(index_path):
             with open(index_path, 'w') as f:
                f.write(f"---\nlayout: default\ntitle: {subject}\n---\n# {subject}\n")

        with open(index_path, 'r') as f:
            if "Attack_Outline.md" not in f.read():
                with open(index_path, 'a') as af:
                    af.write(f"\n\n### [>> ACCESS EXAM OUTLINE <<](Attack_Outline.md)\n")

    print("--- CONTENT DEPLOYED. ---")

if __name__ == "__main__":
    main()