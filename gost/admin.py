from django.contrib import admin

from .models import Gost33259_flange

class AdminGost33259(admin.ModelAdmin):
    list_display = (
        'id', 'dn_passage', 'pn', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11', 'b2_lower', 'h_lower',
        'h1_lower', 'h2_lower', 'h3_lower', 'h4_lower', 'h5_lower', 'dm', 'dn', 'd1_lower', 'b_lower', 'h', 'd', 'd1',
        'd_lower', 'n_lower', 'pin'
        )
    list_filter = ('dn_passage',)
    empty_value_display = 'пусто'


admin.site.register(Gost33259_flange, AdminGost33259)
