from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class BookRecommendationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            age = int(request.POST.get('age'))
            if age < 3:
                return HttpResponseBadRequest('Вы слишком малы что бы читать')
            elif age >= 3 and age <= 10:
                request.club = ' Вам рекомендуется: Сказки и народные истории '
            elif age >= 11 and age <= 18:
                request.club = 'Вам рекомендуется: Научная фантастика, Фэнтези, Романтика и Детективы  '
            elif age >= 18 and age <= 100:
                request.club = 'Вам рекомендуется: Художественная литература, Историческая литература и Философия и эссеистика'

        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'rec', 'Ничего не могу порекомендовать')
