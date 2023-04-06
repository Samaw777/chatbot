from django.shortcuts import render, redirect
from django.http import JsonResponse
from .chatbot_ai import getResponse
# Create your views here.

def index(request):
    return render(request, 'mainchat/index.html')

def home(request):
    if request.method == 'POST':
        return redirect('mainchat-home')  

    return render(request, 'mainchat/home.html')

def output(request):  
    return render(request, 'mainchat/output.html')

def chatbot_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        response = getResponse(user_input, any)
        return JsonResponse({'response': response})

    return render(request, 'mainchat/home.html')
