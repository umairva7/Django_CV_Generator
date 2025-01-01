from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Education
import io, pdfkit
from django.http import HttpResponse
from django.template import loader

# Home view
def home(request):
    if request.user.is_authenticated:
        return render(request, 'list.html')  # Show dashboard for logged-in users
    return render(request, 'home.html')  # Show home page for guests

@login_required
def submit(request):
    if request.method == "POST":
        # Get education details
        degree = request.POST.get("degree")
        school = request.POST.get("school")
        university = request.POST.get("university")
        education = Education(degree=degree, school=school, university=university)
        education.save()

        # Get profile details
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        summary = request.POST.get("summary")
        experience = request.POST.get("experience")
        skills = request.POST.get("skills")

        # Save profile and link to education
        profile = Profile(name=name, email=email, number=number, summary=summary, experience=experience, skills=skills, education=education)
        profile.save()
        return redirect("waiting", id=profile.id)

    return render(request, "input.html")  # Render form

@login_required
def waiting(request, id):
    data = Profile.objects.get(pk=id)
    return render(request, 'waiting.html', {'profile': data})

@login_required
def generating(request, id):
    profile = Profile.objects.get(pk=id)
    skills_list = [skill.strip() for skill in profile.skills.split(",")] if profile.skills else []
    template = loader.get_template('resume.html')
    html = template.render({'profile': profile, 'skills_list': skills_list})
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
        'no-outline': None,
    }
    pdf = pdfkit.from_string(html, False, options=options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename="resume.pdf"'
    return response

@login_required
def list(request):
    profiles = Profile.objects.all()
    return render(request, 'list.html', {'profiles': profiles})
