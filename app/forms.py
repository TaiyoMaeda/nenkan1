from django import forms
from django.contrib.auth.forms import UserCreationForm

class SeisakuForm(forms.Form):
    name = forms.Field(label='お名前', required=True)
    inquiry = forms.CharField(label='お問い合わせ内容', required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = '名前を入力'
        self.fields['inquiry'].widget.attrs['placeholder'] = 'メッセージを入力'

