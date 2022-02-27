from django.views.generic import ListView
from django.shortcuts import render
from django.db.models import Prefetch
from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    object_list = Student.objects.order_by(ordering).prefetch_related('teacher')
    context = {'object_list': object_list}
    return render(request, template, context)
