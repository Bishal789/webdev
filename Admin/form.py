from django import forms
from admin.models import admin

class AdminForm(froms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"