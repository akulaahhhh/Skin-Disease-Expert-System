"""
Knowledge Base for Skin Disease Expert System
Contains all rules, input/output variables, and question definitions
Updated with 4-layer rule system
"""

# ============================================
# INPUT VARIABLES DEFINITION
# ============================================

INPUT_VARIABLES = {
    'patient_profile': [
        {
            'id': 'age_group',
            'name': 'Age Group',
            'type': 'Selection',
            'values': ['Child', 'Adult', 'Elderly']
        },
        {
            'id': 'allergy',
            'name': 'Allergy',
            'type': 'Selection',
            'values': ['None', 'Peanut', 'Seafood']
        }
    ],
    'symptoms': [
        {
            'id': 'itching',
            'name': 'Itching',
            'type': 'Selection',
            'values': ['Yes', 'No']
        },
        {
            'id': 'burning_sensation',
            'name': 'Burning Sensation',
            'type': 'Selection',
            'values': ['Yes', 'No']
        },
        {
            'id': 'pain',
            'name': 'Pain',
            'type': 'Selection',
            'values': ['Yes', 'No']
        }
    ],
    'lesion_appearance': [
        {
            'id': 'appearance',
            'name': 'Appearance',
            'type': 'Multiple Selection',
            'values': [
                'Circular',
                'Annular',
                'Scaly / Flaky',
                'Well-Demarcated',
                'Swollen',
                'Papules / Pustules',
                'Crusting / Oozing',
                'Hyperpigmented / Depigmented',
                'Ulcer'
            ]
        },
        {
            'id': 'lesion_size',
            'name': 'Lesion Size',
            'type': 'Selection',
            'values': ['Larger than 5mm', 'Smaller than 5mm']
        }
    ]
}

# ============================================
# OUTPUT VARIABLES DEFINITION
# ============================================

OUTPUT_VARIABLES = {
    'disease': {
        'name': 'Disease',
        'type': 'Inference Result',
        'possible_values': [
            'Eczema',
            'Contact Dermatitis',
            'Ringworm',
            'Acne Vulgaris',
            'Skin Ulcer'
        ]
    },
    'treatment': {
        'name': 'Treatment',
        'type': 'Recommendation',
        'possible_values': [
            'Topical Corticosteroid',
            'Moisturizer Therapy',
            'Antifungal Cream',
            'Antibiotic Ointment',
            'Pain Relief Medication'
        ]
    },
    'lifestyle': {
        'name': 'Lifestyle',
        'type': 'Recommendation',
        'possible_values': [
            'Avoid Sharing Personal Items',
            'Maintain Skin Hygiene',
            'Avoid Scratching',
            'Avoid Irritants',
            'Regular Wound Care',
            'Reduce Sun Exposure',
            'Seek Medical Attention',
            'Parental Supervision and Assistance',
            'Caregiver or Guardian Assistance'
        ]
    },
    'diet': {
        'name': 'Diet',
        'type': 'Recommendation',
        'possible_values': [
            'Avoid Peanut Products',
            'Avoid Seafood',
            'Anti-Inflammatory Diet',
            'Low Sugar Diet',
            'High Protein Diet',
            'Adequate Hydration'
        ]
    }
}

# ============================================
# LAYER 1: DISEASE IDENTIFICATION RULES
# ============================================

