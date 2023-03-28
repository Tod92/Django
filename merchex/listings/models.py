from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Band(models.Model):

    def __str__(self):
        return f'{self.name}'

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        ROCK = 'RO'
        ELECTRO = 'EL'
        DRUM_AND_BASS = 'DB'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(max_length=5,choices=Genre.choices)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    active = models.fields.BooleanField(default=True)
    #  Nous pouvons utiliser l'option null=True pour autoriser les valeurs NULL dans la base de données. Et lorsque
    #  nous créerons un formulaire pour créer ou modifier des objets Band , le fait de définir blank=True ici nous
    #  permettra de soumettre ce formulaire avec une zone de texte vide pour ce champ.
    official_homepage = models.fields.URLField(null=True, blank=True)

class Listing(models.Model):

    class Type(models.TextChoices):
        RECORDS = 'RE'
        CLOTHINGS = 'CL'
        POSTERS = 'PO'
        MISCELLANEOUS = 'MI'

    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null=True)
    type = models.fields.CharField(max_length=5,choices=Type.choices)