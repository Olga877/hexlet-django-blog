from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View


# def index(request):
#     return HttpResponse("article")

class IndexView(View):
    template_name = "articles/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Article"
        return context

# def index(request):
#     return render(
#         request,
#         "articles/index.html",
#         context={
#             "name": "Article",
#         },
#     )
