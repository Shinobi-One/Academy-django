from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import ArticleCategory, Article, ArticleComments


# Create your views here.


class ArticlesView(ListView):
    template_name = 'article_module/articles_page.html'
    paginate_by = 5
    context_object_name = "article"
    model = Article

    def get_context_data(self,*args , **kwargs):
        data = super(ArticlesView, self).get_context_data(*args , **kwargs)
        return data

    def get_queryset(self):
        query = super(ArticlesView,self).get_queryset()
        query = query.filter(is_active=True)
        this_category = self.kwargs.get('category')
        print(self.kwargs)
        if this_category is not None :
            query = query.filter(selected_categories__url__iexact=this_category)

        return query


class ArticleDetailView(DetailView):
    template_name = "article_module/article-detail.html"
    context_object_name = 'article'
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView,self).get_context_data(**kwargs)
        article = kwargs.get('object')
        comment : ArticleComments = ArticleComments.objects.filter(article_id=article.id,parent=None).prefetch_related("parent_comment")

        context['comments'] = comment
        return context
def category_components(request):
    main_categories = ArticleCategory.objects.filter(is_active=True,parent = None)
    context = {
        "main_categories" : main_categories
    }
    return render(request, "article_module/components/category_components.html", context)