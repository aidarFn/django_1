from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import forms, models, middlewares


# register
class RegistrationView(CreateView):
    form_class = forms.CustomRegisterForm
    template_name = "users/registration.html"
    success_url = "/login/"

    def form_valid(self, form):
        response = super().form_valid(form)
        age = form.cleaned_data["age"]
        if age < 3:
            self.object.club = "Вам рекомендуется: Сказки и народные истории"
        elif 3 <= age <= 10:
            self.object.club = "Вам рекомендуется: Сказки и народные истории"
        elif 11 <= age <= 18:
            self.object.club = "Вам рекомендуется: Научная фантастика, Фэнтези, Романтика и Детективы"
        elif 18 <= age <= 100:
            self.object.club = "Вам рекомендуется: Художественная литература, Историческая литература и Философия и эссеистика рекомендуется: Сказки и народные истории"
        else:
            self.object.club = "Ничего не могу порекомендовать"
        self.object.save()
        return response


# authorization
class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "users/login.html"

    def get_success_url(self):
        return reverse("users:user_list")


# Logout
class AuthLogoutView(LogoutView):
    next_page = reverse_lazy("users:login")


class UserListView(ListView):
    template_name = "users/user_list.html"
    model = models.CustomUser

    def get_queryset(self):
        return models.CustomUser.objects.filter().order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rec"] = getattr(self.request, "rec", "Ничего не могу порекомендовать")
        return context