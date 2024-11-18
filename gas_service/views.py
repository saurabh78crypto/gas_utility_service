from django.shortcuts import render, redirect
from django.contrib.auth import logout


def landing_page(request):
    return render(request, 'landing_page.html')

def logout_view(request):
    logout(request)
    return redirect('landing_page')
