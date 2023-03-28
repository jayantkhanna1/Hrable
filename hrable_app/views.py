from django.shortcuts import render,redirect
from .models import HR, Employee, Admin, Jobs, Job_Application, Refferal, Quote, Query
from passlib.hash import sha512_crypt as sha512
import random
import string
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
import random
from datetime import date
from dotenv import load_dotenv
import os
load_dotenv()
otp : str


def index(request):
    jobs  = Jobs.objects.all()
    return render(request,'index.html',{'jobs':jobs})

def login_hr(request):
    return render(request,'hr_login.html')

def login_employee(request):
    return render(request,'employee_login.html')

def login_admin(request):
    return render(request,'admin_login.html')

def login_employee_user(request):
    email=request.POST['email']
    pwd1=request.POST['password']
    email=email.lower()
    if Employee.objects.filter(email=email).exists():
        user=Employee.objects.get(email=email)
        password_verify=user.password
        pwd1=sha512.hash(pwd1, rounds=5000,salt=os.environ.get('EMPLOYEE_SALT'))
        print(pwd1)
        if pwd1==password_verify:
            privatekey=''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(30))
            request.session['hrableprivatekey_employee']=privatekey
            user.private_key=privatekey
            user.save()
            return redirect('employee_dashboard/'+privatekey)
        else:
            messages.info(request,'Wrong Password !')
            return redirect('login_employee')
    else:
            messages.info(request,'Wrong Email !')
            return redirect('login_employee')

def login_hr_user(request):
    email=request.POST['email']
    pwd1=request.POST['password']
    email=email.lower()
    if HR.objects.filter(email=email).exists():
        user=HR.objects.get(email=email)
        password_verify=user.password
        pwd1=sha512.hash(pwd1, rounds=5000,salt=os.environ.get('HR_SALT'))
        if pwd1==password_verify:
            privatekey=''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(30))
            request.session['hrableprivatekey_hr']=privatekey
            user.private_key=privatekey
            user.save()
            return redirect('hr_dashboard/'+privatekey)
        else:
            messages.info(request,'Wrong Password !')
            return redirect('login_hr')
    else:
            messages.info(request,'Wrong Email !')
            return redirect('login_hr')

def login_admin_user(request):
    email=request.POST['email']
    pwd1=request.POST['password']
    email=email.lower()
    if Admin.objects.filter(email=email).exists():
        user=Admin.objects.get(email=email)
        password_verify=user.password
        pwd1=sha512.hash(pwd1, rounds=5000,salt=os.environ.get('ADMIN_SALT'))
        if pwd1==password_verify:
            privatekey=''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(30))
            request.session['hrableprivatekey_admin']=privatekey
            user.private_key=privatekey
            user.save()
            return redirect('admin_dashboard/'+privatekey)
        else:
            messages.info(request,'Wrong Password !')
            return redirect('admin_login')

def employee_dashboard(request,member):
    if 'hrableprivatekey_employee' in request.session:
        if request.session['hrableprivatekey_employee']==member:
            jobs = Jobs.objects.all()
            quote1 = Quote.objects.all()
            length = len(quote1)
            num = random.randint(1,length)
            quote = Quote.objects.get(id= num)
            name = Employee.objects.get(private_key=member)
            return render(request,'employee_dashboard.html',{'joining_date':name.joining_date,'name':name.name,'id':name.id,'jobs':jobs,'quote':quote})
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_employee')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_employee')
        
def hr_dashboard(request,member):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            hr = HR.objects.get(private_key=member)
            jobs = Jobs.objects.all()
            job_Applications = Job_Application.objects.all()
            pendingapplication = Job_Application.objects.filter(status='Pending')
            quote1 = Quote.objects.all()
            length = len(quote1)
            num = random.randint(1,length)
            quote = Quote.objects.get(id= num)
            return render(request,'hr_dashboard.html',{'username':hr.name,'pending_applications':pendingapplication,'quote' : quote.quote,'jobs':jobs,'employees':Employee.objects.all(),'job_Applications':job_Applications,'refferals':Refferal.objects.all()})
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')

