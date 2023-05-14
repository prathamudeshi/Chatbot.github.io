import openai
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ChatForm

openai.api_key = "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"

def chat(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            response = openai.Completion.create(
                engine="davinci",
                prompt=user_input,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.7,
            )
            chatbot_response = response.choices[0].text.strip()
            return render(request, 'chat.html', {'form': form, 'chatbot_response': chatbot_response})
    else:
        form = ChatForm()
    return render(request, 'chat.html', {'form': form})
