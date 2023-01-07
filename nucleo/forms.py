from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','bajada','contenido','imagen','categoria','etiquetas']

        widgets = {
            'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'bajada':forms.Textarea(attrs={'class':'form-control'}),
            'contenido':forms.Textarea(attrs={'class':'form-control'}),
            'imagen':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'categoria':forms.Select(attrs={'class':'form-control'}),
            'etiquetas':forms.SelectMultiple(attrs={'class':'form-control'}),
        }

