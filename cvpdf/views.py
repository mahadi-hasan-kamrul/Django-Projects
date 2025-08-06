from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Profile
import pdfkit
from django.template import loader
# Create your views here.
def index(request):

    if request.method == "POST":

        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        prof_tag = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        address = request.POST.get("address","")
        #degree = request.POST.get("degree","")
        school = request.POST.get("school","")
        university = request.POST.get("university","")
        previous_work = request.POST.get("previous_work","")
        previous_work_1 = request.POST.get("previous_work_1","")
        skills = request.POST.get("skills","")
        hobbies = request.POST.get("hobbies","")
        lang = request.POST.get("lang","")
        
        profile = Profile(name=name,email=email,phone=phone,summary=summary,school=school,
                          university=university,previous_work=previous_work,skills=skills,
                          previous_work_1=previous_work_1, hobbies=hobbies, lang=lang, prof_tag=prof_tag, address=address)
        profile.save()
    

   
    return render(request, 'cvpdf/accept.html')


def resume(request,id):
 

    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('cvpdf/resume1.html')
    html = template.render({'user_profile':user_profile})
    options ={

        'page-size':'Letter',
        'encoding':"UTF-8",
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] ='attachment'
    filename = "resume.pdf"
    return response

def test(request):
    return render(request, 'cvpdf/resume1.html')

def list(request):
    profiles = Profile.objects.all()
    return render(request,'cvpdf/list.html',{'profiles':profiles})