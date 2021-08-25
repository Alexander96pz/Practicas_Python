from django import forms
from .models import Course
class CoursesForm(forms.ModelForm):
    title=forms.CharField(required=True)
    class Meta:
        model=Course
        fields=['title']