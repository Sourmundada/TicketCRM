from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from accounts.models import Staff

class Ticket(models.Model):

    STATUS_CHOICE = (
        ('Draft', 'Draft'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Archived', 'Archived'),
    )

    name = models.CharField(max_length=200, unique=True)
    description = RichTextUploadingField(blank=True, null=True)
    assigned_to = models.ForeignKey(Staff, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=100, choices=STATUS_CHOICE, default='Draft')

    def __str__(self):
        return self.name

class Attachment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/uploads/', null=True)

    def __str__(self):
        return self.ticket.name