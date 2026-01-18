"""
Backend package for Skin Disease Expert System
"""

from .inference_engine import InferenceEngine
from .knowledge_base import (
    QUESTIONS,
    INPUT_VARIABLES,
    OUTPUT_VARIABLES,
    DISEASE_RULES,
    TREATMENT_RULES,
    LIFESTYLE_RULES,
    DIET_RULES,
    DISEASE_INFO,
    ALL_RULES
)

__all__ = [
    'InferenceEngine',
    'QUESTIONS',
    'INPUT_VARIABLES',
    'OUTPUT_VARIABLES',
    'DISEASE_RULES',
    'TREATMENT_RULES',
    'LIFESTYLE_RULES',
    'DIET_RULES',
    'DISEASE_INFO',
    'ALL_RULES'
]