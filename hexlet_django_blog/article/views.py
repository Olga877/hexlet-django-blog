from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from hexlet_django_blog.article.models import Article


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