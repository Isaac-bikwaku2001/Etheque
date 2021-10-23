from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Auteur(models.Model):
    nom = models.CharField(max_length=200, null=True)
    prenom = models.CharField(max_length=200, null=True)
    nationalite = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nom

class Genre(models.Model):
    libelle = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.libelle

class Livre(models.Model):
    titre = models.CharField(max_length=300, null=True)
    langue = models.CharField(max_length=200, null=True)
    date_edition = models.DateField()
    image = models.ImageField(null=True, blank=True)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

class Exemplaire(models.Model):
    nombre_exemplaire = models.IntegerField()
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)

    def __str__(self):
        return "N° exemplaire: " + str(self.nombre_exemplaire) + " " + "Titre: "+ self.livre.titre

class Emprunt(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    date_emprunt = models.DateTimeField(auto_now_add=True)

