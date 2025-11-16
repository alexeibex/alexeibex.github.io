
document.addEventListener('DOMContentLoaded', function() {
    const terminalContent = document.getElementById('terminal-content');
    const sourceData = document.getElementById('source-data');
    
    // The sequence of "commands" to execute
    const sequence = [
        { text: "> INITIALIZING LEGAL_OS v3.0...", delay: 500, class: "system-msg" },
        { text: "> VERIFYING IDENTITY_TOKENS...", delay: 800, class: "system-msg" },
        { text: "> ACCESS GRANTED: ALEXEI FURS [JD_GRADUATE]", delay: 1200, class: "success-msg" },
        { text: "> EXECUTE identity.py --verbose", delay: 1500, class: "command" },
        { text: "  ... Loading Professional Profile", delay: 1800, class: "output" },
        { text: "  ... Linking Google DeepMind Credentials", delay: 2000, class: "output" },
        { text: "  ... Mounting NYS Bar Admission", delay: 2200, class: "output" },
        { text: "> DONE.", delay: 2500, class: "success-msg" }
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
        }, 30); // Speed of typing (lower is faster)
    }

    function runSequence() {
        if (currentIndex < sequence.length) {
            const step = sequence[currentIndex];
            setTimeout(() => {
                typeLine(step, runSequence);
                currentIndex++;
            }, 300);
        } else {
            // Sequence complete, reveal the main GUI
            document.getElementById('main-gui').classList.add('visible');
            document.querySelector('.cursor-line').style.display = 'block';
        }
    }

    // Start the boot sequence
    runSequence();
});
