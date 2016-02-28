from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django import forms 
from django_boto.s3 import upload

# Create your views here.

def index(request):
  return HttpResponse("INDEX")

class UploadFileForm(forms.Form):
   file = forms.FileField()

def upload_file(request): 
  if request.method=='GET' or request.method !='POST':
    form =UploadFileForm()
    return render(request, "employees/upload_file.html",{'form': form})
  
  form = UploadFileForm(request.POST, request.FILES)
  if form.is_valid():
    upload_path = upload(request.FILES['file'])
#    e = UserProfile(user=request.user)
#    e.photo = upload_path
# 
    print upload_path
    
  return HttpResponse("Uploaded")




# 
# if form.is_valid():
#   print request.FILES['file']
#   upload_path = upload(request.FILES['file'])
#   print upload_path
#   photo = Photo()
#   photo.photo =upload_path
#   photo.save()
#   listing.photos.add(photo)


# e=employee()
# e.user = User.objects.all()[0]
# e.company = Company.objects.all()[0]


