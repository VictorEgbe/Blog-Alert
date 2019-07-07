from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, f"Thanks You for Submitting Your Contact. I'll get back to you as soon as possible.")
            return redirect('home')
    context = {
        'title': 'Contact',
        'form': form,
    }
    return render(request, 'contact/page.html', context)
