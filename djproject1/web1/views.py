from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm,  FinanceForm,FinanceForm2, FinanceForm3, FinanceForm4, TravelForm, TravelForm2, TravelForm3, TravelForm4, SymposiumForm, SymposiumForm2, SymposiumForm3, SymposiumForm4
from .models import Post1, fin1, fin2, fin3, fin4, trav1, trav2, trav3, trav4, symp1, symp3, symp4
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, View 
from django.views.generic.edit import CreateView, UpdateView, DeleteView



def user_register(request):
    
    template = 'web1/register1.html'
    
    if request.method == 'POST':
        
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form, 
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form, 
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form, 
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user: 
                user = User.objects.create_user(
                    form.cleaned_data['username'], 
                    form.cleaned_data['email'], 
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()


        form1=Post1()
        form1.username = request.POST.get('username')
        form1.email = request.POST.get('email')
        form1.password = request.POST.get('password')
        form1.first_name = request.POST.get('first_name')
        form1.last_name = request.POST.get('last_name')
        form1.phone_number = request.POST.get('phone_number')
        form1.save()
                   
        return redirect('user_login')
           
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})
     



def user_login(request):
 

   if request.method == 'POST':
          
          username1 = request.POST.get('username')
          password1 = request.POST.get('password')
          user = authenticate(username=username1, password=password1)
          if user is not None:
              if user.is_active:
                  login(request, user)
                  return redirect('index1')

          else:
              return HttpResponse("invalid login details ")
   else:
        
        return render(request, 'web1/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def index(request):
    return render(request, "web1/index.html")
 

def index1(request):
    return render(request, "web1/index1.html")


@login_required
def special(request):
    return HttpResponse("You are logged in !")


def finance(request):
    return render(request, "web1/finance.html")


def showf(request):  
    fin1_list = fin1.objects.filter(user=request.user.id)

    return render(request,"fshow.html",{'fin1_list':fin1_list}) 

def editf(request,id):
    fin11 = fin1.objects.get(id=id)
    return render(request,"fedit.html",{'fin11':fin11})

def deletef(request, id):
    fin11 = fin1.objects.get(id=id)  
    fin11.delete()  
    return redirect('viewf') 

def updatef(request,id):
    fin11 = fin1.objects.get(id=id)
    form=FinanceForm(request.POST,instance=fin11)
    if form.is_valid():
        form.save()
        return redirect('viewf')
    return render(request,"fedit.html",{'fin11':fin11})


def fin_asst(request):
    
    template = 'web1/fin_asst.html'
    
    if request.method == 'POST':
        
      form = FinanceForm(request.POST)
      if form.is_valid():
        first_name = form.cleaned_data['first_name'],
        last_name = form.cleaned_data['last_name'],
        dob = form.cleaned_data['dob'],
        designation = form.cleaned_data['designation'],
        event = form.cleaned_data['event'],
        venue = form.cleaned_data['venue'],
        start_date = form.cleaned_data['start_date'],
        end_date = form.cleaned_data['end_date'],
        number = form.cleaned_data['number']




      form2=fin1()
      form2.first_name = request.POST.get('first_name')
      form2.last_name = request.POST.get('last_name')
      form2.dob = request.POST.get('dob')
      form2.designation = request.POST.get('designation')
      form2.event = request.POST.get('event')
      form2.venue = request.POST.get('venue')
      form2.start_date = request.POST.get('start_date')
      form2.end_date = request.POST.get('end_date')
      form2.number = request.POST.get('number')
      form2.user_id = request.user.id
      form2.save()      

      return redirect('viewf')
		   
    else:
        form = FinanceForm()

    return render(request, template, {'form': form})


def showf2(request):  
    fin1_list = fin2.objects.all()  
    return render(request,"fshow2.html",{'fin1_list':fin1_list}) 

def editf2(request,id):
    fin11 = fin2.objects.get(id=id)
    return render(request,"fedit2.html",{'fin11':fin11})

def deletef2(request, id):
    fin11 = fin2.objects.get(id=id)  
    fin11.delete()  
    return redirect('viewf2') 

def updatef2(request,id):
    fin11 = fin2.objects.get(id=id)
    form=FinanceForm2(request.POST,instance=fin11)
    if form.is_valid():
        form.save()
        return redirect('viewf2')
    return render(request,"fedit2.html",{'fin11':fin11})

def fin_asst2(request):

    template = 'web1/fin_asst2.html'
    
    if request.method == 'POST':
        
      form = FinanceForm2(request.POST)
      if form.is_valid():

         firstname = form.cleaned_data['first_name'],
         lastname = form.cleaned_data['last_name'],
         dob = form.cleaned_data['dob'],
         gender = form.cleaned_data['gender'],
         nationality = form.cleaned_data['nationality'],
         designation = form.cleaned_data['designation'],
         address = form.cleaned_data['address'],
         mobile = form.cleaned_data['mobile'],
         email  =  form.cleaned_data['email'],
         work_dept = form.cleaned_data['work_dept'],
         work_institute = form.cleaned_data['work_institute'],
         work_city = form.cleaned_data['work_city'],
         work_state = form.cleaned_data['work_state'],
         work_pin = form.cleaned_data['work_pin'],
         hod_name = form.cleaned_data['hod_name'],
         hod_mobile = form.cleaned_data['hod_mobile'],
         hod_email  =  form.cleaned_data['hod_email'],
         degree  =  form.cleaned_data['degree'],
         name1 = form.cleaned_data['name1'],
         date1 = form.cleaned_data['date1'],
         percentage1 = form.cleaned_data['percentage1'],
         division1 = form.cleaned_data['division1'],
         degree1 = form.cleaned_data['degree1'],
         name2  =  form.cleaned_data['name2'],
         date2  =  form.cleaned_data['date2'],
         percentage2 = form.cleaned_data['percentage2'],
         division2 = form.cleaned_data['division2'],
         other_degree = form.cleaned_data['other_degree'],
         name3  =  form.cleaned_data['name3'],
         date3  =  form.cleaned_data['date3'],
         percentage3 = form.cleaned_data['percentage3'],
         division3 = form.cleaned_data['division3'], 
         specification = form.cleaned_data['specification'],
         basic_salary = form.cleaned_data['basic_salary'],
         event = form.cleaned_data['event'],
         venue = form.cleaned_data['venue'],
         start_date = form.cleaned_data['start_date'],
         end_date = form.cleaned_data['end_date'],
         discipline = form.cleaned_data['discipline'],
         paper = form.cleaned_data['paper'],
         purpose = form.cleaned_data['purpose'],
         org = form.cleaned_data['org'],
         parent_org = form.cleaned_data['parent_org'],
         any_other = form.cleaned_data['any_other'],
         cost = form.cleaned_data['cost'],
         amount = form.cleaned_data['amount'],
         dir_name = form.cleaned_data['dir_name'],
         name11 = form.cleaned_data['name11'],
         title11 = form.cleaned_data['title11'],
         volume11 = form.cleaned_data['volume11'],
         name12 = form.cleaned_data['name12'],
         title12 = form.cleaned_data['title12'],
         volume12 = form.cleaned_data['volume12'],
         csir_name = form.cleaned_data['csir_name'],
         csir_year = form.cleaned_data['csir_year'],
         csir_place = form.cleaned_data['csir_place'],
         csir_number = form.cleaned_data['csir_number'],
         csir_amount = form.cleaned_data['csir_amount'],
         other_info = form.cleaned_data['other'],
         agree = form.cleaned_data['agree']

      form21 = fin2()
      form21.firstname = request.POST.get('first_name')
      form21.lastname = request.POST.get('last_name')
      form21.dob = request.POST.get('dob')
      form21.gender = request.POST.get('gender')
      form21.nationality = request.POST.get('nationality')
      form21.designation = request.POST.get('designation')
      form21.address = request.POST.get('address')
      form21.mobile = request.POST.get('mobile')
      form21.email  =  request.POST.get('email')
      form21.work_dept = request.POST.get('work_dept')
      form21.work_institute = request.POST.get('work_institute')
      form21.work_city = request.POST.get('work_city')
      form21.work_state = request.POST.get('work_state')
      form21.work_pin = request.POST.get('work_pin')
      form21.hod_name = request.POST.get('hod_name')
      form21.hod_mobile = request.POST.get('hod_mobile')
      form21.hod_email  =  request.POST.get('hod_email')
      form21.degree  =  request.POST.get('degree')
      form21.name1  =  request.POST.get('name1')
      form21.date1  =  request.POST.get('date1')
      form21.percentage1 = request.POST.get('percentage1')
      form21.division1 = request.POST.get('division1')
      form21.degree1  =  request.POST.get('degree1')
      form21.name2  =  request.POST.get('name2')
      form21.date2  =  request.POST.get('date2')
      form21.percentage2 = request.POST.get('percentage2')
      form21.division2 = request.POST.get('division2')
      form21.other_degree = request.POST.get('other_degree')
      form21.name3  =  request.POST.get('name3')
      form21.date3  =  request.POST.get('date3')
      form21.percentage3 = request.POST.get('percentage3')
      form21.division3 = request.POST.get('division3') 
      form21.specification = request.POST.get('specification')
      form21.basic_salary = request.POST.get('basic_salary')
      form21.event = request.POST.get('event')
      form21.venue = request.POST.get('venue')
      form21.start_date = request.POST.get('start_date')
      form21.end_date = request.POST.get('end_date')
      form21.discipline = request.POST.get('discipline')
      form21.paper = request.POST.get('paper')
      form21.purpose = request.POST.get('purpose')
      form21.org = request.POST.get('org')
      form21.parent_org = request.POST.get('parent_org')
      form21.any_other = request.POST.get('any_other')
      form21.cost = request.POST.get('cost')
      form21.amount = request.POST.get('amount')
      form21.dir_name = request.POST.get('dir_name')
      form21.name11 = request.POST.get('name11')
      form21.title11 = request.POST.get('title11')
      form21.volume11 = request.POST.get('volume11')
      form21.name12 = request.POST.get('name12')
      form21.title12 = request.POST.get('title12')
      form21.volume12 = request.POST.get('volume12')
      form21.csir_name = request.POST.get('csir_name')
      form21.csir_year = request.POST.get('csir_year')
      form21.csir_place = request.POST.get('csir_place')
      form21.csir_number = request.POST.get('csir_number')
      form21.csir_amount = request.POST.get('csir_amount')
      form21.other_info = request.POST.get('other')
      form21.agree = request.POST.get('agree')
      form21.save()
      return render('viewf2')
 
    else:
        form = FinanceForm2()

        return render(request, template, {'form': form})



def showf3(request):  
    fin1_list = fin3.objects.all()  
    return render(request,"fshow3.html",{'fin1_list':fin1_list}) 

def editf3(request,id):
    fin11 = fin3.objects.get(id=id)
    return render(request,"fedit3.html",{'fin11':fin11})

def deletef3(request, id):
    fin11 = fin3.objects.get(id=id)  
    fin11.delete()  
    return redirect('viewf3') 

def updatef3(request,id):
    fin11 = fin3.objects.get(id=id)
    form=FinanceForm3(request.POST,instance=fin11)
    if form.is_valid():
        form.save()
        return redirect('viewf3')
    return render(request,"fedit3.html",{'fin11':fin11})



def fin_asst3(request):
    
    template = 'web1/fin_asst3.html'
    
    if request.method == 'POST':
        
      form = FinanceForm3(request.POST)
      if form.is_valid():
	    
        name = form.cleaned_data['name'],
        address = form.cleaned_data['address'],
        city = form.cleaned_data['city'],
        state = form.cleaned_data['state'],
        pin = form.cleaned_data['pin'],
        mobile = form.cleaned_data['mobile'],
        email = form.cleaned_data['email'],
        type1 = form.cleaned_data['type1'],
        venue = form.cleaned_data['venue'],
        date_from = form.cleaned_data['date_from'],
        date_to = form.cleaned_data['date_to'],
        amount = form.cleaned_data['amount'],
        flight = form.cleaned_data['flight'],
        airlines = form.cleaned_data['airlines'],
        authority = form.cleaned_data['authority']


      form22=fin3()
      form22.name = request.POST.get('name')
      form22.address = request.POST.get('address')
      form22.city = request.POST.get('city')
      form22.state = request.POST.get('state')
      form22.pin = request.POST.get('pin')
      form22.mobile = request.POST.get('mobile')
      form22.email= request.POST.get('email')
      form22.type1 = request.POST.get('type1')
      form22.venue = request.POST.get('venue')
      form22.date_from = request.POST.get('date_from')
      form22.date_to = request.POST.get('date_to')
      form22.amount = request.POST.get('amount')
      form22.flight = request.POST.get('flight')
      form22.airlines = request.POST.get('airlines')
      form22.authority = request.POST.get('authority')
      form22.save()      

      return redirect('viewf3')
		   
    else:
        form = FinanceForm3()

    return render(request, template, {'form': form})




def showf4(request):  
    fin1_list = fin4.objects.all()  
    return render(request,"fshow4.html",{'fin1_list':fin1_list}) 

def editf4(request,id):
    fin11 = fin4.objects.get(id=id)
    return render(request,"fedit4.html",{'fin11':fin11})

def deletef4(request, id):
    fin11 = fin4.objects.get(id=id)  
    fin11.delete()  
    return redirect('viewf4') 

def updatef4(request,id):
    fin11 = fin4.objects.get(id=id)
    form=FinanceForm4(request.POST,instance=fin11)
    if form.is_valid():
        form.save()
        return redirect('viewf4')
    return render(request,"fedit4.html",{'fin11':fin11})




def fin_asst4(request):
    
    template = 'web1/fin_asst4.html'
    
    if request.method == 'POST':
        
      form = FinanceForm4(request.POST)
      if form.is_valid():
	    
        applicant = form.cleaned_data['applicant'],
        designation = form.cleaned_data['designation'],
        work_dept = form.cleaned_data['work_dept'],
        work_institute = form.cleaned_data['work_institute'],
        work_city = form.cleaned_data['work_city'],
        work_state = form.cleaned_data['work_state'],
        work_pin = form.cleaned_data['work_pin'],
        mobile = form.cleaned_data['mobile'],
        email = form.cleaned_data['email'],
        event = form.cleaned_data['event'],
        venue = form.cleaned_data['venue'],
        start_date = form.cleaned_data['start_date'],
        end_date = form.cleaned_data['end_date'],
        checkin_date = form.cleaned_data['checkin_date'],
        checkout_date = form.cleaned_data['checkout_date'],
        out_date = form.cleaned_data['out_date'],
        in_date = form.cleaned_data['in_date'],
        ideas = form.cleaned_data['ideas'],
        highlights = form.cleaned_data['highlights'],
        scientists = form.cleaned_data['scientists'],
        linkage= form.cleaned_data['linkage'],
        observations = form.cleaned_data['observations']


      form23=fin4()
      form23.applicant = request.POST.get('applicant')
      form23.designation = request.POST.get('designation')
      form23.work_dept = request.POST.get('work_dept')
      form23.work_institute = request.POST.get('work_institute')
      form23.work_city = request.POST.get('work_city')
      form23.work_state = request.POST.get('work_state')
      form23.work_pin = request.POST.get('work_pin')
      form23.mobile = request.POST.get('mobile')
      form23.email = request.POST.get('email')
      form23.event = request.POST.get('event')
      form23.venue = request.POST.get('venue')
      form23.start_date = request.POST.get('start_date')
      form23.end_date = request.POST.get('end_date')
      form23.checkin_date = request.POST.get('checkin_date')
      form23.checkout_date = request.POST.get('checkout_date')
      form23.out_date = request.POST.get('out_date')
      form23.in_date = request.POST.get('in_date')
      form23.ideas = request.POST.get('ideas')
      form23.highlights = request.POST.get('highlights')
      form23.scientists = request.POST.get('scientists')
      form23.linkage= request.POST.get('linkage')
      form23.observations = request.POST.get('observations')
      form23.save()      

      return redirect('viewf4')
		   
    else:
        form = FinanceForm4()

    return render(request, template, {'form': form})


def travel(request):
    return render(request, "web1/travel.html")





def showt1(request):  
    trav1_list = trav1.objects.all()  
    return render(request,"tshow.html",{'trav1_list':trav1_list}) 

def editt1(request,id):
    trav11 = trav1.objects.get(id=id)
    return render(request,"tedit.html",{'trav11':trav11})

def deletet1(request, id):
    trav11 = trav1.objects.get(id=id)  
    trav11.delete()  
    return redirect('viewt') 

def updatet1(request,id):
    trav11 = trav1.objects.get(id=id)
    form=TravelForm(request.POST,instance=trav11)
    if form.is_valid():
        form.save()
        return redirect('viewt')
    return render(request,"tedit.html",{'trav11':trav11})


def travel_grant(request):
    template = 'web1/travel_grant.html'
    
    if request.method == 'POST':
        
      form = TravelForm(request.POST)
      if form.is_valid():
	    
        first_name = form.cleaned_data['first_name'],
        last_name = form.cleaned_data['last_name'],
        dob = form.cleaned_data['dob'],
        designation = form.cleaned_data['designation'],
        event = form.cleaned_data['event'],
        venue = form.cleaned_data['venue'],
        start_date = form.cleaned_data['start_date'],
        end_date=form.cleaned_data['end_date']
        number = form.cleaned_data['number']


      form3=trav1()
      form3.first_name = request.POST.get('first_name')
      form3.last_name = request.POST.get('last_name')
      form3.dob = request.POST.get('dob')
      form3.designation = request.POST.get('designation')
      form3.event = request.POST.get('event')
      form3.venue = request.POST.get('venue')
      form3.start_date = request.POST.get('start_date')
      form3.end_date = request.POST.get('end_date')
      form3.number = request.POST.get('number')
      form3.save()      

      return redirect('viewt')
		   
    else:
        form = TravelForm()

    return render(request, template, {'form': form})



def showt2(request):  
    trav1_list = trav2.objects.all()  
    return render(request,"tshow2.html",{'trav1_list':trav1_list}) 

def editt2(request,id):
    trav11 = trav2.objects.get(id=id)
    return render(request,"tedit2.html",{'trav11':trav11})

def deletet2(request, id):
    trav11 = trav2.objects.get(id=id)  
    trav11.delete()  
    return redirect('viewt2') 

def updatet2(request,id):
    trav11 = trav2.objects.get(id=id)
    form=TravelForm2(request.POST,instance=trav11)
    if form.is_valid():
        form.save()
        return redirect('viewt2')
    return render(request,"tedit2.html",{'trav11':trav11})


def travel_grant2(request):
    template = 'web1/travel_grant2.html'
    
    if request.method == 'POST':       
      form = TravelForm2(request.POST)
      if form.is_valid():

         firstname = form.cleaned_data['first_name'],
         lastname = form.cleaned_data['last_name'],
         dob = form.cleaned_data['dob'],
         gender = form.cleaned_data['gender'],
         nationality = form.cleaned_data['nationality'],
         designation = form.cleaned_data['designation'],
         address = form.cleaned_data['address'],
         mobile = form.cleaned_data['mobile'],
         email  =  form.cleaned_data['email'],
         work_dept = form.cleaned_data['work_dept'],
         work_institute = form.cleaned_data['work_institute'],
         work_city = form.cleaned_data['work_city'],
         work_state = form.cleaned_data['work_state'],
         work_pin = form.cleaned_data['work_pin'],
         hod_name = form.cleaned_data['hod_name'],
         hod_mobile = form.cleaned_data['hod_mobile'],
         hod_email  =  form.cleaned_data['hod_email'],
         degree  =  form.cleaned_data['degree'],
         name1 = form.cleaned_data['name1'],
         date1 = form.cleaned_data['date1'],
         percentage1 = form.cleaned_data['percentage1'],
         division1 = form.cleaned_data['division1'],
         degree1 = form.cleaned_data['degree1'],
         name2  =  form.cleaned_data['name2'],
         date2  =  form.cleaned_data['date2'],
         percentage2 = form.cleaned_data['percentage2'],
         division2 = form.cleaned_data['division2'],
         name3  =  form.cleaned_data['name3'],
         date3  =  form.cleaned_data['date3'],
         percentage3 = form.cleaned_data['percentage3'],
         division3 = form.cleaned_data['division3'], 
         specification = form.cleaned_data['specification'],
         basic_salary = form.cleaned_data['basic_salary'],
         event = form.cleaned_data['event'],
         venue = form.cleaned_data['venue'],
         start_date = form.cleaned_data['start_date'],
         end_date = form.cleaned_data['end_date'],
         discipline = form.cleaned_data['discipline'],
         paper = form.cleaned_data['paper'],
         purpose = form.cleaned_data['purpose'],
         org = form.cleaned_data['org'],
         parent_org = form.cleaned_data['parent_org'],
         any_other = form.cleaned_data['any_other'],
         cost = form.cleaned_data['cost'],
         amount = form.cleaned_data['amount'],
         dir_name = form.cleaned_data['dir_name'],
         name11 = form.cleaned_data['name11'],
         title11 = form.cleaned_data['title11'],
         volume11 = form.cleaned_data['volume11'],
         name12 = form.cleaned_data['name12'],
         title12 = form.cleaned_data['title12'],
         volume12 = form.cleaned_data['volume12'],
         csir_name = form.cleaned_data['csir_name'],
         csir_year = form.cleaned_data['csir_year'],
         csir_place = form.cleaned_data['csir_place'],
         csir_number = form.cleaned_data['csir_number'],
         csir_amount = form.cleaned_data['csir_amount'],
         other_info = form.cleaned_data['other'],
         agree = form.cleaned_data['agree']

      form31 = trav2()
      form31.firstname = request.POST.get('first_name')
      form31.lastname = request.POST.get('last_name')
      form31.dob = request.POST.get('dob')
      form31.gender = request.POST.get('gender')
      form31.nationality = request.POST.get('nationality')
      form31.designation = request.POST.get('designation')
      form31.address = request.POST.get('address')
      form31.mobile = request.POST.get('mobile')
      form31.email  =  request.POST.get('email')
      form31.work_dept = request.POST.get('work_dept')
      form31.work_institute = request.POST.get('work_institute')
      form31.work_city = request.POST.get('work_city')
      form31.work_state = request.POST.get('work_state')
      form31.work_pin = request.POST.get('work_pin')
      form31.hod_name = request.POST.get('hod_name')
      form31.hod_mobile = request.POST.get('hod_mobile')
      form31.hod_email  =  request.POST.get('hod_email')
      form31.degree  =  request.POST.get('degree')
      form31.name1  =  request.POST.get('name1')
      form31.date1  =  request.POST.get('date1')
      form31.percentage1 = request.POST.get('percentage1')
      form31.division1 = request.POST.get('division1')
      form31.degree1  =  request.POST.get('degree1')
      form31.name2  =  request.POST.get('name2')
      form31.date2  =  request.POST.get('date2')
      form31.percentage2 = request.POST.get('percentage2')
      form31.division2 = request.POST.get('division2')
      form31.name3  =  request.POST.get('name3')
      form31.date3  =  request.POST.get('date3')
      form31.percentage3 = request.POST.get('percentage3')
      form31.division3 = request.POST.get('division3') 
      form31.specification = request.POST.get('specification')
      form31.basic_salary = request.POST.get('basic_salary')
      form31.event = request.POST.get('event')
      form31.venue = request.POST.get('venue')
      form31.start_date = request.POST.get('start_date')
      form31.end_date = request.POST.get('end_date')
      form31.discipline = request.POST.get('discipline')
      form31.paper = request.POST.get('paper')
      form31.purpose = request.POST.get('purpose')
      form31.org = request.POST.get('org')
      form31.parent_org = request.POST.get('parent_org')
      form31.any_other = request.POST.get('any_other')
      form31.cost = request.POST.get('cost')
      form31.amount = request.POST.get('amount')
      form31.dir_name = request.POST.get('dir_name')
      form31.name11 = request.POST.get('name11')
      form31.title11 = request.POST.get('title11')
      form31.volume11 = request.POST.get('volume11')
      form31.name12 = request.POST.get('name12')
      form31.title12 = request.POST.get('title12')
      form31.volume12 = request.POST.get('volume12')
      form31.csir_name = request.POST.get('csir_name')
      form31.csir_year = request.POST.get('csir_year')
      form31.csir_place = request.POST.get('csir_place')
      form31.csir_number = request.POST.get('csir_number')
      form31.csir_amount = request.POST.get('csir_amount')
      form31.other_info = request.POST.get('other')
      form31.agree = request.POST.get('agree')
      form31.save()
      return redirect('viewt2')
 
    else:
        form = TravelForm2()

        return render(request, 'web1/travel_grant2.html', {'form': form})




def showt3(request):  
    trav1_list = trav3.objects.all()  
    return render(request,"tshow3.html",{'trav1_list':trav1_list}) 

def editt3(request,id):
    trav11 = trav3.objects.get(id=id)
    return render(request,"tedit3.html",{'trav11':trav11})

def deletet3(request, id):
    trav11 = trav3.objects.get(id=id)  
    trav11.delete()  
    return redirect('viewt3') 

def updatet3(request,id):
    trav11 = trav3.objects.get(id=id)
    form=TravelForm3(request.POST,instance=trav11)
    if form.is_valid():
        form.save()
        return redirect('viewt3')
    return render(request,"tedit3.html",{'trav11':trav11})




def travel_grant3(request):
    
    template = 'web1/travel_grant3.html'
    
    if request.method == 'POST':
        
      form = TravelForm3(request.POST)
      if form.is_valid():
	    
        name = form.cleaned_data['name'],
        address = form.cleaned_data['address'],
        city = form.cleaned_data['city'],
        state = form.cleaned_data['state'],
        pin = form.cleaned_data['pin'],
        mobile = form.cleaned_data['mobile'],
        email = form.cleaned_data['email'],
        type1 = form.cleaned_data['type1'],
        venue = form.cleaned_data['venue'],
        date_from = form.cleaned_data['date_from'],
        date_to = form.cleaned_data['date_to'],
        amount = form.cleaned_data['amount'],
        flight = form.cleaned_data['flight'],
        airlines = form.cleaned_data['airlines'],
        authority = form.cleaned_data['authority']


      form32=trav3()
      form32.name = request.POST.get('name')
      form32.address = request.POST.get('address')
      form32.city = request.POST.get('city')
      form32.state = request.POST.get('state')
      form32.pin = request.POST.get('pin')
      form32.mobile = request.POST.get('mobile')
      form32.email= request.POST.get('email')
      form32.type1 = request.POST.get('type1')
      form32.venue = request.POST.get('venue')
      form32.date_from = request.POST.get('date_from')
      form32.date_to = request.POST.get('date_to')
      form32.amount = request.POST.get('amount')
      form32.flight = request.POST.get('flight')
      form32.airlines = request.POST.get('airlines')
      form32.authority = request.POST.get('authority')
      form32.save()      

      return redirect('viewt3')
		   
    else:
        form = TravelForm3()

    return render(request, template, {'form': form})




def showt4(request):  
    trav1_list = trav4.objects.all()  
    return render(request,"tshow4.html",{'trav1_list':trav1_list}) 

def editt4(request,id):
    trav11 = trav4.objects.get(id=id)
    return render(request,"tedit4.html",{'trav11':trav11})

def deletet4(request, id):
    trav11 = trav4.objects.get(id=id)  
    trav11.delete()  
    return redirect('viewt4') 

def updatet4(request,id):
    trav11 = trav4.objects.get(id=id)
    form=TravelForm4(request.POST,instance=trav11)
    if form.is_valid():
        form.save()
        return redirect('viewt4')
    return render(request,"tedit4.html",{'trav11':trav11})


def travel_grant4(request):
    
    template = 'web1/travel_grant4.html'
    
    if request.method == 'POST':
        
      form = FinanceForm4(request.POST)
      if form.is_valid():
	    
        applicant = form.cleaned_data['applicant'],
        designation = form.cleaned_data['designation'],
        work_dept = form.cleaned_data['work_dept'],
        work_institute = form.cleaned_data['work_institute'],
        work_city = form.cleaned_data['work_city'],
        work_state = form.cleaned_data['work_state'],
        work_pin = form.cleaned_data['work_pin'],
        mobile = form.cleaned_data['mobile'],
        email = form.cleaned_data['email'],
        event = form.cleaned_data['event'],
        venue = form.cleaned_data['venue'],
        start_date = form.cleaned_data['start_date'],
        end_date = form.cleaned_data['end_date'],
        checkin_date = form.cleaned_data['checkin_date'],
        checkout_date = form.cleaned_data['checkout_date'],
        out_date = form.cleaned_data['out_date'],
        in_date = form.cleaned_data['in_date'],
        ideas = form.cleaned_data['ideas'],
        highlights = form.cleaned_data['highlights'],
        scientists = form.cleaned_data['scientists'],
        linkage= form.cleaned_data['linkage'],
        observations = form.cleaned_data['observations']


      form33=trav4()
      form33.applicant = request.POST.get('applicant')
      form33.designation = request.POST.get('designation')
      form33.work_dept = request.POST.get('work_dept')
      form33.work_institute = request.POST.get('work_institute')
      form33.work_city = request.POST.get('work_city')
      form33.work_state = request.POST.get('work_state')
      form33.work_pin = request.POST.get('work_pin')
      form33.mobile = request.POST.get('mobile')
      form33.email = request.POST.get('email')
      form33.event = request.POST.get('event')
      form33.venue = request.POST.get('venue')
      form33.start_date = request.POST.get('start_date')
      form33.end_date = request.POST.get('end_date')
      form33.checkin_date = request.POST.get('checkin_date')
      form33.checkout_date = request.POST.get('checkout_date')
      form33.out_date = request.POST.get('out_date')
      form33.in_date = request.POST.get('in_date')
      form33.ideas = request.POST.get('ideas')
      form33.highlights = request.POST.get('highlights')
      form33.scientists = request.POST.get('scientists')
      form33.linkage= request.POST.get('linkage')
      form33.observations = request.POST.get('observations')
      form33.save()      

      return redirect('viewt4')
		   
    else:
        form = TravelForm4()

    return render(request, template, {'form': form})



def symposium(request):
    return render(request, "web1/symposium.html")



def shows1(request):  
    symp1_list = symp1.objects.all()  
    return render(request,"sshow.html",{'symp1_list':symp1_list}) 

def edits1(request,id):
    symp11 = symp1.objects.get(id=id)
    return render(request,"sedit.html",{'symp11':symp11})

def deletes1(request, id):
    symp11 = symp1.objects.get(id=id)  
    symp11.delete()  
    return redirect('views1') 

def updates1(request,id):
    symp11 = symp1.objects.get(id=id)
    form=SymposiumForm(request.POST,instance=symp11)
    if form.is_valid():
        form.save()
        return redirect('views1')
    return render(request,"sedit.html",{'symp11':symp11})


def symposium1(request):
    template = 'web1/symposium1.html'
    
    if request.method == 'POST':
        
      form = SymposiumForm(request.POST)
      if form.is_valid():
	    
        society_name = form.cleaned_data['society_name'],
        title = form.cleaned_data['title'],
        event_type = form.cleaned_data['event_type'],
        venue = form.cleaned_data['venue'],
        city = form.cleaned_data['city'],
        start_date = form.cleaned_data['start_date'],
        end_date = form.cleaned_data['end_date'],
        chairperson = form.cleaned_data['chairperson'],
        secretary = form.cleaned_data['secretary'],
        delegates = form.cleaned_data['delegates'],
        expenditure = form.cleaned_data['expenditure'],
        required = form.cleaned_data['required'],
        requested = form.cleaned_data['requested']


      form4=symp1()
      form4.society_name = request.POST.get('society_name')
      form4.title = request.POST.get('title')
      form4.event_type = request.POST.get('event_type')
      form4.venue = request.POST.get('venue')
      form4.city = request.POST.get('city')
      form4.start_date = request.POST.get('start_date')
      form4.end_date = request.POST.get('end_date')
      form4.chairperson = request.POST.get('chairperson')
      form4.secretary = request.POST.get('secretary')
      form4.delegates = request.POST.get('delegates')
      form4.expenditure = request.POST.get('expenditure')
      form4.required = request.POST.get('required')
      form4.requested = request.POST.get('requested')
      form4.save()      

      return redirect('symposium')
		   
    else:
        form = SymposiumForm()

    return render(request, template, {'form': form})



def shows2(request):  
    symp1_list = symp2.objects.all()  
    return render(request,"sshow2.html",{'symp1_list':symp1_list}) 

def edits2(request,id):
    symp11 = symp2.objects.get(id=id)
    return render(request,"sedit2.html",{'symp11':symp11})

def deletes2(request, id):
    symp11 = symp2.objects.get(id=id)  
    symp11.delete()  
    return redirect('views2') 

def updates2(request,id):
    symp11 = symp2.objects.get(id=id)
    form=SymposiumForm2(request.POST,instance=symp11)
    if form.is_valid():
        form.save()
        return redirect('views1')
    return render(request,"sedit.html",{'symp11':symp11})


def symposium2(request):
    return render(request, "web1/symposium2.html")




def shows3(request):  
    symp1_list = symp3.objects.all()  
    return render(request,"sshow3.html",{'symp1_list':symp1_list}) 

def edits3(request,id):
    symp11 = symp3.objects.get(id=id)
    return render(request,"sedit3.html",{'symp11':symp11})

def deletes3(request, id):
    symp11 = symp3.objects.get(id=id)  
    symp11.delete()  
    return redirect('views3') 

def updates3(request,id):
    symp11 = symp3.objects.get(id=id)
    form=SymposiumForm3(request.POST,instance=symp11)
    if form.is_valid():
        form.save()
        return redirect('views3')
    return render(request,"sedit3.html",{'symp11':symp11})


def symposium3(request):
    template = 'web1/symposium3.html'
    
    if request.method == 'POST':
        
      form = SymposiumForm3(request.POST)
      if form.is_valid():
           
          organisation_name=form.cleaned_data['organisation_name']
          event_name=form.cleaned_data['event_name'],
          venue=form.cleaned_data['venue'],
          start_date= form.cleaned_data['start_date'],
          end_date= form.cleaned_data['end_date'],
          grant_amount=form.cleaned_data['grant_amount']
          actual_amount=form.cleaned_data['actual_amount'],
          claim_amount=form.cleaned_data['claim_amount'],
          authority=form.cleaned_data['authority'],
          org_name=form.cleaned_data['org_name'],
          org_desig=form.cleaned_data['org_desig'],
          org_add=form.cleaned_data['org_add'],
          org_city=form.cleaned_data['org_city'],
          org_state=form.cleaned_data['org_state'],
          org_pin=form.cleaned_data['org_pin'],
          org_mobile=form.cleaned_data['org_mobile'],
          org_email =form.cleaned_data['org_email'],
          head_name=form.cleaned_data['head_name'],
          head_desig=form.cleaned_data['head_desig'],
          head_add=form.cleaned_data['head_add'],
          head_city=form.cleaned_data['head_city'],
          head_state=form.cleaned_data['head_state'],
          head_pin=form.cleaned_data['head_pin'],
          head_mobile=form.cleaned_data['head_mobile'],
          head_email =form.cleaned_data['head_email']
      
      form42=symp3()
      form42.organisation_name = request.POST.get('organisation_name')
      form42.event_name = request.POST.get('event_name')
      form42.venue = request.POST.get('venue')
      form42.start_date = request.POST.get('start_date')
      form42.end_date = request.Post.get('end_date')
      form42.grant_amount = request.Post.get('grant_amount')
      form42.actual_amount = request.Post.get('actual_amount')
      form42.claim_amount = request.Post.get('claim_amount')
      form42.authority = request.Post.get('authority')
      form42.org_name = request.Post.get('org_name')
      form42.org_desig = request.Post.get('org_desig')
      form42.org_add = request.Post.get('org_add')
      form42.org_city = request.Post.get('org_city')
      form42.org_state = request.Post.get('org_state')
      form42.org_pin = request.Post.get('org_pin')
      form42.org_mobile = request.Post.get('org_mobile')
      form42.org_email = request.Post.get('org_email')
      form42.head_name = request.Post.get('head_name')
      form42.head_desig = request.Post.get('head_desig')
      form42.head_add = request.Post.get('head_add')
      form42.head_city = request.Post.get('head_city')
      form42.head_state = request.Post.get('head_state')
      form42.head_pin = request.Post.get('head_pin')
      form42.head_mobile = request.Post.get('head_mobile')
      form42.head_email = request.Post.get('head_email')
      form42.save()      

      return redirect('symposium')
		   
    else:
        form = SymposiumForm3()

    return render(request, template, {'form': form})



def shows4(request):  
    symp1_list = symp4.objects.all()  
    return render(request,"sshow4.html",{'symp1_list':symp1_list}) 

def edits4(request,id):
    symp11 = symp4.objects.get(id=id)
    return render(request,"sedit4.html",{'symp11':symp11})

def deletes4(request, id):
    symp11 = symp4.objects.get(id=id)  
    symp11.delete()  
    return redirect('views4') 

def updates4(request,id):
    symp11 = symp4.objects.get(id=id)
    form=SymposiumForm4(request.POST,instance=symp11)
    if form.is_valid():
        form.save()
        return redirect('views4')
    return render(request,"sedit4.html",{'symp11':symp11})


def symposium4(request):
    template = 'web1/symposium4.html'
    
    if request.method == 'POST':
        
      form = SymposiumForm4(request.POST)
      if form.is_valid():
           
          society_name=form.cleaned_data['society_name'],
          event_name=form.cleaned_data['event_name'],
          start_date= form.cleaned_data['start_date'],
          end_date= form.cleaned_data['end_date'],
          grant_amount=form.cleaned_data['grant_amount'],
          expenditure_amount=form.cleaned_data['expenditure'],
          csir_grant=form.cleaned_data['csir_grant'],
          senior_amount=form.cleaned_data['senior_amount'],
          young_amount=form.cleaned_data['young_amount'],
          senior_regist=form.cleaned_data['senior_regist'],
          young_regist=form.cleaned_data['young_regist'],
          promo_fee=form.cleaned_data['promo_fee'],
          assist_fee=form.cleaned_data['assist_fee'],
          hospitality=form.cleaned_data['hospitality'],
          venue_fee=form.cleaned_data['venue_fee'],
          expendtotal=form.cleaned_data['expendtotal'],    
          org_name=form.cleaned_data['org_name'],
          org_desig=form.cleaned_data['org_desig'],
          org_mobile=form.cleaned_data['org_mobile'],
          org_email =form.cleaned_data['org_email'],
          fin_name=form.cleaned_data['fin_name'],
          fin_mobile=form.cleaned_data['fin_mobile'],
          fin_email =form.cleaned_data['fin_email'],
          head_name=form.cleaned_data['head_name'],
          head_desig=form.cleaned_data['head_desig'],
          head_mobile=form.cleaned_data['head_mobile'],
          head_email =form.cleaned_data['head_email']

      form43=symp4()
      form43.society_name=request.Post.get('society_name')
      form43.event_name=request.Post.get('event_name')
      form43.start_date= request.Post.get('start_date')
      form43.end_date= request.Post.get('end_date')
      form43.grant_amount=request.Post.get('grant_amount')
      form43.expenditure_amount=request.Post.get('expenditure')
      form43.csir_grant=request.Post.get('csir_grant')
      form43.senior_amount=request.Post.get('senior_amount')
      form43.young_amount=request.Post.get('young_amount')
      form43.senior_regist=request.Post.get('senior_regist')
      form43.young_regist=request.Post.get('young_regist')
      form43.promo_fee=request.Post.get('promo_fee')
      form43.assist_fee=request.Post.get('assist_fee')
      form43.hospitality=request.Post.get('hospitality')
      form43.venue_fee=request.Post.get('venue_fee')
      form43.expendtotal=request.Post.get('expendtotal')    
      form43.org_name=request.Post.get('org_name')
      form43.org_desig=request.Post.get('org_desig')
      form43.org_mobile=request.Post.get('org_mobile')
      form43.org_email =request.Post.get('org_email')
      form43.fin_name=request.Post.get('fin_name')
      form43.fin_mobile=request.Post.get('fin_mobile')
      form43.fin_email =request.Post.get('fin_email')
      form43.head_name=request.Post.get('head_name')
      form43.head_desig=request.Post.get('head_desig')
      form43.head_mobile=request.Post.get('head_mobile')
      form43.head_email =request.Post.get('head_email')
      form43.save()      

      return redirect('symposium')
		   
    else:
        form = SymposiumForm4()

    return render(request, template, {'form': form})