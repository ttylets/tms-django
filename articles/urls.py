from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/like', views.like, name='like'),
]

    # path('<int:question_id>/vote', views.vote, name='vote'),
    # path('<int:question_id>/results', views.results, name='results'),