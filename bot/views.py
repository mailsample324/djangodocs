
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        user_input = request.POST['user_input']
        # Process user input and generate a response
        response = generate_response(user_input)
        return render(request, 'chatbot.html', {'response': response})
    else:
        return render(request, 'chatbot.html')

def generate_response(user_input):
    # Implement your chatbot's logic here
    if 'hello' in user_input.lower():
        return 'Hello! How can I help you today?'
    elif 'weather' in user_input.lower():
        return 'I am sorry, but I am not able to provide weather information.'
    else:
        return 'I am sorry, I do not understand your input.'

# Create your views here.

