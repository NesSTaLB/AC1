from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

# مسارات العملاء
customer_urls = [
    path('', views.customer_list, name='customer_list'),
    path('add/', views.add_customer, name='add_customer'),
    path('<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('<int:customer_id>/edit/', views.edit_customer, name='edit_customer'),
    path('<int:customer_id>/delete/', views.delete_customer, name='delete_customer'),
    path('export/excel/', views.export_customers_excel, name='export_customers_excel'),
    path('export/pdf/', views.export_customers_pdf, name='export_customers_pdf'),
]

# مسارات المهندسين
engineer_urls = [
    path('', views.engineer_list, name='engineer_list'),
    path('add/', views.add_engineer, name='add_engineer'),
    path('<int:engineer_id>/', views.engineer_detail, name='engineer_detail'),
    path('<int:engineer_id>/edit/', views.edit_engineer, name='edit_engineer'),
    path('<int:engineer_id>/delete/', views.delete_engineer, name='delete_engineer'),
]

# مسارات الفنيين
technician_urls = [
    path('', views.technician_list, name='technician_list'),
    path('add/', views.add_technician, name='add_technician'),
    path('<int:technician_id>/', views.technician_detail, name='technician_detail'),
    path('<int:technician_id>/edit/', views.edit_technician, name='edit_technician'),
    path('<int:technician_id>/delete/', views.delete_technician, name='delete_technician'),
]

# مسارات المنتجات
product_urls = [
    path('', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('<int:product_id>/delete/', views.delete_product, name='delete_product'),
]

# مسارات المشاريع
project_urls = [
    path('', views.project_list, name='project_list'),
    path('add/', views.add_project, name='add_project'),
    path('<int:project_id>/', views.project_detail, name='project_detail'),
    path('<int:project_id>/edit/', views.edit_project, name='edit_project'),
    path('<int:project_id>/delete/', views.delete_project, name='delete_project'),
]

# مسارات عروض الأسعار
quotation_urls = [
    path('', views.quotation_list, name='quotation_list'),
    path('add/', views.add_quotation, name='add_quotation'),
    path('<int:quotation_id>/', views.quotation_detail, name='quotation_detail'),
    path('<int:quotation_id>/edit/', views.edit_quotation, name='edit_quotation'),
    path('<int:quotation_id>/delete/', views.delete_quotation, name='delete_quotation'),
]

# مسارات مهام الصيانة
maintenance_urls = [
    path('', views.maintenance_task_list, name='maintenance_task_list'),
    path('add/', views.add_maintenance_task, name='add_maintenance_task'),
    path('<int:task_id>/', views.maintenance_task_detail, name='maintenance_task_detail'),
    path('<int:task_id>/edit/', views.edit_maintenance_task, name='edit_maintenance_task'),
    path('<int:task_id>/delete/', views.delete_maintenance_task, name='delete_maintenance_task'),
]

# مسارات الموارد
resource_urls = [
    path('', views.resource_list, name='resource_list'),
    path('add/', views.add_resource, name='add_resource'),
    path('<int:resource_id>/edit/', views.edit_resource, name='edit_resource'),
    path('<int:resource_id>/delete/', views.delete_resource, name='delete_resource'),
]

# مسارات جدولة الصيانة
maintenance_schedule_urls = [
    path('', views.maintenance_schedule_list, name='maintenance_schedule_list'),
    path('add/', views.add_maintenance_schedule, name='add_maintenance_schedule'),
    path('<int:schedule_id>/edit/', views.edit_maintenance_schedule, name='edit_maintenance_schedule'),
    path('<int:schedule_id>/delete/', views.delete_maintenance_schedule, name='delete_maintenance_schedule'),
]

# مسارات التقارير
report_urls = [
    path('create/', views.create_report, name='create_report'),
    path('', views.report_list, name='report_list'),
    path('<int:report_id>/', views.report_detail, name='report_detail'),
]

# مسارات تسجيل الدخول والتسجيل
auth_urls = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]

# المسارات الرئيسية
urlpatterns = [
    path('', views.home, name='home'),
    path('customers/', include(customer_urls)),
    path('engineers/', include(engineer_urls)),
    path('technicians/', include(technician_urls)),
    path('products/', include(product_urls)),
    path('projects/', include(project_urls)),
    path('quotations/', include(quotation_urls)),
    path('maintenance/', include(maintenance_urls)),
    path('resources/', include(resource_urls)),
    path('maintenance-schedules/', include(maintenance_schedule_urls)),
    path('reports/', include(report_urls)),
    path('auth/', include(auth_urls)),
    # مسار التقويم الجديد
    path('calendar/', views.calendar_view, name='calendar_view'),
]

# إضافة مسار لملفات الوسائط (Media) في وضع التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
