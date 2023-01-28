from django.contrib import admin

from app.models import Season, Culture, Farmer, Plots


@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    model = Farmer


@admin.register(Culture)
class FarmerAdmin(admin.ModelAdmin):
    model = Culture


@admin.register(Season)
class FarmerAdmin(admin.ModelAdmin):
    model = Season


@admin.register(Plots)
class PlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_farmers', 'get_cultures', 'get_seasons')
    list_display_links = ('id', 'get_farmers',)
    list_filter = ('farmer__name', 'season__how_season', 'culture__name')
    save_on_top = True
    save_as = True

    def get_farmers(self, obj):
        return obj.farmer.name

    def get_cultures(self, obj):
        if obj.culture is not None:
            return obj.culture.name
        else:
            return obj.culture

    def get_seasons(self, obj):
        return obj.season.how_season