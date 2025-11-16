
document.addEventListener('DOMContentLoaded', function() {
    const terminalContent = document.getElementById('terminal-content');
    const mainGui = document.getElementById('main-gui');
    const inputLine = document.getElementById('input-line');
    const cmdInput = document.getElementById('cmd-input');
    const history = document.getElementById('history');

    // --- KNOWLEDGE BASE (RESUME DATA LOADED) ---
    const db = {
        "who": "IDENTITY: Alexei Furs | Senior Privacy Engineer @ Google DeepMind | Admitted Attorney (NYS).",
        "about": "BIO: Operating at the intersection of Law & Code. Focused on AI Governance, Privacy Engineering, and Digital Rights.",
        "resume": "ACCESSING FILE... <a href='/assets/Alexei_Furs_Resume.pdf' target='_blank'>[ DOWNLOAD_RESUME.PDF ]</a>",
        "contact": "UPLINK ESTABLISHED: <a href='https://www.linkedin.com/in/alexei-furs-35587773/' target='_blank'>[ LINKEDIN_PROFILE ]</a>",
        "github": "REPO SOURCE: <a href='https://github.com/alexeibex' target='_blank'>github.com/alexeibex</a>",
        "papers": "INDEXING RESEARCH... See the <a href='#research-papers'>Research Module</a> below for full text.",
        "notes": "ACCESSING ARCHIVE... Law school notes are available in the <a href='#legal-archive'>Archive Module</a> below.",
        
        // --- EXPANDED COMMANDS ---
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

        "help": "AVAILABLE COMMANDS: who, about, experience, education, skills, bar, projects, resume, contact, papers, notes, clear, exit."
    };

    // --- BOOT SEQUENCE ---
    const sequence = [
        { text: "> INITIALIZING LEGAL_OS v4.0...", delay: 300, class: "system-msg" },
        { text: "> VERIFYING ENCRYPTION KEYS...", delay: 600, class: "system-msg" },
        { text: "> ACCESS GRANTED: ALEXEI FURS [JD_GRADUATE]", delay: 1000, class: "success-msg" },
        { text: "> EXECUTE identity.py --verbose", delay: 1400, class: "command" },
        { text: "  ... Loading Professional Profile", delay: 1700, class: "output" },
        { text: "  ... Linking Google DeepMind Credentials", delay: 1900, class: "output" },
        { text: "  ... Mounting NYS Bar Admission", delay: 2100, class: "output" },
        { text: "> SYSTEM READY. WAITING FOR INPUT.", delay: 2400, class: "success-msg" }
    ];

    let currentIndex = 0;

    function typeLine(lineObj, callback) {
        const line = document.createElement('div');
        line.className = 'terminal-line ' + lineObj.class;
        terminalContent.appendChild(line);

        let charIndex = 0;
        const typeInterval = setInterval(() => {
            if (charIndex < lineObj.text.length) {
                line.textContent += lineObj.text.charAt(charIndex);
                charIndex++;
                // Only auto-scroll during boot sequence, not interactive mode
                window.scrollTo(0, document.body.scrollHeight);
            } else {
                clearInterval(typeInterval);
                if (callback) callback();
            }
        }, 10); 
    }

    function runSequence() {
        if (currentIndex < sequence.length) {
            const step = sequence[currentIndex];
            setTimeout(() => {
                typeLine(step, runSequence);
                currentIndex++;
            }, step.delay / 2);
        } else {
            // Boot complete: Reveal GUI and Enable Input
            mainGui.classList.add('visible');
            inputLine.style.display = 'flex';
            cmdInput.focus();
        }
    }

    // --- INTERACTIVE LOGIC ---
    cmdInput.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            const rawInput = cmdInput.value;
            const cmd = rawInput.trim().toLowerCase();
            
            // 1. Echo Command to History
            addHistory("user@legal-os:~$ " + rawInput, "command-echo");
            
            // 2. Process Command
            cmdInput.value = '';
            processCommand(cmd);
            
            // 3. NO AUTO SCROLL - Keeps view stable at the top input
        }
    });

    function addHistory(text, type) {
        const line = document.createElement('div');
        line.className = 'terminal-line ' + type;
        line.innerHTML = text;
        // Prepend to history so newest is at top (optional) or Append?
        // Standard terminal appends. Since input is at top, let's try prepending 
        // to make it feel like a reverse feed, OR just append and let it grow down.
        // Given layout, appending works best as history sits ABOVE input in standard HTML flow,
        // BUT we moved input to top. So history should be BELOW input? 
        // Let's stick to appending to the 'history' div. 
        // NOTE: In the HTML structure, 'history' is ABOVE 'input-line' or BELOW?
        // User asked to move input higher. In standard terminal, input is at bottom. 
        // If input is at top, history should probably appear below it.
        // Let's adjust the HTML structure in the python script to put history BELOW input.
        history.appendChild(line);
    }

    function processCommand(cmd) {
        if (cmd === 'clear' || cmd === 'cls') {
            history.innerHTML = '';
            return;
        }
        if (cmd === 'exit') {
            addHistory("> SESSION TERMINATED. GOODBYE.", "system-msg");
            cmdInput.disabled = true;
            return;
        }

        // Search Knowledge Base
        let response = "> ERROR: UNRECOGNIZED COMMAND. TRY 'HELP'.";
        
        if (db[cmd]) {
            response = db[cmd];
        } else {
            // Fuzzy Search
            if (cmd.includes('resume') || cmd.includes('cv')) response = db['resume'];
            else if (cmd.includes('who') || cmd.includes('name')) response = db['who'];
            else if (cmd.includes('contact') || cmd.includes('email') || cmd.includes('linkedin')) response = db['contact'];
            else if (cmd.includes('job') || cmd.includes('work') || cmd.includes('google')) response = db['experience'];
            else if (cmd.includes('school') || cmd.includes('degree')) response = db['education'];
            else if (cmd.includes('skill') || cmd.includes('tech')) response = db['skills'];
            else if (cmd.includes('paper') || cmd.includes('mit')) response = db['papers'];
            else if (cmd.includes('note') || cmd.includes('law')) response = db['notes'];
        }
        
        addHistory(response, "response-msg");
    }

    // Start System
    runSequence();
    
    // Keep focus
    document.addEventListener('click', function() {
        if(inputLine.style.display !== 'none') cmdInput.focus();
    });
});