DISEASE_RULES = [
    {
        'id': 'rule_1a',
        'name': 'Eczema (with Allergy)',
        'layer': 1,
        'conditions': {
            'itching': 'Yes',
            'allergy': ['Peanut', 'Seafood'],  # Has allergy
            'appearance': ['Scaly / Flaky', 'Hyperpigmented / Depigmented', 'Smaller than 5mm']
        },
        'logic': 'IF Itching AND Allergy AND (Scaly OR Hyperpigmented OR Small_Lesions)',
        'conclusion': 'Eczema',
        'contagious': False
    },
    {
        'id': 'rule_1b',
        'name': 'Eczema (without Allergy)',
        'layer': 1,
        'conditions': {
            'itching': 'Yes',
            'allergy': ['None'],  # No allergy
            'appearance': ['Scaly / Flaky', 'Hyperpigmented / Depigmented', 'Smaller than 5mm']
        },
        'logic': 'IF Itching AND NOT Allergy AND (Scaly OR Hyperpigmented OR Small_Lesions)',
        'conclusion': 'Eczema',
        'contagious': False
    },
    {
        'id': 'rule_2',
        'name': 'Contact Dermatitis',
        'layer': 1,
        'conditions': {
            'burning_sensation': 'Yes',
            'allergy': ['Peanut', 'Seafood'],  # Has allergy
            'appearance': ['Well-Demarcated', 'Crusting / Oozing', 'Swollen']
        },
        'logic': 'IF Burning_Sensation AND Allergy AND (Well_Demarcated OR Crusting OR Swollen)',
        'conclusion': 'Contact Dermatitis',
        'contagious': False
    },
    {
        'id': 'rule_3',
        'name': 'Ringworm',
        'layer': 1,
        'conditions': {
            'itching': 'Yes',
            'appearance': ['Circular', 'Annular', 'Scaly / Flaky']
        },
        'logic': 'IF Itching AND (Circular OR Annular OR Scaly)',
        'conclusion': 'Ringworm',
        'contagious': True
    },
    {
        'id': 'rule_4',
        'name': 'Acne Vulgaris',
        'layer': 1,
        'conditions': {
            'appearance': ['Papules / Pustules'],
            'lesion_size': 'Smaller than 5mm',
            'pain': 'No'
        },
        'logic': 'IF Papules_Pustules AND (Small_Lesions OR NOT Pain)',
        'conclusion': 'Acne Vulgaris',
        'contagious': False
    },
    {
        'id': 'rule_5',
        'name': 'Skin Ulcer',
        'layer': 1,
        'conditions': {
            'appearance': ['Ulcer'],
            'pain': 'Yes',
            'lesion_size': 'Larger than 5mm'
        },
        'logic': 'IF Ulcer AND Pain AND Large_Lesions',
        'conclusion': 'Skin Ulcer',
        'contagious': False
    }
]

# ============================================
# LAYER 2: TREATMENT RULES
# ============================================

TREATMENT_RULES = [
    {
        'id': 'rule_t1',
        'name': 'Eczema Large Lesion Treatment',
        'layer': 2,
        'conditions': {
            'disease': 'Eczema',
            'lesion_size': 'Larger than 5mm'
        },
        'logic': 'IF Disease = Eczema AND Large_Lesions',
        'conclusion': 'Topical Corticosteroid'
    },
    {
        'id': 'rule_t2',
        'name': 'Eczema Small Lesion Treatment',
        'layer': 2,
        'conditions': {
            'disease': 'Eczema',
            'lesion_size': 'Smaller than 5mm'
        },
        'logic': 'IF Disease = Eczema AND Small_Lesions',
        'conclusion': 'Moisturizer Therapy'
    },
    {
        'id': 'rule_t3',
        'name': 'Ringworm Treatment',
        'layer': 2,
        'conditions': {
            'disease': 'Ringworm'
        },
        'logic': 'IF Disease = Ringworm',
        'conclusion': 'Antifungal Cream'
    },
    {
        'id': 'rule_t4',
        'name': 'Acne Vulgaris Treatment',
        'layer': 2,
        'conditions': {
            'disease': 'Acne Vulgaris',
            'lesion_size': 'Smaller than 5mm'
        },
        'logic': 'IF Disease = Acne_Vulgaris AND Small_Lesions',
        'conclusion': 'Antibiotic Ointment'
    },
    {
        'id': 'rule_t5',
        'name': 'Contact Dermatitis Treatment',
        'layer': 2,
        'conditions': {
            'disease': 'Contact Dermatitis'
        },
        'logic': 'IF Disease = Contact_Dermatitis',
        'conclusion': 'Topical Corticosteroid'
    },
    {
        'id': 'rule_t6',
        'name': 'Skin Ulcer Treatment',
        'layer': 2,
        'conditions': {
            'disease': 'Skin Ulcer',
            'pain': 'Yes'
        },
        'logic': 'IF Disease = Skin_Ulcer AND Pain',
        'conclusion': 'Antibiotic Ointment'
    },
    {
        'id': 'rule_t7',
        'name': 'Pain Relief Treatment',
        'layer': 2,
        'conditions': {
            'pain': 'Yes',
            'disease_not': 'Acne Vulgaris'
        },
        'logic': 'IF Pain AND NOT Disease = Acne_Vulgaris',
        'conclusion': 'Pain Relief Medication'
    }
]

