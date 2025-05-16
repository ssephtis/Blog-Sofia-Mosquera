from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Message
from .forms import MessageForm

class InboxView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'messenger/inbox.html'
    context_object_name = 'mensajes'

    def get_queryset(self):
        return Message.objects.filter(destinatario=self.request.user).order_by('-fecha')


class SendMessageView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'messenger/send_message.html'
    success_url = reverse_lazy('inbox')

    def form_valid(self, form):
        form.instance.remitente = self.request.user
        return super().form_valid(form)