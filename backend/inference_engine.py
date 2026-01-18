"""
Inference Engine for Skin Disease Expert System
Implements forward chaining with 4-layer rule evaluation
"""

from backend.knowledge_base import (
    DISEASE_RULES, TREATMENT_RULES, LIFESTYLE_RULES, DIET_RULES, DISEASE_INFO
)


class InferenceEngine:
    """
    Forward chaining inference engine with 4-layer rule evaluation
    Layer 1: Disease Identification
    Layer 2: Treatment Recommendation
    Layer 3: Lifestyle Recommendation
    Layer 4: Diet Recommendation
    """
    
    def __init__(self):
        self.fired_rules = []
        
    def diagnose(self, user_facts):
        """
        Main diagnosis method using forward chaining through 4 layers
        
        Args:
            user_facts (dict): User's answers to questions
            
        Returns:
            dict: Complete diagnosis results with disease, treatment, lifestyle, and diet
        """
        self.fired_rules = []
        
        # Layer 1: Disease Identification
        disease = self._infer_disease(user_facts)
        
        if not disease:
            return {
                'success': False,
                'message': 'No diagnosis found based on the provided symptoms. Please consult a healthcare professional.',
                'disease': None,
                'contagious': None,
                'treatment': [],
                'lifestyle': [],
                'diet': [],
                'explanation': self.fired_rules
            }
        
        # Add disease to facts for subsequent layers
        facts_with_disease = user_facts.copy()
        facts_with_disease['disease'] = disease
        
        # Layer 2: Treatment Recommendation
        treatments = self._infer_treatment(facts_with_disease)
        
        # Layer 3: Lifestyle Recommendation
        lifestyle = self._infer_lifestyle(facts_with_disease)
        
        # Layer 4: Diet Recommendation
        diet = self._infer_diet(facts_with_disease)
        
        # Get disease info
        disease_info = DISEASE_INFO.get(disease, {})
        
        return {
            'success': True,
            'disease': disease,
            'disease_description': disease_info.get('description', ''),
            'contagious': disease_info.get('contagious', False),
            'treatment': treatments,
            'lifestyle': lifestyle,
            'diet': diet,
            'explanation': self.fired_rules
        }
    
    def _infer_disease(self, user_facts):
        """
        Layer 1: Fire disease identification rules
        """
        for rule in DISEASE_RULES:
            if self._evaluate_disease_rule(rule, user_facts):
                self.fired_rules.append({
                    'layer': 1,
                    'rule_id': rule['id'],
                    'name': rule['name'],
                    'logic': rule['logic'],
                    'conclusion': rule['conclusion']
                })
                return rule['conclusion']
        return None
    
    def _evaluate_disease_rule(self, rule, facts):
        """
        Evaluate disease identification rule conditions
        """
        conditions = rule['conditions']
        
        for key, required_value in conditions.items():
            # Skip disease_not conditions (handled separately)
            if key == 'disease_not':
                continue
                
            user_value = facts.get(key)
            
            if user_value is None:
                return False
            
            # Handle appearance (multiple selection in both rule and user input)
            if key == 'appearance':
                # User's appearance is a list, required is also a list
                # Need to check if ANY of the required values are in user's selection
                if isinstance(user_value, list):
                    if not any(val in user_value for val in required_value):
                        return False
                else:
                    return False
            
            # Handle allergy with list of valid values
            elif key == 'allergy':
                if isinstance(required_value, list):
                    if user_value not in required_value:
                        return False
                else:
                    if user_value != required_value:
                        return False
            
            # Handle single value comparison
            else:
                if isinstance(required_value, list):
                    if user_value not in required_value:
                        return False
                else:
                    if user_value != required_value:
                        return False
        
        return True
    
    def _infer_treatment(self, facts):
        """
        Layer 2: Fire treatment rules
        """
        treatments = []
        
        for rule in TREATMENT_RULES:
            if self._evaluate_rule_with_disease(rule, facts):
                self.fired_rules.append({
                    'layer': 2,
                    'rule_id': rule['id'],
                    'name': rule['name'],
                    'logic': rule['logic'],
                    'conclusion': rule['conclusion']
                })
                if rule['conclusion'] not in treatments:
                    treatments.append(rule['conclusion'])
        
        return treatments
    
    def _infer_lifestyle(self, facts):
        """
        Layer 3: Fire lifestyle rules
        """
        lifestyle = []
        
        for rule in LIFESTYLE_RULES:
            if self._evaluate_rule_with_disease(rule, facts):
                self.fired_rules.append({
                    'layer': 3,
                    'rule_id': rule['id'],
                    'name': rule['name'],
                    'logic': rule['logic'],
                    'conclusion': rule['conclusion']
                })
                # Conclusion can be a list
                if isinstance(rule['conclusion'], list):
                    for item in rule['conclusion']:
                        if item not in lifestyle:
                            lifestyle.append(item)
                else:
                    if rule['conclusion'] not in lifestyle:
                        lifestyle.append(rule['conclusion'])
        
        return lifestyle
    
    def _infer_diet(self, facts):
        """
        Layer 4: Fire diet rules
        """
        diet = []
        
        for rule in DIET_RULES:
            if self._evaluate_rule_with_disease(rule, facts):
                self.fired_rules.append({
                    'layer': 4,
                    'rule_id': rule['id'],
                    'name': rule['name'],
                    'logic': rule['logic'],
                    'conclusion': rule['conclusion']
                })
                # Conclusion can be a list
                if isinstance(rule['conclusion'], list):
                    for item in rule['conclusion']:
                        if item not in diet:
                            diet.append(item)
                else:
                    if rule['conclusion'] not in diet:
                        diet.append(rule['conclusion'])
        
        return diet
    
    def _evaluate_rule_with_disease(self, rule, facts):
        """
        Evaluate rules that may have disease conditions and disease_not conditions
        """
        conditions = rule['conditions']
        
        for key, required_value in conditions.items():
            # Handle negative disease condition
            if key == 'disease_not':
                if facts.get('disease') == required_value:
                    return False
                continue
            
            user_value = facts.get(key)
            
            if user_value is None:
                return False
            
            # Handle value comparison
            if isinstance(required_value, list):
                if user_value not in required_value:
                    return False
            else:
                if user_value != required_value:
                    return False
        
        return True
    
    def get_explanation(self):
        """
        Get list of rules that fired during last diagnosis
        """
        return self.fired_rules