# ============================================
# LAYER 3: LIFESTYLE RULES
# ============================================

LIFESTYLE_RULES = [
    {
        'id': 'rule_l1',
        'name': 'Ringworm Lifestyle',
        'layer': 3,
        'conditions': {
            'disease': 'Ringworm'
        },
        'logic': 'IF Disease = Ringworm',
        'conclusion': ['Avoid Sharing Personal Items', 'Maintain Skin Hygiene']
    },
    {
        'id': 'rule_l2',
        'name': 'Eczema Child Lifestyle',
        'layer': 3,
        'conditions': {
            'disease': 'Eczema',
            'age_group': 'Child'
        },
        'logic': 'IF Disease = Eczema AND Age_Group = Child',
        'conclusion': ['Avoid Scratching']
    },
    {
        'id': 'rule_l3',
        'name': 'Eczema Adult Lifestyle',
        'layer': 3,
        'conditions': {
            'disease': 'Eczema',
            'age_group': 'Adult'
        },
        'logic': 'IF Disease = Eczema AND Age_Group = Adult',
        'conclusion': ['Avoid Irritants']
    },
    {
        'id': 'rule_l4',
        'name': 'Eczema Elderly Lifestyle',
        'layer': 3,
        'conditions': {
            'disease': 'Eczema',
            'age_group': 'Elderly'
        },
        'logic': 'IF Disease = Eczema AND Age_Group = Elderly',
        'conclusion': ['Regular Wound Care']
    },
    {
        'id': 'rule_l5',
        'name': 'Acne Adult Lifestyle',
        'layer': 3,
        'conditions': {
            'disease': 'Acne Vulgaris',
            'age_group': 'Adult'
        },
        'logic': 'IF Disease = Acne_Vulgaris AND Age_Group = Adult',
        'conclusion': ['Reduce Sun Exposure']
    },
    {
        'id': 'rule_l6',
        'name': 'Contact Dermatitis Lifestyle',
        'layer': 3,
        'conditions': {
            'disease': 'Contact Dermatitis'
        },
        'logic': 'IF Disease = Contact_Dermatitis',
        'conclusion': ['Avoid Irritants']
    },
    {
        'id': 'rule_l7',
        'name': 'Large Lesion Lifestyle',
        'layer': 3,
        'conditions': {
            'lesion_size': 'Larger than 5mm',
            'disease_not': 'Acne Vulgaris'
        },
        'logic': 'IF Lesion_Size = Large AND NOT Disease = Acne_Vulgaris',
        'conclusion': ['Seek Medical Attention']
    },
    {
        'id': 'rule_l8',
        'name': 'Elderly Pain Lifestyle',
        'layer': 3,
        'conditions': {
            'age_group': 'Elderly',
            'pain': 'Yes'
        },
        'logic': 'IF Age_Group = Elderly AND Pain',
        'conclusion': ['Regular Wound Care']
    },
    {
        'id': 'rule_l9',
        'name': 'Child Supervision',
        'layer': 3,
        'conditions': {
            'age_group': 'Child'
        },
        'logic': 'IF Age_Group = Child',
        'conclusion': ['Parental Supervision and Assistance']
    },
    {
        'id': 'rule_l10',
        'name': 'Elderly Assistance',
        'layer': 3,
        'conditions': {
            'age_group': 'Elderly'
        },
        'logic': 'IF Age_Group = Elderly',
        'conclusion': ['Caregiver or Guardian Assistance']
    }
]

# ============================================
# LAYER 4: DIET RULES
# ============================================

