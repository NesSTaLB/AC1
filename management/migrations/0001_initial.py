# Generated by Django 5.1.4 on 2025-01-07 15:16

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم العميل')),
                ('phone', models.CharField(max_length=15, verbose_name='الهاتف')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='البريد الإلكتروني')),
                ('address', models.TextField(blank=True, null=True, verbose_name='العنوان')),
            ],
            options={
                'verbose_name': 'عميل',
                'verbose_name_plural': 'العملاء',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم المنتج')),
                ('description', models.TextField(blank=True, null=True, verbose_name='الوصف')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='السعر')),
                ('quantity', models.IntegerField(default=0, verbose_name='الكمية')),
            ],
            options={
                'verbose_name': 'منتج',
                'verbose_name_plural': 'المنتجات',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='الهاتف')),
                ('is_engineer', models.BooleanField(default=False, verbose_name='مهندس')),
                ('is_technician', models.BooleanField(default=False, verbose_name='فني')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'مستخدم',
                'verbose_name_plural': 'المستخدمين',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.CharField(max_length=100, verbose_name='التخصص')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='engineer_profile', to=settings.AUTH_USER_MODEL, verbose_name='المستخدم')),
            ],
            options={
                'verbose_name': 'مهندس',
                'verbose_name_plural': 'المهندسين',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم المشروع')),
                ('description', models.TextField(blank=True, null=True, verbose_name='وصف المشروع')),
                ('start_date', models.DateField(verbose_name='تاريخ البدء')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='تاريخ الانتهاء')),
                ('status', models.CharField(default='قيد التنفيذ', max_length=50, verbose_name='حالة المشروع')),
                ('foundation_status', models.CharField(default='غير مكتمل', max_length=50, verbose_name='حالة التأسيس')),
                ('extension_status', models.CharField(default='غير مكتمل', max_length=50, verbose_name='حالة التمديد')),
                ('internal_units_status', models.CharField(default='غير مكتمل', max_length=50, verbose_name='حالة الوحدات الداخلية')),
                ('air_ducts_status', models.CharField(default='غير مكتمل', max_length=50, verbose_name='حالة مجاري الهواء (الدكت)')),
                ('external_units_status', models.CharField(default='غير مكتمل', max_length=50, verbose_name='حالة الوحدات الخارجية والجريلات')),
                ('operation_status', models.CharField(default='غير مكتمل', max_length=50, verbose_name='حالة التشغيل')),
                ('completion_status', models.CharField(default='غير مكتمل', max_length=50, verbose_name='حالة الإكمال')),
                ('project_file', models.FileField(blank=True, null=True, upload_to='project_files/', verbose_name='ملف المشروع')),
                ('project_image', models.ImageField(blank=True, null=True, upload_to='project_images/', verbose_name='صورة المشروع')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='management.customer', verbose_name='العميل')),
                ('engineer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='management.engineer', verbose_name='مهندس المشروع')),
            ],
            options={
                'verbose_name': 'مشروع',
                'verbose_name_plural': 'المشاريع',
            },
        ),
        migrations.CreateModel(
            name='MaintenanceTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=100, verbose_name='المهمة')),
                ('start_date', models.DateField(verbose_name='تاريخ البدء')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='تاريخ الانتهاء')),
                ('status', models.CharField(default='قيد التنفيذ', max_length=50, verbose_name='حالة المهمة')),
                ('maintenance_date', models.DateField(blank=True, null=True, verbose_name='تاريخ الصيانة')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='ملاحظات الصيانة')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_tasks', to='management.project', verbose_name='المشروع')),
            ],
            options={
                'verbose_name': 'مهمة صيانة',
                'verbose_name_plural': 'مهام الصيانة',
            },
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='التاريخ')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='المبلغ الإجمالي')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='ملاحظات')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotations', to='management.customer', verbose_name='العميل')),
                ('engineer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotations', to='management.engineer', verbose_name='المهندس')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotations', to='management.product', verbose_name='المنتج')),
            ],
            options={
                'verbose_name': 'عرض سعر',
                'verbose_name_plural': 'عروض الأسعار',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم التقرير')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('filters', models.JSONField(blank=True, null=True, verbose_name='الفلاتر')),
                ('export_format', models.CharField(choices=[('pdf', 'PDF'), ('excel', 'Excel'), ('csv', 'CSV')], max_length=10, verbose_name='صيغة التصدير')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to=settings.AUTH_USER_MODEL, verbose_name='تم الإنشاء بواسطة')),
            ],
            options={
                'verbose_name': 'تقرير',
                'verbose_name_plural': 'التقارير',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم المورد')),
                ('description', models.TextField(blank=True, null=True, verbose_name='وصف المورد')),
                ('quantity', models.IntegerField(default=0, verbose_name='الكمية المتاحة')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='management.project', verbose_name='المشروع')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='management.maintenancetask', verbose_name='المهمة')),
            ],
            options={
                'verbose_name': 'مورد',
                'verbose_name_plural': 'الموارد',
            },
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.CharField(max_length=100, verbose_name='التخصص')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='technician_profile', to=settings.AUTH_USER_MODEL, verbose_name='المستخدم')),
            ],
            options={
                'verbose_name': 'فني',
                'verbose_name_plural': 'الفنيين',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='technician',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='management.technician', verbose_name='الفني'),
        ),
        migrations.AddField(
            model_name='maintenancetask',
            name='technician',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_tasks', to='management.technician', verbose_name='الفني'),
        ),
        migrations.CreateModel(
            name='MaintenanceSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=100, verbose_name='المهمة')),
                ('start_date', models.DateField(verbose_name='تاريخ البدء')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='تاريخ الانتهاء')),
                ('frequency', models.CharField(choices=[('daily', 'يومي'), ('weekly', 'أسبوعي'), ('monthly', 'شهري'), ('yearly', 'سنوي')], max_length=50, verbose_name='التكرار')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_schedules', to='management.project', verbose_name='المشروع')),
                ('technician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_schedules', to='management.technician', verbose_name='الفني')),
            ],
            options={
                'verbose_name': 'جدول الصيانة',
                'verbose_name_plural': 'جداول الصيانة',
            },
        ),
    ]
