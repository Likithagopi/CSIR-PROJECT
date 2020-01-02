from django import forms
from .models import Post1, fin1, fin2, fin3, fin4, trav1, trav2, trav3, trav4, symp1, symp2, symp3, symp4

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, max_length=10)
    password_repeat = forms.CharField(widget=forms.PasswordInput, max_length=10)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    phone_number = forms.CharField(required=False)

    class Meta:
        model = Post1
        fields = ['username','email', 'password', 'first_name', 'last_name', 'phone_number']






class FinanceForm(forms.ModelForm):
    first_name= forms.CharField(max_length=30)
    last_name= forms.CharField(max_length=30)
    dob=forms.DateField()
    designation= forms.CharField(max_length=50)
    event= forms.CharField(max_length=50)
    venue= forms.CharField(max_length=50)
    start_date= forms.DateField()
    end_date= forms.DateField()
    number= forms.CharField(max_length=30)

    class Meta:
        model = fin1
        fields = ['first_name','last_name', 'dob', 'designation', 'event', 'venue', 'start_date', 'end_date', 'number']

GEND_CHOICES= [
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
    ('OTHERS','OTHERS'),
    ]

DEGREE= [
    ('M.Sc', 'M.Sc'),
    ('MBBS', 'MBBS'),
    ('BE','BE'),
    ('B-Pharma', 'B-Pharma'),
    ]

DEGREE1= [
    ('PHD', 'PHD'),
    ('MD', 'MD'),
    ('ME','ME'),
    ('M-Pharma', 'M-Pharma'),
    ]

discipline= [
('Chemical Sciences', 'Chemical Sciences'),
('Life Sciences', 'Life Sciences'),
('Engineering', 'Engineering'),
('Mathematical Sciences', 'Mathematical Sciences'), 
('Physical Sciences', 'Physical Sciences'),
('Earth Environment, Ocean and Atmospheric Sciences', 'Earth Environment, Ocean and Atmospheric Sciences'), 
('Medical Sciences', 'Medical Sciences'),
('Multi-disciplinary','Multi-disciplinary'),
('IT/ITES/Information Sciences', 'IT/ITES/Information Sciences'),
]

agree= [
	('agreed', 'agreed'),
]


class FinanceForm2(forms.ModelForm):
    firstname=forms.CharField(max_length=30)
    lastname=forms.CharField(max_length=30)
    dob=forms.DateField()
    gender=forms.CharField(label='gender', widget=forms.RadioSelect(choices=GEND_CHOICES))
    nationality=forms.CharField(max_length=50)
    designation=forms.CharField(max_length=50)
    address=forms.CharField(max_length=100)
    mobile=forms.CharField(required=False)
    email = forms.EmailField(max_length=50)
    work_dept=forms.CharField(max_length=30)
    work_institute=forms.CharField(max_length=30)
    work_city=forms.CharField(max_length=30)
    work_state=forms.CharField(max_length=30)
    work_pin=forms.CharField(max_length=30)
    hod_name=forms.CharField(max_length=30)
    hod_mobile=forms.CharField(required=False)
    hod_email = forms.EmailField(max_length=50)
    degree = forms. CharField(label='degree', widget=forms.RadioSelect(choices=DEGREE))
    name1 = forms. CharField(max_length=50)
    date1 = forms.DateField()
    percentage1=forms.CharField(max_length=30)
    division1=forms.CharField(max_length=30)
    degree1 = forms. CharField(label='degree1', widget=forms.RadioSelect(choices=DEGREE1))
    name2 = forms. CharField(max_length=50)
    date2 = forms.DateField()
    percentage2=forms.CharField(max_length=30)
    division2=forms.CharField(max_length=30)
    other_degree= forms.CharField(max_length=50)
    name3 = forms. CharField(max_length=50)
    date3 = forms.DateField()
    percentage3=forms.CharField(max_length=30)
    division3=forms.CharField(max_length=30) 
    specification=forms.CharField(max_length=30)
    basic_salary=forms.CharField(max_length=30)
    event=forms.CharField(max_length=30)
    venue=forms.CharField(max_length=30)
    start_date=forms.DateField()
    end_date=forms.DateField()
    discipline=forms.CharField(label='discipline', widget=forms.RadioSelect(choices=discipline))
    paper=forms.CharField(max_length=30)
    purpose=forms.CharField(max_length=30)
    org=forms.CharField(max_length=30)
    parent_org=forms.CharField(max_length=30)
    any_other=forms.CharField(max_length=30)
    cost=forms.CharField(max_length=30)
    amount=forms.CharField(max_length=30)
    dir_name=forms.CharField(max_length=30)
    name11=forms.CharField(max_length=30)
    title11=forms.CharField(max_length=30)
    volume11=forms.CharField(max_length=30)
    name12=forms.CharField(max_length=30)
    title12=forms.CharField(max_length=30)
    volume12=forms.CharField(max_length=30)
    csir_name=forms.CharField(max_length=30)
    csir_year=forms.CharField(max_length=30)
    csir_place=forms.CharField(max_length=30)
    csir_number=forms.CharField(max_length=30)
    csir_amount=forms.CharField(max_length=30)
    other_info=forms.CharField(max_length=30)
    agree=forms.CharField(label='agree', widget=forms.RadioSelect(choices=agree))



    class Meta:
          model = fin2
          fields = "__all__"	

