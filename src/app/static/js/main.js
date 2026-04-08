// CrackNet - Frontend JavaScript

const API_BASE_URL = window.location.origin;

// DOM Elements
const passwordInput = document.getElementById('passwordInput');
const togglePassword = document.getElementById('togglePassword');
const analyzeBtn = document.getElementById('analyzeBtn');
const checkBreachBtn = document.getElementById('checkBreachBtn');
const resultsSection = document.getElementById('resultsSection');

// Result Elements
const strengthBadge = document.getElementById('strengthBadge');
const scoreValue = document.getElementById('scoreValue');
const riskBadge = document.getElementById('riskBadge');
const meterFill = document.getElementById('meterFill');
const basicTime = document.getElementById('basicTime');
const gpuTime = document.getElementById('gpuTime');
const aiTime = document.getElementById('aiTime');
const patternsContainer = document.getElementById('patternsContainer');
const scorecardContainer = document.getElementById('scorecardContainer');
const breachCard = document.getElementById('breachCard');
const breachResult = document.getElementById('breachResult');

// Toggle password visibility
togglePassword.addEventListener('click', () => {
    const type = passwordInput.type === 'password' ? 'text' : 'password';
    passwordInput.type = type;
    togglePassword.querySelector('.eye-icon').textContent = 
        type === 'password' ? '👁️' : '🙈';
});

// Analyze password
analyzeBtn.addEventListener('click', async () => {
    const password = passwordInput.value;
    
    if (!password) {
        alert('Please enter a password to analyze');
        return;
    }
    
    // Show loading state
    analyzeBtn.classList.add('loading');
    analyzeBtn.disabled = true;
    analyzeBtn.innerHTML = '<span class="btn-icon">⏳</span> Analyzing...';
    
    try {
        const response = await fetch(`${API_BASE_URL}/api/analyze`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ password })
        });
        
        const data = await response.json();
        
        if (data.success) {
            displayResults(data);
            resultsSection.style.display = 'block';
            resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        } else {
            alert('Error: ' + (data.error || 'Analysis failed'));
        }
    } catch (error) {
        console.error('Analysis error:', error);
        alert('Failed to analyze password. Please try again.');
    } finally {
        // Reset button
        analyzeBtn.classList.remove('loading');
        analyzeBtn.disabled = false;
        analyzeBtn.innerHTML = '<span class=\"btn-icon\">🔍</span> Analyze Password';
    }
});

// Check breach status
checkBreachBtn.addEventListener('click', async () => {
    const password = passwordInput.value;
    
    if (!password) {
        alert('Please enter a password to check');
        return;
    }
    
    // Show loading state
    checkBreachBtn.classList.add('loading');
    checkBreachBtn.disabled = true;
    checkBreachBtn.innerHTML = '<span class=\"btn-icon\">⏳</span> Checking...';
    
    try {
        const response = await fetch(`${API_BASE_URL}/api/check_breach`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ password })
        });
        
        const data = await response.json();
        
        if (data.success) {
            displayBreachResult(data);
            breachCard.style.display = 'block';
            breachCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
        } else {
            alert('Error: ' + (data.error || 'Breach check failed'));
        }
    } catch (error) {
        console.error('Breach check error:', error);
        alert('Failed to check breach status. Please try again.');
    } finally {
        // Reset button
        checkBreachBtn.classList.remove('loading');
        checkBreachBtn.disabled = false;
        checkBreachBtn.innerHTML = '<span class=\"btn-icon\">⚠️</span> Check Breach Status';
    }
});

