from django import forms

class ProcessForm(forms.Form):
    input_text = forms.CharField(widget=forms.Textarea)