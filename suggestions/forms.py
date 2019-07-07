from django import forms

from .models import Suggestion

class SuggestionForm(forms.ModelForm):
    name = forms.CharField(required=False)
    suggestion = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5}),
        help_text='Please Enter a suggestion, a thought or a remark.',
        label='')
    class Meta:
        model = Suggestion
        fields = ['name', 'suggestion']
