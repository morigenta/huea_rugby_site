from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("内容")
    created_at = models.DateTimeField("作成日時", default=timezone.now)
    published_at = models.DateTimeField("公開日時", null=True, blank=True)
    is_published = models.BooleanField("公開する", default=False)
    
    class Meta:
        verbose_name = "ニュース記事"
        verbose_name_plural = "ニュース記事"
        ordering = ['-created_at']  # 作成日時の新しい順に並べる
    
    def __str__(self):
        return self.title