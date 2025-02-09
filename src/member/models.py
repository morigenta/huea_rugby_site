from django.db import models

class Member(models.Model):
    GRADE_CHOICES = [
        ('B1', '学部1年'),
        ('B2', '学部2年'),
        ('B3', '学部3年'),
        ('B4', '学部4年'),
        ('M1', '修士1年'),
        ('M2', '修士2年'),
        ('D1', '博士1年'),
        ('D2', '博士2年'),
        ('D3', '博士3年'),
    ]

    name = models.CharField("氏名", max_length=100)
    grade = models.CharField("学年", max_length=2, choices=GRADE_CHOICES)
    major = models.CharField("所属専攻", max_length=100)
    weight = models.IntegerField("体重(kg)")
    motto = models.CharField("座右の銘", max_length=200)
    message = models.TextField("新入生に一言")
    photo = models.ImageField("写真", upload_to='member_photos/%Y/%m/', blank=True, null=True)
    is_active = models.BooleanField("現役部員", default=True)
    created_at = models.DateTimeField("登録日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    class Meta:
        verbose_name = "部員"
        verbose_name_plural = "部員"
        ordering = ['grade', 'name']  # 学年順、名前順で並べる

    def __str__(self):
        return f"{self.get_grade_display()} {self.name}"