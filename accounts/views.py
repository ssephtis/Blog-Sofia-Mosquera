from django.contrib.auth import logout
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile

# Registro
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

# Logout por POST
@method_decorator(csrf_protect, name='dispatch')
class CustomLogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

# Ver perfil
class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile_detail.html'

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)

# Editar perfil
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile_form.html'
    success_url = '/accounts/profile/'

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)