def admin_dashboard(request,member):
    if 'hrableprivatekey_admin' in request.session:
        if request.session['hrableprivatekey_admin']==member:
            return render(request,'admin_dashboard.html')
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('admin_login')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('admin_login')


def recruitment(request,member):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            return render(request,'recruitment.html',{'jobs' : Jobs.objects.all()})
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')


def newjobhtml(request,member):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            return render(request,'newjob.html')
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')


def newjob(request,member):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            name = request.POST['name']
            description = request.POST['description']
            requirements = request.POST['requirements']
            salary = request.POST['salary']
            state = request.POST['state']
            city = request.POST['city']
            startdate = request.POST['startdate']
            enddate = request.POST['enddate']
            category = request.POST['category']
            jobtype = request.POST['jobtype']
            Jobs.objects.create(category = category,jobtype = jobtype,name = name, description = description, requirements = requirements, salary = salary, state = state, city = city, startdate = startdate, enddate = enddate)
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')

def newrefferal(request,jobid, member):
    if 'hrableprivatekey_employee' in request.session:
        if request.session['hrableprivatekey_employee']==member:
            jobid = jobid
            email = request.POST['referral']
            email = email.lower()
            emp = Employee.objects.get(private_key= member)
            emp_name = emp.name
            if Refferal.objects.filter(job_id = jobid, email = email).exists():
                messages.info(request,'Already Provided with a referral!')
                return redirect(request.META['HTTP_REFERER'])
            Refferal.objects.create(job_id=jobid,email=email,name_of_referrer = emp_name)
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_employee')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_employee')

def acceptApplication(request,member):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            application_id = request.POST['application_id']
            Job_Application.objects.filter(id = application_id).update(status = 'Accepted')
            job_app = Job_Application.objects.get(id = application_id)
            job = Jobs.objects.get(id = job_app.job_id)
            message = "Dear "+job_app.name+"\n We are glad to tell you That your application for the job "+job.name+" has been accepted.\n\n Regards,\n HRable"
            subject = "Application Accepted for "+job.name
            recepient = [job_app.email]
            send_mail(subject,message,os.environ.get('EMAIL'),recepient)
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')


def rejectApplication(request,member):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            application_id = request.POST['application_id']
            Job_Application.objects.filter(id = application_id).update(status = 'Rejected')
            job_app = Job_Application.objects.get(id = application_id)
            job = Jobs.objects.get(id = job_app.job_id)
            message = "Dear "+job_app.name+"\n We are sorry to tell you That your application for the job "+job.name+" has been rejected, Keep your head up as many more opportunities will come your way\n We have stored your information will soon contact you if we find a job of your matching.\n\n Regards,\n HRable"
            subject = "Application Status for "+job.name
            recepient = [job_app.email]
            send_mail(subject,message,os.environ.get('EMAIL'),recepient)
            Job_Application.objects.filter(id = application_id).delete()
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')


def onboardinghtml(request,member):
    return render(request,'hr_onboarding.html',{'member':member,'jobs':Jobs.objects.all()})


def onboarding(request, member):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            name = request.POST['name']
            email = request.POST['email']
            jobid = request.POST['job_id']
            message = "Dear "+name+"\n We are glad to tell you that you have been onboarded to HRable.\n Please go to following address: 127.0.0.1:8000/login_employee \n Username : "+email+"\n password = temppass\n please change password after logging in  \n\n Regards,\n HRable"
            subject = "Welcome to HRable "
            recepient = [email]
            pwd = sha512.hash("temppass", rounds=5000,salt=os.environ.get('EMPLOYEE_SALT'))
            temp_empl = Job_Application.objects.get(email = email, job_id = jobid)
            if not Employee.objects.filter(email=email).exists():
                from datetime import date
                date = date.today()
                Employee.objects.create(department = temp_empl.name,name=name,email=email,password=pwd,dob= temp_empl.dob,gender = temp_empl.gender, mobile_number = temp_empl.mobile_number,joining_date = date)
                send_mail(subject,message,os.environ.get('EMAIL'),recepient)
                messages.info(request,'Mail Sent')
                return redirect(request.META['HTTP_REFERER'])
            else:
                messages.info(request,'User is already an Employee! Thus cannot be Onboarded Please change their branch instead!')
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')


