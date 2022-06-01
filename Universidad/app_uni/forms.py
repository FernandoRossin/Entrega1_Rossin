from django import forms


class Curso_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()


class Estudiante_formulario(forms.Form):

   nombre = forms.CharField(max_length=40)
   apellido = forms.CharField(max_length=40)
   email = forms.EmailField()

class Profesor_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=40)

