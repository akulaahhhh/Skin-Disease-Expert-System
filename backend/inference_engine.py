"""
Inference Engine for Skin Disease Expert System
Implements forward chaining with priority-based pattern selection
"""

from backend.knowledge_base import (
    PATTERN_RULES, DIAGNOSIS_RULES, TREATMENT_RULES, PATTERN_PRIORITY
)


class InferenceEngine:
    """
    Forward chaining inference engine with explanation facility
    """
    
    def __init__(self):
        self.fired_rules = []  # Track which rules fired for explanation
        
    def diagnose(self, user_facts):
        """
        Main diagnosis method using forward chaining
        
        Args:
            user_facts (dict): User's answers to questions
            
        Returns:
            dict: Diagnosis results with pattern, diagnosis, treatment, and explanation
        """
        self.fired_rules = []  # Reset for new diagnosis
        
        # Step 1: Fire pattern rules and select best pattern
        pattern = self._infer_pattern(user_facts)
        
        if not pattern:
            return {
                'success': False,
                'message': 'No diagnosis found. Please consult a healthcare professional.',
                'pattern': None,
                'diagnosis': None,
                'treatment': [],
                'explanation': self.fired_rules
            }
        
        # Step 2: Fire diagnosis rules
        diagnosis = self._infer_diagnosis(pattern, user_facts)
        
        if not diagnosis:
            return {
                'success': False,
                'message': 'Pattern identified but no specific diagnosis matched.',
                'pattern': pattern,
                'diagnosis': None,
                'treatment': [],
                'explanation': self.fired_rules
            }
        
        # Step 3: Fire treatment rules
        treatment = self._infer_treatment(diagnosis, user_facts)
        
        return {
            'success': True,
            'pattern': pattern,
            'diagnosis': diagnosis,
            'treatment': treatment,
            'explanation': self.fired_rules
        }
    
    def _infer_pattern(self, user_facts):
        """
        Fire all pattern rules and select highest priority pattern
        """
        matched_patterns = []
        
        for rule in PATTERN_RULES:
            if self._evaluate_rule(rule, user_facts):
                matched_patterns.append(rule['conclusion'])
                self.fired_rules.append(rule['name'])
        
        if not matched_patterns:
            return None
        
        # Remove duplicates while preserving order
        unique_patterns = list(dict.fromkeys(matched_patterns))
        
        # If multiple patterns, select highest priority
        if len(unique_patterns) > 1:
            best_pattern = max(unique_patterns, key=lambda p: PATTERN_PRIORITY.get(p, 0))
            return best_pattern
        
        return unique_patterns[0]
    
    def _infer_diagnosis(self, pattern, user_facts):
        """
        Fire diagnosis rules based on selected pattern
        """
        # Add pattern to facts for diagnosis rules
        facts_with_pattern = user_facts.copy()
        facts_with_pattern['pattern'] = pattern
        
        for rule in DIAGNOSIS_RULES:
            if self._evaluate_rule(rule, facts_with_pattern):
                self.fired_rules.append(rule['name'])
                return rule['conclusion']
        
        return None
    
    def _infer_treatment(self, diagnosis, user_facts):
        """
        Fire treatment rules based on diagnosis
        Priority rules fire first (Rule 17, Rule 18)
        """
        facts_with_diagnosis = user_facts.copy()
        facts_with_diagnosis['diagnosis'] = diagnosis
        
        # Sort rules: priority rules first
        sorted_rules = sorted(TREATMENT_RULES, 
                            key=lambda r: r.get('priority', False), 
                            reverse=True)
        
        for rule in sorted_rules:
            if self._evaluate_rule(rule, facts_with_diagnosis):
                self.fired_rules.append(rule['name'])
                return rule['conclusion']
        
        return []
    
    def _evaluate_rule(self, rule, facts):
        """
        Evaluate if a rule's conditions are satisfied by the facts
        
        Args:
            rule (dict): Rule with conditions
            facts (dict): User facts
            
        Returns:
            bool: True if all conditions are met
        """
        conditions = rule['conditions']
        
        for key, required_values in conditions.items():
            # Handle negative conditions (NOT)
            if key.endswith('_not'):
                actual_key = key.replace('_not', '')
                user_value = facts.get(actual_key)
                
                # For multiple selections (lists)
                if isinstance(user_value, list):
                    # Check if ANY required value is in user's selection (then fail)
                    if any(val in user_value for val in required_values):
                        return False
                else:
                    # For single selection
                    if user_value in required_values:
                        return False
                continue
            
            # Normal conditions
            user_value = facts.get(key)
            
            if user_value is None:
                return False
            
            # Handle multiple selections (lesion_appearance, lesion_location)
            if isinstance(user_value, list):
                # Check if ANY required value is in user's selection
                if not any(val in user_value for val in required_values):
                    return False
            else:
                # Single selection must match
                if user_value not in required_values:
                    return False
        
        return True
    
    def get_explanation(self):
        """
        Get list of rules that fired during last diagnosis
        """
        return self.fired_rules