from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from employee.models import Employee,Department,Section
@login_required
def dashboard(request):
    context = {
        'count_employees': Employee.objects.all().count(),
        'count_dep': Department.objects.all().count(),
        'count_section': Section.objects.all().count(),
    }
    return render(request, 'dashboard.html', context)


# Create your views here.
