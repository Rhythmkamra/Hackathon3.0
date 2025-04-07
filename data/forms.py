from django import forms
from .models import Student_cultural, Student_sports, Student_technical

class StudentFormBase(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentFormBase, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True  # Make all fields mandatory

class StudentFormCultural(StudentFormBase):
    intercollege_mcq = forms.BooleanField(label='Intercollege', required=True)
    intracollege_mcq = forms.BooleanField(label='Intracollege', required=True)

    class Meta:
        model = Student_cultural
        fields = ['name', 'rollno', 'year', 'event_name', 'event_description', 'event_type', 'intercollege_mcq', 'intracollege_mcq', 'position', 'certificate']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'rollno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter roll number'}),
            'year': forms.Select(attrs={'class': 'form-control'}),
            'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event name'}),
            'event_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Event description'}),
            'event_type': forms.Select(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
        }

class StudentFormSports(StudentFormBase):
    intercollege_mcq = forms.BooleanField(label='Intercollege', required=True)
    intracollege_mcq = forms.BooleanField(label='Intracollege', required=True)

    class Meta:
        model = Student_sports
        fields = ['name', 'rollno', 'year', 'event_name', 'event_description', 'event_type', 'intercollege_mcq', 'intracollege_mcq', 'position', 'certificate']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'rollno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter roll number'}),
            'year': forms.Select(attrs={'class': 'form-control'}),
            'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event name'}),
            'event_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Event description'}),
            'event_type': forms.Select(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
        }

class StudentFormTechnical(StudentFormBase):
    intercollege_mcq = forms.BooleanField(label='Intercollege', required=True)
    intracollege_mcq = forms.BooleanField(label='Intracollege', required=True)

    class Meta:
        model = Student_technical
        fields = ['name', 'rollno', 'year', 'event_name', 'event_description', 'event_type', 'intercollege_mcq', 'intracollege_mcq', 'position', 'certificate']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'rollno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter roll number'}),
            'year': forms.Select(attrs={'class': 'form-control'}),
            'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event name'}),
            'event_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Event description'}),
            'event_type': forms.Select(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
        }