def openjob(request,member):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            jobid = request.POST['job_id']
            return JsonResponse('openjobhtml/'+jobid,safe = False)
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')

def openjobhtml(request,member,jobid):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            job = Jobs.objects.get(id = jobid)
            return render(request,'openjob.html',{'job':job})
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')

def editjob(request,member,jobid):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            name = request.POST['name']
            description = request.POST['description']
            requirements = request.POST['requirements']
            salary = request.POST['salary']
            state = request.POST['state']
            city = request.POST['city']
            startdate = request.POST['startdate']
            enddate = request.POST['enddate']
            category = request.POST['category']
            jobtype = request.POST['jobtype']
            Jobs.objects.create(category = category,jobtype = jobtype,name = name, description = description, requirements = requirements, salary = salary, state = state, city = city, startdate = startdate, enddate = enddate)
            return redirect('home')
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')

def deletejob(request,member,jobid):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            #Jobs.objects.filter(id = jobid).delete()
            return redirect('home')
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')


def home(request):
    member = request.session['hrableprivatekey_hr']
    return redirect('hr_dashboard/'+member)


def employee_recruitment(request,member):
    if 'hrableprivatekey_employee' in request.session:
        if request.session['hrableprivatekey_employee']==member:
            return render(request,'emp_recruitment.html',{'jobs' : Jobs.objects.all()})
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_employee')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_employee')

def openjob_emp(request,member):
    if 'hrableprivatekey_employee' in request.session:
        if request.session['hrableprivatekey_employee']==member:
            jobid = request.POST['job_id']
            return JsonResponse('openjobhtml_emp/'+jobid,safe = False)
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')
    
def openjobhtml_emp(request,member,jobid):
    if 'hrableprivatekey_employee' in request.session:
        if request.session['hrableprivatekey_employee']==member:
            job = Jobs.objects.get(id = jobid)
            return render(request,'openjob_emp.html',{'job':job})
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')


def employee_info(request,member):
    return render(request,'employee_info.html',{'member':member,'employees':Employee.objects.all()})

def openemployeeinfo(request,member):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            id = request.POST['employeeid']
            return JsonResponse('openemployeeinfohtml/'+id,safe = False)
        else:
            messages.info(request,'This user does not Exist!')
            return JsonResponse('login_hr',safe = False)
    else:
        messages.info(request,'Session Expired please Re - login!')
        return JsonResponse('login_hr',safe = False)

def openemployeeinfohtml(request,member,employeeid):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            employee = Employee.objects.get(id = employeeid)
            return render(request,'openemployeeinfo.html',{'employee':employee})
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')


def editemployeeinfo(request,member):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            empid = request.POST['id']
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['mobnum']
            gender = request.POST['gender']
            dob = request.POST['dob']
            j_date = request.POST['joindate']
            department = request.POST['joindate']
            empid = empid.replace('Employe id = ','')
            Employee.objects.filter(id = empid).update(department = department,name = name, email = email, mobile_number = phone, gender = gender, dob = dob, joining_date = j_date)
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')

def newemployee(request, member):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            return render(request,'newemployee.html')
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')

