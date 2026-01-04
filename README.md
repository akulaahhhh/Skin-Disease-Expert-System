# 🩺 Skin Disease Expert System

A rule-based expert system for diagnosing common skin conditions using forward chaining inference with priority-based pattern selection.

## 📋 Features

- **Visual Question Interface**: Modern, one-question-per-screen design
- **Rule-Based Inference**: 18 carefully crafted rules with priority system
- **Pattern Detection**: Identifies 5 distinct skin condition patterns
- **Diagnosis**: Provides 5 possible diagnoses (Eczema, Fungal Tinea, Acne Vulgaris, Contact Dermatitis, Skin Ulcer)
- **Treatment Recommendations**: Suggests appropriate self-care and treatments
- **Explanation Facility**: Shows which rules were fired during diagnosis
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## 🎨 Design

The interface uses a clean purple theme with the following color scheme:
- Primary: `#7C72E5`
- Light Purple: `#D9D4F7`
- Very Light Purple: `#E8E5FA`
- Dark Text: `#0C092A`

## 🏗️ Project Structure

```
skin_disease_expert_system/
│
├── backend/
│   ├── __init__.py                # Module initialization
│   ├── knowledge_base.py          # All 18 rules and question definitions
│   ├── inference_engine.py        # Forward chaining logic with priority
│   └── utils.py                   # Helper functions (if needed)
│
├── frontend/
│   ├── templates/
│   │   └── index.html             # Main single-page application
│   └── static/
│       ├── css/
│       │   └── style.css          # Purple theme styling
│       └── js/
│           └── app.js             # Frontend logic and API calls
│
├── app.py                          # Flask application (main entry point)
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone/Download the Project

Download this project folder to your computer.

### Step 2: Create Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Step 5: Open in Browser

Open your web browser and navigate to:
```
http://localhost:5000
```

## 🎯 How to Use

1. **Start**: Click the "START DIAGNOSIS" button on the landing page
2. **Answer Questions**: Go through 9 questions about your skin condition
   - Click options for single-choice questions
   - Check multiple boxes for multi-select questions
   - Use "NEXT" to proceed, "BACK" to go back
3. **View Results**: See your diagnosis, pattern, and treatment recommendations
4. **View Explanation**: Click "View Explanation" to see which rules were fired
5. **Start Over**: Click "START NEW DIAGNOSIS" to diagnose another condition

## 🧠 Knowledge Base

### Input Questions (9 total)

1. Age group (Child, Adult, Elderly)
2. Duration of lesion (Hours, Days, Weeks, Months)
3. Itching level (None, Mild, Severe)
4. Pain level (None, Mild, Severe)
5. Burning sensation (Yes, No)
6. Lesion location (Face, Body, Hands, Legs) - Multiple select
7. Lesion appearance (10 options) - Multiple select
8. Lesion size (Small, Medium, Large)
9. Border type (Regular, Irregular, Raised)

### Output

- **Skin Condition Pattern**: One of 5 patterns
  - Inflammatory Pattern
  - Fungal Infection Pattern
  - Bacterial/Pustular Pattern
  - Allergic Reaction Pattern
  - Non-Healing Wound Pattern

- **Possible Diagnosis**: One of 5 diagnoses
  - Eczema
  - Fungal Tinea (Ringworm)
  - Acne Vulgaris
  - Contact Dermatitis
  - Skin Ulcer

- **Treatment Recommendations**: Specific to diagnosis

### Rules Summary

**Pattern Rules (1-6):** Identify skin condition patterns
**Diagnosis Rules (7-11):** Map patterns to specific diagnoses
**Treatment Rules (12-18):** Provide treatment recommendations

### Priority System

When multiple patterns match, the system uses this priority order:
1. Allergic Reaction Pattern (Highest - most urgent)
2. Bacterial/Pustular Pattern
3. Non-Healing Wound Pattern
4. Fungal Infection Pattern
5. Inflammatory Pattern (Lowest - most general)

## 🧪 Testing the System

### Test Case 1: Eczema
- Age: Adult
- Duration: Weeks
- Itching: Severe
- Pain: None
- Burning: No
- Location: Hands, Body
- Appearance: Scaly/Flaky
- Size: Medium
- Border: Regular

**Expected Result:** Inflammatory Pattern → Eczema

### Test Case 2: Ringworm
- Age: Adult
- Duration: Weeks
- Itching: Mild
- Pain: None
- Burning: No
- Location: Body
- Appearance: Circular, Well-Demarcated, Scaly/Flaky
- Size: Medium
- Border: Regular

**Expected Result:** Fungal Infection Pattern → Fungal Tinea (Ringworm)

### Test Case 3: Acne
- Age: Adult
- Duration: Days
- Itching: None
- Pain: Mild
- Burning: No
- Location: Face
- Appearance: Papules/Pustules
- Size: Small
- Border: Regular

**Expected Result:** Bacterial/Pustular Pattern → Acne Vulgaris

### Test Case 4: Contact Dermatitis
- Age: Adult
- Duration: Days
- Itching: Severe
- Pain: Mild
- Burning: Yes
- Location: Hands
- Appearance: Swollen, Crusting/Oozing
- Size: Medium
- Border: Irregular

**Expected Result:** Allergic Reaction Pattern → Contact Dermatitis

### Test Case 5: Skin Ulcer
- Age: Elderly
- Duration: Months
- Itching: None
- Pain: Severe
- Burning: No
- Location: Legs
- Appearance: Ulcer
- Size: Large
- Border: Irregular

**Expected Result:** Non-Healing Wound Pattern → Skin Ulcer

## 🔧 Troubleshooting

### Problem: Port 5000 already in use
**Solution:** Change the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Use port 5001 instead
```

