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
            'itching': ['Mild', 'Severe'],
            'lesion_appearance': ['Scaly / Flaky'],
            'duration': ['Weeks', 'Months']
        },
        'conclusion': 'Inflammatory Pattern'
    },
    {
        'id': 'rule_2',
        'name': 'Rule 2: Fungal Infection Pattern',
        'conditions': {
            'lesion_appearance': ['Circular', 'Annular', 'Well-Demarcated'],
            'itching': ['Mild', 'Severe']  # itching is present
        },
        'conclusion': 'Fungal Infection Pattern'
    },
    {
        'id': 'rule_3',
        'name': 'Rule 3: Bacterial/Pustular Pattern',
        'conditions': {
            'lesion_appearance': ['Papules / Pustules'],
            'pain': ['Mild', 'Severe'],
            'lesion_location': ['Face', 'Body']
        },
        'conclusion': 'Bacterial/Pustular Pattern'
    },
    {
        'id': 'rule_4',
        'name': 'Rule 4: Allergic Reaction Pattern',
        'conditions': {
            'burning': ['Yes'],
            'itching': ['Severe'],
            'lesion_appearance': ['Swollen', 'Crusting / Oozing']
        },
        'conclusion': 'Allergic Reaction Pattern'
    },
    {
        'id': 'rule_5',
        'name': 'Rule 5: Non-Healing Wound Pattern',
        'conditions': {
            'lesion_appearance': ['Ulcer'],
            'duration': ['Weeks', 'Months'],
            'lesion_size': ['Medium 5mm ~ 20mm', 'Large > 20mm']
        },
        'conclusion': 'Non-Healing Wound Pattern'
    },
    {
        'id': 'rule_6',
        'name': 'Rule 6: Inflammatory Pattern (Alternative)',
        'conditions': {
            'lesion_appearance': ['Scaly / Flaky'],
            'itching': ['Mild', 'Severe'],  # itching is present
            'lesion_location': ['Hands', 'Body']
        },
        'conclusion': 'Inflammatory Pattern'
    }
]

# ============================================
# DIAGNOSIS RULES (Rules 7-11)
# ============================================

DIAGNOSIS_RULES = [
    {
        'id': 'rule_7',
        'name': 'Rule 7: Eczema Diagnosis',
        'conditions': {
            'pattern': ['Inflammatory Pattern'],
            'itching': ['Severe'],
            'lesion_location': ['Hands', 'Body']
        },
        'conclusion': 'Eczema'
    },
    {
        'id': 'rule_8',
        'name': 'Rule 8: Fungal Tinea (Ringworm) Diagnosis',
        'conditions': {
            'pattern': ['Fungal Infection Pattern'],
            'lesion_appearance': ['Scaly / Flaky']
        },
        'conclusion': 'Fungal Tinea (Ringworm)'
    },
    {
        'id': 'rule_9',
        'name': 'Rule 9: Acne Vulgaris Diagnosis',
        'conditions': {
            'pattern': ['Bacterial/Pustular Pattern'],
            'lesion_location': ['Face'],
            'age_group': ['Child', 'Adult']
        },
        'conclusion': 'Acne Vulgaris'
    },
    {
        'id': 'rule_10',
        'name': 'Rule 10: Contact Dermatitis Diagnosis',
        'conditions': {
            'pattern': ['Allergic Reaction Pattern'],
            'lesion_location': ['Hands', 'Face']
        },
        'conclusion': 'Contact Dermatitis'
    },
    {
        'id': 'rule_11',
        'name': 'Rule 11: Skin Ulcer Diagnosis',
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
        'id': 'rule_12',
        'name': 'Rule 12: Eczema Treatment (General)',
        'conditions': {
            'diagnosis': ['Eczema'],
            'lesion_location_not': ['Face']  # NOT face
        },
        'conclusion': [
            'Moisturizers / emollients',
            'Oral antihistamines',
            'Topical corticosteroids'
        ]
    },
    {
        'id': 'rule_17',
        'name': 'Rule 17: Eczema Treatment (Face) - PRIORITY',
        'conditions': {
            'diagnosis': ['Eczema'],
            'lesion_location': ['Face']
        },
        'conclusion': [
            'Moisturizers / emollients ONLY'
        ],
        'priority': True  # Higher priority than Rule 12
    },
    {
        'id': 'rule_13',
        'name': 'Rule 13: Fungal Tinea Treatment (General)',
        'conditions': {
            'diagnosis': ['Fungal Tinea (Ringworm)'],
            'lesion_location_not': ['Hands', 'Legs']
        },
        'conclusion': [
            'Topical antifungal creams',
            'Keep affected area clean and dry'
        ]
    },
    {
        'id': 'rule_18',
        'name': 'Rule 18: Fungal Tinea Treatment (Hands/Legs) - PRIORITY',
        'conditions': {
            'diagnosis': ['Fungal Tinea (Ringworm)'],
            'lesion_location': ['Hands', 'Legs']
        },
        'conclusion': [
            'Topical antifungal creams',
            'Avoid moisture exposure'
        ],
        'priority': True
    },
    {
        'id': 'rule_14',
        'name': 'Rule 14: Acne Vulgaris Treatment',
        'conditions': {
            'diagnosis': ['Acne Vulgaris']
        },
        'conclusion': [
            'Gentle cleansing',
            'Avoid oily products'
        ]
    },
    {
        'id': 'rule_15',
        'name': 'Rule 15: Contact Dermatitis Treatment',
        'conditions': {
            'diagnosis': ['Contact Dermatitis']
        },
        'conclusion': [
            'Avoid irritants and harsh products',
            'Oral antihistamines',
            'Topical corticosteroids'
        ]
    },
    {
        'id': 'rule_16',
        'name': 'Rule 16: Skin Ulcer Treatment',
        'conditions': {
            'diagnosis': ['Skin Ulcer']
        },
        'conclusion': [
            'Proper wound care & hygiene',
            'Hygiene maintenance'
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
        'question': 'How long have you had this skin condition?',
        'type': 'single',
        'options': ['Hours', 'Days', 'Weeks', 'Months']
    },
    {
        'id': 'itching',
        'question': 'Do you experience itching?',
        'type': 'single',
        'options': ['None', 'Mild', 'Severe']
    },
    {
        'id': 'pain',
        'question': 'Do you experience pain?',
        'type': 'single',
        'options': ['None', 'Mild', 'Severe']
    },
    {
        'id': 'burning',
        'question': 'Do you experience a burning sensation?',
        'type': 'single',
        'options': ['Yes', 'No']
    },
    {
        'id': 'lesion_location',
        'question': 'Where is the skin condition located?',
        'type': 'multiple',
        'options': ['Face', 'Body', 'Hands', 'Legs']
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
            'Irregular mole'
        ]
    },
    {
        'id': 'lesion_size',
        'question': 'What is the size of the lesion?',
        'type': 'single',
        'options': ['Small < 5mm', 'Medium 5mm ~ 20mm', 'Large > 20mm']
    },
    {
        'id': 'border',
        'question': 'How would you describe the border of the lesion?',
        'type': 'single',
        'options': ['Regular', 'Irregular', 'Raised']
    }
]