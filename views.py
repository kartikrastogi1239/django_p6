from django.shortcuts import render
from .forms import UserForm



def user_form_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Message: {message}")
            return render(request, 'success.html')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})
