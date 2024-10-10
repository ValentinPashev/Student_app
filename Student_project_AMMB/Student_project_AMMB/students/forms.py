#Forms ==>
from django import forms
from Student_project_AMMB.students.models import Student



class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'