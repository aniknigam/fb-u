from django.shortcuts import render, redirect
from .models import Requirement

# Create your views here.
def requirement(mssg):
    # if request.method == "POST":
    # requirement_text = request.POST.get("requirement")
    requirement_text = mssg
    
    req = Requirement(requirement_text=requirement_text)
    
    req.save()
    # messages.success(request, " Your requirement has been posted")
    print("Your requirement has been posted")
    return
    
    # else:
    #     return render(request, 'postrequirement/requirementlist.html')
    
def requirementlist(request):
    if request.method == "POST":
        requirement_text = request.POST.get("requirement")
        requirement(requirement_text)
    req = Requirement.objects.all()
    return render(request, 'postrequirement/requirementlist.html', {'requirements': req})
