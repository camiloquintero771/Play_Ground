from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Profile


class SignUpView(CreateView):  # vista de registro
    form_class = UserCreationFormWithEmail
    template_name = "registration/signup.html"

    def get_success_url(self):
        return reverse_lazy('login') + '?register'


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):  # vista para editar el perfil
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = "registration/profile_form.html"

    def get_object(self):
        profile, created = \
            Profile.objects.get_or_create(user=self.request.user)
        return profile


class EmailUpdate(UpdateView):  # vista para editar el perfil
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = "registration/profile_email_form.html"

    def get_object(self):

        return self.request.user
