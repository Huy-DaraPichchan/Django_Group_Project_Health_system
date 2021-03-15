from django.shortcuts import render, redirect
from .models import Covid_Report, Symptom_Analysis
# Create your views here.


def index(request):
    covid = Covid_Report.objects.all()
    return render(request, "index.html", {'covid': covid})


def symptom_analysis(request):
    if request.method == "POST":
        sa = Symptom_Analysis(
            q1=True if request.POST['q1'] == 'Yes' else False,
            q2=True if request.POST['q2'] == 'Yes' else False,
            q3=True if request.POST['q3'] == 'Yes' else False,
            q4=True if request.POST['q4'] == 'Yes' else False,
            q5=True if request.POST['q5'] == 'Yes' else False,
        )
        count = 5
        for x in request.POST.values():
            if x == "No":
                count -= 1

        sa.save()
        # , {'count': count}
        return render(request, 'result.html', {'count': count})
    else:
        return render(request, "symptom_analysis.html")


def result(request):
    return render(request, "result.html")
