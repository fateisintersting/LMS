from django.urls import path
from  . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,  name='home'),
    path('create-class/', views.create_class_view, name='create_class'),
    path('class/<uuid:unique_id>/', views.class_detail_view, name='class_detail'),
    path('edit/class/list/' , views.editclasslist, name='listofclass'),
     path('classes/', views.class_list, name='class_list'),
    path('join/<int:class_id>/', views.join_class, name='join_class'),
    path('class_content/<int:class_id>/', views.class_content, name='class_content'),
    path('class/<str:unique_id>/members/', views.class_members_view, name='class_members'),
    path('start-content/<int:content_id>/', views.start_content_view, name='start_content_view'),
    path('end-content/<int:content_id>/', views.end_content_view, name='end_content_view'),
    path('mark-as-read/<int:content_id>/', views.mark_as_read, name='mark_as_read'),
     path('member_progress/<int:studentid>/', views.member_progress, name='member_progress'),
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

