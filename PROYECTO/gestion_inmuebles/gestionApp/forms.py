from django import forms
from django.contrib.auth.models import User
from .models import Usuario, TipoUsuario, Region, Comuna, TipoInmueble

#Clase para registrar usuario
class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    tipo_usuario = forms.ModelChoiceField(queryset=TipoUsuario.objects.all(), empty_label="Seleccione tipo de usuario")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            tipo_usuario = self.cleaned_data['tipo_usuario']
            Usuario.objects.create(
                nombre=self.cleaned_data['username'],
                apellido='',
                tipo_usuario=tipo_usuario
            )
        return user

#Clase para actualizar usuario
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


#buscador de inmuebles
class PropertySearchForm(forms.Form):
    tipo_inmueble = forms.ModelChoiceField(queryset=TipoInmueble.objects.all(), required=False, label="Tipo de Inmueble")
    region = forms.ModelChoiceField(queryset=Region.objects.all(), required=False, label="Región", widget=forms.Select(attrs={'class': 'region-select'}))
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.none(), required=False, label="Comuna", widget=forms.Select(attrs={'class': 'comuna-select'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['comuna'].queryset = Comuna.objects.filter(region_id=region_id).order_by('nombre')
            except (ValueError, TypeError):
                pass
        elif self.initial.get('region'):
            self.fields['comuna'].queryset = Comuna.objects.filter(region=self.initial['region']).order_by('nombre')

