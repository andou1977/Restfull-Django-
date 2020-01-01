from django.db import models


# Create your models here.

class Utilisateur(models.Model):
    nom_utilisateur = models.CharField(max_length=50)
    pseudo = models.CharField(max_length=50)
    droit = models.CharField(max_length=50)
    etat = models.CharField(max_length=50)
    password = models.CharField(max_length=50)







class Institution(models.Model):
    nom_institution = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fondateur = models.CharField(max_length=50)
    date = models.DateField()

    class Meta:
        ordering = ('nom_institution',)

    def __str__(self):
        return self.nom_institution


class Faculter(models.Model):
    nom_faculte = models.CharField(max_length=50)
    no_institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_faculte

    class Meta:
        ordering = ('nom_faculte',)


class Option(models.Model):
    nom_option = models.CharField(max_length=50)
    moyenne = models.CharField(max_length=50)
    nbre_de_cours = models.IntegerField()
    no_faculter = models.ForeignKey(Faculter, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_option

    class Meta:
        ordering = ('nom_option',)


class Expert(models.Model):
    nom_expert = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=50)
    universiter = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    option = models.CharField(max_length=50)
    no_faculter = models.ForeignKey(Faculter,on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_expert

    class Meta:
        ordering = ('nom_expert',)


