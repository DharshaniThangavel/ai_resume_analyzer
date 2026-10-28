from django import forms
from .models import Resume, JobDescription

class ResumeUploadForm(forms.ModelForm):
    job_description_text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 6, 
            'placeholder': 'Paste the target Job Description (JD) here...'
        }),
        label="Target Job Description"
    )
    
    class Meta:
        model = Resume
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
        labels = {
            'file': 'Upload Resume (PDF or DOCX)'
        }