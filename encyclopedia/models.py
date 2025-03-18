from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    image = models.ImageField(upload_to='items/', verbose_name="Изображение", blank=True, null=True)
    video_url = models.URLField(verbose_name="Ссылка на видео", blank=True, null=True)
    three_d_model = models.FileField(upload_to='models/', verbose_name="3D модель", blank=True, null=True)

    def __str__(self):
        return self.name
