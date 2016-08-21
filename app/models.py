from django.db import models


class Site(models.Model):
    """
    A Site with several entries.
    """
    name = models.CharField("name", max_length=400, unique=True)

    def __str__(self):
        return "{} Site".format(self.name)


class DataEntry(models.Model):
    """
    A data row attached to a Site.
    """
    site = models.ForeignKey(to=Site, on_delete=models.CASCADE)
    date = models.DateField()
    a_value = models.FloatField()
    b_value = models.FloatField()

    def __str__(self):
        return "Data entry {} for site {}".format(self.id, self.site)
