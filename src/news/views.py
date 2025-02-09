from django.views.generic import ListView, DetailView
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'news/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        # 公開済みの記事のみを取得
        return Article.objects.filter(is_published=True).order_by('-published_at')

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'news/article_detail.html'
    context_object_name = 'article'

    def get_queryset(self):
        # 公開済みの記事のみを取得
        return Article.objects.filter(is_published=True)
