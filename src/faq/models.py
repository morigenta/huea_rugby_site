from django.db import models

class Category(models.Model):
    name = models.CharField("カテゴリ名", max_length=100)
    order = models.IntegerField("表示順", default=0)

    class Meta:
        verbose_name = "FAQカテゴリ"
        verbose_name_plural = "FAQカテゴリ"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

class FAQ(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name="カテゴリ",
        on_delete=models.PROTECT,
        related_name='faqs'
    )
    question = models.CharField("Q.", max_length=200)
    answer = models.TextField("A.")
    is_published = models.BooleanField("公開する", default=True)
    order = models.IntegerField("表示順", default=0)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"
        ordering = ['category', 'order', 'created_at']

    def __str__(self):
        return self.question