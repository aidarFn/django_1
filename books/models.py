from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class BookAge(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=200)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Books(models.Model):

    # PROGRAMMING_STATUS = (
    #     ('Full Stack', 'Full Stack'),
    #     ('Backend Development', 'Backend Development'),
    #     ('Frontend Development', 'Frontend Development'),
    #     ('UX-UI development', 'UX-UI development'),
    # )

    name = models.CharField(max_length=100)
    # email = models.EmailField(default='@gmail.com')
    image = models.ImageField(upload_to="images/")
    about_emp = models.TextField()
    # programming_status = models.CharField(max_length=100, choices=PROGRAMMING_STATUS, null=True)
    # rezume = models.FileField(upload_to='rezume/')
    # date_of_birth = models.DateField()
    # github = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Книгу"
        verbose_name_plural = "Книги"


class ReviewBooks(models.Model):
    reviews_book = models.ForeignKey(
        Books, on_delete=models.CASCADE, related_name="reviews_book"
    )

    text = models.TextField()
    stars = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.stars}-{self.reviews_book}"
