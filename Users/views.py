import random
import smtplib
from email.message import EmailMessage

from django.conf import settings

from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
User=get_user_model()

# Create your views here.

def createAccount(request):
    
    if request.method=='POST':

        if 'AccountCreate' in request.POST:
            try:
                data=request.POST
                
                First_Name=data.get('First_Name')
                Last_Name=data.get('Last_Name')
                
                Email=data.get("Email")
                Password=data.get("Password")
                
                About_Me=data.get('About_Me')
                Phone_Number=data.get('Phone_Number')
                Location=data.get('Location')
                DoB=data.get('DoB')
                Gender=data.get("Gender")
                
                user=User.objects.create(
                    email=Email,
                    first_name=First_Name,
                    last_name=Last_Name,
                    about_me=About_Me,
                    phone_number=Phone_Number,
                    location=Location,
                    gender=Gender,
                    date_of_birth=DoB
                    )
                user.set_password(Password)
                user.save()
                
                messages.info(request," Account Created Successfully ^_^")
                
                print(f"Dob: {DoB}\nEmail: {Email}\nPassword: {Password}")
                return redirect("/login")
                
            except:
                messages.info(request, "Something Went wrong!!")
                return redirect("/createaccount")
        
        
    return render(request,"users/create_Account_page.html")

#-----------------------------------------------------------------------------------------------------------------------------------------
def loginAccount(request):
    
    next_url=request.GET.get('next','/')
    
    if request.method=='POST':
        data=request.POST
        
        Email=data.get('Email')
        Password=data.get('Password')
        
        is_user=User.objects.filter(email=Email)
        
        if is_user is None:
            messages.warning(request,"No User Found!!")
            return redirect("/login/")
        else:
            user=authenticate(email=Email,password=Password)
            
            if user is not None:
                login(request,user)
                messages.info(request,"Login Successful ^_^")
                return redirect(next_url)
            else:
                messages.info( request,"Invalid Details!!")
                return redirect ("/login/")
            
    return render(request, 'users/Login_page.html')

#-----------------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url='/login/')
def logoutAccount(request):
    
    logout(request)
    messages.info(request,"Logout!!")
    
    return redirect("/home")

#-----------------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url='/login/')
def userDashboard(request):
    
    return render(request, 'users/dashboard_Page.html')

#-----------------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url='/login/')
def userProfile(request):
    
    if request.user.is_verified ==0:
        messages.info(request,"Please Verify Your Email!!\nOtherwise After 356 Days your account will be deleted Permanently(From Last Login)")
        
    return render(request, 'users/profile_page.html')

#-----------------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url='/login/')
def verifyEmail(request):
    
    if request.user.is_verified:
        return redirect('/profile')
    
    if request.method=="POST":
        if 'SendEmail' in request.POST:
            try: 
                otp=''
                for i in range(6):
                    otp+=str(random.randint(0,9))
                    
                User.objects.filter(email=request.user.email).update(user_ott=otp)
                
                server=smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                print("You are here!!")
                ourEmail=settings.EMAIL_HOST_USER
                ourPass=settings.EMAIL_HOST_PASSWORD
                
                print(ourEmail,ourPass)
                server.login(ourEmail,ourPass)
                
                msg=EmailMessage()
                
                msg['Subject']= 'OTP Verification'
                
                msg['From']= ourEmail
                
                msg['To']= request.user.email
                
                msg.set_content(f"""\
                                Dear {request.user.first_name},

                                Your sign-in code for Heavenly Bytes is: 

                                🔢 {otp}

                                This code is usable for Until you request for new code. Keep it private and do not share it.

                                If this request was not made by you, simply ignore this email.

                                Best,  
                                Heavenly Bytes Team
                                """)
                
                server.send_message(msg)
                
                messages.info(request, "Check Your Mail!!")
                return redirect('/otpconformation/')
            except:
                messages.info(request, "Something wrong!!")
            
    return render(request, 'users/verify_email_page.html')


#-----------------------------------------------------------------------------------------------------------------------------------------
def otpConformation(request):
    
    if 'OTP_SUBMISSION' in request.POST:
            data=request.POST

            userInput=data.get('OTP')
            print(userInput,type(userInput))
            otp=User.objects.get(email=request.user.email).user_ott
            
            if otp==str(userInput):
                User.objects.filter(email=request.user.email).update(is_verified=True)
                User.objects.filter(email=request.user.email).update(user_ott='')
                messages.info(request, "Verified ^_^")
                return redirect('/profile/')
            else:
                messages.info(request, "Invaild OTP")
                
                
    return render(request,'users/otp_conformation_page.html')