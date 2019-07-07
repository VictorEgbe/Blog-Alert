from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import SuggestionForm


def suggestions(request):
    form = SuggestionForm()
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, f"Thank You For Your Suggestions(s).")
            return redirect('home')
    context = {
        'title': 'Suggestions',
        'form': form,
    }
    return render(request, 'suggestions/page.html', context)
