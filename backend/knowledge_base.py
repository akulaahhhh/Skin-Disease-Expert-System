"""
Knowledge Base for Skin Disease Expert System
Contains all rules, patterns, and priorities
"""

# Pattern Priority (higher number = higher priority)
PATTERN_PRIORITY = {
    'Allergic Reaction Pattern': 5,
    'Bacterial/Pustular Pattern': 4,
    'Non-Healing Wound Pattern': 3,
    'Fungal Infection Pattern': 2,
    'Inflammatory Pattern': 1
}

# ============================================
# PATTERN RULES (Rules 1-6)
# ============================================

PATTERN_RULES = [
    {
        'id': 'rule_1',
        'name': 'Rule 1: Inflammatory Pattern',
        'conditions': {
            'duration': ['Yes'],
            'symptoms': ['Mild Itching', 'Severe Itching', 'Burning Sensation'],
            'lesion_appearance': ['Scaly / Flaky', 'Well-Demarcated'],
            'lesion_size': ['Yes']
        },
        'conclusion': 'Inflammatory Pattern'
    },
    {
        'id': 'rule_2',
        'name': 'Rule 2: Fungal Infection Pattern',
        'conditions': {
            'symptoms': ['Mild Itching', 'Severe Itching'],
            'lesion_appearance': ['Circular', 'Annular', 'Scaly / Flaky', 'Well-Demarcated'],
            'border': ['Raised'],
            'lesion_size': ['Yes']
        },
        'conclusion': 'Fungal Infection Pattern'
    },
    {
        'id': 'rule_3',
        'name': 'Rule 3: Bacterial / Pustular Pattern',
        'conditions': {
            'symptoms': ['Pain Sensation'],
            'lesion_appearance': ['Papules / Pustules', 'Swollen'],
            'lesion_size': ['Yes']
        },
        'conclusion': 'Bacterial/Pustular Pattern'
    },
    {
        'id': 'rule_4',
        'name': 'Rule 4: Allergic Reaction Pattern',
        'conditions': {
            'duration': ['Yes'],
            'symptoms': ['Severe Itching'],
            'lesion_appearance': ['Swollen', 'Well-Demarcated'],
            'lesion_size': ['No']
        },
        'conclusion': 'Allergic Reaction Pattern'
    },
    {
        'id': 'rule_5',
        'name': 'Rule 5: Non-Healing Wound Pattern',
        'conditions': {
            'duration': ['Yes'],
            'symptoms': ['Pain Sensation'],
            'lesion_appearance': ['Ulcer', 'Crusting / Oozing'],
            'age_group': ['Elderly']
        },
        'conclusion': 'Non-Healing Wound Pattern'
    }
]


# ============================================
# DIAGNOSIS RULES (Rules 7-11)
# ============================================

DIAGNOSIS_RULES = [
    {
        'id': 'rule_6',
        'name': 'Rule 6: Eczema Diagnosis',
        'conditions': {
            'pattern': ['Inflammatory Pattern'],
            'symptoms': ['Severe Itching'],
            'lesion_appearance': ['Hyperpigmented / Depigmented (White)'],
            'border': ['Regular']
        },
        'conclusion': 'Eczema'
    },
    {
        'id': 'rule_7',
        'name': 'Rule 7: Fungal Tinea (Ringworm) Diagnosis',
        'conditions': {
            'pattern': ['Fungal Infection Pattern'],
            'lesion_appearance': ['Circular', 'Annular']
        },
        'conclusion': 'Fungal Tinea (Ringworm)'
    },
    {
        'id': 'rule_8',
        'name': 'Rule 8: Acne Vulgaris Diagnosis',
        'conditions': {
            'pattern': ['Bacterial/Pustular Pattern'],
            'age_group': ['Child', 'Adult']
        },
        'conclusion': 'Acne Vulgaris'
    },
    {
        'id': 'rule_9',
        'name': 'Rule 9: Contact Dermatitis Diagnosis',
        'conditions': {
            'pattern': ['Allergic Reaction Pattern']
        },
        'conclusion': 'Contact Dermatitis'
    },
    {
        'id': 'rule_10',
        'name': 'Rule 10: Skin Ulcer Diagnosis',
        'conditions': {
            'pattern': ['Non-Healing Wound Pattern']
        },
        'conclusion': 'Skin Ulcer'
    }
]


# ============================================
# TREATMENT RULES (Rules 12-18)
# ============================================

TREATMENT_RULES = [
    {
        'id': 'rule_11',
        'name': 'Rule 11: Eczema Treatment',
        'conditions': {
            'diagnosis': ['Eczema']
        },
        'conclusion': [
            'Moisturizers / emollients',
            'Topical corticosteroids',
            'Avoid irritants and harsh products'
        ]
    },
    {
        'id': 'rule_12',
        'name': 'Rule 12: Fungal Tinea Treatment',
        'conditions': {
            'diagnosis': ['Fungal Tinea (Ringworm)']
        },
        'conclusion': [
            'Topical antifungal creams',
            'Avoid irritants and harsh products'
        ]
    },
    {
        'id': 'rule_13',
        'name': 'Rule 13: Acne Vulgaris Treatment',
        'conditions': {
            'diagnosis': ['Acne Vulgaris']
        },
        'conclusion': [
            'Proper wound care & hygiene',
            'Avoid irritants and harsh products'
        ]
    },
    {
        'id': 'rule_14',
        'name': 'Rule 14: Contact Dermatitis Treatment',
        'conditions': {
            'diagnosis': ['Contact Dermatitis']
        },
        'conclusion': [
            'Oral antihistamines',
            'Topical corticosteroids',
            'Avoid irritants and harsh products'
        ]
    },
    {
        'id': 'rule_15',
        'name': 'Rule 15: Skin Ulcer Treatment',
        'conditions': {
            'diagnosis': ['Skin Ulcer']
        },
        'conclusion': [
            'Proper wound care & hygiene'
        ]
    }
]


# ============================================
# QUESTION DEFINITIONS
# ============================================

QUESTIONS = [
    {
        'id': 'age_group',
        'question': 'What is your age group?',
        'type': 'single',
        'options': ['Child', 'Adult', 'Elderly']
    },
    {
        'id': 'duration',
        'question': 'Do you experience this skin condition for more than a week?',
        'type': 'single',
        'options': ['Yes', 'No']
    },
    {
        'id': 'symptoms',
        'question': 'Do you experience any of these symptomss?',
        'type': 'multiple',
        'options': ['Mild Itching', 'Severe Itching', 'Pain Sensation', 'Burning Sensation']
    },
    {
        'id': 'lesion_appearance',
        'question': 'How does the skin condition appear? (Select all that apply)',
        'type': 'multiple',
        'options': [
            'Circular',
            'Annular',
            'Scaly / Flaky',
            'Well-Demarcated',
            'Swollen',
            'Papules / Pustules',
            'Crusting / Oozing',
            'Hyperpigmented / Depigmented (White)',
            'Ulcer',
        ]
    },
    {
        'id': 'lesion_size',
        'question': 'Is the size of the lesion larger than 5 mm?',
        'type': 'single',
        'options': ['Yes', 'No']
    },
    {
        'id': 'border',
        'question': 'How would you describe the border of the lesion?',
        'type': 'single',
        'options': ['Regular', 'Irregular', 'Raised']
    }
]