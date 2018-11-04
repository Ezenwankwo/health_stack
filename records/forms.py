from django import forms

from .models import Folder, File


class FolderForm(forms.ModelForm):

    class Meta:
        model = Folder
        widgets = {'date_of_birth': forms.DateInput(attrs={'class': 'datepicker'})}
        fields = ['full_name', 'gender', 'date_of_birth',]


class FileForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ['hospital_name', 'folder', 'file']
