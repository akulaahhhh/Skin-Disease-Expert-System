import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_explanation(pattern, diagnosis, facts, triggered_rules):
    """
    Generate HOW and WHY explanation for a rule-based expert system using the latest Gemini SDK.
    """
    prompt = f"""
You are an expert skin disease explanation assistant. 

Explain in **simple and clear language** JUST BRIEF. NO LONG EXPLANATION, MAKE IT SHORT:
1. How the person might have developed this skin condition (possible causes, lifestyle, environment, triggers).(answer simply and short)
2. How long it might take to heal under normal circumstances.(answer simply and short)
3. Give practical advice or self-care measures in a friendly way.(answer simply and short)

Do NOT list rule IDs or technical terms. Focus on the user. 

Skin Condition Pattern: {pattern}
Diagnosis: {diagnosis}
Symptoms: {', '.join(facts.get('symptoms', []))}
Lesion Appearance: {', '.join(facts.get('lesion_appearance', []))}
Triggered Rules: {', '.join(triggered_rules)}

End with a short medical disclaimer.
"""


    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",  # latest model for text explanations
        contents=prompt
    )

    return response.text

