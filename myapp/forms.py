from django import forms
from .models import CourseClass
from .models import ClassContent


class CourseClassForm(forms.ModelForm):
    class Meta:
        model = CourseClass
        fields = ['course_name', 'image', 'passkey', 'description']
        widgets = {
            'passkey': forms.PasswordInput(),  # To hide the passkey input
        }


# forms.py

class ClassContentForm(forms.ModelForm):
    class Meta:
        model = ClassContent
        fields = ['title', 'description', 'file', 'video_link']