FLIGHT= [
    ('YES', 'YES'),
    ('NO', 'NO'),
    ]

AUTHORITY= [
    ('DIRECTOR','DIRECTOR'),
    ('REGISTRAR','REGISTRAR'),
    ('DEAN','DEAN'),
    ('FINANCE OFFICER','FINANCE OFFICER'),
    ('MEDICAL SUPERINDENT','MEDICAL SUPERINDENT'),
    ('OTHER','OTHER'),
]

class FinanceForm3(forms.ModelForm):
    name=forms.CharField(max_length=50)
    address=forms.CharField(max_length=100)
    city=forms.CharField(max_length=30)
    state=forms.CharField(max_length=30)
    pin=forms.CharField(max_length=30)
    mobile=forms.CharField(required=False)
    email = forms.EmailField(max_length=50)
    type1=forms.CharField(max_length=50)
    venue=forms.CharField(max_length=50)
    date_from=forms.DateField()
    date_to=forms.DateField()
    amount=forms.CharField(max_length=50)
    airlines= forms.CharField(label='flight', widget=forms.RadioSelect(choices=FLIGHT))
    flight=forms.CharField(max_length=50)
    authority=forms.CharField(label='authority', widget=forms.RadioSelect(choices=AUTHORITY))


    class Meta:
        model = fin3
        fields = ['name','address', 'city', 'state', 'pin', 'mobile', 'email', 'type1', 'venue', 'date_from', 'date_to', 'amount', 'airlines', 'flight', 'authority']


class FinanceForm4(forms.ModelForm):
    applicant=forms.CharField(max_length=30)
    designation=forms.CharField(max_length=50)
    work_dept=forms.CharField(max_length=100)
    work_institute=forms.CharField(max_length=30)
    work_city=forms.CharField(max_length=30)
    work_state=forms.CharField(max_length=30)
    work_pin=forms.CharField(max_length=30)
    mobile=forms.CharField(required=False)
    email = forms.EmailField(max_length=50)
    event=forms.CharField(max_length=50)
    venue=forms.CharField(max_length=30)
    start_date=forms.DateField()
    end_date=forms.DateField()   
    checkin_date=forms.DateField()
    checkout_date=forms.DateField()
    out_date=forms.DateField()
    in_date=forms.DateField()
    ideas=forms.CharField(max_length=255)
    highlights=forms.CharField(max_length=255)
    scientists=forms.CharField(max_length=255)
    linkage=forms.CharField(max_length=255)
    observations=forms.CharField(max_length=255)


    class Meta:
        model = fin4
        fields=['applicant', 'designation', 'work_dept', 'work_institute', 'work_city', 'work_state', 'work_pin', 'mobile', 'email', 'event', 'venue', 'start_date', 'end_date', 'checkin_date', 'checkout_date', 'out_date', 'in_date', 'ideas', 'highlights', 'scientists', 'linkage', 'observations']




class TravelForm(forms.ModelForm):
    first_name= forms.CharField(max_length=30)
    last_name= forms.CharField(max_length=30)
    dob=forms.DateField()
    designation= forms.CharField(max_length=50)
    event= forms.CharField(max_length=50)
    venue= forms.CharField(max_length=50)
    start_date= forms.DateField()
    end_date= forms.DateField()
    number= forms.CharField(max_length=30)

    class Meta:
        model = trav1
        fields = ['first_name','last_name', 'dob', 'designation', 'event', 'venue', 'start_date', 'end_date', 'number']


