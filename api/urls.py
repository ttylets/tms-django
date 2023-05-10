
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('questions', views.QuestionViewSet, basename='question')
router.register('choices', views.ChoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]