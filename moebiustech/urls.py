from django.contrib import admin
from django.urls import include, path
from api import views
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register("products", views.ProductViewSet)
router.register("questions", views.QuestionViewSet)
router.register("choices", views.ChoiceViewSet)
router.register("searches", views.SearcheViewSet)
router.register("contractors", views.ContractorViewSet)
router.register("results", views.ResultViewSet)
# router.register('clients', views.Client)
# router.register('contractors', views.Contractor)

urlpatterns = [
    # path('app/', include('app.urls')),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
