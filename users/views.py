from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserLoginForm, UserRegisterForm, UserProfileForm
from .models import User

# Create your views here.

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        send_mail(
            subject='Добро пожаловать!',
            message='Спасибо за регистрацию в SkyStore!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email],
            fail_silently=True,
        )

        return response

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')

class UserProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class UserLogoutView(LogoutView):
    next_page = reverse_lazy("home")