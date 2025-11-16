
document.addEventListener('DOMContentLoaded', function() {
    const terminalContent = document.getElementById('terminal-content');
    const mainGui = document.getElementById('main-gui');
    const inputLine = document.getElementById('input-line');
    const cmdInput = document.getElementById('cmd-input');
    const history = document.getElementById('history');

    // --- KNOWLEDGE BASE ---
    const db = {
        "who": "IDENTITY: Alexei Furs | Senior Privacy Engineer @ Google DeepMind | Admitted Attorney (NYS).",
        "about": "BIO: Operating at the intersection of Law & Code. Focused on AI Governance, Privacy Engineering, and Digital Rights.",
        "resume": "ACCESSING FILE... <a href='/assets/Alexei_Furs_Resume.pdf' target='_blank'>[ DOWNLOAD_RESUME.PDF ]</a>",
        "contact": "UPLINK ESTABLISHED: <a href='https://www.linkedin.com/in/alexei-furs-35587773/' target='_blank'>[ LINKEDIN_PROFILE ]</a>",
        "github": "REPO SOURCE: <a href='https://github.com/alexeibex' target='_blank'>github.com/alexeibex</a>",
        "papers": "INDEXING RESEARCH... See the <a href='#research-papers'>Research Module</a> above for full text.",
        "notes": "ACCESSING ARCHIVE... Law school notes are available in the <a href='#legal-archive'>Archive Module</a> above.",
        "help": "AVAILABLE COMMANDS: who, about, resume, contact, papers, notes, clear, exit."
    };

    // --- BOOT SEQUENCE ---
    const sequence = [
        { text: "> INITIALIZING LEGAL_OS v3.1...", delay: 300, class: "system-msg" },
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
            
            // 3. Auto Scroll
            setTimeout(() => window.scrollTo(0, document.body.scrollHeight), 10);
        }
    });

    function addHistory(text, type) {
        const line = document.createElement('div');
        line.className = 'terminal-line ' + type;
        line.innerHTML = text;
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
            else if (cmd.includes('job') || cmd.includes('work') || cmd.includes('google')) response = db['who'];
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
