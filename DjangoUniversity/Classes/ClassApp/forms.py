from django.forms import ModelForm
from .models import DjangoClasses

class ClassesForm(ModelForm):
    class Meta:
        model = DjangoClasses
        fields = '__all__'