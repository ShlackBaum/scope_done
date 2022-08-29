from django.views.generic import ListView
from django.shortcuts import render

from school.models import Student, Teacher

def students_list(request):
    template = 'school/students_list.html'
    teacher_objects = Teacher.objects.all()
    student_objects = Student.objects.all()

    context = {"teachers": teacher_objects,
               "students": student_objects}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
