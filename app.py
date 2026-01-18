"""
Flask Application for Skin Disease Expert System
Handles routes and API endpoints for multi-page navigation
"""

from flask import Flask, render_template, request, jsonify, session
from backend.inference_engine import InferenceEngine
from backend.knowledge_base import (
    QUESTIONS, INPUT_VARIABLES, OUTPUT_VARIABLES, 
    DISEASE_RULES, TREATMENT_RULES, LIFESTYLE_RULES, DIET_RULES
)
import secrets

app = Flask(__name__, 
            template_folder='frontend/templates',
            static_folder='frontend/static')
app.secret_key = secrets.token_hex(16)

# Initialize inference engine
engine = InferenceEngine()


@app.route('/')
def index():
    """Main landing page with Start Diagnosis button"""
    return render_template('index.html')


@app.route('/diagnosis')
def diagnosis():
    """Diagnosis page for input selection"""
    return render_template('diagnosis.html')


@app.route('/documentation')
def documentation():
    """Documentation page with system information"""
    return render_template('documentation.html')


@app.route('/report')
def report():
    """Diagnosis report page"""
    return render_template('report.html')


@app.route('/api/questions', methods=['GET'])
def get_questions():
    """Get all questions for diagnosis form"""
    return jsonify({
        'success': True,
        'questions': QUESTIONS
    })


@app.route('/api/diagnose', methods=['POST'])
def diagnose():
    """Run inference engine with all answers and return complete diagnosis"""
    data = request.json
    answers = data.get('answers', {})
    
    if not answers:
        return jsonify({
            'success': False,
            'message': 'No answers provided. Please complete all fields.'
        })
    
    # Store answers in session for report page
    session['answers'] = answers
    
    # Run inference
    result = engine.diagnose(answers)
    
    # Store result in session
    session['diagnosis_result'] = result
    
    return jsonify(result)


@app.route('/api/get-result', methods=['GET'])
def get_result():
    """Get stored diagnosis result for report page"""
    result = session.get('diagnosis_result')
    answers = session.get('answers', {})
    
    if not result:
        return jsonify({
            'success': False,
            'message': 'No diagnosis result found. Please complete the diagnosis first.'
        })
    
    return jsonify({
        **result,
        'user_answers': answers
    })


@app.route('/api/documentation', methods=['GET'])
def get_documentation():
    """Get system documentation data"""
    # Format rules for display
    all_rules = []
    
    # Layer 1: Disease Rules
    for rule in DISEASE_RULES:
        all_rules.append({
            'layer': 1,
            'layer_name': 'Disease Identification',
            'id': rule['id'],
            'name': rule['name'],
            'logic': rule['logic'],
            'conclusion': rule['conclusion']
        })
    
    # Layer 2: Treatment Rules
    for rule in TREATMENT_RULES:
        all_rules.append({
            'layer': 2,
            'layer_name': 'Suggested Treatment',
            'id': rule['id'],
            'name': rule['name'],
            'logic': rule['logic'],
            'conclusion': rule['conclusion']
        })
    
    # Layer 3: Lifestyle Rules
    for rule in LIFESTYLE_RULES:
        conclusion = rule['conclusion']
        if isinstance(conclusion, list):
            conclusion = ' OR '.join(conclusion)
        all_rules.append({
            'layer': 3,
            'layer_name': 'Suggested Lifestyle',
            'id': rule['id'],
            'name': rule['name'],
            'logic': rule['logic'],
            'conclusion': conclusion
        })
    
    # Layer 4: Diet Rules
    for rule in DIET_RULES:
        conclusion = rule['conclusion']
        if isinstance(conclusion, list):
            conclusion = ' OR '.join(conclusion)
        all_rules.append({
            'layer': 4,
            'layer_name': 'Diet Recommendation',
            'id': rule['id'],
            'name': rule['name'],
            'logic': rule['logic'],
            'conclusion': conclusion
        })
    
    return jsonify({
        'success': True,
        'input_variables': INPUT_VARIABLES,
        'output_variables': OUTPUT_VARIABLES,
        'rules': all_rules
    })


@app.route('/api/reset', methods=['POST'])
def reset():
    """Reset session and clear diagnosis"""
    session.clear()
    return jsonify({
        'success': True,
        'message': 'Session reset successfully'
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)