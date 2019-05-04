from django import forms

from oauth_app import models


class AppCreateForm(forms.ModelForm):
    class Meta:
        model = models.AppModel
        fields = ('name', 'description', 'app_url')
