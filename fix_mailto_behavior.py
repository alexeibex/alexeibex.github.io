import os

# --- 1. THE NEURAL ENGINE (JAVASCRIPT) ---
TERMINAL_JS = """
document.addEventListener('DOMContentLoaded', function() {
    const terminalContent = document.getElementById('terminal-content');
    const mainGui = document.getElementById('main-gui');
    const inputLine = document.getElementById('input-line');
    const cmdInput = document.getElementById('cmd-input');
    const history = document.getElementById('history');
    const promptText = document.querySelector('.prompt');

    // --- CONFIGURATION ---
    // REPLACE THESE WITH YOUR ACTUAL DETAILS
    const API_KEY = "AIzaSyCQz68Pa_FSesxzCxYJMjMgj7dnHHwijwc"; 
    const OWNER_EMAIL = "alexeifurs92@gmail.com";
    
    const SYSTEM_PROMPT = `You are Legal_OS v7.1, a cyberpunk portfolio assistant for Alexei Furs. 
    Alexei is a Senior Privacy Engineer at Google DeepMind and an Admitted Attorney (NYS). 
    Key Bio:
    - Current: Google DeepMind (Privacy for Gemini/AI Agents).
    - Previous: Google (Search/Assistant), Twitter, BetterCloud.
    - Education: Brooklyn Law (JD), Georgetown (BA).
    - Tech: Python, SQL, Privacy Engineering.
    - Projects: MIT Computational Law Report co-author.
    
    INSTRUCTIONS:
    1. Answer the user's question briefly (under 3 sentences).
    2. Use a cool, professional, cyberpunk tone (e.g., "Affirmative," "Data retrieved").
    3. If asked about general facts (math, history), answer correctly but briefly.
    4. If asked for legal advice, state that you are a portfolio bot and cannot provide legal counsel.`;

    // --- STATE MANAGEMENT ---
    let currentMode = 'BOOT'; // BOOT, INTERROGATION, ACCESS_GRANTED
    let interrogationStep = 0;
    
    const visitorLog = {
        name: "",
        purpose: "",
        metAlexei: "",
        wantsMeeting: "N/A",
        timestamp: new Date().toISOString()
    };

    const interrogationSequence = [
        { text: "IDENTIFY YOURSELF.", field: "name" },
        { text: "STATE YOUR PURPOSE.", field: "purpose" },
        { text: "RELATIONSHIP STATUS: HAVE YOU ENCOUNTERED TARGET [ALEXEI] IN PHYSICAL REALITY? (Y/N)", field: "metAlexei" },
        { text: "DO YOU SEEK A MEETING? (Y/N)", field: "wantsMeeting" }, 
        { text: "TRANSMIT IDENTIFICATION LOGS TO SECURE SERVER? (Y/N)", field: "transmit" }
    ];

    // --- KNOWLEDGE BASE ---
    const knowledge = {
        "experience": `WORK HISTORY:
        <br>> <strong>Google DeepMind</strong> (2025-Present): Senior Privacy Engineer (AI Agents, Gemini).
        <br>> <strong>Google</strong> (2021-2025): Senior Privacy Engineer (Search & Assistant, Devices).
        <br>> <strong>BetterCloud</strong> (2019-2021): Legal Intern (Commercial Transactions).
        <br>> <strong>Twitter</strong> (2019): Legal Intern (Product Counsel, IP, Policy).
        <br>> <strong>Optimatic</strong> (2014-2018): Lead Product Manager (AdTech).`,
        
        "education": `ACADEMIC RECORD:
        <br>> <strong>Brooklyn Law School</strong> (J.D. 2021): Certificate in IP, Media & Info Law.
        <br>> <strong>Georgetown University</strong> (B.A. 2014): Government.`,
        
        "skills": `SKILLSET MATRIX:
        <br>> <strong>LEGAL:</strong> Privacy Law (GDPR/CCPA/DMA), IP Licensing, Commercial Contracts.
        <br>> <strong>TECH:</strong> Python, SQL, HTML/CSS, GitHub, Distributed Systems.
        <br>> <strong>CORE:</strong> Privacy by Design, AI Governance, Product Management.`,
        
        "bar": "STATUS: <strong>Admitted Attorney</strong> - NYS Appellate Division, 2nd Dept (Feb 2023).",
        
        "projects": `KEY PROJECTS:
        <br>> <strong>MIT Computational Law Report:</strong> Co-Author, "Trust in a Trustless System".
        <br>> <strong>BLIP:</strong> Contributor to Blockchain Law for Information Privacy.`,
        
        "contact": "UPLINK ESTABLISHED: <a href='https://www.linkedin.com/in/alexei-furs-35587773/' target='_blank'>[ LINKEDIN_PROFILE ]</a>",
        
        "resume": "ACCESSING FILE... <a href='/assets/Alexei_Furs_Resume.pdf' target='_blank'>[ DOWNLOAD_RESUME.PDF ]</a>"
    };

    // --- BOOT SEQUENCE ---
    const bootSequence = [
        { text: "> INITIALIZING SECURITY PROTOCOL...", delay: 200, class: "system-msg" },
        { text: "> SCANNING BIOMETRICS...", delay: 400, class: "system-msg" },
        { text: "> UNIDENTIFIED USER DETECTED.", delay: 600, class: "error-msg" },
        { text: "> HALT. SECURITY CLEARANCE REQUIRED.", delay: 1000, class: "error-msg" }
    ];

    function typeLine(lineObj, container, callback) {
        const line = document.createElement('div');
        line.className = 'terminal-line ' + (lineObj.class || '');
        container.appendChild(line);

        let charIndex = 0;
        const typeInterval = setInterval(() => {
            if (charIndex < lineObj.text.length) {
                line.innerHTML += lineObj.text.charAt(charIndex);
                charIndex++;
                window.scrollTo(0, document.body.scrollHeight);
            } else {
                clearInterval(typeInterval);
                if (callback) callback();
            }
        }, 5);
    }

    function runBoot(index = 0) {
        if (index < bootSequence.length) {
            typeLine(bootSequence[index], terminalContent, () => {
                setTimeout(() => runBoot(index + 1), bootSequence[index].delay / 2);
            });
        } else {
            currentMode = 'INTERROGATION';
            promptText.innerText = "UNKNOWN_USER@GATEKEEPER:~$";
            promptText.style.color = "#ff2a2a"; 
            cmdInput.style.color = "#ff2a2a";
            inputLine.style.display = 'flex';
            inputLine.style.borderColor = "#ff2a2a";
            askNextQuestion();
        }
    }

    function askNextQuestion() {
        let q = interrogationSequence[interrogationStep];
        
        // Skip "Meeting" question if they HAVE met Alexei
        if (q.field === "wantsMeeting" && (visitorLog.metAlexei.toLowerCase().startsWith('y'))) {
            interrogationStep++;
            askNextQuestion();
            return;
        }

        const line = document.createElement('div');
        line.className = 'terminal-line question-msg';
        line.innerText = "> " + q.text;
        history.appendChild(line);
        
        cmdInput.value = "";
        cmdInput.focus();
        window.scrollTo(0, document.body.scrollHeight);
    }

    function grantAccess() {
        currentMode = 'ACCESS_GRANTED';
        const grantMsg = [
            { text: "> IDENTITY VERIFIED.", delay: 500, class: "success-msg" },
            { text: "> UNLOCKING GEMINI 2.5 NEURAL NET...", delay: 800, class: "success-msg" },
            { text: "> ACCESS GRANTED: WELCOME TO LEGAL_OS.", delay: 1200, class: "success-msg" }
        ];

        let i = 0;
        function showGrant() {
            if (i < grantMsg.length) {
                typeLine(grantMsg[i], history, () => {
                    setTimeout(() => { i++; showGrant(); }, 300);
                });
            } else {
                promptText.innerText = "user@legal-os:~$";
                promptText.style.color = "#00f3ff"; 
                cmdInput.style.color = "#00ff41";
                inputLine.style.borderColor = "#333";
                mainGui.classList.add('visible');
                // UPDATED PROMPT HERE
                cmdInput.placeholder = "Ask me anything (e.g. 'Who is Alexei Furs?', 'Draft an NDA')";
                cmdInput.focus();
            }
        }
        showGrant();
    }

    function handleInterrogationInput(input) {
        const currentQ = interrogationSequence[interrogationStep];
        visitorLog[currentQ.field] = input;
        
        const echo = document.createElement('div');
        echo.className = 'terminal-line command-echo';
        echo.style.color = "#ff2a2a";
        echo.innerText = input;
        history.appendChild(echo);

        if (currentQ.field === "transmit") {
            if (input.toLowerCase().startsWith('y')) {
                const subject = `LEGAL_OS VISITOR LOG: ${visitorLog.name}`;
                const body = `VISITOR LOG CAPTURED:\n\nNAME: ${visitorLog.name}\nPURPOSE: ${visitorLog.purpose}\nMET ALEXEI: ${visitorLog.metAlexei}\nWANTS MEETING: ${visitorLog.wantsMeeting}\n\nTIMESTAMP: ${visitorLog.timestamp}`;
                
                // FALLBACK DISPLAY
                const fallback = document.createElement('div');
                fallback.className = 'terminal-line system-msg';
                fallback.innerHTML = `> INITIATING UPLINK...<br>> IF EMAIL CLIENT FAILS, COPY LOG BELOW:<br><br>--------------------<br>${body.replace(/\\n/g, '<br>')}<br>--------------------`;
                history.appendChild(fallback);

                // OPEN IN NEW TAB (Prevents Page Takeover)
                setTimeout(() => {
                    window.open(`mailto:${OWNER_EMAIL}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`, '_blank');
                }, 1000);
            } else {
                const skip = document.createElement('div');
                skip.className = 'terminal-line system-msg';
                skip.innerText = "> TRANSMISSION ABORTED. LOCAL LOGS PURGED.";
                history.appendChild(skip);
            }
            
            setTimeout(grantAccess, 1500);
            return;
        }

        interrogationStep++;
        if (interrogationStep < interrogationSequence.length) {
            setTimeout(askNextQuestion, 500);
        } else {
            grantAccess();
        }
    }

    // --- DOCUMENT GENERATOR (RESTORED) ---
    function generateDoc(type) {
        const disclaimer = `<br><strong style="color:#ff2a2a;">DISCLAIMER: I AM NOT YOUR LAWYER. THIS IS A PRE-SET TEMPLATE FOR PORTFOLIO DEMONSTRATION PURPOSES ONLY. IT DOES NOT CONSTITUTE LEGAL ADVICE. USE AT YOUR OWN RISK.</strong><br>`;

        const templates = {
            "nda": `> GENERATING NON-DISCLOSURE AGREEMENT (v1.0)...
            ${disclaimer}
            <br>---------------------------------------------------
            <br><strong>MUTUAL NON-DISCLOSURE AGREEMENT</strong>
            <br>
            <br>This Agreement is entered into by and between <strong>[ALEXEI_FURS_CLIENT]</strong> ("Disclosing Party") 
            <br>and <strong>[COUNTERPARTY_ENTITY]</strong> ("Receiving Party").
            <br>
            <br>1. <strong>Confidential Information:</strong> Shall include all data, code, and algorithms.
            <br>2. <strong>Obligations:</strong> Receiving Party shall encrypt all data with AES-256.
            <br>3. <strong>Term:</strong> This agreement survives until the heat death of the universe.
            <br>
            <br>[SIGNED_CRYPTOGRAPHICALLY]
            <br>---------------------------------------------------`,
            
            "cease": `> GENERATING CEASE & DESIST ORDER...
            ${disclaimer}
            <br>---------------------------------------------------
            <br><strong>NOTICE OF INTELLECTUAL PROPERTY INFRINGEMENT</strong>
            <br>
            <br>TO: <strong>[OFFENDING_ENTITY]</strong>
            <br>RE: UNAUTHORIZED USE OF PROPRIETARY ALGORITHMS
            <br>
            <br>We have detected unauthorized execution of code belonging to <strong>Alexei Furs</strong>.
            <br>You are hereby ordered to:
            <br>   1. TERMINATE all instances immediately.
            <br>   2. PURGE all local caches.
            <br>   3. SUBMIT a compliance report within 24 hours.
            <br>
            <br>Failure to comply will result in immediate legal escalation via Smart Contract enforcement.
            <br>---------------------------------------------------`
        };
        
        return templates[type] || "> ERROR: TEMPLATE_NOT_FOUND. TRY 'generate nda' OR 'generate cease'.";
    }

    // --- AI LOGIC: GEMINI 2.5 API CALL ---
    async function callGemini(prompt) {
        if (API_KEY.includes("PUT_YOUR")) return "> ERROR: API KEY NOT CONFIGURED.";
        const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${API_KEY}`;
        try {
            const response = await fetch(url, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ contents: [{ parts: [{ text: SYSTEM_PROMPT + "\\n\\nUSER QUERY: " + prompt }] }] })
            });
            const data = await response.json();
            if (data.error) return `> API ERROR: ${data.error.message}`;
            if (data.candidates && data.candidates.length > 0) return data.candidates[0].content.parts[0].text.replace(/\\n/g, "<br>");
            return "> API ERROR: No response.";
        } catch (error) { return "> CONNECTION FAILURE."; }
    }

    function simulateThinking(callback) {
        const id = 'proc-' + Date.now();
        const line = document.createElement('div');
        line.id = id;
        line.className = 'terminal-line system-msg';
        line.innerText = "> NEURAL_NET_PROCESSING: [                    ] 0%";
        history.appendChild(line);

        let progress = 0;
        const interval = setInterval(() => {
            progress += Math.floor(Math.random() * 15) + 5;
            if (progress > 100) progress = 100;
            const bars = "|".repeat(Math.floor(progress / 5));
            const spaces = " ".repeat(20 - Math.floor(progress / 5));
            line.innerText = `> NEURAL_NET_PROCESSING: [${bars}${spaces}] ${progress}%`;
            if (progress === 100) {
                clearInterval(interval);
                setTimeout(() => { line.remove(); callback(); }, 200);
            }
        }, 30);
    }

    // --- INPUT HANDLER ---
    cmdInput.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            const rawInput = cmdInput.value.trim();
            if (!rawInput) return;

            if (currentMode === 'INTERROGATION') {
                handleInterrogationInput(rawInput);
                return;
            }

            // ACCESS GRANTED MODE
            const echo = document.createElement('div');
            echo.className = 'terminal-line command-echo';
            echo.innerText = `user@legal-os:~$ ${rawInput}`;
            history.appendChild(echo);
            
            cmdInput.value = '';
            cmdInput.disabled = true;

            let localResponse = null;
            const lowerInput = rawInput.toLowerCase();
            
            // 1. Check Generator Commands FIRST
            if (lowerInput.startsWith("generate") || lowerInput.startsWith("draft")) {
                const type = lowerInput.includes("nda") ? "nda" : (lowerInput.includes("cease") ? "cease" : null);
                const docOutput = type ? generateDoc(type) : "> ERROR: PLEASE SPECIFY DOCUMENT TYPE (NDA / CEASE).";
                
                const respDiv = document.createElement('div');
                respDiv.className = 'terminal-line response-msg';
                respDiv.innerHTML = docOutput;
                history.appendChild(respDiv);
                
                cmdInput.disabled = false;
                cmdInput.focus();
                return;
            }

            if (lowerInput === 'clear') {
                history.innerHTML = '';
                cmdInput.disabled = false;
                cmdInput.focus();
                return;
            }
            
            // 2. Check Knowledge Base
            for (const [intent, keywords] of Object.entries({
                "experience": ["work", "job", "history", "career"],
                "education": ["school", "college", "degree", "law"],
                "skills": ["skill", "tech", "python", "sql"],
                "contact": ["email", "phone", "linkedin", "contact"],
                "bar": ["bar", "lawyer", "attorney", "admitted"],
                "projects": ["project", "paper", "mit", "blip"]
            })) {
                if (keywords.some(k => lowerInput.includes(k)) && knowledge[intent]) {
                    localResponse = knowledge[intent];
                    break;
                }
            }

            if (localResponse) {
                const respDiv = document.createElement('div');
                respDiv.className = 'terminal-line response-msg';
                respDiv.innerHTML = localResponse;
                history.appendChild(respDiv);
                cmdInput.disabled = false;
                cmdInput.focus();
            } else {
                // 3. Fallback to AI
                simulateThinking(async () => {
                    const aiResponse = await callGemini(rawInput);
                    const respDiv = document.createElement('div');
                    respDiv.className = 'terminal-line response-msg';
                    respDiv.style.borderLeftColor = "#00f3ff"; 
                    respDiv.innerHTML = aiResponse;
                    history.appendChild(respDiv);
                    cmdInput.disabled = false;
                    cmdInput.focus();
                });
            }
        }
    });

    runBoot();
    
    document.addEventListener('click', () => {
        if(inputLine.style.display !== 'none' && !cmdInput.disabled) cmdInput.focus();
    });
});
"""

def main():
    print("--- FIXING MAILTO BEHAVIOR ---")
    with open('assets/js/terminal.js', 'w') as f:
        f.write(TERMINAL_JS)
    print(" > Terminal Logic Updated.")

if __name__ == "__main__":
    main()