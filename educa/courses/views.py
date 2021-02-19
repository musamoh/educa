from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from .models import Course, Module, Subject
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin



class OwnerMixin(object):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin, PermissionRequiredMixin):
    model = Course
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')

class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    template_name ='course/manage/course/list.html'


class ManageCourseListView(OwnerCourseMixin, ListView):
    template_name = 'course/manage/course/list.html'
    permission_required = 'courses.view_course'

class CourseCreateView(OwnerCourseEditMixin, CreateView):
    template_name = 'course/manage/course/form.html'
    permission_required ='course.add_course'


class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    template_name = 'course/manage/course/form.html'
    permission_required ='course.change_course'


class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name = 'course/manage/course/delete.html'
    permission_required ='course.delete_course'


