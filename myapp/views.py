from django.shortcuts import render
from . models import *
from . models import balance



# Create your views here.

def RegisterPage(request):
    return render(request,'app/register.html')


#view for user registration

def UserRegister(request):
    if request.method == "POST":
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        contact=request.POST["contact"]
        password=request.POST["password"]
        cpassword=request.POST["cpassword"]

        #validate that user already exist

        user = User.objects.filter(Email=email)
        instance = balance(user = request.User, balance = 0)
        instance.save()
        
        if user:
            message="user already exist"
            return render(request,"app/register.html",{'msg':message})
        else:
            if password == cpassword:
                newuser=User.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password)
                message = "user register sucessfully"
                instance = balance(user = request.User, balance = 0)
                instance.save()
                return render(request,"app/login.html",{'msg':message,})
            else:
                message = "Password and Confirm Password does not match"
                return render(request,"app/register.html",{'msg':message})


#login view
def LoginPage(request):
    return render(request,"app/login.html")

#login user

def LoginUser(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        #checking the email with database

        user=User.objects.get(Email=email)

        if user:
            if user.Password==password:
                request.session['Firstname']=user.Firstname
                request.session['Lastname']=user.Lastname
                request.session['Email']=user.Email
                return render(request,"app/home.html")
            else:
                message="Password does not match"
                return render(request,"app/login.html",{'msg':message})
    else:
        message="User does not exist"
        return render(request,"app/register.html",{'msg':message})



# balance request

def profile(request):
    user = balance.objects.get(user=request.user)
    return render(request,'profile.html',{"balance":user.balance})


# request for transfer  of reciving  nmoney
def profile(request):
    msg=""
    if request.method == "POST":
        try:
            username = request.POST["username"]
            amount = request.POST["amount"]
            senderUser= User.objects.get(username=request.user.username)
            receiverUser=User.objects.get(username=username)
            sender = balance.objects.get(user = senderUser)
            receiver = balance.objects.get(user = receiverUser)           
            sender.balance = sender.balance - int(amount)
            receiver.balance = receiver.balance + int(amount)
            sender.save()
            receiver.save()
            msg = "Transaction Success"
        except Exception as e:
            print(e)
            msg = "Transaction Failure, Please check and try again"
    user = balance.objects.get(user=request.user)
    return render(request,'home.html',{"balance":user.balance,"msg":msg})