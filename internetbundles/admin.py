from django.contrib import admin
from .models import SpeedBundles

# model admin class for the SpeedBundles model
class SpeedBundlesModelAdmin(admin.ModelAdmin):
    list_display = ["bundle_name", "bundle_speed", "bundle_price", "bundle_vat"]
    list_filter = ["bundle_name", "bundle_speed"]
    search_fields = ["bundle_name", "bundle_speed", "bundle_price", "bundle_vat"]

    class Meta:
        model = SpeedBundles

# Register SpeedBundles model
admin.site.register(SpeedBundles, SpeedBundlesModelAdmin)