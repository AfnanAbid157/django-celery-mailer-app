from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from .models import Message
from .tasks import send_message_task
from django.shortcuts import redirect

def home(request):
    return redirect('login') 

@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user).order_by('-created_at')
    return render(request, 'mailer/inbox.html', {'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            # trigger celery background task
            send_message_task.delay(request.user.id, msg.receiver.id, msg.subject, msg.body)
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'mailer/send_message.html', {'form': form})

@login_required
def sent_messages(request):
    messages = Message.objects.filter(sender=request.user).order_by('-created_at')
    return render(request, 'mailer/sent_messages.html', {'messages': messages})
