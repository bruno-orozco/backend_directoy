import json

from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from restaurants.models import Restaurant


class RestaurantViews(View):
    """DESCRIPTION: Views for Model Restaurant"""

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        """DESCRIPTION: Method GET"""
        if id > 0:
            id_restaurant = list(Restaurant.objects.filter(id=id).values())
            if len(id_restaurant) > 0:
                id_restaurant = id_restaurant[0]
                data = {'message': 'Success',
                        'restaurants': id_restaurant}
            else:
                data = {'message': 'Restaurants not fond ...'}
            return JsonResponse(data)
        else:
            restaurant = list(Restaurant.objects.values())
            if len(restaurant) > 0:
                data = {'message': 'Success',
                        'restaurants': restaurant}
            else:
                data = {'message': 'Restaurants not fond ...'}
            return JsonResponse(data)

    def post(self, request):
        """DESCRIPTION: Method POST"""
        jd = json.loads(request.body)
        Restaurant.objects.create(restaurant_name=jd['restaurant_name'],
                                  restaurant_type=jd['restaurant_type'],
                                  address=jd['address'],
                                  phone_number=jd['phone_number'])
        data = {'message': 'Success'}
        return JsonResponse(data)

    def put(self, request, id):
        """DESCRIPTION: Method PUT"""
        jd = json.loads(request.body)
        id_restaurant = list(Restaurant.objects.filter(id=id).values())
        if len(id_restaurant) > 0:
            restaurant = Restaurant.objects.get(id=id)
            restaurant.restaurant_name = jd['restaurant_name']
            restaurant.restaurant_type = jd['restaurant_type']
            restaurant.address = jd['address']
            restaurant.phone_number = jd['phone_number']
            restaurant.save()
            data = {'message': 'Success'}
        else:
            data = {'message': 'Restaurants not fond ...'}
        return JsonResponse(data)

    def delete(self, request, id):
        """DESCRIPTION: Method DELETE"""
        id_restaurant = list(Restaurant.objects.filter(id=id).values())
        if len(id_restaurant) > 0:
            Restaurant.objects.filter(id=id).delete()
            data = {'message': 'Success'}
        else:
            data = {'message': 'Restaurants not fond ...'}
        return JsonResponse(data)
