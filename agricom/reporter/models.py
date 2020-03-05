from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
import os

# Create your models here.
image = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/default.jpg'))

class Borne(models.Model):
    name = models.CharField(max_length=250)
    east = models.FloatField()
    nord = models.FloatField()
    picture = models.ImageField(default=image)#on utilise défault pour l'image par défaut
    geom = models.PointField(srid=4326)
    objects = GeoManager()

    def __unicode__(self):
        return self.title
    @property
    def picture_url(self):
        return self.picture.url

    class meta:
        verbose_name_plural = 'Bornes'

class Region(models.Model):
    sce_geo = models.CharField(max_length=50)
    sce_sem = models.CharField(max_length=50)
    date = models.DateField()
    origine = models.CharField(max_length=50)
    region = models.CharField(max_length=3)
    nom = models.CharField(max_length=50)
    superficie = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def _unicode_(self):
        return self.counties
