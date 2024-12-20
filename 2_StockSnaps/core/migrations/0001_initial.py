# Generated by Django 4.2.16 on 2024-11-21 06:12

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('nickname', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('income_level', models.IntegerField(blank=True, null=True)),
                ('member_number', models.CharField(blank=True, max_length=50, null=True)),
                ('joined_products', models.JSONField(blank=True, default=list, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DepositProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('financial_company_code', models.CharField(max_length=20)),
                ('financial_product_code', models.CharField(max_length=20)),
                ('financial_product_name', models.CharField(max_length=255)),
                ('join_way', models.CharField(blank=True, max_length=100, null=True)),
                ('interest_rate_type', models.CharField(blank=True, max_length=50, null=True)),
                ('interest_rate_type_name', models.CharField(blank=True, max_length=50, null=True)),
                ('basic_interest_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('max_interest_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cur_unit', models.CharField(max_length=10)),
                ('cur_nm', models.CharField(max_length=100)),
                ('ttb', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('tts', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('deal_bas_r', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('bkpr', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('yy_efee_r', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('ten_dd_efee_r', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('kftc_deal_bas_r', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('kftc_bkpr', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinancialInstitution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_code', models.CharField(max_length=20, unique=True)),
                ('institution_name', models.CharField(max_length=255)),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SavingsProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('financial_company_code', models.CharField(max_length=20)),
                ('financial_product_code', models.CharField(max_length=20)),
                ('financial_product_name', models.CharField(max_length=255)),
                ('join_way', models.CharField(blank=True, max_length=100, null=True)),
                ('interest_rate_type', models.CharField(blank=True, max_length=50, null=True)),
                ('interest_rate_type_name', models.CharField(blank=True, max_length=50, null=True)),
                ('basic_interest_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('max_interest_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('maturity_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('stock_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RealAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('value', models.DecimalField(decimal_places=2, max_digits=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='real_assets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('item_id', models.PositiveIntegerField()),
                ('liked_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.stockboard')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.stockboard')),
            ],
        ),
    ]
