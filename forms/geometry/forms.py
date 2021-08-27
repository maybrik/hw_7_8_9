from django import forms

from .models import Person


class TriangleCathetus(forms.Form):
    a = forms.IntegerField(label="Первый катет", help_text="Введите положительное целочисленное значение")
    b = forms.IntegerField(label="Второй катет", help_text="Введите положительное целочисленное значение")


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email')
    first_name = forms.CharField(label="Имя", max_length=20)
    last_name = forms.CharField(label="Фамилия", max_length=30)
    email = forms.EmailField(label="Электронная почта")
