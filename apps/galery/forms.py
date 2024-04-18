from django import forms
from apps.galery.models import Photo

class PhotoForms(forms.ModelForm):

    # Overrideing __init__ to get request.user
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(PhotoForms, self).__init__(*args, **kwargs)

    class Meta:
        model = Photo
        exclude = ['publish', 'user']
    
        labels = {
            'name': 'Nome',
            'subtitle': 'Legenda',
            'description': 'Descrição',
            'category': 'Categoria',
            'date': 'Data de registro',
            'photoPath': 'Arquivo de imagem',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'photoPath': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                }
            ),
        }

    # Overriding save method
    def save(self, commit=True):
        instance = super(PhotoForms, self).save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance