from django.db import models

class LivroModel(models.Model):
    titulo  = models.CharField('Título ', max_length=200)
    editora = models.CharField('Editora', max_length=200)
    autor   = models.CharField('Autor  ', max_length=200)
    isbn    = models.IntegerField(null=True)
    paginas = models.IntegerField(null=True)
    ano     = models.IntegerField(null=True)
    
    def __str__(self):
        return self.titulo