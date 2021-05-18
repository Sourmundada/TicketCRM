from django import forms
from django.forms.widgets import TextInput, Textarea
from .models import Ticket, Attachment
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class TicketForm(forms.ModelForm):
    
    name = forms.CharField(label='', widget=TextInput(attrs={'placeholder': 'Enter Ticket Name', 'class': 'form-control'}))
    description = forms.CharField(label='', widget=CKEditorUploadingWidget(attrs={'placeholder': 'Write Project Description'}))



    class Meta:
        model = Ticket
        fields = ['name', 'description', 'assigned_to', 'status']

class AttachmentForm(forms.ModelForm):

    class Meta:
        model = Attachment
        fields = ['ticket', 'file']