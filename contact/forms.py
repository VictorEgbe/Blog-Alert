from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    email = forms.EmailField(help_text='Enter a Valid Email')
    name = forms.CharField(required=False)
    description = forms.CharField(
        help_text='Please, leave a short reason why you want to be contacted.',
        widget=forms.Textarea(attrs={'rows': 2})
        )
    class Meta:
        model = Contact
        fields = ['email', 'name', 'description']
