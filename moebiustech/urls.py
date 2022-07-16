from django.contrib import admin
from django.urls import include, path
from api import views
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register('products', views.Product)
router.register('questions', views.Question)
router.register('choices', views.Choice)
router.register('services', views.Service)
#router.register('searches', views.Searche)
#router.register('clients', views.Client)
#router.register('contractors', views.Contractor)
#router.register('productdetails', views.ProductDetails)

urlpatterns = [
    #path('app/', include('app.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]