DIET_RULES = [
    {
        'id': 'rule_d1',
        'name': 'Peanut Allergy Diet',
        'layer': 4,
        'conditions': {
            'allergy': 'Peanut'
        },
        'logic': 'IF Allergy = Peanut',
        'conclusion': ['Avoid Peanut Products']
    },
    {
        'id': 'rule_d2',
        'name': 'Seafood Allergy Diet',
        'layer': 4,
        'conditions': {
            'allergy': 'Seafood'
        },
        'logic': 'IF Allergy = Seafood',
        'conclusion': ['Avoid Seafood']
    },
    {
        'id': 'rule_d3',
        'name': 'Eczema No Allergy Diet',
        'layer': 4,
        'conditions': {
            'disease': 'Eczema',
            'allergy': 'None'
        },
        'logic': 'IF Disease = Eczema AND NOT Allergy',
        'conclusion': ['Anti-Inflammatory Diet']
    },
    {
        'id': 'rule_d4',
        'name': 'Acne Vulgaris Diet',
        'layer': 4,
        'conditions': {
            'disease': 'Acne Vulgaris'
        },
        'logic': 'IF Disease = Acne_Vulgaris',
        'conclusion': ['Low Sugar Diet']
    },
    {
        'id': 'rule_d5',
        'name': 'Skin Ulcer Diet',
        'layer': 4,
        'conditions': {
            'disease': 'Skin Ulcer'
        },
        'logic': 'IF Disease = Skin_Ulcer',
        'conclusion': ['High Protein Diet']
    },
    {
        'id': 'rule_d6',
        'name': 'Elderly Diet',
        'layer': 4,
        'conditions': {
            'age_group': 'Elderly',
            'disease_not': 'Acne Vulgaris'
        },
        'logic': 'IF Age_Group = Elderly AND NOT Disease = Acne_Vulgaris',
        'conclusion': ['High Protein Diet']
    },
    {
        'id': 'rule_d7',
        'name': 'Child No Allergy Diet',
        'layer': 4,
        'conditions': {
            'age_group': 'Child',
            'allergy': 'None'
        },
        'logic': 'IF Age_Group = Child AND NOT Allergy',
        'conclusion': ['Adequate Hydration']
    }
]

# ============================================
# QUESTION DEFINITIONS
# ============================================

QUESTIONS = [
    # Patient Profile
    {
        'id': 'age_group',
        'category': 'Patient Profile',
        'question': 'What is your age group?',
        'type': 'single',
        'options': ['Child', 'Adult', 'Elderly']
    },
    {
        'id': 'allergy',
        'category': 'Patient Profile',
        'question': 'Do you have any known allergies?',
        'type': 'single',
        'options': ['None', 'Peanut', 'Seafood']
    },
    # Symptoms
    {
        'id': 'itching',
        'category': 'Symptoms',
        'question': 'Are you experiencing itching?',
        'type': 'single',
        'options': ['Yes', 'No']
    },
    {
        'id': 'burning_sensation',
        'category': 'Symptoms',
        'question': 'Are you experiencing a burning sensation?',
        'type': 'single',
        'options': ['Yes', 'No']
    },
    {
        'id': 'pain',
        'category': 'Symptoms',
        'question': 'Are you experiencing pain?',
        'type': 'single',
        'options': ['Yes', 'No']
    },
    # Lesion Appearance
    {
        'id': 'appearance',
        'category': 'Lesion Appearance',
        'question': 'How does the skin lesion appear? (Select all that apply)',
        'type': 'multiple',
        'options': [
            'Circular',
            'Annular',
            'Scaly / Flaky',
            'Well-Demarcated',
            'Swollen',
            'Papules / Pustules',
            'Crusting / Oozing',
            'Hyperpigmented / Depigmented',
            'Ulcer'
        ]
    },
    {
        'id': 'lesion_size',
        'category': 'Lesion Appearance',
        'question': 'What is the size of the lesion?',
        'type': 'single',
        'options': ['Larger than 5mm', 'Smaller than 5mm']
    }
]

# ============================================
# ALL RULES COMBINED (for documentation)
# ============================================

ALL_RULES = {
    'layer_1': DISEASE_RULES,
    'layer_2': TREATMENT_RULES,
    'layer_3': LIFESTYLE_RULES,
    'layer_4': DIET_RULES
}

# Disease information for display
DISEASE_INFO = {
    'Eczema': {
        'description': 'A chronic inflammatory skin condition causing dry, itchy, and inflamed skin.',
        'contagious': False
    },
    'Contact Dermatitis': {
        'description': 'An inflammatory skin reaction caused by direct contact with allergens or irritants.',
        'contagious': False
    },
    'Ringworm': {
        'description': 'A contagious fungal infection that causes a ring-shaped rash on the skin.',
        'contagious': True
    },
    'Acne Vulgaris': {
        'description': 'A common skin condition characterized by pimples, blackheads, and whiteheads.',
        'contagious': False
    },
    'Skin Ulcer': {
        'description': 'An open sore on the skin that fails to heal properly.',
        'contagious': False
    }
}