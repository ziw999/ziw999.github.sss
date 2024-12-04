from django.db import models






class Index(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название магазина')

    class Meta:
        verbose_name='название'
        verbose_name_plural='Название'
   
    def __str__(self):
        return self.name
    
    

class About(models.Model):
    content=models.CharField(max_length=50, verbose_name='Тема:')
    article=models.TextField(verbose_name='Информация:')
    
    class Meta:
        verbose_name='Информацию'
        verbose_name_plural='Информация'
   
    def __str__(self):
        return self.content
    
    
class Contact(models.Model):
    address=models.CharField(max_length=250, verbose_name='Адрес:')
    phone=models.CharField(max_length=20, verbose_name='Телефон:')
    email=models.EmailField(max_length=30, verbose_name='E-mail:')
    
    class Meta:
        verbose_name='Контакт'
        verbose_name_plural='Контакты'
   
    def __str__(self):
        return self.address
    
    
class Delivery(models.Model):
    content=models.CharField(max_length=50, verbose_name='Тема:')
    article=models.TextField(verbose_name='Информация:')
    
    class Meta:
        verbose_name='оплату и услугу сервиса'
        verbose_name_plural='Оплата и услуги сервиса'
   
    def __str__(self):
        return self.content
    

class Stocks(models.Model):
    title=models.CharField(max_length=50, verbose_name='Тема:')
    article=models.TextField(verbose_name='Информация:')
    
    class Meta:
        verbose_name='акцию'
        verbose_name_plural='Акции'
   
    def __str__(self):
        return self.title
    

class Offer(models.Model):
    title=models.CharField(max_length=50, verbose_name='Тема:')
    article=models.TextField(verbose_name='Информация:')
    
    class Meta:
        verbose_name='офферту'
        verbose_name_plural='Офферты'
   
    def __str__(self):
        return self.title
    

class Confidentiality(models.Model):
    title=models.CharField(max_length=50, verbose_name='Тема:')
    article=models.TextField(verbose_name='Информация:')
    
    class Meta:
        verbose_name='политику конфеденциальности'
        verbose_name_plural='Политика конфеденциальности'
   
    def __str__(self):
        return self.title
    

class News(models.Model):
    title=models.CharField(max_length=50, verbose_name='Тема:')
    article=models.TextField(verbose_name='Информация:')
    
    class Meta:
        verbose_name='новость'
        verbose_name_plural='новости'
   
    def __str__(self):
        return self.title
    

class Interesting(models.Model):
    title=models.CharField(max_length=50, verbose_name='Тема:')
    article=models.TextField(verbose_name='Информация:')
    
    class Meta:
        verbose_name='интересный факт'
        verbose_name_plural='Интересные факты'
   
    def __str__(self):
        return self.title
