from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Country(models.Model):
    '''Страна'''
    name = models.CharField('Страна', max_length=30, unique=True)
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Hotel_type(models.Model):
    '''Тип Отеля'''
    name = models.CharField('Тип отеля', max_length=30, unique= True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип отеля'
        verbose_name_plural = 'Типы отеля'


class Food_type(models.Model):
    '''Тип Питания'''
    name = models.CharField('Тип питания', max_length=30, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип питания'
        verbose_name_plural = 'Типы питания'


class Beach_type(models.Model):
    '''Тип пляжа'''
    name = models.CharField('Тип пляжа', max_length=30, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип пляжа'
        verbose_name_plural = 'Типы пляжей'


class Hotel(models.Model):
    '''Отель'''
    name = models.CharField('Название', max_length=160, unique=True)
    country = models.ForeignKey(Country, verbose_name='Страна', null=True, on_delete=models.SET_NULL)
    hotel_type = models.ForeignKey(Hotel_type, verbose_name='Тип отеля', null=True, on_delete=models.SET_NULL)
    food_type = models.ForeignKey(Food_type, verbose_name='Тип питания', null=True, on_delete=models.SET_NULL)
    beach_type = models.ForeignKey(Beach_type, verbose_name='Тип пляжа', null=True, on_delete=models.SET_NULL)
    price = models.PositiveIntegerField('Стоимость проживания', help_text='Цена указывается за сутки')
    description = models.TextField('Описание')
    poster = models.ImageField('Главное фото', upload_to='hotel_posters/')
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('hotel_detail', kwargs={'slug': self.url})

    def get_absolut_url_order(self):
        return reverse('order', kwargs={'slug': self.url})


    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'


class Food_in_hotel(models.Model):
    '''Питание в отеле'''
    hotel = models.ForeignKey(Hotel, verbose_name='Отель', on_delete=models.CASCADE)
    food_type = models.ForeignKey(Food_type, verbose_name='Тип питания', on_delete=models.CASCADE)
    price = models.PositiveIntegerField('Стоимость питания', )

    def __str__(self):
        return f'{self.hotel} - {self.food_type}'

    class Meta:
        verbose_name = 'Питание в отеле'
        verbose_name_plural = 'Питание в отелях'


class Services(models.Model):
    '''Услуги'''
    hotel = models.OneToOneField(Hotel, verbose_name='Отель', on_delete=models.CASCADE, primary_key=True)
    wifi = models.BooleanField('Wi-fi', default=False)
    conditioner = models.BooleanField('Кондиционер в номере', default=False)
    swimming_pool = models.BooleanField('Бассейн', default=False)
    waterslides = models.BooleanField('Водные горки', default=False)
    spa = models.BooleanField('SPA-центр', default=False)
    gym = models.BooleanField('Спортзал', default=False)
    disco = models.BooleanField('Дискотека', default=False)
    car_rental = models.BooleanField('Прокат авто', default=False)

    def __str__(self):
        return str(self.hotel)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Hotel_photos(models.Model):
    '''Фотографии отеля'''
    hotel = models.ForeignKey(Hotel, verbose_name='Отель', on_delete=models.CASCADE)
    photo = models.ImageField('Фотография', upload_to='hotel_photos/')

    def __str__(self):
        return f'{self.hotel} - {self.photo}'

    class Meta:
        verbose_name = 'Фотография отеля'
        verbose_name_plural = 'Фотографии отеля'


class Reviews(models.Model):
    '''Отзывы'''
    hotel = models.ForeignKey(Hotel, verbose_name='Отель', on_delete=models.CASCADE)
    name = models.CharField('ФИО', default='Аноним', max_length=150)
    email = models.EmailField('E-mail', default='example@inbox.ru')
    text = models.TextField('Текст отзыва', max_length=5000)

    def __str__(self):
        return f'{self.hotel} - {self.email}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Orders(models.Model):
    '''Заказы'''
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    email = models.EmailField('E-mail')
    phone_number = models.CharField('Номер телефона', max_length=12)
    hotel = models.ForeignKey(Hotel, verbose_name='Отель', on_delete=models.CASCADE)
    food_type = models.ForeignKey(Food_type, verbose_name='Тип питания', on_delete=models.SET_NULL, null=True)
    days_number = models.PositiveIntegerField('Количество дней')
    persons_number = models.PositiveIntegerField('Количество человек')
    departure_date = models.DateField('Дата вылета', default=date.today)
    price = models.PositiveIntegerField('Стоимость')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.hotel}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