### Problem: Module not found errors
**Solution:** Make sure you're in the correct directory and virtual environment is activated:
```bash
cd skin_disease_expert_system
pip install -r requirements.txt
```

### Problem: Browser shows "This site can't be reached"
**Solution:** 
- Check if Flask is running (you should see output in terminal)
- Try `http://127.0.0.1:5000` instead of `localhost:5000`
- Check if firewall is blocking the connection

### Problem: CSS/JS not loading
**Solution:** 
- Hard refresh browser (Ctrl+F5 or Cmd+Shift+R)
- Check browser console for errors (F12)
- Verify folder structure is correct

## 📚 Technical Details

### Backend Architecture

**Inference Engine (`inference_engine.py`):**
- Forward chaining algorithm
- Priority-based pattern selection
- Explanation generation
- Handles single and multiple selection inputs

**Knowledge Base (`knowledge_base.py`):**
- 18 rules stored as Python dictionaries
- Pattern priority definitions
- Question definitions with metadata

### Frontend Architecture

**Single Page Application:**
- Dynamic question rendering
- State management in JavaScript
- RESTful API communication with backend
- Smooth animations and transitions

### API Endpoints

- `GET /` - Landing page
- `POST /start` - Initialize diagnosis session
- `GET /get-question` - Get current question
- `POST /submit-answer` - Submit answer and proceed
- `POST /diagnose` - Run inference and get results
- `POST /reset` - Reset session

## ⚠️ Disclaimer

This is an **educational expert system** developed for academic purposes. It should **NOT** be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified dermatologist or healthcare provider for skin conditions.

## 👨‍💻 Development

### Adding New Rules

1. Add rule to appropriate section in `knowledge_base.py`
2. Follow existing rule structure
3. Test thoroughly with various inputs

### Adding New Questions

1. Add question to `QUESTIONS` list in `knowledge_base.py`
2. Specify type ('single' or 'multiple')
3. Update rules to use new question data

### Modifying UI

- **Colors:** Edit CSS variables in `style.css`
- **Layout:** Modify HTML structure in `index.html`
- **Logic:** Update JavaScript in `app.js`

## 📄 License

This project is created for educational purposes as part of a Knowledge Base Systems course.

## 🙋 Support

For issues or questions:
1. Check this README thoroughly
2. Review code comments in files
3. Test with provided test cases
4. Check browser console for JavaScript errors
5. Check terminal for Python errors

---

**Created with ❤️ for Knowledge Base Systems course**