// Display analysis results
function displayResults(data) {
    // Strength badge
    const strength = data.strength.toLowerCase();
    strengthBadge.textContent = data.strength;
    strengthBadge.className = `strength-badge ${strength}`;
    
    // Score
    scoreValue.textContent = `${data.strength_score}/100`;
    
    // Risk level
    const risk = data.risk_level.toLowerCase();
    riskBadge.textContent = data.risk_level;
    riskBadge.className = `risk-badge ${risk}`;
    
    // Meter fill
    meterFill.style.width = `${data.strength_score}%`;
    
    // Crack times
    basicTime.textContent = data.crack_times.basic;
    gpuTime.textContent = data.crack_times.gpu;
    aiTime.textContent = data.crack_times.ai;
    
    // Patterns
    displayPatterns(data.patterns_detected);
    
    // Scorecard
    displayScorecard(data.scorecard);
}

// Display patterns
function displayPatterns(patterns) {
    if (patterns.length === 0) {
        patternsContainer.innerHTML = '<p class=\"no-data\">✅ No concerning patterns detected!</p>';
        return;
    }
    
    const patternsList = document.createElement('ul');
    patternsList.className = 'patterns-list';
    
    patterns.forEach(pattern => {
        const li = document.createElement('li');
        li.className = 'pattern-item';
        li.textContent = pattern;
        patternsList.appendChild(li);
    });
    
    patternsContainer.innerHTML = '';
    patternsContainer.appendChild(patternsList);
}

// Display scorecard
function displayScorecard(scorecard) {
    const html = `
        <div class=\"assessment\">
            <strong>Overall Assessment:</strong> ${scorecard.overall_assessment}
        </div>
        
        <div class=\"scorecard-section\">
            <h3>💪 Strengths</h3>
            <ul class=\"scorecard-list\">
                ${scorecard.strengths.map(item => 
                    `<li class=\"scorecard-item strength\">${item}</li>`
                ).join('')}
            </ul>
        </div>
        
        <div class=\"scorecard-section\">
            <h3>⚠️ Weaknesses</h3>
            <ul class=\"scorecard-list\">
                ${scorecard.weaknesses.map(item => 
                    `<li class=\"scorecard-item weakness\">${item}</li>`
                ).join('')}
            </ul>
        </div>
        
        <div class=\"scorecard-section\">
            <h3>💡 Recommendations</h3>
            <ul class=\"scorecard-list\">
                ${scorecard.recommendations.map(item => 
                    `<li class=\"scorecard-item recommendation\">${item}</li>`
                ).join('')}
            </ul>
        </div>
    `;
    
    scorecardContainer.innerHTML = html;
}

// Display breach result
function displayBreachResult(data) {
    const isBreached = data.breached;
    const className = isBreached ? 'breached' : 'safe';
    
    let html = '';
    if (isBreached) {
        html = `
            <div class=\"breach-result ${className}\">
                <div style=\"font-size: 3rem; margin-bottom: 10px;\">🚨</div>
                <div><strong>PASSWORD COMPROMISED!</strong></div>
                <div class=\"breach-count\">${data.breach_count.toLocaleString()}</div>
                <div>This password has been seen in ${data.breach_count.toLocaleString()} data breaches.</div>
                <div style=\"margin-top: 15px; font-size: 0.95rem;\">
                    ⚠️ <strong>Do NOT use this password anywhere!</strong>
                </div>
            </div>
        `;
    } else {
        html = `
            <div class=\"breach-result ${className}\">
                <div style=\"font-size: 3rem; margin-bottom: 10px;\">✅</div>
                <div><strong>NO BREACHES FOUND</strong></div>
                <div style=\"margin-top: 15px;\">
                    This password has not been found in known data breaches.
                </div>
                <div style=\"margin-top: 10px; font-size: 0.9rem; opacity: 0.8;\">
                    However, this doesn't guarantee it's secure. Always use strong, unique passwords.
                </div>
            </div>
        `;
    }
    
    breachResult.innerHTML = html;
}

// Allow Enter key to trigger analysis
passwordInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        analyzeBtn.click();
    }
});

// Health check on page load
window.addEventListener('load', async () => {
    try {
        const response = await fetch(`${API_BASE_URL}/api/health`);
        const data = await response.json();
        console.log('CrackNet Status:', data);
    } catch (error) {
        console.error('Health check failed:', error);
    }
});
