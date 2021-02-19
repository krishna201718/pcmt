from django.shortcuts import render, HttpResponse, redirect
from .models import Account
from django.db import IntegrityError
from .decorator import allowed_users
from django.contrib.auth.decorators import login_required


@login_required(login_url='college:login')
def studentsRegistration(request):
    user = Account.object.get(email=request.user.email)
    if request.POST:
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.year = request.POST.get('year')
        user.semester = request.POST.get('semester')
        user.registration_no = request.POST.get('registration_no')
        user.university_roll = request.POST.get('university_roll_no')
        user.department = request.POST.get('department')
        user.gender = request.POST.get('gender')
        user.phone = request.POST.get('phone')
        user.address = request.POST.get('address')
        user.image = request.FILES.get("image")

        try:
            user.save()
            msg = 'Submitted successfully'
            color = 'success'
            return render(request, "registration.html", context={'msg': msg, 'color': color})
        except:
            msg = 'Pleas try to form correctly Email already Exist'
            color = 'danger'
            return render(request, "registration.html", context={'msg': msg, 'color': color})

    return render(request, "registration.html")


@login_required(login_url='college:login')
def student_data_view(request):
    if request.POST:
        if request.POST.get('university_roll'):
            university_roll = request.POST.get('university_roll')
            print('university_roll', university_roll)
            User = Account.object.filter(university_roll=university_roll)
            return render(request, "student_data_view.html", context={'user': User})
        else:
            year = request.POST.get('go_year')
            semester = request.POST.get('go_semester')
            print('year', year)
            print('semester', semester)

            User = Account.object.filter(semester=semester, year=year)
            return render(request, "student_data_view.html", context={'user': User})
    elif request.user.is_HOD:
        user = Account.object.filter(is_student=True, department=request.user.department)
        return render(request, "student_data_view.html", context={'user': user})
    elif request.user.is_admin:
        user = Account.object.filter(is_student=True)
        return render(request, "student_data_view.html", context={'user': user})

    elif request.user.is_BOC:
        user = Account.object.filter(is_student=True, year=request.user.year, semester=request.user.semester)
        return render(request, "student_data_view.html", context={'user': user})
    return render(request, "registration.html")
