from django.db import models
from django.contrib import admin
from django.utils import timezone, html
from django.utils.html import format_html
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Advertisement(models.Model): # это класс-модель 
    # он реализует таблицу Advertisment
    title = models.CharField("заголовок", max_length=128)
    text = models.TextField("описание")
    price = models.FloatField("цена")
    auction = models.BooleanField("торг", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    image = models.ImageField("изображение", upload_to='media/', default='static/img/adv.png') 

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "advertisements"
       
    def __str__(self) -> str:
        return f"Advertisements(id = {self.id}, title = {self.title}, price = {self.price})"

    @admin.display(description="Дата создания")
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            create_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color:green; font-weight: bold;">Сегодня в {}</span>', create_time
            )
        return self.created_at.strftime('%d.%m.%y at %H:%M:%S')
        

    @admin.display(description="Дата обновления")
    def update_date(self):
        if self.update_at.date() == timezone.now().date():
            update_time = self.update_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color:purple; font-weight: bold;">Сегодня в {}</span>', update_time
            )
        return self.update_at.strftime('%d.%m.%y at %H:%M:%S')
    
