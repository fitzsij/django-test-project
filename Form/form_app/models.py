from django.db import models

# Create your models here.

class Package (models.Model):
	name = models.CharField(max_length=50)
	product_number = models.CharField(max_length=12)
	description = models.CharField(max_length=255)
	def __unicode__(self):
		return self.name + " - " + self.product_number

class PackageRevision (models.Model):
	package = models.ForeignKey(Package)
	version = models.CharField(max_length=100)
	date_created = models.DateTimeField(null=True, blank=True)
	def __unicode__(self):
		return str(self.package) + " - " + self.version
