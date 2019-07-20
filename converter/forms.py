from django import forms
from .models import RequestVideo


class UrlForm(forms.ModelForm):
    url = forms.RegexField(regex=r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$', max_length=256)

    class Meta:
        model = RequestVideo
        exclude = ('url', 'date_request')
