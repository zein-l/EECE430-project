
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('home/', views.home, name='home'),  # Home page URL, handling unified task actions.
    path('success/', views.success, name='success'),  
    path('home2', views.home2, name='home2'),# Success page URL.
    path('Manager1/', views.Manager1, name ='Manager1'),
    path('manage_tasks/', views.manage_tasks, name='manage_tasks'),
    path('view_tasks/', views.view_tasks, name='view_tasks'),
    path('update_task/<int:task_id>/', views.update_task, name='update_task'),
    path('update_tasks/', views.update_tasks, name='update_tasks'),
    path('delete_task/', views.delete_task, name='delete_task'),
    path('Manager3/', views.Manager3, name='Manager3'),
    path('delete_employee/', views.delete_employee, name='delete_employee'),
    path('perform_delete_employee/', views.perform_delete_employee, name='perform_delete_employee'),
    path('update_employee/<int:employee_id>/', views.update_employee, name='update_employee'),
    path('list_employee/', views.list_employee, name='list_employee'),
    path('list_tasks/', views.list_tasks, name='list_tasks'),
    path('assign_tasks/', views.assign_tasks, name='assign_tasks'),
    path('post_announcement/', views.post_announcement, name='post_announcement'),
    path('announcements/', views.announcement_list, name='announcement_list'),
    path('assign_employee/<int:task_id>/', views.assign_employee, name='assign_employee'),
    path('view_employee/<int:employee_id>/', views.view_employee, name='view_employee'),
    re_path(r'^index/$', views.index, name='index'),
    re_path(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),  
    re_path(r'^event/new/$', views.event, name='event_new'),
    re_path(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),  
    path('see_announcements/', views.see_announcements, name='see_announcements'),
    path('select_announcement/', views.select_announcement, name='select_announcement'),
    path('page/', views.page, name='page')



    
   
    # other paths


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


