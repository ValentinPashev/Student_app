#Forms ==>
from django import forms
from Student_project_AMMB.students.models import Student




class StudentBaseForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Student Name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'profile_picture': forms.Textarea(attrs={'placeholder': 'Add Image Url'}),
        }

        labels = {
            'name': 'Student Name',
            'date_of_birth': 'Date of Birth',
            'profile_picture': 'Link to Image',
        }





class StudentAddForm(StudentBaseForm):
    pass


class StudentDeleteForm(StudentBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True