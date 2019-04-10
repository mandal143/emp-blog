from django.conf.urls import url

from . import views


urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^employee/$', views.employee, name='employee'),
    url(r'^form/$', views.form, name='form'),
    url(r'^employeeSave/$', views.employeeSave, name='employeeSave'),
    url(r'^employee_del/(.*)/$', views.employee_del, name='employee_del'),
    url(r'^employee_edit/(.*)/$', views.employee_edit, name='employee_edit'),
    url(r'^employee_update/(.*)/$', views.employee_update, name='employee_update'),
    url(r'^calendar/(.*)/$', views.calendar, name='calendar'),
    url(r'^details/(.*)/$', views.details, name='details'),
    url(r'^details_save/$', views.details_save, name='details_save'),
    url(r'^details_display/(.*)/$', views.details_display, name='details_display'),
    url(r'^export/csv/$', views.export_users_csv, name='export_users_csv'),
    url(r'^register/$', views.register, name='register'),
    
    
    url(r'^userLogOut/$', views.userLogOut, name='userLogOut'),
    
    
 
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    
]