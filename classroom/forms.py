import csv
from io import TextIOWrapper
from django import forms
from django.contrib.auth.forms import UserCreationForm
from classroom.models import (
    User,
    Teacher,
    Student,
    StudentMarks,
    MessageToTeacher,
    ClassNotice,
    ClassAssignment,
    SubmitAssignment,
    Question,
    QuestionsInAssignment,
)
from django.db import transaction


## User Login Form (Applied in both student and teacher login)
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "answer"}),
            "password1": forms.PasswordInput(attrs={"class": "answer"}),
            "password2": forms.PasswordInput(attrs={"class": "answer"}),
        }


## Teacher Registration Form
class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["name", "subject_name", "phone", "email"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "answer"}),
            "subject_name": forms.TextInput(attrs={"class": "answer"}),
            "phone": forms.NumberInput(attrs={"class": "answer"}),
            "email": forms.EmailInput(attrs={"class": "answer"}),
        }


## Teacher Profile Update Form
class TeacherProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["name", "subject_name", "email", "phone", "teacher_profile_pic"]


## Student Registration Form
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "roll_no", "phone", "email"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "answer"}),
            "roll_no": forms.NumberInput(attrs={"class": "answer"}),
            "phone": forms.NumberInput(attrs={"class": "answer"}),
            "email": forms.EmailInput(attrs={"class": "answer"}),
        }


## Student profile update form
class StudentProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "roll_no", "email", "phone", "student_profile_pic"]


## Form for uploading marks and also for updating it.
class MarksForm(forms.ModelForm):
    class Meta:
        model = StudentMarks
        fields = ["subject_name", "marks_obtained", "maximum_marks"]


## Writing message to teacher
class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageToTeacher
        fields = ["message"]


## Writing notice in the class
class NoticeForm(forms.ModelForm):
    class Meta:
        model = ClassNotice
        fields = ["message"]


## Form for uploading or updating assignment (teachers only)
class AssignmentForm(forms.ModelForm):
    class Meta:
        model = ClassAssignment
        fields = ["assignment_name", "assignment"]


## Form for submitting assignment (Students only)
class SubmitForm(forms.ModelForm):
    class Meta:
        model = SubmitAssignment
        fields = ["submit"]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question_number", "marks"]


class QuestionsInAssignmentForm(forms.ModelForm):
    class Meta:
        model = QuestionsInAssignment
        fields = ["question"]

class MassAddStudentsForm(forms.Form):
    csv_file = forms.FileField(label='CSV File')

    def save(self):
        csv_file = TextIOWrapper(self.cleaned_data['csv_file'].file, encoding='utf-8')
        reader = csv.DictReader(csv_file)
        for row in reader:
            # Assuming your CSV has columns like 'name', 'roll_no', 'phone', 'email'
            name = row.get('name')
            roll_no = row.get('roll_no')
            phone = row.get('phone')
            email = row.get('email')

            # Check if a student with the same email already exists
            student, created = Student.objects.get_or_create(email=email, defaults={'name': name, 'roll_no': roll_no, 'phone': phone})

            # If a new student is created, you can add it to the class
            if created:
                # Add the student to the class (add your logic here)
                # For example:
                # student.class = some_class
                # student.save()
                pass