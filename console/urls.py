from django.conf.urls import include, url
from rest_framework import routers
from console import views

router = routers.DefaultRouter()
router.register(r'foods', views.FoodViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]