class TravelForm2(forms.ModelForm):
    firstname=forms.CharField(max_length=30)
    lastname=forms.CharField(max_length=30)
    dob=forms.DateField()
    gender=forms.CharField(label='gender', widget=forms.RadioSelect(choices=GEND_CHOICES))
    nationality=forms.CharField(max_length=50)
    designation=forms.CharField(max_length=50)
    address=forms.CharField(max_length=100)
    mobile=forms.CharField(required=False)
    email = forms.EmailField(max_length=50)
    work_dept=forms.CharField(max_length=30)
    work_institute=forms.CharField(max_length=30)
    work_city=forms.CharField(max_length=30)
    work_state=forms.CharField(max_length=30)
    work_pin=forms.CharField(max_length=30)
    hod_name=forms.CharField(max_length=30)
    hod_mobile=forms.CharField(required=False)
    hod_email = forms.EmailField(max_length=50)
    degree = forms. CharField(label='degree', widget=forms.RadioSelect(choices=DEGREE))
    name1 = forms. CharField(max_length=50)
    date1 = forms.DateField()
    percentage1=forms.CharField(max_length=30)
    division1=forms.CharField(max_length=30)
    degree1 = forms. CharField(label='degree1', widget=forms.RadioSelect(choices=DEGREE1))
    name2 = forms. CharField(max_length=50)
    date2 = forms.DateField()
    percentage2=forms.CharField(max_length=30)
    division2=forms.CharField(max_length=30)
    other_degree= forms.CharField(max_length=50)
    name3 = forms. CharField(max_length=50)
    date3 = forms.DateField()
    percentage3=forms.CharField(max_length=30)
    division3=forms.CharField(max_length=30) 
    specification=forms.CharField(max_length=30)
    basic_salary=forms.CharField(max_length=30)
    event=forms.CharField(max_length=30)
    venue=forms.CharField(max_length=30)
    start_date=forms.DateField()
    end_date=forms.DateField()
    discipline=forms.CharField(label='discipline', widget=forms.RadioSelect())
    paper=forms.CharField(max_length=30)
    purpose=forms.CharField(max_length=30)
    org=forms.CharField(max_length=30)
    parent_org=forms.CharField(max_length=30)
    any_other=forms.CharField(max_length=30)
    cost=forms.CharField(max_length=30)
    amount=forms.CharField(max_length=30)
    dir_name=forms.CharField(max_length=30)
    name11=forms.CharField(max_length=30)
    title11=forms.CharField(max_length=30)
    volume11=forms.CharField(max_length=30)
    name12=forms.CharField(max_length=30)
    title12=forms.CharField(max_length=30)
    volume12=forms.CharField(max_length=30)
    csir_name=forms.CharField(max_length=30)
    csir_year=forms.CharField(max_length=30)
    csir_place=forms.CharField(max_length=30)
    csir_number=forms.CharField(max_length=30)
    csir_amount=forms.CharField(max_length=30)
    other_info=forms.CharField(max_length=30)
    agree=forms.CharField(label='agree', widget=forms.RadioSelect())


    class Meta:
        model = trav2
        fields = "__all__"


FLIGHT= [
    ('YES', 'YES'),
    ('NO', 'NO'),
    ]


AUTHORITY= [
    ('DIRECTOR','DIRECTOR'),
    ('REGISTRAR','REGISTRAR'),
    ('DEAN','DEAN'),
    ('FINANCE OFFICER','FINANCE OFFICER'),
    ('MEDICAL SUPERINDENT','MEDICAL SUPERINDENT'),
    ('OTHER','OTHER'),
]


class TravelForm3(forms.ModelForm):
    name=forms.CharField(max_length=50)
    address=forms.CharField(max_length=100)
    city=forms.CharField(max_length=30)
    state=forms.CharField(max_length=30)
    pin=forms.CharField(max_length=30)
    mobile=forms.CharField(required=False)
    email = forms.EmailField(max_length=50)
    type1=forms.CharField(max_length=50)
    venue=forms.CharField(max_length=50)
    date_from=forms.DateField()
    date_to=forms.DateField()
    amount=forms.CharField(max_length=50)
    airlines= forms.CharField(label='flight', widget=forms.RadioSelect(choices=FLIGHT))
    flight=forms.CharField(max_length=50)
    authority=forms.CharField(label='authority', widget=forms.RadioSelect(choices=AUTHORITY))


    class Meta:
        model = trav3
        fields = ['name','address', 'city', 'state', 'pin', 'mobile', 'email', 'type1', 'venue', 'date_from', 'date_to', 'amount', 'airlines', 'flight', 'authority']



