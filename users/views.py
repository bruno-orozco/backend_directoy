import json

from django.http.response import JsonResponse
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View


class UsersViews(View):
    """DESCRIPTION: Views for Model Users"""

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        jd = json.loads(request.body)
        user = list(User.objects.create_user(username=jd['username'],
                                             email=jd['email'],
                                             password=jd['password']).values())
        data = {'message': 'Success', 'detail': user}
        return JsonResponse(data)
