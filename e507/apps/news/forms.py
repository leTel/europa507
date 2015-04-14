from django import forms
from django.conf import settings

import datetime

LANGUAGES = settings.LANGUAGES

class NewsForm(forms.Form):
    title = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.widgets.Textarea())
    start_date = forms.DateTimeField(initial=datetime.datetime.now())
    end_date = forms.DateTimeField(required=False)
    active = forms.BooleanField(initial=True)
    language = forms.ChoiceField(choices=LANGUAGES, initial='fr')