class TravelForm4(forms.ModelForm):
    applicant=forms.CharField(max_length=30)
    designation=forms.CharField(max_length=50)
    work_dept=forms.CharField(max_length=100)
    work_institute=forms.CharField(max_length=30)
    work_city=forms.CharField(max_length=30)
    work_state=forms.CharField(max_length=30)
    work_pin=forms.CharField(max_length=30)
    mobile=forms.CharField(required=False)
    email = forms.EmailField(max_length=50)
    event=forms.CharField(max_length=50)
    venue=forms.CharField(max_length=30)
    start_date=forms.DateField()
    end_date=forms.DateField()   
    checkin_date=forms.DateField()
    checkout_date=forms.DateField()
    out_date=forms.DateField()
    in_date=forms.DateField()
    ideas=forms.CharField(max_length=255)
    highlights=forms.CharField(max_length=255)
    scientists=forms.CharField(max_length=255)
    linkage=forms.CharField(max_length=255)
    observations=forms.CharField(max_length=255)

    class Meta:
        model = trav4
        fields=['applicant', 'designation', 'work_dept', 'work_institute', 'work_city', 'work_state', 'work_pin', 'mobile', 'email', 'event', 'venue', 'start_date', 'end_date', 'checkin_date', 'checkout_date', 'out_date', 'in_date', 'ideas', 'highlights', 'scientists', 'linkage', 'observations']


EVENT_CHOICES= [
    ('REGIONAL', 'REGIONAL'),
    ('NATIONAL', 'NATIONAL'),
    ('INTERNATIONAL','INTERNATIONAL'),
    ]


class SymposiumForm(forms.ModelForm):
    society_name= forms.CharField(max_length=100)
    title= forms.CharField(max_length=100)
    event_type= forms.CharField(label='event', widget=forms.RadioSelect(choices=EVENT_CHOICES))
    venue= forms.CharField(max_length=50)
    city= forms.CharField(max_length=50) 
    start_date= forms.DateField()
    end_date= forms.DateField()
    chairperson= forms.CharField(max_length=50)
    secretary= forms.CharField(max_length=50)
    delegates= forms.CharField(max_length=30)
    expenditure= forms.IntegerField()
    required= forms.IntegerField()
    requested= forms.IntegerField()

    class Meta:
        model = symp1
        fields = ['society_name','title', 'event_type', 'venue', 'city', 'start_date', 'end_date', 'chairperson', 'secretary', 'delegates', 'expenditure', 'required', 'requested']



