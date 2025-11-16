
document.addEventListener('DOMContentLoaded', function() {
    const terminalContent = document.getElementById('terminal-content');
    const mainGui = document.getElementById('main-gui');
    const inputLine = document.getElementById('input-line');
    const cmdInput = document.getElementById('cmd-input');
    const history = document.getElementById('history');

    // --- CONFIGURATION ---
    // REPLACE THIS WITH YOUR ACTUAL API KEY FROM GOOGLE AI STUDIO
    const API_KEY = "AIzaSyAkWiLWRhGEFPJy7U4nh1PVYw69FUMbRh8"; 
    
    const SYSTEM_PROMPT = `You are Legal_OS v6.1, a cyberpunk portfolio assistant for Alexei Furs. 
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
    4. If asked for legal advice, state that you are a portfolio bot and cannot provide legal counsel.
    5. Do NOT make up facts about Alexei. Refuse if unsure.`;

    // --- 1. LOCAL KNOWLEDGE BASE (FAST PATH) ---
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

    // --- 2. INTENT MAPPING (FAST PATH) ---
    const intentMap = {
        "experience": ["work", "job", "history", "career", "google", "deepmind", "twitter", "optimatic", "experience", "resume", "background"],
        "education": ["school", "college", "university", "degree", "law", "brooklyn", "georgetown", "education", "study", "academic"],
        "skills": ["skill", "tech", "python", "sql", "coding", "program", "language", "tool", "stack", "technology"],
        "contact": ["email", "phone", "linkedin", "reach", "contact", "message", "connect", "hire"],
        "bar": ["bar", "lawyer", "attorney", "admitted", "court", "license", "esq"],
        "projects": ["project", "paper", "research", "mit", "blip", "writing", "publication"]
    };

    // --- 3. BOOT SEQUENCE ---
    const bootSequence = [
        { text: "> INITIALIZING LEGAL_OS v6.1 (GEMINI INTEGRATED)...", delay: 200, class: "system-msg" },
        { text: "> ESTABLISHING NEURAL UPLINK...", delay: 400, class: "system-msg" },
        { text: "> ACCESS GRANTED: ALEXEI FURS [JD_GRADUATE]", delay: 1000, class: "success-msg" },
        { text: "> SYSTEM READY. WAITING FOR INPUT.", delay: 1200, class: "success-msg" }
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
            mainGui.classList.add('visible');
            inputLine.style.display = 'flex';
            cmdInput.focus();
        }
    }

    // --- AI LOGIC: GEMINI API CALL ---
    async function callGemini(prompt) {
        if (API_KEY === "PUT_YOUR_GEMINI_API_KEY_HERE") {
            return "> ERROR: API KEY NOT CONFIGURED. PLEASE UPDATE terminal.js.";
        }

        // UPDATED URL: Uses 'gemini-1.5-flash-latest' to fix 404 error
        const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=${API_KEY}`;
        
        try {
            const response = await fetch(url, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    contents: [{
                        parts: [{ text: SYSTEM_PROMPT + "\n\nUSER QUERY: " + prompt }]
                    }]
                })
            });

            const data = await response.json();
            
            if (data.error) {
                return `> API ERROR: ${data.error.message}`;
            }

            // Extract text
            const text = data.candidates[0].content.parts[0].text;
            // Simple formatting: replace newlines with breaks for HTML
            return text.replace(/\n/g, "<br>");

        } catch (error) {
            return "> CONNECTION FAILURE: UNABLE TO REACH NEURAL NET.";
        }
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
                setTimeout(() => {
                    line.remove(); 
                    callback();
                }, 200);
            }
        }, 50);
    }

    // --- INPUT HANDLER ---
    cmdInput.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            const rawInput = cmdInput.value.trim();
            if (!rawInput) return;

            // Echo Input
            const echo = document.createElement('div');
            echo.className = 'terminal-line command-echo';
            echo.innerText = `user@legal-os:~$ ${rawInput}`;
            history.appendChild(echo);
            
            cmdInput.value = '';
            cmdInput.disabled = true;

            // Check Local Intents First (Fast Path)
            let localResponse = null;
            const lowerInput = rawInput.toLowerCase();
            
            // Check hardcoded commands
            if (lowerInput === 'clear' || lowerInput === 'cls') {
                history.innerHTML = '';
                cmdInput.disabled = false;
                cmdInput.focus();
                return;
            }
            if (lowerInput === 'help') {
                localResponse = "AVAILABLE COMMANDS: experience, education, skills, bar, projects, contact, resume.<br>OR ASK ANYTHING: 'Who is the president?', 'Draft an NDA'.";
            } else {
                // Check Intent Map
                for (const [intent, keywords] of Object.entries(intentMap)) {
                    if (keywords.some(k => lowerInput.includes(k)) && knowledge[intent]) {
                        localResponse = knowledge[intent];
                        break;
                    }
                }
            }

            if (localResponse) {
                // Instant Response for Local Knowledge
                const respDiv = document.createElement('div');
                respDiv.className = 'terminal-line response-msg';
                respDiv.innerHTML = localResponse;
                history.appendChild(respDiv);
                cmdInput.disabled = false;
                cmdInput.focus();
            } else {
                // API Call for Everything Else
                simulateThinking(async () => {
                    const aiResponse = await callGemini(rawInput);
                    
                    const respDiv = document.createElement('div');
                    respDiv.className = 'terminal-line response-msg';
                    // Add a subtle style to show it came from AI
                    respDiv.style.borderLeftColor = "#00f3ff"; 
                    respDiv.innerHTML = aiResponse;
                    history.appendChild(respDiv);
                    
                    cmdInput.disabled = false;
                    cmdInput.focus();
                });
            }
        }
    });

    // Init
    runBoot();
    
    document.addEventListener('click', () => {
        if(inputLine.style.display !== 'none' && !cmdInput.disabled) cmdInput.focus();
    });
});
