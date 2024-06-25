from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


class CustomUser(User):

    GENDER = (("Male", "Male"), ("Female", "Female"), ("Other", "Other"), ("Secret", "Secret"))

    phone_number = models.CharField(max_length=14, default="+996")
    age = models.PositiveIntegerField(
        default=18, validators=[MaxValueValidator(100), MinValueValidator(3)]
    )
    gender = models.CharField(max_length=100, choices=GENDER)
    birth_date = models.DateField(null=True, blank=True)
    country = CountryField(blank_label='(select country)')
    rec = models.CharField(max_length=50, default="Ничего не могу порекомендовать")


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

