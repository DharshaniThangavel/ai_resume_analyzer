from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    raw_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Resume ({self.user.username}) - {self.uploaded_at.strftime('%Y-%m-%d %H:%M')}"


class JobDescription(models.Model):
    title = models.CharField(max_length=255, default="Target Job Description")
    company = models.CharField(max_length=255, blank=True, null=True)
    description_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"JD ({self.created_at.strftime('%Y-%m-%d')})"


class AnalysisReport(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='reports')
    job_description = models.ForeignKey(JobDescription, on_delete=models.CASCADE)
    
    # Quantitative Scores
    overall_score = models.FloatField(default=0.0)
    semantic_score = models.FloatField(default=0.0)
    skill_match_score = models.FloatField(default=0.0)
    
    # Skill Analysis Data
    matched_skills = models.TextField(blank=True, null=True)
    missing_skills = models.TextField(blank=True, null=True)
    bullet_suggestions = models.JSONField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report #{self.id} for {self.resume.user.username} - Score: {self.overall_score}%"