from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=40)
    preco = models.CharField(max_length=9)
    descricao = models.CharField(max_length=11)
    categoria = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nome
    