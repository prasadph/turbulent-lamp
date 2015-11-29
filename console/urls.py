from django.conf.urls import include, url
from rest_framework import routers
from console import views

router = routers.DefaultRouter()
router.register(r'foods', views.FoodViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register(r'order', views.OrderViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]
