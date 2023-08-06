from django.db.models import Count
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import ArticleCategory, Article, ArticleComments



# Create your views here.


class ArticlesView(ListView):
    template_name = 'article_module/articles_page.html'
    paginate_by = 2

    context_object_name = "article"
    model = Article
    ordering = ['-date_created',]

    def get_context_data(self,*args , **kwargs):
        context = super(ArticlesView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        query = super(ArticlesView,self).get_queryset()
        query = query.filter(is_active=True)
        this_category = self.kwargs.get('category')
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
        comment : ArticleComments = ArticleComments.objects.filter(article_id=article.id,parent=None).order_by('-date_created').prefetch_related("parent_comment")
        context['comments'] = comment
        context['comment_count'] = ArticleComments.objects.annotate(comment_count=Count('article')).filter(article_id=article.id).count()
        return context
def category_components(request):
    main_categories = ArticleCategory.objects.prefetch_related('articlecategory_set').filter(is_active=True,parent = None)
    context = {
        "main_categories" : main_categories
    }
    return render(request, "article_module/components/category_components.html", context)

def add_article_comment(request: HttpRequest):
    if request.user.is_authenticated:
        article_id = request.GET.get('article_id')
        article_comment = request.GET.get('article_comment')
        parent_id = request.GET.get('parent_id')
        new_comment = ArticleComments(article_id=article_id, text=article_comment ,author_id=request.user.id, parent_id=parent_id)
        new_comment.save()

        context = {
            'comments': ArticleComments.objects.filter(article_id=article_id, parent=None).order_by(
                '-date_created'),
            'comments_count': ArticleComments.objects.filter(article_id=article_id).count()
        }
        data = render_to_string('article_module/components/comment_component.html' , context)
        return JsonResponse({
        'status' : 'success' ,
        'response' : data
    })




