from django.contrib import admin
from RIGS import models
import reversion

# Register your models here.
admin.site.register(models.Person, reversion.VersionAdmin)
admin.site.register(models.Organisation, reversion.VersionAdmin)
admin.site.register(models.VatRate, reversion.VersionAdmin)