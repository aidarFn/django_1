from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField

from .models import CustomUser

GENDER = (("Male", "Male"), ("Female", "Female"), ("Other", "Other"), ("Secret", "Secret"))


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(), required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "age",
            "gender",
            "phone_number",
            "country",
            "birth_date"
        )

    def save(self, commit=True):
        user = super(CustomRegisterForm, self).save(commit=True)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


@receiver(post_save, sender=CustomUser)
def set_rec(sender, instance, created, **kwargs):
    if created:
        print("Сигнал обработан успешно пользователь зарегистрировался")
        age = instance.age
        if age < 3:
            instance.rec = "Вам рекомендуется: Сказки и народные истории"
        elif age >= 5 and age <= 10:
            instance.rec = "Вам рекомендуется: Сказки и народные истории"
        elif age >= 11 and age <= 18:
            instance.rec = "Вам рекомендуется: Научная фантастика, Фэнтези, Романтика и Детективы"
        elif age >= 18 and age <= 45:
            instance.rec = "Вам рекомендуется: Художественная литература, Историческая литература и Философия и эссеистика"
        else:
            instance.rec = "Ничего не могу порекомендовать"
        instance.save()