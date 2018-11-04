from django.db import models
from django.urls import reverse
from django.conf import settings

from autoslug import AutoSlugField


class Folder(models.Model):
    MALE = "MA"
    FEMALE = "FE"
    NOTAPPLICABLE = "NA"
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NOTAPPLICABLE, 'Not Applicable'),
    )
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=2, choices=GENDER, default=MALE)
    date_of_birth = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='full_name', unique_with='created__day')

    class Meta:
        verbose_name = "Folder"
        verbose_name_plural = "Folders"
        ordering = ("-created",)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('detail_folder', kwargs={"slug": self.slug})


class File(models.Model):
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    hospital_name = models.CharField(max_length=255)
    file = models.FileField(upload_to='records/%Y-%m-%d')
    created = models.DateTimeField(auto_now_add=True)
    slug =  AutoSlugField(populate_from='hospital_name', unique_with='created__day')

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"
        ordering = ("-created",)

    def __str__(self):
        return '{0} - {1}'.format(self.folder, self.hospital_name)
