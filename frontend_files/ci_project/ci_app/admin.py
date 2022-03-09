from django.contrib import admin
from ci_app.models.team_member import TeamMember
from ci_app.models.inventory import Inventory
# Register your models here.

admin.site.register(TeamMember)
admin.site.register(Inventory)