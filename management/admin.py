from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Engineer, Technician, Customer, Product, Project, Quotation, MaintenanceTask, Resource, MaintenanceSchedule, Report

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'role', 'is_staff')
    list_filter = ('role', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('معلومات الشخصية', {'fields': ('email', 'phone', 'role')}),
        ('الصلاحيات', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('تواريخ مهمة', {'fields': ('last_login', 'date_joined')}),
    )
    search_fields = ('username', 'email', 'phone')

@admin.register(Engineer)
class EngineerAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'specialty', 'phone', 'email')
    search_fields = ('user__username', 'specialty', 'phone', 'email')

    def get_username(self, obj):
        return obj.user.username  # عرض اسم المستخدم (المهندس)
    get_username.short_description = 'اسم المهندس'  # عنوان العمود في لوحة الإدارة

@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'specialty', 'phone', 'email')  # إضافة الهاتف والبريد الإلكتروني
    search_fields = ('user__username', 'specialty', 'phone', 'email')  # إضافة الهاتف والبريد الإلكتروني للبحث

    def get_username(self, obj):
        return obj.user.username  # عرض اسم المستخدم (الفني)
    get_username.short_description = 'اسم الفني'  # عنوان العمود في لوحة الإدارة

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address')
    search_fields = ('name', 'phone', 'email')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    search_fields = ('name', 'description')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'customer', 'engineer', 'technician', 'status')
    search_fields = ('name', 'customer__name', 'engineer__user__username', 'technician__user__username')

@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'engineer', 'product', 'date', 'total_amount')
    search_fields = ('customer__name', 'engineer__user__username', 'product__name')

@admin.register(MaintenanceTask)
class MaintenanceTaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'project', 'technician', 'status', 'maintenance_date')
    search_fields = ('task', 'project__name', 'technician__user__username')

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'quantity', 'project', 'task')
    search_fields = ('name', 'description')

@admin.register(MaintenanceSchedule)
class MaintenanceScheduleAdmin(admin.ModelAdmin):
    list_display = ('task', 'project', 'technician', 'start_date', 'end_date', 'frequency')
    search_fields = ('task', 'project__name', 'technician__user__username')

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at', 'export_format')
    search_fields = ('name', 'created_by__username')