class SymposiumForm2(forms.ModelForm):
     org_name=forms.CharField(max_length=50)
     nature=forms.CharField(label='nature', widget=forms.RadioSelect())
     title=forms.CharField(max_length=50)
     discipline=forms.CharField(label='discipline', widget=forms.RadioSelect())
     address=forms.CharField(max_length=100)
     city=forms.CharField(max_length=30)
     state=forms.CharField(max_length=30)
     pin=forms.CharField(max_length=30)
     event_start=forms.DateField()
     event_end=forms.DateField()
     chair_name=forms.CharField(max_length=50)
     chair_org=forms.CharField(max_length=100)
     name=forms.CharField(max_length=30)
     gender=forms.CharField(label='gender', widget=forms.RadioSelect(choices=GEND_CHOICES))    
     person_desig=forms.CharField(max_length=50)
     person_dept=forms.CharField(max_length=50)
     person_inst=forms.CharField(max_length=100)
     person_add=forms.CharField(max_length=100)
     person_city=forms.CharField(max_length=30)
     person_state=forms.CharField(max_length=30)
     person_pin=forms.CharField(max_length=30)
     person_phone=forms.IntegerField(required=False)
     person_email = forms.EmailField(max_length=50)
     last_activity = forms.CharField(max_length=50)
     theme=forms.CharField(max_length=50)
     details=forms.CharField(max_length=255)
     relevance=forms.CharField(max_length=100)
     promotion=forms.CharField(max_length=255)
     csir_lab1=forms.CharField(max_length=100)
     theme1=forms.CharField(max_length=100)
     csir_lab2=forms.CharField(max_length=100)
     theme2=forms.CharField(max_length=100)
     sci_name1=forms.CharField(max_length=100)
     sci_lab1=forms.CharField(max_length=100)
     sci_name2=forms.CharField(max_length=100)
     sci_lab2=forms.CharField(max_length=100)
     permit=forms.CharField(label='permit', widget=forms.RadioSelect())
     national_no=forms.CharField(max_length=50)
     international_no=forms.CharField(max_length=50)
     phd_no=forms.CharField(max_length=50)
     postgrad_no=forms.CharField(max_length=50)
     speak_name1=forms.CharField(max_length=50)
     speak_institute1=forms.CharField(max_length=50)
     speak_name2=forms.CharField(max_length=50)
     speak_institute2=forms.CharField(max_length=50)
     speak_name3=forms.CharField(max_length=50)
     speak_institute3=forms.CharField(max_length=50)
     session_type=forms.CharField(label='session_type', widget=forms.RadioSelect())
     support_travel=forms.CharField(max_length=50)
     support_registration=forms.CharField(max_length=50)
     support_hospitality=forms.CharField(max_length=50)
     asenior_amount=forms.CharField(max_length=50)
     ayoung_amount=forms.CharField(max_length=50)
     asenior_regist=forms.CharField(max_length=50)
     ayoung_regist=forms.CharField(max_length=50)
     apromo_fee=forms.CharField(max_length=50)
     aassist_fee=forms.CharField(max_length=50)
     ahospitality=forms.CharField(max_length=50)
     avenue_fee=forms.CharField(max_length=50)
     aanti_expendtotal=forms.CharField(max_length=50)
     anti_regist=forms.CharField(max_length=50)
     anti_ehibit=forms.CharField(max_length=50)
     anti_grant=forms.CharField(max_length=50)
     anti_sponser=forms.CharField(max_length=50)
     anti_other=forms.CharField(max_length=50)
     anti_total=forms.CharField(max_length=50)
     esenior_amount=forms.CharField(max_length=50)
     eyoung_amount=forms.CharField(max_length=50)
     esenior_regist=forms.CharField(max_length=50)
     eyoung_regist=forms.CharField(max_length=50)
     epromo_fee=forms.CharField(max_length=50)
     eassist_fee=forms.CharField(max_length=50)
     ehospitality=forms.CharField(max_length=50)
     evenue_fee=forms.CharField(max_length=50)
     eanti_expendtotal=forms.CharField(max_length=50)
     rd_name1=forms.CharField(max_length=50)
     rd_req1=forms.CharField(max_length=50)
     rd_rec1=forms.CharField(max_length=50)
     rd_exp1=forms.CharField(max_length=50)
     rd_name2=forms.CharField(max_length=50)
     rd_req2=forms.CharField(max_length=50)
     rd_rec2=forms.CharField(max_length=50)
     rd_exp2=forms.CharField(max_length=50)
     rd_name3=forms.CharField(max_length=50)
     rd_req3=forms.CharField(max_length=50)
     rd_rec3=forms.CharField(max_length=50)
     rd_exp3=forms.CharField(max_length=50)
     csir_amount1=forms.CharField(max_length=50)
     csir_grant1=forms.CharField(max_length=50)
     csir_title1=forms.CharField(max_length=50)
     csir_audit1=forms.CharField(max_length=50)
     csir_amount2=forms.CharField(max_length=50)
     csir_grant2=forms.CharField(max_length=50)
     csir_title2=forms.CharField(max_length=50)
     csir_audit2=forms.CharField(max_length=50)
     csir_amount3=forms.CharField(max_length=50)
     csir_grant3=forms.CharField(max_length=50)
     csir_title3=forms.CharField(max_length=50)
     csir_audit3=forms.CharField(max_length=50)
     authority_name=forms.CharField(max_length=50)
     other_info=forms.CharField(max_length=255)
     org_sectname=forms.CharField(max_length=50)
     org_sectmobile=forms.IntegerField(required=False)
     org_sectemail=forms.EmailField()
     org_chairname=forms.CharField(max_length=50)
     org_chairmobile=forms.IntegerField(required=False)
     org_chairemail=forms.EmailField()
     org_headname=forms.CharField(max_length=50)
     org_headmobile=forms.IntegerField(required=False)
     org_heademail=forms.EmailField()
     
