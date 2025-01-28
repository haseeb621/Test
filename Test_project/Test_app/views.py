import csv
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from Test_app.models import CustomUser

def index(request):
 return render(request,'index.html')
def signup_view(request):
 if request.method=='POST':
  username=request.POST['username']
  email=request.POST['email']
  password=request.POST['password']
  password_confirm=request.POST['password_confirm']
  
  if password!=password_confirm:
   messages.error(request,'Passwords did not match ')
   return redirect('signup')
  user=User.objects.create_user(username=username,email=email,password=password)
  user.save()
  messages.error(request,'User created')
  return render(request,'index.html')
def login_view(request):
 if request.method == 'POST':
  uname = request.POST['uname']
  pass1 = request.POST['pass1']
  user = authenticate(username=uname, password=pass1)
  if user is not None:
   login(request, user)
   return redirect('index')
  else:
   messages.error(request, 'Username or password incorrect')
   return redirect('login')
 else:
  return render(request, 'login.html')

def logout_view(request):
  logout(request)
  messages.error(request,'Logged out')
  return redirect('index')

@login_required
def fetch_csv(request):
  fetched_data = []
  with open('C:/Users/HASHMI/OneDrive/Desktop/file.csv', 'r') as file:
   reader = csv.reader(file)
   for row in reader:
    cnic = row[1]  
    phone_number = row[3]  
    CustomUser.objects.create(cnic=cnic, phone_number=phone_number)
    fetched_data.append({'CNIC': cnic, 'Phone': phone_number})
  return render(request, 'index.html', {'fetched_data': fetched_data})

@login_required
def get_cnic(request, user_id):
  user = CustomUser.objects.get(id=user_id)
  # decrypted_cnic = user.decrypt_cnic()
  return render(request, 'index.html')