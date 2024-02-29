from django.shortcuts import render, HttpResponse #import HttpResponse
from .models import*
# Create your views here.
# file: appName/views.py


def home(request):
  books = Book.objects.all()
  data={
    'books':books
  }
  return render(request, 'home.html',data)


def about(request):
    team_members = TeamMember.objects.all()
    return render(request, 'about.html', {'team_members': team_members})

def contact_us(request):
  return render(request, 'contact.html')

def Custom_Order(request):
  success = False
  if request.method =='POST':
      name  = request.POST.get('name')
      email  = request.POST.get('email')
      phone = request.POST.get('phone')
      text  = request.POST.get('text')

      user_text = Custom(name=name, email=email, phone=phone, text=text)
      user_text.save()
      success = True
  return render(request, 'Custom_Order.html', {'success': success})

