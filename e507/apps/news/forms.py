from django import forms
from django.conf import settings
from django.utils.translation import ugettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from redactor.widgets import RedactorEditor

import datetime

LANGUAGES = settings.LANGUAGES
MY_FORMAT = ['%d %m %Y, %H:%M']

class NewsForm(forms.Form):
    title = forms.CharField(label=_('The news title'), max_length=100)
    message = forms.CharField(label=_('Enter your message'), widget=RedactorEditor())
    start_date = forms.DateTimeField(label=_('The news will be published the'), input_formats=MY_FORMAT, initial=datetime.datetime.now(), widget=forms.TextInput(attrs={'class': 'datetimepicker',}))
    end_date = forms.DateTimeField(label=_('The news will be removed the'), input_formats=MY_FORMAT, required=False, widget=forms.TextInput(attrs={'class': 'datetimepicker',}))
    active = forms.BooleanField(required=False, initial=True, widget=forms.HiddenInput())
    language = forms.ChoiceField(choices=LANGUAGES, initial='fr', widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'add-news-form'
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', _('Add new')))
