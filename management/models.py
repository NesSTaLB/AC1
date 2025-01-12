from django.db import models
from django.contrib.auth.models import AbstractUser

# نموذج المستخدم المخصص
class CustomUser(AbstractUser):
    ROLES = [
        ('manager', 'مدير'),
        ('engineer', 'مهندس'),
        ('technician', 'فني'),
    ]
    phone = models.CharField(max_length=15, verbose_name="الهاتف", blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLES, default='technician', verbose_name="الدور")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "مستخدم"
        verbose_name_plural = "المستخدمين"
        permissions = [
            ("can_view_reports", "Can view reports"),
            ("can_export_reports", "Can export reports"),
            ("can_manage_users", "Can manage users"),
        ]

# نموذج المهندس
class Engineer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name="المستخدم", related_name="engineer_profile")
    specialty = models.CharField(max_length=100, verbose_name="التخصص")
    phone = models.CharField(max_length=15, verbose_name="الهاتف", blank=True, null=True)
    email = models.EmailField(verbose_name="البريد الإلكتروني", blank=True, null=True)

    def __str__(self):
        return self.user.username  # عرض اسم المستخدم (المهندس)

    class Meta:
        verbose_name = "مهندس"
        verbose_name_plural = "المهندسين"

# نموذج الفني
class Technician(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name="المستخدم", related_name="technician_profile")
    specialty = models.CharField(max_length=100, verbose_name="التخصص")
    phone = models.CharField(max_length=15, verbose_name="الهاتف", blank=True, null=True)  # إضافة حقل الهاتف
    email = models.EmailField(verbose_name="البريد الإلكتروني", blank=True, null=True)  # إضافة حقل البريد الإلكتروني

    def __str__(self):
        return self.user.username  # عرض اسم المستخدم (الفني)

    class Meta:
        verbose_name = "فني"
        verbose_name_plural = "الفنيين"

# نموذج العميل
class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم العميل")
    phone = models.CharField(max_length=15, verbose_name="الهاتف")
    email = models.EmailField(verbose_name="البريد الإلكتروني", blank=True, null=True)
    address = models.TextField(verbose_name="العنوان", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "عميل"
        verbose_name_plural = "العملاء"

# نموذج المنتج
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم المنتج")
    description = models.TextField(verbose_name="الوصف", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    quantity = models.IntegerField(verbose_name="الكمية", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

# نموذج المشروع
class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم المشروع")
    description = models.TextField(verbose_name="وصف المشروع", blank=True, null=True)
    start_date = models.DateField(verbose_name="تاريخ البدء")
    end_date = models.DateField(verbose_name="تاريخ الانتهاء", blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="العميل", related_name="projects")
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE, verbose_name="مهندس المشروع", related_name="projects")
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, verbose_name="الفني", related_name="projects")
    status = models.CharField(max_length=50, verbose_name="حالة المشروع", default="قيد التنفيذ")
    foundation_status = models.CharField(max_length=50, verbose_name="حالة التأسيس", default="غير مكتمل")
    extension_status = models.CharField(max_length=50, verbose_name="حالة التمديد", default="غير مكتمل")
    internal_units_status = models.CharField(max_length=50, verbose_name="حالة الوحدات الداخلية", default="غير مكتمل")
    air_ducts_status = models.CharField(max_length=50, verbose_name="حالة مجاري الهواء (الدكت)", default="غير مكتمل")
    external_units_status = models.CharField(max_length=50, verbose_name="حالة الوحدات الخارجية والجريلات", default="غير مكتمل")
    operation_status = models.CharField(max_length=50, verbose_name="حالة التشغيل", default="غير مكتمل")
    completion_status = models.CharField(max_length=50, verbose_name="حالة الإكمال", default="غير مكتمل")
    project_file = models.FileField(upload_to='project_files/', verbose_name="ملف المشروع", blank=True, null=True)
    project_image = models.ImageField(upload_to='project_images/', verbose_name="صورة المشروع", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "مشروع"
        verbose_name_plural = "المشاريع"

# نموذج عرض السعر
class Quotation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="العميل", related_name="quotations")
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE, verbose_name="المهندس", related_name="quotations")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="المنتج", related_name="quotations")
    date = models.DateField(verbose_name="التاريخ")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ الإجمالي")
    notes = models.TextField(verbose_name="ملاحظات", blank=True, null=True)

    def __str__(self):
        return f"عرض سعر #{self.id} - {self.customer.name}"

    class Meta:
        verbose_name = "عرض سعر"
        verbose_name_plural = "عروض الأسعار"

# نموذج مهمة الصيانة
class MaintenanceTask(models.Model):
    task = models.CharField(max_length=100, verbose_name="المهمة")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="المشروع", related_name="maintenance_tasks")
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, verbose_name="الفني", related_name="maintenance_tasks")
    start_date = models.DateField(verbose_name="تاريخ البدء")
    end_date = models.DateField(verbose_name="تاريخ الانتهاء", blank=True, null=True)
    status = models.CharField(max_length=50, verbose_name="حالة المهمة", default="قيد التنفيذ")
    maintenance_date = models.DateField(verbose_name="تاريخ الصيانة", blank=True, null=True)
    notes = models.TextField(verbose_name="ملاحظات الصيانة", blank=True, null=True)

    def __str__(self):
        return self.task

    class Meta:
        verbose_name = "مهمة صيانة"
        verbose_name_plural = "مهام الصيانة"

# نموذج المورد
class Resource(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم المورد")
    description = models.TextField(verbose_name="وصف المورد", blank=True, null=True)
    quantity = models.IntegerField(verbose_name="الكمية المتاحة", default=0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="المشروع", related_name="resources", blank=True, null=True)
    task = models.ForeignKey(MaintenanceTask, on_delete=models.CASCADE, verbose_name="المهمة", related_name="resources", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "مورد"
        verbose_name_plural = "الموارد"

# نموذج جدول الصيانة
class MaintenanceSchedule(models.Model):
    task = models.CharField(max_length=100, verbose_name="المهمة")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="المشروع", related_name="maintenance_schedules")
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, verbose_name="الفني", related_name="maintenance_schedules")
    start_date = models.DateField(verbose_name="تاريخ البدء")
    end_date = models.DateField(verbose_name="تاريخ الانتهاء", blank=True, null=True)
    frequency = models.CharField(max_length=50, verbose_name="التكرار", choices=[
        ('daily', 'يومي'),
        ('weekly', 'أسبوعي'),
        ('monthly', 'شهري'),
        ('yearly', 'سنوي'),
    ])

    def __str__(self):
        return self.task

    class Meta:
        verbose_name = "جدول الصيانة"
        verbose_name_plural = "جداول الصيانة"

# نموذج التقرير
class Report(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم التقرير")
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="تم الإنشاء بواسطة", related_name="reports")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    filters = models.JSONField(verbose_name="الفلاتر", blank=True, null=True)
    export_format = models.CharField(max_length=10, choices=[('pdf', 'PDF'), ('excel', 'Excel'), ('csv', 'CSV')], verbose_name="صيغة التصدير")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "تقرير"
        verbose_name_plural = "التقارير"
