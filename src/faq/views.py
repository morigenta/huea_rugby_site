from django.views.generic import ListView
from .models import Category, FAQ

class FAQListView(ListView):
    template_name = 'faq/faq_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        # カテゴリと、その中の公開されているFAQを取得
        categories = Category.objects.prefetch_related(
            'faqs'
        ).filter(
            faqs__is_published=True
        ).distinct()

        return categories

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # カテゴリごとのFAQを取得
        context['faq_by_category'] = {
            category: category.faqs.filter(is_published=True)
            for category in context['categories']
        }
        return context