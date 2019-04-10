import csv
import pprint
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render , redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login,authenticate, logout 

from rest_framework.views import APIView
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.response import Response 
from rest_framework.authentication import TokenAuthentication

from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes

from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)




from rest_framework import viewsets, serializers
from .serializers import EmployeeSerializer

from .models import Question,Choice,Employee,Event
from django.utils.datastructures import MultiValueDictKeyError


def index(request):
    return render(request, 'polls/index.html', )
    
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login_api(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)
                    
@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)
    
    
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
def employee(request):
    latest_employee_list = Employee.objects.order_by('emp_name')
    context = {'latest_employee_list': latest_employee_list}
    return render(request, 'polls/employee.html', context)
    
def employee_del(request,id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    latest_employee_list = Employee.objects.order_by('emp_name')
    context = {'latest_employee_list': latest_employee_list}
    return render(request,'polls/employee.html',context)    
 
def employee_edit(request,id):
    
    emp = Employee.objects.get(id=id)
    context = {'emp': emp}
    return render(request,'polls/emp_edit.html',context)    
             
def employee_update(request,id):
    
    emp = Employee.objects.get(id=id)
    emp_name = request.POST['name']
    emp_age= request.POST['age']
    emp_salary= request.POST['salary']
    emp.emp_name = emp_name
    emp.emp_age = emp_age
    emp.emp_salary = emp_salary    
    emp.save()
    
    latest_employee_list = Employee.objects.order_by('emp_name')
    context = {'latest_employee_list': latest_employee_list}
    return render(request, 'polls/employee.html', context)
        
def form(request):
    latest_form_list = Employee.objects.order_by('emp_name')
    context = {'latest_form_list': latest_form_list}
    return render(request, 'polls/form.html', context)
    
def employeeSave(request):
    pprint.pprint(request.POST)
    emp_name = request.POST['name']
    emp_age= request.POST['age']
    emp_salary= request.POST['salary']
    if Employee.objects.filter(emp_name=emp_name).exists():
        latest_employee_list = Employee.objects.order_by('emp_name')
        context = {'latest_employee_list': latest_employee_list,'employee_error': 'NAME ALREADY EXITS...'}
        return render(request, 'polls/employee.html', context)
    else:
        pprint.pprint("employee name is: "+str(emp_name))
        pprint.pprint("employee age is: "+str(emp_age))
        pprint.pprint("employee salary is: "+str(emp_salary))
        Employee_instance=Employee.objects.create(emp_name=emp_name,emp_age=emp_age,emp_salary=emp_salary)
        latest_employee_list = Employee.objects.order_by('emp_name')
        context = {'latest_employee_list': latest_employee_list}
        return render(request, 'polls/employee.html', context)
    

    
def login(request):
    user_name = request.POST['email']
    password = request.POST['password']
    pprint.pprint("Username is: "+str(user_name))
    pprint.pprint("Password is: "+str(password))
    context={}
    if authenticate(username=user_name,password=password):
        pprint.pprint("Proper User..Please come in!!!!")
        return render(request, 'polls/home_page.html', context)
    else:
        context={'error_msg':'Invalid username or password'}
        return render(request, 'polls/index.html', context)
        
def userLogOut(request):
    logout(request)
    context={'error_msg':'Logged out successfully'}
    return render(request, 'polls/index.html', context)
    
    
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    return HttpResponse("You're voting on question %s." % question_id)
    
def calendar(request,id):
    emp = Employee.objects.get(id=id)
    context = {'emp': emp}
    return render(request, 'polls/calendar.html',context)
    
    
def details(request,id):
    emp = Employee.objects.get(id=id)
    context = {'emp': emp}
    return render(request, 'polls/calendar3.html',context)
    
    
def details_save(request):
    pprint.pprint(request.POST)
    event_name = request.POST['eventname']
    no_of_people = request.POST['no-of-people']
    start_date = request.POST['start_date']
    start_time = request.POST['start_time']
    end_date = request.POST['end_date']
    end_time = request.POST['end_time']
    notes = request.POST['description']
    Event_instance=Event.objects.create(event_name=event_name,no_of_people=no_of_people,start_date=start_date,start_time=start_time,end_date=end_date,end_time=end_time,notes=notes)
    pprint.pprint("Event name is: " +str(Event_instance))
    event_list = Event.objects.all()
    context = {'event_list':event_list}
    return render(request, 'polls/calendar3.html',context)
    
def details_display(request,id):
    
    emp = Employee.objects.get(id=id)
    event_list = Event.objects.filter(start_date=timezone.now())
    context = {'event_list': event_list,'emp': emp}
    return render(request, 'polls/cal_display.html',context)
    
    
def employee_update(request,id):
    emp = Employee.objects.get(id=id)
    emp_name = request.POST['name']
    emp_age= request.POST['age']
    emp_salary= request.POST['salary']
    
    if Employee.objects.filter(emp_name=emp_name).exists():
        latest_employee_list = Employee.objects.order_by('emp_name')
        context = {'latest_employee_list': latest_employee_list,'employee_error': 'NAME ALREADY EXITS...'}
        return render(request, 'polls/employee.html', context)
    else:
        emp.emp_name = emp_name
        emp.emp_age = emp_age
        emp.emp_salary = emp_salary    
        emp.save()
        latest_employee_list = Employee.objects.order_by('emp_name')
        context = {'latest_employee_list': latest_employee_list}
        return render(request, 'polls/employee.html', context)
        
def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Employee.csv"'

    writer = csv.writer(response)
    writer.writerow(['Emp_name','Emp_age','Emp_salary'])

    users = Employee.objects.order_by('emp_name').values_list('emp_name','emp_age','emp_salary')
    for user in users:
        writer.writerow(user)

    return response
    
def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            context = {'msg': 'Account created successfully Please Log In..'}
            return render(request, 'polls/index.html',context)

    else:
        f = CustomUserCreationForm()

    return render(request, 'polls/register.html', {'form': f})

    
    
# class LoginView(APIView):
    # def post(self, request):
        # serializer = LoginSerializer(data=request.data)
        # serializer.is_valid(raise_exceptions=True)
        # user = serializer.validated_data["user"]
        # django_login(request, user)
        # token, created = Token.objects.get_or_create(user=user)
        # return Response({"token": token.key}, status=200)
        
        
        
# class LogoutView(APIView):
    # authentication_classes = (TokenAuthentication, )
    
    # def post(self, request):
        # django_logout(request)
        # return Response(status=204)
        
        

