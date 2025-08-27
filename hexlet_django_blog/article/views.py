from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from hexlet_django_blog.article.models import Article
from .forms import CommentArticleForm
from .models import ArticleComment


# def index(request):
#     return HttpResponse("article")

class IndexView(View):
    # template_name = "articles/index.html"
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["name"] = "Article"
    #     return context
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles,
            },
        )

class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(
            request,
            "articles/show.html",
            context={
                "article": article,
            },
        )



# def index(request):
#     return render(
#         request,
#         "articles/index.html",
#         context={
#             "name": "Article",
#         },
#     )

def index(request, tags, article_id):
    url = reverse('article', kwargs={'tags': 'python', 'article_id': 42})
    return redirect(url)

class CommentArticleView(View):
    # если метод POST, то мы обрабатываем данные
    def post(self, request, *args, **kwargs):
        form = CommentArticleForm(request.POST)  # Получаем данные формы из запроса
        if form.is_valid():  # Проверяем данные формы на корректность
            comment = ArticleComment(
                content=form.cleaned_data[
                    "content"
                ],  # Получаем очищенные данные из поля content
            )  #  и создаем новый комментарий
            comment.save()

    # если метод GET, то создаем пустую форму
    def get(self, request, *args, **kwargs):
        form = CommentArticleForm()  # Создаем экземпляр нашей формы
        return render(
            request, "comment.html", {"form": form}
        )  # Передаем нашу форму в контексте