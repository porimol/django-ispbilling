from django.contrib import admin
from .models import Clients, ClientUsageBundle

# ClientModelAdmin class define
class ClientModelAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "nid_number", "mobile_number", "email_address", "present_address"]
    list_filter = ["first_name"]
    search_fields = ["first_name", "last_name", "nid_number", "mobile_number", "email_address", "present_address"]

    # Django class meta
    class Meta:
        model = Clients

# ClientUsageBundleModelAdmin model admin class
class ClientUsageBundleModelAdmin(admin.ModelAdmin):
    list_display = ["client", "package", "subscription_fee", "service_charge"]
    list_filter = ["client", "package"]
    search_fields = ["client", "package", "subscription_fee", "service_charge"]

    # Django class meta
    class Meta:
        model = ClientUsageBundle

# Client model admin register
admin.site.register(Clients, ClientModelAdmin)

# ClientUsageBundle model admin register
admin.site.register(ClientUsageBundle, ClientUsageBundleModelAdmin)