from .forms import MessageForm
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .models import Message
from Crypto.Cipher import AES
import base64
import hashlib
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime
# Create your views here.

from django.views.generic import View

def Login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/received')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, "index.html")


def Logout(request):

    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)


class MessageView(FormView):
    template_name = 'message.html'
    form_class = MessageForm
    success_url = '/message'

    @method_decorator(login_required(login_url='/login'))
    def dispatch(self, *args, **kwargs):
        return super(MessageView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(MessageView, self).form_valid(form)


class ReceivedMessage(ListView):
    template_name = 'received.html'
    model = Message

    @method_decorator(login_required(login_url='/login'))
    def dispatch(self, *args, **kwargs):
        return super(ReceivedMessage, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ReceivedMessage, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['instance'] = []
        for instance in Message.objects.all():
            context['time'] = datetime.now()
            decryption_suite = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
            plain_text = decryption_suite.decrypt(base64.b64decode(instance.encrypted_message))
            h = hashlib.sha384()
            h.update(plain_text)
            if h.hexdigest() == instance.hashed_message and plain_text.strip() == instance.message.strip():
                context['instance'].append(instance)
            else:
                instance.message = 'Message is corrupted'
                instance.save()
                context['instance'].append(instance)

        return context

