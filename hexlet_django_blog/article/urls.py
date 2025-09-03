from django.urls import path

# from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import IndexView, ArticleView, ArticleFormCreateView, ArticleFormEditView

urlpatterns = [
    # path("", views.index),
    path('', IndexView.as_view(), name="articles"),
    path("<int:id>/edit/", ArticleFormEditView.as_view(), name="articles_update"),
    path("<int:id>/", ArticleView.as_view(), name="article"),
    path("create/", ArticleFormCreateView.as_view(), name="articles_create"),
    # path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view()),
    # path('<str:tags>/<int:article_id>/', views.index, name='article'),

]