from django.contrib.auth.forms import UserCreationForm      #formulario predefinido, que ya viene de la libreria auth.forms
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm): #se pasa por parametro a la clase el formulario UsercreationForm
    email=forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido")
    class Meta:
        model=User
        fields= ("username","email", "password1","password2")

    def clean_email(self):
        email=self.cleaned_data.get("email") #recupera el email resgitrado en el formulario
        if User.objects.filter(email=email).exists(): #valida si el email esta en la base de datos
            raise forms.ValidationError("El email ya esta registrado, prueba con otro.")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ['avatar', 'bio', 'link']
        widgets={'avatar':forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
                 'Bio':forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Biografia'}),
                 'link':forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace'}),
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido")

    class Meta:
        model= User
        fields= ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")  # recupera el email resgitrado en el formulario
        if User.objects.filter(email=email).exists():  # valida si el email esta en la base de datos
            raise forms.ValidationError("El email ya esta registrado, prueba con otro.")
        return email
