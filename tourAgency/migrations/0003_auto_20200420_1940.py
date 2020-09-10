# Generated by Django 3.0.5 on 2020-04-20 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourAgency', '0002_auto_20200417_2207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beach_type',
            options={'verbose_name': 'Тип пляжа', 'verbose_name_plural': 'Типы пляжей'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Страна', 'verbose_name_plural': 'Страны'},
        ),
        migrations.AlterModelOptions(
            name='food_in_hotel',
            options={'verbose_name': 'Питание в отеле', 'verbose_name_plural': 'Питание в отелях'},
        ),
        migrations.AlterModelOptions(
            name='food_type',
            options={'verbose_name': 'Тип питания', 'verbose_name_plural': 'Типы питания'},
        ),
        migrations.AlterModelOptions(
            name='hotel',
            options={'verbose_name': 'Отель', 'verbose_name_plural': 'Отели'},
        ),
        migrations.AlterModelOptions(
            name='hotel_photos',
            options={'verbose_name': 'Фотография отеля', 'verbose_name_plural': 'Фотографии отеля'},
        ),
        migrations.AlterModelOptions(
            name='hotel_type',
            options={'verbose_name': 'Тип отеля', 'verbose_name_plural': 'Типы отеля'},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AddField(
            model_name='orders',
            name='price',
            field=models.PositiveIntegerField(default=1000, verbose_name='Стоимость'),
            preserve_default=False,
        ),
    ]