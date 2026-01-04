"""
Flask Application for Skin Disease Expert System
Handles routes and API endpoints
"""

from flask import Flask, render_template, request, jsonify, session
from backend.inference_engine import InferenceEngine
from backend.knowledge_base import QUESTIONS
from backend.gemini_service import generate_explanation
import secrets

#llm gemini
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__, 
            template_folder='frontend/templates',
            static_folder='frontend/static')
app.secret_key = secrets.token_hex(16)

# Initialize inference engine
engine = InferenceEngine()


@app.route('/')
def index():
    """Landing page with START button"""
    return render_template('index.html')


@app.route('/start', methods=['POST'])
def start_diagnosis():
    """Initialize new diagnosis session"""
    session.clear()
    session['current_question'] = 0
    session['answers'] = {}
    return jsonify({
        'success': True,
        'message': 'Diagnosis started'
    })


@app.route('/get-question', methods=['GET'])
def get_question():
    """Get current question"""
    current_index = session.get('current_question', 0)
    
    if current_index >= len(QUESTIONS):
        return jsonify({
            'finished': True,
            'message': 'All questions answered'
        })
    
    question = QUESTIONS[current_index]
    
    return jsonify({
        'finished': False,
        'question': question,
        'current': current_index + 1,
        'total': len(QUESTIONS)
    })


@app.route('/submit-answer', methods=['POST'])
def submit_answer():
    """Submit answer and move to next question"""
    data = request.json
    question_id = data.get('question_id')
    answer = data.get('answer')
    
    # Store answer in session
    answers = session.get('answers', {})
    answers[question_id] = answer
    session['answers'] = answers
    
    # Move to next question
    current_index = session.get('current_question', 0)
    session['current_question'] = current_index + 1
    
    # Check if finished
    if session['current_question'] >= len(QUESTIONS):
        return jsonify({
            'success': True,
            'finished': True,
            'message': 'All questions completed'
        })
    
    return jsonify({
        'success': True,
        'finished': False,
        'message': 'Answer recorded'
    })


@app.route('/diagnose', methods=['POST'])
def diagnose():
    """Run inference engine and return diagnosis"""
    answers = session.get('answers', {})
    
    if not answers:
        return jsonify({
            'success': False,
            'message': 'No answers found. Please start again.'
        })
    
    # Run inference
    result = engine.diagnose(answers)
    explanation = generate_explanation(
        pattern=result['pattern'],
        diagnosis=result['diagnosis'],
        facts=result['facts'],
        triggered_rules=result['explanation']
    )
    result['llm_explanation'] = explanation
    
    return jsonify(result)


@app.route('/reset', methods=['POST'])
def reset():
    """Reset session and start over"""
    session.clear()
    return jsonify({
        'success': True,
        'message': 'Session reset'
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)