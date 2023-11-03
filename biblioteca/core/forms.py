from django import forms
from django.core.exceptions import ValidationError
from core.models import LivroModel


def validate_titulo(titulo):
    if len(titulo) < 3:
        raise ValidationError('Deve ter pelo menos 3 caracteres')
    
def validate_editora(editora):
    if len(editora) < 3:
        raise ValidationError('Deve ter pelo menos 3 caracteres')
    
def validate_autor(autor):
    if len(autor) < 10:
        raise ValidationError('Deve ter pelo menos 10 caracteres')
    
def validate_isbn(isbn):
    numero_str = str(isbn)
    if len(numero_str) != 13:
        raise ValidationError('Deve ter 13 caracteres')
    
def validate_paginas(paginas):
    if paginas < 1 or  paginas > 999:
        raise ValidationError('Deve ter de 1 a 3 caracteres')
    

def validate_ano(ano):
    numero_str = str(ano)
    if len(numero_str) != 4:
        raise ValidationError('Deve ter 4 caracteres')
    
    



class LivroForm(forms.ModelForm):

    class Meta:
        model = LivroModel
        fields = ['titulo', 'editora','autor','isbn','paginas','ano']
        error_messages = {
            'titulo': {
                'required': ("Informe o título do livro."),
            },
            'editora': {
                'required': ("Informe a editora do livro."),
            },
            'autor': {
                'required': ("Informe o autor do livro."),
            },
            'isbn': {
                'required': ("Informe a ISBN do livro."),
            },
            'paginas': {
                'required': ("Informe o número de páginas do livro."),
            },
            'ano': {
                'required': ("Informe o ano do livro."),
            },

        }

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        validate_titulo(titulo)
        return titulo

    def clean_editora(self):
        editora = self.cleaned_data['editora']
        validate_editora(editora)
        return editora
    
    def clean_autor(self):
        autor = self.cleaned_data['autor']
        validate_autor(autor)
        return autor

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        validate_isbn(isbn)
        return isbn
    
    def clean_paginas(self):
        paginas = self.cleaned_data['paginas']
        validate_paginas(paginas)
        return paginas

    def clean_ano(self):
        ano = self.cleaned_data['ano']
        validate_ano(ano)
        return ano
    
    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data

