from django.shortcuts import render
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from plans.helpers import PlanMixin

from .forms import FolderForm, FileForm
from .models import Folder, File


class FolderCreateView(PlanMixin, SuccessMessageMixin, generic.CreateView):
    form_class = FolderForm
    template_name = 'record/create_folder.html'
    success_url = reverse_lazy('list_folder')
    success_message = "%(full_name)s folder was created successfully"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.account = self.request.user
        return super(FolderCreateView, self).form_valid(form)


class FolderListView(LoginRequiredMixin, generic.ListView):
    model = Folder
    paginate_by = 10
    template_name = 'record/list_folder.html'

    def get_queryset(self):
        qs = Folder.objects.all().filter(account=self.request.user)
        return qs


class FolderUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Folder
    fields = ['full_name', 'gender', 'date_of_birth',]
    template_name = 'record/update_folder.html'
    success_url = reverse_lazy('list_folder')
    success_message = "%(full_name)s folder was updated successfully"

    def get_queryset(self):
        qs = Folder.objects.all().filter(account=self.request.user)
        return qs

class FolderDetailView(LoginRequiredMixin, generic.DetailView):
    model = Folder
    template_name = 'record/detail_folder.html'


class FolderDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Folder
    template_name = 'record/delete_folder.html'
    success_url = reverse_lazy('list_folder')
    success_message = "You deleted %(full_name)s folder"

    def get_queryset(self):
        qs = Folder.objects.all().filter(account=self.request.user)
        return qs

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(FolderDeleteView, self).delete(request, *args, **kwargs)


class FileUploadView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = FileForm
    template_name = 'record/upload_file.html'
    success_url = reverse_lazy('list_file')
    success_message = "%(file)s file was uploaded successfully"

    def get_form(self, *args, **kwargs):
        form = super(FileUploadView, self).get_form(*args, **kwargs)
        form.fields['folder'].queryset = Folder.objects.filter(account=self.request.user)
        return form

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.account = self.request.user
        return super(FileUploadView, self).form_valid(form)


class FileUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = File
    fields = ['hospital_name', 'folder', 'file']
    template_name = 'record/update_file.html'
    success_url = reverse_lazy('list_file')
    success_message = "%(file)s file was updated successfully"

    def get_queryset(self):
        qs = File.objects.all().filter(account=self.request.user)
        return qs

    def get_form(self, *args, **kwargs):
        form = super(FileUpdateView, self).get_form(*args, **kwargs)
        form.fields['folder'].queryset = Folder.objects.filter(account=self.request.user)
        return form


class FileListView(LoginRequiredMixin, generic.ListView):
    model = File
    paginate_by = 10
    template_name = 'record/list_file.html'

    def get_queryset(self):
        qs = File.objects.all().filter(account=self.request.user)
        return qs


class FileDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = File
    template_name = 'record/delete_file.html'
    success_url = reverse_lazy('list_file')
    success_message = "You deleted %(file)s"

    def get_queryset(self):
        qs = File.objects.all().filter(account=self.request.user)
        return qs

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(FileDeleteView, self).delete(request, *args, **kwargs)
