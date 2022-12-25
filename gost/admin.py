from django.contrib import admin

from .models import *


class AdminGost33259(admin.ModelAdmin):
    list_display = (
        'id', 'dn_passage', 'pn', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11', 'b2_lower', 'h_lower',
        'h1_lower', 'h2_lower', 'h3_lower', 'h4_lower', 'h5_lower', 'dm', 'dn', 'd1_lower', 'b_lower', 'h', 'd', 'd1',
        'd_lower', 'n_lower', 'pin',
        )
    list_filter = ('dn_passage',)
    empty_value_display = 'пусто'


class AdminGost33259Type(admin.ModelAdmin):
    list_display = (
        'id', 'type_fl', 'flange_drawing',
    )


class AdminGost33259Surface(admin.ModelAdmin):
    list_display = (
        'id', 'surface_fl', 'flange_surface',
    )


admin.site.register(Gost33259Flange, AdminGost33259)
admin.site.register(Gost33259Type, AdminGost33259Type)
admin.site.register(Gost33259Surface, AdminGost33259Surface)
