---
layout: default
title: Internet & AI Law Comprehensive Outline
---
# // INTERNET, PRIVACY & AI: THE FUTURE SHOCK
### STATUS: FINAL_REVIEW_MODE


<div class="export-controls" style="margin-bottom: 30px; border-bottom: 1px solid #333; padding-bottom: 20px;">
    <button onclick="window.print()" style="background: #00ff41; color: black; border: none; padding: 10px 20px; font-family: 'Fira Code', monospace; font-weight: bold; cursor: pointer; margin-right: 10px;">[ SAVE AS PDF ]</button>
    <a href="Attack_Outline.md" download="Attack_Outline.md" style="color: #00f3ff; text-decoration: none; font-family: 'Fira Code', monospace; font-weight: bold;">[ DOWNLOAD MARKDOWN ]</a>
</div>


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
