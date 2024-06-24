from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
import random
from . import models, forms
from django.shortcuts import render, get_object_or_404
from django.views import generic


class SearchView(generic.ListView):
    template_name = "books/books_list.html"
    context_object_name = "emp"
    paginate_by = 5

    def get_queryset(self):
        return models.Books.objects.filter(
            name__icontains=self.request.GET.get("q")
        ).order_by("-id")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context


class EditBookView(generic.UpdateView):
    template_name = "books/edit_book.html"
    form_class = forms.BookForm
    success_url = "/books/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=book_id)


# def edit_book_view(request,id):
#     book_id = get_object_or_404(models.Books, id=id)
#     if request.method == 'POST':
#         form = forms.BookForm(request.POST, instance=book_id)
#         form.save()
#         return HttpResponse('<h3>Employee update successfully!</h3>'
#                             '<a href="/books/">Список книг</a>')
#     else:
#         form = forms.BookForm(instance=book_id)
#     return render(
#         request,
#         template_name='books/edit_book.html',
#         context={
#             'form': form,
#             'book': book_id,
#         }
#     )
#


class DeleteBookView(generic.DeleteView):
    template_name = "books/delete_book.html"
    success_url = "/books/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=book_id)


# def drop_book_view(request, id):
#     book_id = get_object_or_404(models.Books, id=id)
#     book_id.delete()
#     return HttpResponse('<h3>Book delete successfully!</h3>'
#                         '<a href="/books/">Список книг</a>')


class CreateBookView(generic.CreateView):
    template_name = "books/create_book.html"
    form_class = forms.BookForm
    success_url = "/books/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBookView, self).form_valid(form=form)


# def create_book_view(request):
#     if request.method == 'POST':
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h3>Book created successfully!</h3>'
#                                 '<a href="/books/">Список книг</a>')
#
#     else:
#         form = forms.BookForm()
#
#     return render(
#         request,
#         template_name='books/create_book.html',
#         context={'form': form}
#
#     )


class BookListView(generic.ListView):
    template_name = "books/books_list.html"
    context_object_name = "emp"
    model = models.Books

    def get_queryset(self):
        return self.model.objects.filter().order_by("-id")


class BookDetailView(generic.DetailView):
    template_name = "books/books_detail.html"
    context_object_name = "emp_id"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=book_id)


def horror_tags_view(request):
    if request.method == "GET":
        horror_tags = models.BookAge.objects.filter(tags__name="Horror").order_by("-id")
        return render(
            request,
            template_name="all_genre/horror_tags.html",
            context={"horror_tags": horror_tags},
        )


def fantasy_tags_view(request):
    if request.method == "GET":
        fantasy_tags = models.BookAge.objects.filter(tags__name="Fantasy").order_by(
            "-id"
        )
        return render(
            request,
            template_name="all_genre/fantasy_tags.html",
            context={"fantasy_tags": fantasy_tags},
        )


def romance_tags_view(request):
    if request.method == "GET":
        romance_tags = models.BookAge.objects.filter(tags__name="Romance").order_by(
            "-id"
        )
        return render(
            request,
            template_name="all_genre/romance_tags.html",
            context={"romance_tags": romance_tags},
        )


def drama_tags_view(request):
    if request.method == "GET":
        drama_tags = models.BookAge.objects.filter(tags__name="Drama").order_by("-id")
        return render(
            request,
            template_name="all_genre/drama_tags.html",
            context={"drama_tags": drama_tags},
        )


def comedy_tags_view(request):
    if request.method == "GET":
        comedy_tags = models.BookAge.objects.filter(tags__name="Comedy").order_by("-id")
        return render(
            request,
            template_name="all_genre/comedy_tags.html",
            context={"comedy_tags": comedy_tags},
        )


def all_genre(request):
    if request.method == "GET":
        genre = models.BookAge.objects.filter().order_by("-id")
        return render(
            request, template_name="all_genre/all_books.html", context={"genre": genre}
        )


# def books_detail_view(request, id):
#     if request.method == "GET":
#         emp_id = get_object_or_404(models.Books, id=id)
#         return render(
#             request,
#             template_name='books/books_detail.html',
#             context={
#                 'emp_id': emp_id,
#             }
#         )


# def books_list(request):
#     if request.method == 'GET':
#         queryset = models.Books.objects.filter().order_by('-id')
#         return render(
#             request,
#             template_name='books/books_list.html',
#             context={
#                 'emp': queryset
#             }
#         )


def name_view(request):
    if request.method == "GET":
        return HttpResponse("Айдар Догтурбеков, 18 лет")


def hobby_view(request):
    if request.method == "GET":
        return HttpResponse("Играть в игры")


def times_view(request):
    if request.method == "GET":
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse(f"Текущее время: {current_time}")


def random_view(request):
    if request.method == "GET":
        numbers = random.randint(1, 100)
        return HttpResponse(f"Число: {numbers}")
