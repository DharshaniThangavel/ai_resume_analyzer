import re

def audit_bullet_points(resume_text):
    """
    Scans the resume for bullet points, evaluates their impact quality, 
    and offers structured XYZ formula improvement suggestions.
    """
    if not resume_text:
        return []

    # Simple heuristic to extract potential bullet points (lines starting with bullets, dashes, or spacing)
    lines = resume_text.split('\n')
    bullets = []
    
    for line in lines:
        cleaned = line.strip()
        # Look for lines starting with typical bullet symbols or action verbs
        if cleaned.startswith(('•', '-', '*', '–')) or (len(cleaned) > 20 and len(cleaned.split()) > 4):
            # Strip bullet characters if present
            if cleaned.startswith(('•', '-', '*', '–')):
                cleaned = cleaned[1:].strip()
            if len(cleaned) > 15:
                bullets.append(cleaned)

    # Limit to top 5 candidates for evaluation to keep performance fast
    sample_bullets = bullets[:5] if len(bullets) >= 5 else bullets
    feedback_list = []

    # Heuristic impact analysis simulating AI suggestions
    for bullet in sample_bullets:
        has_metrics = bool(re.search(r'\d+%|\d+x|\d+\+|\b(reduced|increased|built|architected|optimized|saved|generated)\b', bullet, re.IGNORECASE))
        
        if has_metrics:
            feedback_list.append({
                "original": bullet,
                "status": "Strong",
                "feedback": "Contains good action verbs and metrics.",
                "suggestion": bullet
            })
        else:
            feedback_list.append({
                "original": bullet,
                "status": "Needs Improvement",
                "feedback": "Passive wording. Lacks quantifiable outcomes or specific metrics.",
                "suggestion": f"Engineered solution for {bullet[:30]}..., optimizing efficiency and performance by 25%."
            })

    return feedback_list