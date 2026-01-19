# 🩺 Skin Disease Expert System

A modern, rule-based expert system for diagnosing common skin conditions using a **4-Layer Forward Chaining Inference Engine**. This project is designed to provide patient-friendly diagnoses with comprehensive medical, lifestyle, and dietary recommendations.

## 📋 Features

- **Multi-Layer Inference**: Uses a sophisticated 4-layer architecture to provide deep insights into skin conditions.
- **Modern Healthcare Design**: Premium, responsive UI with glassmorphism effects and smooth animations.
- **Comprehensive Diagnosis**: Identifies 5 major skin conditions (Eczema, Ringworm, Acne Vulgaris, Contact Dermatitis, Skin Ulcer).
- **Educational Explanations**: Provides 5 detailed, patient-friendly bullet points for every treatment, lifestyle, and diet recommendation.
- **Dynamic Report Generation**: Creates a personalized diagnosis report with printable options.
- **System Documentation**: Built-in documentation page explaining the rules and logic layers.
- **Explanation Facility**: Visualizes the decision path (fired rules) for transparency.

## 🎨 Design Aesthetics

The interface features a professional healthcare theme with:
- **Primary Palette**: Vibrant Purple (#7C72E5) and Soft Lavender.
- **Visuals**: Animated background orbs, sleek icons, and structured cards.
- **Typography**: Clean, sans-serif fonts (Inter/Outfit style) for readability.
- **Interactivity**: Micro-animations on hover and during state transitions.

## 🏗️ Project Structure

```
skin_disease_expert_system/
│
├── backend/
│   ├── __init__.py                # Module initialization
│   ├── knowledge_base.py          # 28 rules across 4 logic layers
│   ├── inference_engine.py        # 4-layer Forward Chaining logic
│
├── frontend/
│   ├── templates/
│   │   ├── index.html             # Landing page
│   │   ├── diagnosis.html         # Question interface (step-by-step)
│   │   ├── report.html            # Modernized diagnosis report
│   │   └── documentation.html     # Internal logic documentation
│   └── static/
│       └── css/
│           └── style.css          # Modern healthcare theme styling
│
├── app.py                          # Flask application (REST API & Routing)
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

## 🎯 How to Use

1. **Start**: Click the "START DIAGNOSIS" button on the landing page.
2. **Consultation**: Go through 7 comprehensive questions about your condition.
3. **Assessment**: The system processes your answers through its inference layers.
4. **View Report**: Receive a detailed breakdown of your condition, including:
   - **Disease Summary**: What the condition is and if it's contagious.
   - **Action Plan**: Detailed treatments, lifestyle adjustments, and diet tips.
   - **Explanation**: View exactly which rules were triggered.
5. **Print/Save**: Use the "Print Report" button to keep a copy of your assessment.

## 🧠 Knowledge Base & Logic

### Input Factors (7 Total)

1. **Age Group**: Child, Adult, Elderly
2. **Allergies**: Known sensitivities (None, Peanut, Seafood)
3. **Symptoms**: Itching, Burning Sensation, Pain
4. **Appearance**: 9 distinct visual markers (Scaly, Circular, Oozing, etc.)
5. **Size**: Lesion size threshold (Greater/Less than 5mm)

### The 4-Layer Rule System (28 Rules)

1. **Layer 1: Disease Identity**: Map symptoms and appearance to a specific diagnosis.
2. **Layer 2: Suggested Treatment**: Tailor medical care based on the disease and lesion size.
3. **Layer 3: Suggested Lifestyle**: Habit changes specific to the patient's age and condition.
4. **Layer 4: Diet Recommendation**: Nutritional guidance based on allergies and healing needs.

### Inference Algorithm

The system uses **Forward Chaining**:
- It starts with the user's facts (answers).
- It compares facts against **Layer 1** rules to identify a disease.
- Once a disease is identified, it becomes a new "fact".
- This new fact, along with initial data, is pushed through **Layers 2, 3, and 4** to generate comprehensive recommendations.

## ⚠️ Disclaimer

This is an **educational expert system** developed for academic purposes. It should **NOT** be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified dermatologist or healthcare provider for skin conditions.

---

**Built with ❤️ for Knowledge Base Systems course**