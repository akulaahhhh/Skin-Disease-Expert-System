/**
 * Skin Disease Expert System - Frontend Logic
 * Handles navigation, question display, and API communication
 */

// Global state
let currentQuestion = null;
let selectedAnswer = null;
let questionHistory = [];

// DOM Elements
const landingScreen = document.getElementById('landing-screen');
const questionScreen = document.getElementById('question-screen');
const resultsScreen = document.getElementById('results-screen');
const loadingOverlay = document.getElementById('loading-overlay');

const startBtn = document.getElementById('start-btn');
const nextBtn = document.getElementById('next-btn');
const backBtn = document.getElementById('back-btn');
const restartBtn = document.getElementById('restart-btn');

const questionText = document.getElementById('question-text');
const optionsContainer = document.getElementById('options-container');
const progressFill = document.getElementById('progress-fill');
const progressCurrent = document.getElementById('progress-current');
const progressTotal = document.getElementById('progress-total');

// Event Listeners
startBtn.addEventListener('click', startDiagnosis);
nextBtn.addEventListener('click', submitAnswer);
backBtn.addEventListener('click', goBack);
restartBtn.addEventListener('click', restart);

// Explanation toggle
document.addEventListener('click', function(e) {
    if (e.target.closest('#explanation-header')) {
        document.querySelector('.collapsible').classList.toggle('open');
    }
});

/**
 * Start new diagnosis
 */
async function startDiagnosis() {
    try {
        showLoading();
        
        const response = await fetch('/start', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        const data = await response.json();
        
        if (data.success) {
            questionHistory = [];
            await loadQuestion();
            showScreen('question');
        }
        
        hideLoading();
    } catch (error) {
        console.error('Error starting diagnosis:', error);
        alert('Failed to start diagnosis. Please try again.');
        hideLoading();
    }
}

/**
 * Load current question from backend
 */
async function loadQuestion() {
    try {
        const response = await fetch('/get-question');
        const data = await response.json();
        
        if (data.finished) {
            // All questions answered, run diagnosis
            await runDiagnosis();
            return;
        }
        
        currentQuestion = data.question;
        selectedAnswer = null;
        
        // Update progress
        progressCurrent.textContent = data.current;
        progressTotal.textContent = data.total;
        const progressPercent = (data.current / data.total) * 100;
        progressFill.style.width = progressPercent + '%';
        
        // Display question
        displayQuestion(currentQuestion);
        
        // Show/hide back button
        backBtn.style.display = data.current > 1 ? 'inline-block' : 'none';
        
    } catch (error) {
        console.error('Error loading question:', error);
        alert('Failed to load question. Please try again.');
    }
}

/**
 * Display question with appropriate input type
 */
function displayQuestion(question) {
    questionText.textContent = question.question;
    optionsContainer.innerHTML = '';
    
    if (question.type === 'single') {
        // Single choice - display as buttons
        question.options.forEach(option => {
            const btn = document.createElement('button');
            btn.className = 'option-btn';
            btn.textContent = option;
            btn.addEventListener('click', () => selectOption(btn, option));
            optionsContainer.appendChild(btn);
        });
    } else if (question.type === 'multiple') {
        // Multiple choice - display as checkboxes
        question.options.forEach((option, index) => {
            const container = document.createElement('div');
            container.className = 'checkbox-container';
            
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.id = `option-${index}`;
            checkbox.value = option;
            checkbox.addEventListener('change', updateMultipleSelection);
            
            const label = document.createElement('label');
            label.htmlFor = `option-${index}`;
            label.textContent = option;
            
            container.appendChild(checkbox);
            container.appendChild(label);
            container.addEventListener('click', (e) => {
                if (e.target !== checkbox) {
                    checkbox.checked = !checkbox.checked;
                    updateMultipleSelection();
                }
            });
            
            optionsContainer.appendChild(container);
        });
        
        selectedAnswer = []; // Initialize as empty array for multiple choice
    }
}

/**
 * Handle single option selection
 */
function selectOption(btn, option) {
    // Remove previous selection
    document.querySelectorAll('.option-btn').forEach(b => {
        b.classList.remove('selected');
    });
    
    // Mark as selected
    btn.classList.add('selected');
    selectedAnswer = option;
}

/**
 * Handle multiple option selection
 */
function updateMultipleSelection() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    selectedAnswer = [];
    
    checkboxes.forEach(checkbox => {
        const container = checkbox.closest('.checkbox-container');
        if (checkbox.checked) {
            selectedAnswer.push(checkbox.value);
            container.classList.add('selected');
        } else {
            container.classList.remove('selected');
        }
    });
}

