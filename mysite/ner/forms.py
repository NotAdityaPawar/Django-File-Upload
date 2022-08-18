
from .models import File
from django.forms import ModelForm


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = '__all__'