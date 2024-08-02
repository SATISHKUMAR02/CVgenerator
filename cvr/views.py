from django.shortcuts import render, get_object_or_404
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
def accept(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        about = request.POST.get("about", "")
        school = request.POST.get("school", "")
        college = request.POST.get("college", "")
        experience = request.POST.get("experience", "")
        skills = request.POST.get("skills", "")
        profile = Profile(
            name=name,
            email=email,
            phone=phone,
            about=about,
            college=college,
            school=school,
            experience=experience,
            skills=skills
        )
        profile = Profile(name=name,email=email,phone=phone,about=about,school=school,college=college,experience=experience,skills=skills)
        profile.save()
 
    
    return render(request,'cvr/forms.html')

def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('cvr/resume.html')
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

def list(request):
    profile=Profile.objects.all()
    return render(request,'cvr/list.html',{'profile':profile})