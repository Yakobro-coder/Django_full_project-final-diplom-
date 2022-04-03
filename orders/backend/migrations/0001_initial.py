# Generated by Django 3.2.9 on 2022-04-03 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Параметр')),
            ],
            options={
                'verbose_name': 'Параметр',
                'verbose_name_plural': 'Параметры',
                'db_table': 'parameters',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название товара')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='backend.categories', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Список продуктов',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Электронный адрес')),
                ('type', models.CharField(choices=[('shop', 'Магазин'), ('buyer', 'Покупатель')], default='buyer', max_length=10, verbose_name='Тип пользователя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, max_length=50, verbose_name='Отчество')),
                ('company', models.CharField(blank=True, max_length=50, verbose_name='Компания')),
                ('position', models.CharField(blank=True, max_length=50, verbose_name='Должность')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Список пользователей',
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название магазина')),
                ('url_shop', models.CharField(blank=True, max_length=50)),
                ('status_work', models.BooleanField(default=True, verbose_name='Статус приёма заказов')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend.users', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
                'db_table': 'shops',
            },
        ),
        migrations.CreateModel(
            name='ProductsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('price_rrc', models.PositiveIntegerField(verbose_name='Рекомендуемая розничная цена')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.products', verbose_name='Товар')),
                ('shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.shops', verbose_name='Магазины')),
            ],
            options={
                'verbose_name': 'Информация о продукте',
                'db_table': 'products_info',
            },
        ),
        migrations.CreateModel(
            name='ProductParameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100, verbose_name='Значение параметра')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.parameters', verbose_name='Параметр')),
                ('product_info_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.productsinfo', verbose_name='Информация о продукте')),
            ],
            options={
                'verbose_name': 'Параметры продукта',
                'db_table': 'product_parameter',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=30, verbose_name='Статус')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='backend.users', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='backend.orders', verbose_name='Заказ')),
                ('product_info_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_product_info', to='backend.productsinfo', verbose_name='Информация о продукте')),
            ],
            options={
                'verbose_name': 'Заказанный товар',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('build', models.CharField(max_length=100, verbose_name='Дом')),
                ('corpus', models.CharField(blank=True, max_length=100, verbose_name='Корпус')),
                ('apartment', models.CharField(blank=True, max_length=100, verbose_name='Квартира')),
                ('phone', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='backend.users', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Контактные данные',
                'verbose_name_plural': 'Контактные данные',
                'db_table': 'contacts',
            },
        ),
        migrations.AddField(
            model_name='categories',
            name='shop',
            field=models.ManyToManyField(related_name='categories', to='backend.Shops', verbose_name='Магазины'),
        ),
        migrations.AddConstraint(
            model_name='productparameter',
            constraint=models.UniqueConstraint(fields=('product_info_id', 'parameter'), name='unique_product_parameter'),
        ),
    ]
