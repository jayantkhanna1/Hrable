
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
     path('', views.index,name='index'),
     path('index', views.index,name='index'),
     path("applytojob", views.applytojob, name="applytojob"),
     path('openjoblisting',views.openjoblisting,name="openjoblisting"),
     path('applytojob/<str:jobid>/',views.applytojob,name="applytojob"),
     path('applytojob/<str:jobid>/applytojob_form',views.applytojob_form,name="applytojob_form"),
     path('login_employee',views.login_employee,name='login_employee'),
     path('login_employee_user',views.login_employee_user,name='login_employee_user'),
     path("employee_dashboard/<str:member>/", views.employee_dashboard, name="employee_dashboard"),
     path("employee_dashboard/<str:member>/newrefferal", views.newrefferal, name="newrefferal"),
     path("employee_dashboard/<str:member>/recruitment", views.employee_recruitment, name="employee_recruitment"),
     path("employee_dashboard/<str:member>/openjob_emp", views.openjob_emp, name="openjob_emp"),
     path("employee_dashboard/<str:member>/openjobhtml_emp/<str:jobid>/", views.openjobhtml_emp, name="openjobhtml_emp"),
     path('back_employee',views.employee_dashboard,name='back_employee'),
     path("employee_dashboard/<str:member>/back_employee", views.employee_dashboard, name="back_employee"),
     path("employee_dashboard/<str:member>/openjobhtml_emp/<str:jobid>/refer", views.newrefferal, name="refer"),
     path("employee_dashboard/<str:member>/reports", views.reports, name="reports"),
     path("employee_dashboard/<str:member>/openqueryemp", views.openqueryemp, name="openqueryemp"),
     path("employee_dashboard/<str:member>/employee_openqueryhtml/emp_queryedit", views.emp_queryedit, name="emp_queryedit"),
     path("employee_dashboard/<str:member>/employee_openqueryhtml/<str:queryid>", views.employee_openqueryhtml, name="employee_openqueryhtml"),
     path("employee_dashboard/<str:member>/newquery", views.newquery, name="newquery"),
     path("employee_dashboard/<str:member>/emp_newquerycreate", views.emp_newquerycreate, name="emp_newquerycreate"),
     
     path('login_admin',views.login_admin,name='login_admin'),
     path('login_admin_user',views.login_admin_user,name='login_admin_user'),
     path("admin_dashboard/<str:member>/", views.admin_dashboard, name="admin_dashboard"),


     path('login',views.login_hr,name='login_hr'),
     path('home',views.home,name='home'),
     
     path('back_hr',views.hr_dashboard,name='back_hr'),
     path('login_hr_user',views.login_hr_user,name='login_hr_user'),
     path("hr_dashboard/<str:member>/", views.hr_dashboard, name="hr_dashboard"),
     path("hr_dashboard/<str:member>/back_hr", views.hr_dashboard, name="hr_dashboard"),
     path("hr_dashboard/<str:member>/recruitment", views.recruitment, name="recruitment"),
     path("hr_dashboard/<str:member>/newjob", views.newjobhtml, name="newjob"),
     path("hr_dashboard/<str:member>/openjob", views.openjob, name="openjob"),
     path("hr_dashboard/<str:member>/openjobhtml/<str:jobid>/", views.openjobhtml, name="openjobhtml"),
     path("hr_dashboard/<str:member>/openjobhtml/<str:jobid>/editjob", views.editjob, name="editjob"),
     path("hr_dashboard/<str:member>/openjobhtml/<str:jobid>/deletejob", views.deletejob, name="deletejob"),
     path("hr_dashboard/<str:member>/new_job", views.newjob, name="hr_dashboard"),
     path("hr_dashboard/<str:member>/acceptApplication", views.acceptApplication, name="acceptApplication"),
     path("hr_dashboard/<str:member>/rejectApplication", views.rejectApplication, name="rejectApplication"),
     path("hr_dashboard/<str:member>/onboarding", views.onboarding, name="onboarding"),
     path("hr_dashboard/<str:member>/onboardinghtml", views.onboardinghtml, name="onboardinghtml"),
     path("hr_dashboard/<str:member>/job_applications", views.job_applications, name="job_applications"),
     path("hr_dashboard/<str:member>/employee_info", views.employee_info, name="employee_info"),
     path("hr_dashboard/<str:member>/openemployeeinfo", views.openemployeeinfo, name="openemployeeinfo"),
     path("hr_dashboard/<str:member>/openemployeeinfohtml/editemployeeinfo", views.editemployeeinfo, name="editemployeeinfo"),
     path("hr_dashboard/<str:member>/newemployee", views.newemployee, name="newemployee"),
     path("hr_dashboard/<str:member>/addemployee", views.addemployee, name="addemployee"),
     path("hr_dashboard/<str:member>/openemployeeinfohtml/back_hr", views.hr_dashboard, name="hr_dashboard"),
     path("hr_dashboard/<str:member>/openjobapplicationhtml/acceptApplication", views.acceptApplication, name="acceptApplication"),
     path("hr_dashboard/<str:member>/openjobapplicationhtml/rejectApplication", views.rejectApplication, name="rejectApplication"),
     path("hr_dashboard/<str:member>/openjobapplication", views.openjobapplication, name="openjobapplication"),
     path("hr_dashboard/<str:member>/openjobapplicationhtml/<str:appid>", views.openjobapplicationhtml, name="openjobapplicationhtml"),
     path("hr_dashboard/<str:member>/openemployeeinfohtml/deleteemployee", views.deleteemployee, name="deleteemployee"),
     path("hr_dashboard/<str:member>/openemployeeinfohtml/<str:employeeid>", views.openemployeeinfohtml, name="openemployeeinfohtml"),
     path("hr_dashboard/<str:member>/query_hr", views.query_hr, name="query_hr"),
     path("hr_dashboard/<str:member>/openquery", views.openquery, name="openquery"),
     path("hr_dashboard/<str:member>/hr_openqueryhtml/queryedit", views.queryedit, name="queryedit"),
     path("hr_dashboard/<str:member>/hr_openqueryhtml/<str:queryid>", views.hr_openqueryhtml, name="hr_openqueryhtml"),
     




]