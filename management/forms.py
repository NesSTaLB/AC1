from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Engineer, Technician, Customer, Product, Project, Quotation, MaintenanceTask, Resource, MaintenanceSchedule, Report

# نموذج تسجيل المستخدم الجديد
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'password1', 'password2', 'role']

# نموذج تسجيل الدخول
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

# نموذج تحديد الأعمدة للتصدير
class ExportColumnsForm(forms.Form):
    columns = forms.MultipleChoiceField(
        choices=[
            ('name', 'اسم المشروع'),
            ('customer__name', 'اسم العميل'),
            ('start_date', 'تاريخ البدء'),
            ('end_date', 'تاريخ الانتهاء'),
            ('status', 'حالة المشروع'),
        ],
        widget=forms.CheckboxSelectMultiple,
        label="اختر الأعمدة للتصدير"
    )

# نماذج أخرى (CustomerForm, EngineerForm, TechnicianForm, ProductForm, ProjectForm, QuotationForm, MaintenanceTaskForm, ResourceForm, MaintenanceScheduleForm, ReportForm)
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email', 'address']
        labels = {
            'name': 'اسم العميل',
            'phone': 'الهاتف',
            'email': 'البريد الإلكتروني',
            'address': 'العنوان',
        }

class EngineerForm(forms.ModelForm):
    class Meta:
        model = Engineer
        fields = ['user', 'specialty', 'phone', 'email']
        labels = {
            'user': 'اسم المهندس',
            'specialty': 'التخصص',
            'phone': 'الهاتف',
            'email': 'البريد الإلكتروني',
        }

class TechnicianForm(forms.ModelForm):
    class Meta:
        model = Technician
        fields = ['user', 'specialty', 'phone', 'email']  # إضافة الحقول الجديدة
        labels = {
            'user': 'المستخدم',
            'specialty': 'التخصص',
            'phone': 'الهاتف',  # تسمية حقل الهاتف
            'email': 'البريد الإلكتروني',  # تسمية حقل البريد الإلكتروني
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']
        labels = {
            'name': 'اسم المنتج',
            'description': 'الوصف',
            'price': 'السعر',
            'quantity': 'الكمية',
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name', 'description', 'start_date', 'end_date', 'customer', 'engineer', 'technician', 'status',
            'foundation_status', 'extension_status', 'internal_units_status', 'air_ducts_status',
            'external_units_status', 'operation_status', 'completion_status',
            'project_file', 'project_image'
        ]
        labels = {
            'name': 'اسم المشروع',
            'description': 'وصف المشروع',
            'start_date': 'تاريخ البدء',
            'end_date': 'تاريخ الانتهاء',
            'customer': 'العميل',
            'engineer': 'مهندس المشروع',
            'technician': 'الفني',
            'status': 'حالة المشروع',
            'foundation_status': 'حالة التأسيس',
            'extension_status': 'حالة التمديد',
            'internal_units_status': 'حالة الوحدات الداخلية',
            'air_ducts_status': 'حالة مجاري الهواء (الدكت)',
            'external_units_status': 'حالة الوحدات الخارجية والجريلات',
            'operation_status': 'حالة التشغيل',
            'completion_status': 'حالة الإكمال',
            'project_file': 'ملف المشروع',
            'project_image': 'صورة المشروع',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = ['customer', 'engineer', 'product', 'date', 'total_amount', 'notes']
        labels = {
            'customer': 'العميل',
            'engineer': 'المهندس',
            'product': 'المنتج',
            'date': 'التاريخ',
            'total_amount': 'المبلغ الإجمالي',
            'notes': 'ملاحظات',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class MaintenanceTaskForm(forms.ModelForm):
    class Meta:
        model = MaintenanceTask
        fields = ['task', 'project', 'technician', 'start_date', 'end_date', 'status', 'maintenance_date', 'notes']
        labels = {
            'task': 'المهمة',
            'project': 'المشروع',
            'technician': 'الفني',
            'start_date': 'تاريخ البدء',
            'end_date': 'تاريخ الانتهاء',
            'status': 'حالة المهمة',
            'maintenance_date': 'تاريخ الصيانة',
            'notes': 'ملاحظات الصيانة',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'maintenance_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'description', 'quantity', 'project', 'task']
        labels = {
            'name': 'اسم المورد',
            'description': 'وصف المورد',
            'quantity': 'الكمية المتاحة',
            'project': 'المشروع',
            'task': 'المهمة',
        }

class MaintenanceScheduleForm(forms.ModelForm):
    class Meta:
        model = MaintenanceSchedule
        fields = ['task', 'project', 'technician', 'start_date', 'end_date', 'frequency']
        labels = {
            'task': 'المهمة',
            'project': 'المشروع',
            'technician': 'الفني',
            'start_date': 'تاريخ البدء',
            'end_date': 'تاريخ الانتهاء',
            'frequency': 'التكرار',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['name', 'filters', 'export_format']
        labels = {
            'name': 'اسم التقرير',
            'filters': 'الفلاتر',
            'export_format': 'صيغة التصدير',
        }
        widgets = {
            'filters': forms.HiddenInput(),
        }