/**
 * Submit current answer and move to next question
 */
async function submitAnswer() {
    // Validate answer
    if (!selectedAnswer || (Array.isArray(selectedAnswer) && selectedAnswer.length === 0)) {
        alert('Please select an answer before continuing.');
        return;
    }
    
    try {
        showLoading();
        
        // Save to history for back navigation
        questionHistory.push({
            question: currentQuestion,
            answer: selectedAnswer
        });
        
        const response = await fetch('/submit-answer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                question_id: currentQuestion.id,
                answer: selectedAnswer
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            if (data.finished) {
                // Run diagnosis
                await runDiagnosis();
            } else {
                // Load next question
                await loadQuestion();
            }
        }
        
        hideLoading();
    } catch (error) {
        console.error('Error submitting answer:', error);
        alert('Failed to submit answer. Please try again.');
        hideLoading();
    }
}

/**
 * Go back to previous question
 */
function goBack() {
    if (questionHistory.length > 0) {
        // Remove last question from history
        questionHistory.pop();
        
        // Navigate back in session
        fetch('/get-question', {
            method: 'GET'
        }).then(() => {
            // Reload previous question
            window.location.reload();
        });
    }
}

/**
 * Run diagnosis and show results
 */
async function runDiagnosis() {
    try {
        showLoading();
        
        const response = await fetch('/diagnose', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        const result = await response.json();
        
        displayResults(result);
        showScreen('results');
        hideLoading();
        
    } catch (error) {
        console.error('Error running diagnosis:', error);
        alert('Failed to complete diagnosis. Please try again.');
        hideLoading();
    }
}

/**
 * Display diagnosis results
 */
function displayResults(result) {
    const resultIcon = document.getElementById('result-icon');
    const resultTitle = document.getElementById('result-title');
    const resultMessage = document.getElementById('result-message');
    const resultPattern = document.getElementById('result-pattern');
    const resultDiagnosis = document.getElementById('result-diagnosis');
    const resultTreatment = document.getElementById('result-treatment');
    const resultExplanation = document.getElementById('result-explanation');
    const diagnosisDetails = document.getElementById('diagnosis-details');
    
    if (result.success) {
        // Success result
        resultIcon.className = 'result-icon success';
        resultTitle.textContent = 'Diagnosis Complete';
        resultMessage.textContent = 'Based on your symptoms, here is the analysis:';
        
        // Show diagnosis details
        diagnosisDetails.style.display = 'block';
        
        // Pattern
        resultPattern.textContent = result.pattern || 'N/A';
        
        // Diagnosis
        resultDiagnosis.textContent = result.diagnosis || 'N/A';
        
        // Treatment
        resultTreatment.innerHTML = '';
        if (result.treatment && result.treatment.length > 0) {
            result.treatment.forEach(treatment => {
                const li = document.createElement('li');
                li.textContent = treatment;
                resultTreatment.appendChild(li);
            });
        } else {
            const li = document.createElement('li');
            li.textContent = 'No specific treatment recommendations available.';
            resultTreatment.appendChild(li);
        }
        
        // Explanation
        resultExplanation.innerHTML = '';
        if (result.explanation && result.explanation.length > 0) {
            result.explanation.forEach(rule => {
                const li = document.createElement('li');
                li.textContent = rule;
                resultExplanation.appendChild(li);
            });
        }
        
    } else {
        // No diagnosis found
        resultIcon.className = 'result-icon warning';
        resultTitle.textContent = 'No Diagnosis Found';
        resultMessage.textContent = result.message || 'We could not determine a diagnosis based on your symptoms.';
        
        // Hide diagnosis details
        diagnosisDetails.style.display = 'none';
    }
}

/**
 * Restart diagnosis
 */
async function restart() {
    try {
        showLoading();
        
        await fetch('/reset', {
            method: 'POST'
        });
        
        hideLoading();
        showScreen('landing');
        
    } catch (error) {
        console.error('Error restarting:', error);
        hideLoading();
        window.location.reload();
    }
}

/**
 * Show specific screen
 */
function showScreen(screen) {
    landingScreen.classList.remove('active');
    questionScreen.classList.remove('active');
    resultsScreen.classList.remove('active');
    
    if (screen === 'landing') {
        landingScreen.classList.add('active');
    } else if (screen === 'question') {
        questionScreen.classList.add('active');
    } else if (screen === 'results') {
        resultsScreen.classList.add('active');
    }
}

/**
 * Show loading overlay
 */
function showLoading() {
    loadingOverlay.classList.add('active');
}

/**
 * Hide loading overlay
 */
function hideLoading() {
    loadingOverlay.classList.remove('active');
}