AUTHORITY1= [
    ('DIRECTOR','DIRECTOR'),
    ('REGISTRAR','REGISTRAR'),
    ('DEAN','DEAN'),
    ('FINANCE OFFICER','FINANCE OFFICER'),
    ('MEDICAL SUPERINDENT','MEDICAL SUPERINDENT'),
    ('PRINCIPAL','PRINCIPAL'),
    ('OTHER','OTHER'),
]

class SymposiumForm3(forms.ModelForm):
     organisation_name=forms.CharField(max_length=100)
     event_name=forms.CharField(max_length=100)
     venue=forms.CharField(max_length=100)
     start_date= forms.DateField()
     end_date= forms.DateField()
     grant_amount=forms.CharField(max_length=50)
     actual_amount=forms.CharField(max_length=50)
     claim_amount=forms.CharField(max_length=50)
     authority=forms.CharField(label='authority', widget=forms.RadioSelect(choices=AUTHORITY1))
     org_name=forms.CharField(max_length=50)
     org_desig=forms.CharField(max_length=50)
     org_add=forms.CharField(max_length=100)
     org_city=forms.CharField(max_length=50)
     org_state=forms.CharField(max_length=50)
     org_pin=forms.CharField(max_length=30)
     org_mobile=forms.IntegerField(required=False)
     org_email =forms.EmailField()
     head_name=forms.CharField(max_length=50)
     head_desig=forms.CharField(max_length=50)
     head_add=forms.CharField(max_length=100)
     head_city=forms.CharField(max_length=50)
     head_state=forms.CharField(max_length=50)
     head_pin=forms.CharField(max_length=30)
     head_mobile=forms.IntegerField(required=False)
     head_email =forms.EmailField()


     class Meta:
        model = symp3
        fields = ['organisation_name', 'event_name', 'venue', 'start_date', 'end_date', 'grant_amount', 'actual_amount', 'claim_amount',
		           'authority', 'org_name', 'org_desig', 'org_add', 'org_city', 'org_state', 'org_pin', 'org_mobile', 'org_email',
				   'head_name', 'head_desig', 'head_add', 'head_city', 'head_state', 'head_pin', 'head_mobile', 'head_email' ]


class SymposiumForm4(forms.ModelForm):
     society_name=forms.CharField(max_length=50)
     event_name=forms.CharField(max_length=50)
     start_date= forms.DateField()
     end_date= forms.DateField()
     grant_amount=forms.CharField(max_length=50)
     expenditure_amount=forms.CharField(max_length=50)
     csir_grant=forms.CharField(max_length=50)
     senior_amount=forms.CharField(max_length=50)
     young_amount=forms.CharField(max_length=50)
     senior_regist=forms.CharField(max_length=50)
     young_regist=forms.CharField(max_length=50)
     promo_fee=forms.CharField(max_length=50)
     assist_fee=forms.CharField(max_length=50)
     hospitality=forms.CharField(max_length=50)
     venue_fee=forms.CharField(max_length=50)
     expendtotal=forms.CharField(max_length=50)    
     org_name=forms.CharField(max_length=50)
     org_desig=forms.CharField(max_length=50)
     org_mobile=forms.IntegerField(required=False)
     org_email =forms.EmailField()
     fin_name=forms.CharField(max_length=50)
     fin_mobile=forms.IntegerField(required=False)
     fin_email =forms.EmailField()
     head_name=forms.CharField(max_length=50)
     head_desig=forms.CharField(max_length=50)
     head_mobile=forms.IntegerField(required=False)
     head_email =forms.EmailField()



     class Meta:
        model = symp4
        fields = ['society_name', 'event_name', 'start_date', 'end_date', 'grant_amount', 'expenditure_amount', 'csir_grant',
		           'senior_amount', 'young_amount', 'senior_regist', 'young_regist', 'promo_fee', 'assist_fee', 'hospitality',
				   'venue_fee', 'expendtotal', 'org_name', 'org_desig', 'org_mobile', 'org_email', 'fin_name', 'fin_mobile', 'fin_email',
				   'head_name', 'head_desig', 'head_mobile', 'head_email' ]