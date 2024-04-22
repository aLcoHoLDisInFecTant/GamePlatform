from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class TherapistRegistrationForm(UserCreationForm):
    specialization = forms.CharField(required=False, help_text="Optional.")
    contact_info = forms.CharField(required=False, help_text="Optional.")

    class Meta:
        model = get_user_model()  # 使用自定义用户模型
        fields = ['username', 'specialization', 'contact_info', 'password1', 'password2']
