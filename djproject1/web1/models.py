from django.db import models
from django.urls import reverse
from django.forms import forms


class Post1(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=20)
    phone_number = models.IntegerField()

    class Meta:
	     db_table="post1"


class fin1(models.Model):
    user = models.ForeignKey(Post1)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob= models.DateField()
    designation = models.CharField(max_length=50)
    event = models.CharField(max_length=50)
    venue = models.CharField(max_length=50)
    start_date= models.DateField()
    end_date= models.DateField()
    number= models.CharField(max_length=20)

    class Meta:
	     db_table="fin1"



class fin2(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    dob=models.DateField()
    gender=models.CharField(max_length=30)
    nationality=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    mobile=models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    work_dept=models.CharField(max_length=30)
    work_institute=models.CharField(max_length=30)
    work_city=models.CharField(max_length=30)
    work_state=models.CharField(max_length=30)
    work_pin=models.CharField(max_length=30)
    hod_name=models.CharField(max_length=30)
    hod_mobile=models.CharField(max_length=30)
    hod_email = models.EmailField(max_length=50)
    degree = models. CharField(max_length=30)
    name1 = models. CharField(max_length=50)
    date1 = models.DateField()
    percentage1=models.CharField(max_length=30)
    division1=models.CharField(max_length=30)
    degree1 = models. CharField(max_length=30)
    name2 = models. CharField(max_length=50)
    date2 = models.DateField()
    percentage2=models.CharField(max_length=30)
    division2=models.CharField(max_length=30)
    other_degree=models.CharField(max_length=50)
    name3 = models. CharField(max_length=50)
    date3 = models.DateField()
    percentage3=models.CharField(max_length=30)
    division3=models.CharField(max_length=30) 
    specification=models.CharField(max_length=30)
    basic_salary=models.CharField(max_length=30)
    event=models.CharField(max_length=30)
    venue=models.CharField(max_length=30)
    start_date=models.DateField()
    end_date=models.DateField()
    discipline=models.CharField(max_length=30)
    paper=models.CharField(max_length=30)
    purpose=models.CharField(max_length=30)
    org=models.CharField(max_length=30)
    parent_org=models.CharField(max_length=30)
    any_other=models.CharField(max_length=30)
    cost=models.CharField(max_length=30)
    amount=models.CharField(max_length=30)
    dir_name=models.CharField(max_length=30)
    name11=models.CharField(max_length=30)
    title11=models.CharField(max_length=30)
    volume11=models.CharField(max_length=30)
    name12=models.CharField(max_length=30)
    title12=models.CharField(max_length=30)
    volume12=models.CharField(max_length=30)
    csir_name=models.CharField(max_length=30)
    csir_year=models.CharField(max_length=30)
    csir_place=models.CharField(max_length=30)
    csir_number=models.CharField(max_length=30)
    csir_amount=models.CharField(max_length=30)
    other_info=models.CharField(max_length=30)
    agree=models.CharField(max_length=30)

    class Meta:
        db_table="fin2"



class fin3(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    pin=models.CharField(max_length=30)
    mobile=models.IntegerField()
    email = models.EmailField()
    type1=models.CharField(max_length=50)
    venue=models.CharField(max_length=50)
    date_from=models.DateField()
    date_to=models.DateField()
    amount=models.CharField(max_length=50)
    airlines=models.CharField(max_length=50)
    flight= models.CharField(max_length=50)
    authority=models.CharField(max_length=50)
 
    class Meta:
        db_table="fin3"



class fin4(models.Model):
    applicant=models.CharField(max_length=30)
    designation=models.CharField(max_length=50)
    work_dept=models.CharField(max_length=100)
    work_institute=models.CharField(max_length=30)
    work_city=models.CharField(max_length=30)
    work_state=models.CharField(max_length=30)
    work_pin=models.CharField(max_length=30)
    mobile=models.IntegerField()
    email = models.EmailField(max_length=50)
    event=models.CharField(max_length=50)
    venue=models.CharField(max_length=30)
    start_date=models.DateField()
    end_date=models.DateField()   
    checkin_date=models.DateField()
    checkout_date=models.DateField()
    out_date=models.DateField()
    in_date=models.DateField()
    ideas=models.CharField(max_length=255)
    highlights=models.CharField(max_length=255)
    scientists=models.CharField(max_length=255)
    linkage=models.CharField(max_length=255)
    observations=models.CharField(max_length=255)

    class Meta:
        db_table="fin4" 



class trav1(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob= models.DateField()
    designation = models.CharField(max_length=50)
    event = models.CharField(max_length=50)
    venue = models.CharField(max_length=50)
    start_date= models.DateField()
    end_date= models.DateField()
    number= models.CharField(max_length=20)

    class Meta:
	     db_table="trav1"




class trav2(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    dob=models.DateField()
    gender=models.CharField(max_length=30)
    nationality=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    mobile=models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    work_dept=models.CharField(max_length=30)
    work_institute=models.CharField(max_length=30)
    work_city=models.CharField(max_length=30)
    work_state=models.CharField(max_length=30)
    work_pin=models.CharField(max_length=30)
    hod_name=models.CharField(max_length=30)
    hod_mobile=models.CharField(max_length=30)
    hod_email = models.EmailField(max_length=50)
    degree = models. CharField(max_length=30)
    name1 = models. CharField(max_length=50)
    date1 = models.DateField()
    percentage1=models.CharField(max_length=30)
    division1=models.CharField(max_length=30)
    degree1 = models. CharField(max_length=30)
    name2 = models. CharField(max_length=50)
    date2 = models.DateField()
    percentage2=models.CharField(max_length=30)
    division2=models.CharField(max_length=30)
    name3 = models. CharField(max_length=50)
    date3 = models.DateField()
    percentage3=models.CharField(max_length=30)
    division3=models.CharField(max_length=30) 
    specification=models.CharField(max_length=30)
    basic_salary=models.CharField(max_length=30)
    event=models.CharField(max_length=30)
    venue=models.CharField(max_length=30)
    start_date=models.DateField()
    end_date=models.DateField()
    discipline=models.CharField(max_length=30)
    paper=models.CharField(max_length=30)
    purpose=models.CharField(max_length=30)
    org=models.CharField(max_length=30)
    parent_org=models.CharField(max_length=30)
    any_other=models.CharField(max_length=30)
    cost=models.CharField(max_length=30)
    amount=models.CharField(max_length=30)
    dir_name=models.CharField(max_length=30)
    name11=models.CharField(max_length=30)
    title11=models.CharField(max_length=30)
    volume11=models.CharField(max_length=30)
    name12=models.CharField(max_length=30)
    title12=models.CharField(max_length=30)
    volume12=models.CharField(max_length=30)
    csir_name=models.CharField(max_length=30)
    csir_year=models.CharField(max_length=30)
    csir_place=models.CharField(max_length=30)
    csir_number=models.CharField(max_length=30)
    csir_amount=models.CharField(max_length=30)
    other_info=models.CharField(max_length=30)
    agree=models.CharField(max_length=30)

    class Meta:
        db_table="trav2"


		
class trav3(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    pin=models.CharField(max_length=30)
    mobile=models.IntegerField()
    email = models.EmailField()
    type1=models.CharField(max_length=50)
    venue=models.CharField(max_length=50)
    date_from=models.DateField()
    date_to=models.DateField()
    amount=models.CharField(max_length=50)
    airlines=models.CharField(max_length=50)
    flight= models.CharField(max_length=50)
    authority=models.CharField(max_length=50)
 
    class Meta:
        db_table="trav3"


class trav4(models.Model):
    applicant=models.CharField(max_length=30)
    designation=models.CharField(max_length=50)
    work_dept=models.CharField(max_length=100)
    work_institute=models.CharField(max_length=30)
    work_city=models.CharField(max_length=30)
    work_state=models.CharField(max_length=30)
    work_pin=models.CharField(max_length=30)
    mobile=models.IntegerField()
    email = models.EmailField(max_length=50)
    event=models.CharField(max_length=50)
    venue=models.CharField(max_length=30)
    start_date=models.DateField()
    end_date=models.DateField()   
    checkin_date=models.DateField()
    checkout_date=models.DateField()
    out_date=models.DateField()
    in_date=models.DateField()
    ideas=models.CharField(max_length=255)
    highlights=models.CharField(max_length=255)
    scientists=models.CharField(max_length=255)
    linkage=models.CharField(max_length=255)
    observations=models.CharField(max_length=255)


    class Meta:
        db_table="trav4" 
		


class symp1(models.Model):
    society_name= models.CharField(max_length=100)
    title= models.CharField(max_length=100)
    event_type= models.CharField(max_length=50)
    venue= models.CharField(max_length=50)
    city= models.CharField(max_length=50) 
    start_date= models.DateField()
    end_date= models.DateField()
    chairperson= models.CharField(max_length=50)
    secretary= models.CharField(max_length=50)
    delegates= models.CharField(max_length=30)
    expenditure=  models.IntegerField()
    required= models.IntegerField()
    requested= models.IntegerField()


    class Meta:
	     db_table="symp1"




class symp2(models.Model):
     org_name=models.CharField(max_length=50)
     nature=models.CharField(max_length=50)
     title=models.CharField(max_length=50)
     discipline=models.CharField(max_length=50)
     address=models.CharField(max_length=100)
     city=models.CharField(max_length=30)
     state=models.CharField(max_length=30)
     pin=models.CharField(max_length=30)
     event_start=models.DateField()
     event_end=models.DateField()
     chair_name=models.CharField(max_length=50)
     chair_org=models.CharField(max_length=100)
     name=models.CharField(max_length=30)
     gender=models.CharField(max_length=20)    
     person_desig=models.CharField(max_length=50)
     person_dept=models.CharField(max_length=50)
     person_inst=models.CharField(max_length=100)
     person_add=models.CharField(max_length=100)
     person_city=models.CharField(max_length=30)
     person_state=models.CharField(max_length=30)
     person_pin=models.CharField(max_length=30)
     person_phone=models.IntegerField()
     person_email = models.EmailField(max_length=50)
     last_activity = models.CharField(max_length=50)
     theme=models.CharField(max_length=50)
     details=models.CharField(max_length=255)
     relevance=models.CharField(max_length=100)
     promotion=models.CharField(max_length=255)
     csir_lab1=models.CharField(max_length=100)
     theme1=models.CharField(max_length=100)
     csir_lab2=models.CharField(max_length=100)
     theme2=models.CharField(max_length=100)
     sci_name1=models.CharField(max_length=100)
     sci_lab1=models.CharField(max_length=100)
     sci_name2=models.CharField(max_length=100)
     sci_lab2=models.CharField(max_length=100)
     permit=models.CharField(max_length=50)
     national_no=models.CharField(max_length=50)
     international_no=models.CharField(max_length=50)
     phd_no=models.CharField(max_length=50)
     postgrad_no=models.CharField(max_length=50)
     speak_name1=models.CharField(max_length=50)
     speak_institute1=models.CharField(max_length=50)
     speak_name2=models.CharField(max_length=50)
     speak_institute2=models.CharField(max_length=50)
     speak_name3=models.CharField(max_length=50)
     speak_institute3=models.CharField(max_length=50)
     session_type=models.CharField(max_length=50)
     support_travel=models.CharField(max_length=50)
     support_registration=models.CharField(max_length=50)
     support_hospitality=models.CharField(max_length=50)
     asenior_amount=models.CharField(max_length=50)
     ayoung_amount=models.CharField(max_length=50)
     asenior_regist=models.CharField(max_length=50)
     ayoung_regist=models.CharField(max_length=50)
     apromo_fee=models.CharField(max_length=50)
     aassist_fee=models.CharField(max_length=50)
     ahospitality=models.CharField(max_length=50)
     avenue_fee=models.CharField(max_length=50)
     aanti_expendtotal=models.CharField(max_length=50)
     anti_regist=models.CharField(max_length=50)
     anti_ehibit=models.CharField(max_length=50)
     anti_grant=models.CharField(max_length=50)
     anti_sponser=models.CharField(max_length=50)
     anti_other=models.CharField(max_length=50)
     anti_total=models.CharField(max_length=50)
     esenior_amount=models.CharField(max_length=50)
     eyoung_amount=models.CharField(max_length=50)
     esenior_regist=models.CharField(max_length=50)
     eyoung_regist=models.CharField(max_length=50)
     epromo_fee=models.CharField(max_length=50)
     eassist_fee=models.CharField(max_length=50)
     ehospitality=models.CharField(max_length=50)
     evenue_fee=models.CharField(max_length=50)
     eanti_expendtotal=models.CharField(max_length=50)
     rd_name1=models.CharField(max_length=50)
     rd_req1=models.CharField(max_length=50)
     rd_rec1=models.CharField(max_length=50)
     rd_exp1=models.CharField(max_length=50)
     rd_name2=models.CharField(max_length=50)
     rd_req2=models.CharField(max_length=50)
     rd_rec2=models.CharField(max_length=50)
     rd_exp2=models.CharField(max_length=50)
     rd_name3=models.CharField(max_length=50)
     rd_req3=models.CharField(max_length=50)
     rd_rec3=models.CharField(max_length=50)
     rd_exp3=models.CharField(max_length=50)
     csir_amount1=models.CharField(max_length=50)
     csir_grant1=models.CharField(max_length=50)
     csir_title1=models.CharField(max_length=50)
     csir_audit1=models.CharField(max_length=50)
     csir_amount2=models.CharField(max_length=50)
     csir_grant2=models.CharField(max_length=50)
     csir_title2=models.CharField(max_length=50)
     csir_audit2=models.CharField(max_length=50)
     csir_amount3=models.CharField(max_length=50)
     csir_grant3=models.CharField(max_length=50)
     csir_title3=models.CharField(max_length=50)
     csir_audit3=models.CharField(max_length=50)
     authority_name=models.CharField(max_length=50)
     other_info=models.CharField(max_length=255)
     org_sectname=models.CharField(max_length=50)
     org_sectmobile=models.IntegerField()
     org_sectemail=models.EmailField()
     org_chairname=models.CharField(max_length=50)
     org_chairmobile=models.IntegerField()
     org_chairemail=models.EmailField()
     org_headname=models.CharField(max_length=50)
     org_headmobile=models.IntegerField()
     org_heademail=models.EmailField()


     class Meta:
	     db_table="symp2"




class symp3(models.Model):
     organisation_name=models.CharField(max_length=100)
     event_name=models.CharField(max_length=100)
     venue=models.CharField(max_length=100)
     start_date= models.DateField()
     end_date= models.DateField()
     grant_amount=models.CharField(max_length=50)
     actual_amount=models.CharField(max_length=50)
     claim_amount=models.CharField(max_length=50)
     authority=models.CharField(max_length=50)
     org_name=models.CharField(max_length=50)
     org_desig=models.CharField(max_length=50)
     org_add=models.CharField(max_length=100)
     org_city=models.CharField(max_length=50)
     org_state=models.CharField(max_length=50)
     org_pin=models.CharField(max_length=30)
     org_mobile=models.IntegerField()
     org_email =models.EmailField()
     head_name=models.CharField(max_length=50)
     head_desig=models.CharField(max_length=50)
     head_add=models.CharField(max_length=100)
     head_city=models.CharField(max_length=50)
     head_state=models.CharField(max_length=50)
     head_pin=models.CharField(max_length=30)
     head_mobile=models.IntegerField()
     head_email =models.EmailField()


     class Meta:
	     db_table="symp3"


class symp4(models.Model):
     society_name=models.CharField(max_length=50)
     event_name=models.CharField(max_length=50)
     start_date= models.DateField()
     end_date= models.DateField()
     grant_amount=models.CharField(max_length=50)
     expenditure_amount=models.CharField(max_length=50)
     csir_grant=models.CharField(max_length=50)
     senior_amount=models.CharField(max_length=50)
     young_amount=models.CharField(max_length=50)
     senior_regist=models.CharField(max_length=50)
     young_regist=models.CharField(max_length=50)
     promo_fee=models.CharField(max_length=50)
     assist_fee=models.CharField(max_length=50)
     hospitality=models.CharField(max_length=50)
     venue_fee=models.CharField(max_length=50)
     expendtotal=models.CharField(max_length=50)    
     org_name=models.CharField(max_length=50)
     org_desig=models.CharField(max_length=50)
     org_mobile=models.IntegerField()
     org_email =models.EmailField()
     fin_name=models.CharField(max_length=50)
     fin_mobile=models.IntegerField()
     fin_email =models.EmailField()
     head_name=models.CharField(max_length=50)
     head_desig=models.CharField(max_length=50)
     head_mobile=models.IntegerField()
     head_email =models.EmailField()


     class Meta:
	     db_table="symp4"