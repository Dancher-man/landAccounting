from django.db import models
from django.contrib.gis.db import models as giomodels


class Farmer(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя фермера')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'farmer'
        verbose_name_plural = 'Фермер'
        verbose_name = 'Фермеры'


class Culture(models.Model):
    name = models.CharField(max_length=200, verbose_name='Культура')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'culture'
        verbose_name_plural = 'Культура'
        verbose_name = 'Культуры'


class Season(models.Model):
    how_season = models.PositiveIntegerField(verbose_name='Сезон')

    def __str__(self):
        return str(self.how_season)

    class Meta:
        db_table = 'season'
        verbose_name_plural = 'Сезон'
        verbose_name = 'Сезоны'


class Plots(models.Model):
    contour = giomodels.MultiLineStringField(srid=4326)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='farmer_plots')
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE, related_name='farmer_cultures', null=True, blank=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='farmer_seasons')

    def __str__(self):
        return self.farmer.name

    def __unicode__(self):
        return self.contour

    class Meta:
        db_table = 'plots'
        verbose_name_plural = 'Поле'
        verbose_name = 'Поле'
