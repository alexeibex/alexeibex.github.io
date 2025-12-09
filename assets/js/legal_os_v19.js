
document.addEventListener('DOMContentLoaded', function() {
    const terminalContent = document.getElementById('terminal-content');
    const mainGui = document.getElementById('main-gui');
    const inputLine = document.getElementById('input-line');
    const cmdInput = document.getElementById('cmd-input');
    const history = document.getElementById('history');
    const promptText = document.querySelector('.prompt');

    // --- CONFIGURATION (NO API KEYS) ---
    const OWNER_EMAIL = "alexeifurs92@gmail.com";
    
    // --- LOCAL KNOWLEDGE BASE (THE BRAIN) ---
    const knowledge = {
        "who": "IDENTITY: Alexei Furs | Senior Privacy Engineer @ Google DeepMind | Admitted Attorney (NYS).",
        "alexei": "IDENTITY: Alexei Furs | Senior Privacy Engineer @ Google DeepMind | Admitted Attorney (NYS).",
        "about": "BIO: Operating at the intersection of Law & Code. Focused on AI Governance, Privacy Engineering, and Digital Rights.",
        
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
        
        "resume": "ACCESSING FILE... <a href='/assets/Alexei_Furs_Resume.pdf' target='_blank'>[ DOWNLOAD_RESUME.PDF ]</a>",
        
        "help": "AVAILABLE COMMANDS: experience, education, skills, bar, projects, contact, resume, generate nda, generate cease."
    };

    // --- STATE ---
    let aiLocked = true; 
    let interrogationStep = 0;
    const visitorLog = { name: "", purpose: "", metAlexei: "", wantsMeeting: "N/A" };

    // --- HOLLYWOOD BOOT SEQUENCE ---
    const complexBoot = [
        { text: "Initializing Legal_OS Kernel v19.0...", delay: 50 },
        { text: "Verifying Integrity of /dev/sda1...", delay: 100 },
        { text: "Loading Security Modules...", delay: 100 },
        { cmd: "clear", delay: 300 },
        { text: "> BIOS CHECK: OK", delay: 50 },
        { text: "> CPU: NEURAL_ENGINE_X9", delay: 50 },
        { text: "> MEMORY TEST: 64GB OK", delay: 50 },
        { text: "> MOUNTING VOLUMES...", delay: 200 },
        { cmd: "bar", duration: 1500 }, 
        { text: "> ENCRYPTION: AES-256 ENABLED", delay: 100 },
        { text: "> ESTABLISHING LOCAL CONNECTION...", delay: 300 },
        { text: "> HANDSHAKE COMPLETE.", delay: 100 },
        { cmd: "clear", delay: 300 },
        { text: "Welcome, User.", delay: 500 },
        { text: "Loading Interface...", delay: 500 }
    ];

    const wait = (ms) => new Promise(resolve => setTimeout(resolve, ms));

    async function typeLine(text, container, autoScroll = true) {
        const line = document.createElement('div');
        line.className = 'terminal-line system-msg';
        container.appendChild(line);
        for (let i = 0; i < text.length; i++) {
            line.innerHTML += text.charAt(i);
            await wait(2);
        }
        if (autoScroll) window.scrollTo(0, document.body.scrollHeight);
    }

    async function runProgressBar(duration) {
        const line = document.createElement('div');
        line.className = 'terminal-line system-msg';
        terminalContent.appendChild(line);
        const frames = 30;
        const stepTime = duration / frames;
        for (let i = 0; i <= frames; i++) {
            const percent = Math.floor((i/frames)*100);
            const bars = "█".repeat(i);
            const spaces = "░".repeat(frames - i);
            line.innerText = `> LOADING: [${bars}${spaces}] ${percent}%`;
            await wait(stepTime);
        }
        window.scrollTo(0, document.body.scrollHeight);
    }

    async function runBoot() {
        if (sessionStorage.getItem("boot_complete")) {
            terminalContent.style.display = 'none';
            completeBoot();
            return;
        }
        for (let step of complexBoot) {
            if (step.cmd === 'clear') {
                await wait(step.delay);
                terminalContent.innerHTML = '';
            } else if (step.cmd === 'bar') {
                await runProgressBar(step.duration);
            } else {
                await typeLine(step.text, terminalContent, true);
                await wait(step.delay);
            }
        }
        completeBoot();
    }

    function completeBoot() {
        sessionStorage.setItem("boot_complete", "true");
        mainGui.classList.add('visible');
        inputLine.style.display = 'flex';
        cmdInput.focus();
    }

    // --- MODAL LOGIC ---
    window.closeEmailModal = function() {
        document.getElementById('email-modal').style.display = 'none';
        unlockAI();
    };

    function showEmailModal() {
        const subject = `LEGAL_OS LOG: ${visitorLog.name}`;
        const body = `NAME: ${visitorLog.name}\nPURPOSE: ${visitorLog.purpose}\nMET: ${visitorLog.metAlexei}\nMEETING: ${visitorLog.wantsMeeting}`;
        
        const gmailUrl = `https://mail.google.com/mail/?view=cm&fs=1&to=${OWNER_EMAIL}&su=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
        
        document.getElementById('modal-log-content').innerText = body;
        
        const container = document.getElementById('mail-btn-container');
        container.innerHTML = `<a href="${gmailUrl}" target="gmailPopup" onclick="window.open(this.href, 'gmailPopup', 'width=600,height=700,scrollbars=yes,resizable=yes'); return false;" class="action-btn" style="display:block; text-align:center; text-decoration:none; line-height:40px; color:#0a0a0a;">[ LAUNCH GMAIL POPUP ]</a>`;
        
        document.getElementById('email-modal').style.display = 'flex';
    }

    // --- INTERROGATION ---
    const interrogationSequence = [
        { text: "SECURITY ALERT: UNIDENTIFIED USER.", field: "alert" },
        { text: "TO ACCESS TERMINAL, PLEASE IDENTIFY YOURSELF.", field: "name" },
        { text: "STATE YOUR PURPOSE.", field: "purpose" },
        { text: "HAVE YOU MET THE TARGET [ALEXEI] IN PERSON? (Y/N)", field: "metAlexei", validate: true },
        { text: "DO YOU SEEK A MEETING? (Y/N)", field: "wantsMeeting", validate: true }, 
        { text: "TRANSMIT LOGS TO ADMIN? (Y/N)", field: "transmit", validate: true }
    ];

    function startInterrogation() {
        cmdInput.value = "";
        promptText.style.color = "#ff2a2a";
        promptText.innerText = "SECURITY_PROTOCOL:~$";
        cmdInput.style.color = "#ff2a2a";
        inputLine.style.borderColor = "#ff2a2a";
        printQuestion(0);
    }

    function printQuestion(index) {
        const q = interrogationSequence[index];
        if (q.field === "wantsMeeting" && visitorLog.metAlexei.toLowerCase().startsWith('y')) {
            interrogationStep++;
            printQuestion(interrogationStep);
            return;
        }
        const line = document.createElement('div');
        line.className = 'terminal-line question-msg';
        line.style.color = "#ff2a2a";
        line.innerText = "> " + q.text;
        history.appendChild(line);
        
        if (q.field === "alert") {
            interrogationStep++;
            setTimeout(() => printQuestion(interrogationStep), 800);
        } else {
             const isNearBottom = window.innerHeight + window.scrollY >= document.body.offsetHeight - 100;
             if (isNearBottom) window.scrollTo(0, document.body.scrollHeight);
        }
    }

    function handleInterrogationInput(input) {
        const currentQ = interrogationSequence[interrogationStep];
        const echo = document.createElement('div');
        echo.className = 'terminal-line';
        echo.style.color = "#ff2a2a";
        echo.innerText = input;
        history.appendChild(echo);

        // VALIDATION
        if (currentQ.validate) {
            const validAnswers = ['y', 'yes', 'n', 'no'];
            if (!validAnswers.includes(input.trim().toLowerCase())) {
                const errorMsg = document.createElement('div');
                errorMsg.className = 'terminal-line error-msg';
                errorMsg.innerText = "> ERROR: INVALID FORMAT. EXPECTED [Y/N].";
                history.appendChild(errorMsg);
                setTimeout(() => {
                     const retryLine = document.createElement('div');
                     retryLine.className = 'terminal-line question-msg';
                     retryLine.style.color = "#ff2a2a";
                     retryLine.innerText = "> " + currentQ.text;
                     history.appendChild(retryLine);
                     window.scrollTo(0, document.body.scrollHeight);
                }, 500);
                return; 
            }
        }

        if (currentQ.field !== "alert") visitorLog[currentQ.field] = input;

        if (currentQ.field === "transmit") {
            if (input.toLowerCase().startsWith('y')) {
                showEmailModal();
            } else {
                unlockAI();
            }
            return;
        }

        interrogationStep++;
        if (interrogationStep < interrogationSequence.length) {
            setTimeout(() => printQuestion(interrogationStep), 300);
        } else {
            unlockAI();
        }
    }

    function unlockAI() {
        aiLocked = false;
        const success = document.createElement('div');
        success.className = 'terminal-line success-msg';
        success.innerText = "> ACCESS GRANTED. LOCAL TERMINAL ONLINE.";
        history.appendChild(success);
        promptText.style.color = "#00f3ff";
        promptText.innerText = "user@legal-os:~$";
        cmdInput.style.color = "#00ff41";
        inputLine.style.borderColor = "#333";
        cmdInput.placeholder = "Ask me anything...";
        cmdInput.focus();
    }

    // --- LOCAL BRAIN (NO API) ---
    function processQuery(input) {
        const lower = input.toLowerCase();
        
        // 1. Doc Gen
        if (lower.startsWith("generate") || lower.startsWith("draft")) {
             const type = lower.includes("nda") ? "nda" : (lower.includes("cease") ? "cease" : null);
             return type ? generateDoc(type) : "> SPECIFY DOC: NDA or CEASE.";
        }

        // 2. Keyword Matching
        for (const [key, value] of Object.entries(knowledge)) {
            if (lower.includes(key)) return value;
        }
        
        // 3. Complex Keyword Matching (e.g. "job" -> "experience")
        if (lower.includes("work") || lower.includes("job") || lower.includes("career")) return knowledge["experience"];
        if (lower.includes("school") || lower.includes("college") || lower.includes("degree")) return knowledge["education"];
        if (lower.includes("tech") || lower.includes("code") || lower.includes("stack")) return knowledge["skills"];
        if (lower.includes("lawyer") || lower.includes("attorney")) return knowledge["bar"];
        if (lower.includes("paper") || lower.includes("publication")) return knowledge["projects"];
        if (lower.includes("email") || lower.includes("phone")) return knowledge["contact"];
        
        // 4. Default
        return "> QUERY NOT RECOGNIZED. TRY 'HELP' FOR COMMAND LIST.";
    }

    function generateDoc(type) {
        const disclaimer = `<br><strong style="color:#ff2a2a;">DISCLAIMER: I AM NOT YOUR LAWYER. DEMONSTRATION ONLY.</strong><br>`;
        const templates = {
            "nda": `> GENERATING NDA...${disclaimer}<br>MUTUAL NDA TEMPLATE...`,
            "cease": `> GENERATING CEASE...${disclaimer}<br>CEASE & DESIST TEMPLATE...`
        };
        return templates[type] || "> ERROR: UNKNOWN DOC.";
    }

    function simulateThinking(cb) {
        const line = document.createElement('div');
        line.innerText = "> SEARCHING LOCAL DATABASE...";
        line.className = 'terminal-line system-msg';
        history.appendChild(line);
        setTimeout(() => { line.remove(); cb(); }, 600);
    }

    // --- INPUT HANDLER ---
    cmdInput.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            const rawInput = cmdInput.value.trim();
            if (!rawInput) return;

            if (aiLocked) {
                if (interrogationStep === 0) { startInterrogation(); return; }
                handleInterrogationInput(rawInput);
                cmdInput.value = "";
                return;
            }

            const echo = document.createElement('div');
            echo.className = 'terminal-line command-echo';
            echo.innerText = `user@legal-os:~$ ${rawInput}`;
            history.appendChild(echo);
            cmdInput.value = '';

            if (rawInput.toLowerCase() === 'clear') {
                history.innerHTML = '';
                return;
            }

            simulateThinking(() => {
                 const response = processQuery(rawInput);
                 const respDiv = document.createElement('div');
                 respDiv.className = 'terminal-line response-msg';
                 respDiv.style.borderLeftColor = "#00f3ff"; 
                 respDiv.innerHTML = response;
                 history.appendChild(respDiv);
            });
        }
    });

    runBoot();
});