def addemployee(request, member):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['mobnum']
            gender = request.POST['gender']
            dob = request.POST['dob']
            j_date = request.POST['joindate']
            department = request.POST['department']
            message = "Dear "+name+"\n We are glad to tell you that you have been onboarded to HRable.\n Please go to following address: 127.0.0.1:8000/login_employee \n Username : "+email+"\n password = temppass\n please change password after logging in  \n\n Regards,\n HRable"
            subject = "Welcome to HRable "
            recepient = [email]
            pwd = sha512.hash("temppass", rounds=5000,salt=os.environ.get('EMPLOYEE_SALT'))
            if not Employee.objects.filter(email=email).exists():
                from datetime import date
                date = date.today()
                Employee.objects.create(department = department,name=name,email=email,password=pwd,dob= dob,gender = gender, mobile_number = phone,joining_date = j_date)
                send_mail(subject,message,os.environ.get('EMAIL'),recepient)
                messages.info(request,'Mail Sent')
                return redirect('employee_info')
            else:
                messages.info(request,'User is already an Employee! Thus cannot be Onboarded Please change their branch instead!')
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')

def deleteemployee(request,member):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            employeeid = request.GET['employeeid']
            lor = request.GET['LOR']
            if Employee.objects.filter(id=employeeid).exists():
                emp = Employee.objects.get(id = employeeid)
                if lor == 'True':
                    message = "Hello Here is your LOR \n\n Regards,\n HRable"
                    subject = "LOR "
                    recepient = [emp.email]             
                    send_mail(subject,message,os.environ.get('EMAIL'),recepient) 
                
                message = "Dear "+emp.name+"\n We are Sad to tell you that you have been Removed from the HRable Team Hope we can work again in future\n\n Regards,\n HRable"
                subject = "Goodbye "
                recepient = [emp.email]             
                Employee.objects.filter(id = employeeid).delete()
                send_mail(subject,message,os.environ.get('EMAIL'),recepient)
                messages.info(request,'Mail Sent')
                return redirect('login_hr')
            else:
                messages.info(request,'User is not an Employee! Thus cannot be Offboarded Please change their branch instead!')
            return redirect('back_hr')
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')

def job_applications(request,member):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            applications = Job_Application.objects.all()
            return render(request,'job_application.html',{'job_applications':applications})
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')

def openjobapplication(request,member):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            applicationid = request.POST['applicationid']
            
            return JsonResponse('openjobapplicationhtml/'+applicationid,safe = False)
        else:
            messages.info(request,'This user does not Exist!')
            return JsonResponse('login_hr',safe = False)
    else:
        messages.info(request,'Session Expired please Re - login!')
        return JsonResponse('login_hr',safe = False)

def openjobapplicationhtml(request,member,appid):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            if Job_Application.objects.filter(id=appid).exists():
                application = Job_Application.objects.get(id=appid)
                jobname = Jobs.objects.get(id=application.job_id)
                jobname = jobname.name
                return render(request,'openjobapplicationhtml.html',{'application':application,'jobname':jobname,'referral' : Refferal.objects.filter(job_id=application.job_id,email = application.email)})
            else:
                messages.info(request,'Application does not exist!')
                return redirect('job_applications')
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')

def query_hr(request,member):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            return render(request,'hr_query.html',{'query':Query.objects.all()})

        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')

def openquery(request, member):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            openquery_id = request.POST['openquery_id']
            
            return JsonResponse('hr_openqueryhtml/'+openquery_id,safe = False)
        else:
            messages.info(request,'This user does not Exist!')
            return JsonResponse('login_hr',safe = False)
    else:
        messages.info(request,'Session Expired please Re - login!')
        return JsonResponse('login_hr',safe = False)

def hr_openqueryhtml(request,member,queryid):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            if Query.objects.filter(id=queryid).exists():
                query = Query.objects.get(id=queryid)
                return render(request,'hr_openqueryhtml.html',{'query':query,'hr':HR.objects.all()})
            else:
                messages.info(request,'Query does not exist!')
                return redirect('query_hr')
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')

