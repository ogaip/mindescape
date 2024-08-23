from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm

@login_required
def chat(request):
    messages = Message.objects.all()
    form = MessageForm()
    return render(request, 'chat.html', {'messages': messages, 'form': form})