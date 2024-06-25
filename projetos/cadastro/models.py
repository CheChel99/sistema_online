from django.db import models

# Create your models here.
class Marca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    
    nome = models.CharField(max_length=20)
    telefone = models.CharField(max_length=25) 
    email = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nome} {self.telefone} - {self.email}' 