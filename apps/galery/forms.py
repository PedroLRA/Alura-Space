from django import forms
from apps.galery.models import Photo

class PhotoForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.edit = kwargs.pop('edit', False)
        super(PhotoForms, self).__init__(*args, **kwargs)

        if self.edit:
            self.fields['photoPath'].widget = forms.HiddenInput()

    class Meta:
        model = Photo
        
        fields = [
            'name',
            'subtitle',
            'description',
            'category',
            'date',
            'photoPath'
        ]

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

    def save(self, commit=True):
        instance = super(PhotoForms, self).save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance
