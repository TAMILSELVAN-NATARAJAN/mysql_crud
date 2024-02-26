from django.contrib.auth.forms import UserCreationForm
from .models import Employee
from django.forms import ModelForm

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields =['name','email','password']