def queryedit(request,member):
    if 'hrableprivatekey_hr' in request.session:
        if request.session['hrableprivatekey_hr']==member:
            queryid = request.POST['queryid']
            hr_comment = request.POST['hr_comment']
            status = request.POST['status']
            hr_id = request.POST['hr_id']
            hr = HR.objects.get(id=hr_id)
            hr = hr.name
            Query.objects.filter(id=queryid).update(hr_comment = hr_comment,hr_acknowledging = hr, status = status, hr_id = hr_id )
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_hr')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_hr')

def reports(request,member):
    if 'hrableprivatekey_employee' in request.session:
        if request.session['hrableprivatekey_employee']==member:
            idd = Employee.objects.get(private_key = member)
            idd= idd.id
            query = Query.objects.filter(emp_id= idd)
            return render(request,'emp_reports.html',{'query':query})
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_employee')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_employee')

def openqueryemp(request,member):
    if 'hrableprivatekey_employee' in request.session:
        if request.session['hrableprivatekey_employee']==member:
            openquery_id = request.POST['query_id']
            
            return JsonResponse('employee_openqueryhtml/'+openquery_id,safe = False)
        else:
            messages.info(request,'This user does not Exist!')
            return JsonResponse('login_employee',safe = False)
    else:
        messages.info(request,'Session Expired please Re - login!')
        return JsonResponse('login_employee',safe = False)

def employee_openqueryhtml(request,member,queryid):
    if 'hrableprivatekey_employee' in request.session:
        if request.session['hrableprivatekey_employee']==member:
            if Query.objects.filter(id=queryid).exists():
                query = Query.objects.get(id=queryid)
                return render(request,'employee_openqueryhtml.html',{'query':query})
            else:
                messages.info(request,'Query does not exist!')
                return redirect('reports')
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_employee')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_employee')


def emp_queryedit(request,member):
    if 'hrableprivatekey_employee' in request.session:
        if request.session['hrableprivatekey_employee']==member:
            queryid = request.POST['queryid']
            query_type = request.POST['query_type']
            description = request.POST['description']
            Query.objects.filter(id=queryid).update(query_type = query_type, query = description )
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_employee')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_employee')

def newquery(request,member):
    if 'hrableprivatekey_employee' in request.session:
        if request.session['hrableprivatekey_employee']==member:
            username = Employee.objects.get(private_key = member)
            username = username.name
            return render(request,'emp_newquery.html',{'username':username})
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_employee')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_employee')

def emp_newquerycreate(request,member):
    if 'hrableprivatekey_employee' in request.session:
        if request.session['hrableprivatekey_employee']==member:
            username = request.POST['name']
            query_type = request.POST['query_type']
            query  = request.POST['description']
            emp = Employee.objects.get(private_key = member)
            idd= emp.id
            todays_date = date.today()
            tdate = todays_date
            Query.objects.create(empname = username,emp_id = idd, query_type = query_type, query = query, date = tdate)
            return redirect('reports',member)
        else:
            messages.info(request,'This user does not Exist!')
            return redirect('login_employee')
    else:
        messages.info(request,'Session Expired please Re - login!')
        return redirect('login_employee')

def openjoblisting(request):
    return render(request,'openjoblisting.html',{'jobs':Jobs.objects.all()})

def applytojob(request,jobid):
    return render(request,'applytojob.html',{'job':Jobs.objects.get(id = jobid)})

def applytojob_form(request,jobid):
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['mobile']
            coverletter = request.POST['coverletter']
            state = request.POST['state']
            city = request.POST['city']
            address = request.POST['address']
            zipcode = request.POST['zipcode']
            country = request.POST['country']
            dob = request.POST['dob']
            gender = request.POST['gender']
            jobname = request.POST['jobname']
            if Job_Application.objects.filter(job_id = jobid, email = email).exists():
                messages.info(request,'Already Applied!')
                return redirect(index)
            Job_Application.objects.create(jobname = jobname,job_id=jobid,name=name,email=email,mobile_number=phone,cover_letter=coverletter,state=state,city=city,address=address,zip_code=zipcode,country=country,dob=dob,gender= gender)
            return redirect('index')