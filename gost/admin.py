from django.contrib import admin

from .models import *


class AdminGost33259AvailabilityFlange(admin.ModelAdmin):
    list_display = (
        'pn', 'type_fl', 'dn_10', 'dn_15', 'dn_20', 'dn_25', 'dn_32', 'dn_40', 'dn_50',
        'dn_65', 'dn_80', 'dn_100', 'dn_125', 'dn_150', 'dn_200', 'dn_250', 'dn_300',
        'dn_350', 'dn_400', 'dn_450', 'dn_500', 'dn_600', 'dn_700', 'dn_800', 'dn_900',
        'dn_1000', 'dn_1200', 'dn_1400', 'dn_1600', 'dn_1800', 'dn_2000', 'dn_2200',
        'dn_2400', 'dn_2600', 'dn_2800', 'dn_3000', 'dn_3200', 'dn_3400', 'dn_3600', 'dn_4000',
    )


class AdminGost33259Type01(admin.ModelAdmin):
    list_display = (
        'id', 'dn_passage', 'dn_passage', 'pn', 'dv_lower', 'b_lower', 'c1_lower', 'd',
        'd1', 'd_lower', 'n_lower', 'pin',
    )
    list_filter = ('dn_passage',)


class AdminGost33259Type02(admin.ModelAdmin):
    list_display = (
        'id', 'dn_passage', 'pn', 'd0', 'd2', 'dv_lower', 'b_lower', 'b1_lower', 'c_lower',
        'c1_lower', 'd', 'd1', 'd_lower', 'n_lower', 'pin',
    )
    list_filter = ('dn_passage',)


class AdminGost33259Type11(admin.ModelAdmin):
    list_display = (
        'id', 'dn_passage', 'dm', 'dn', 'd1_lower', 'b_lower', 'h', 'h1', 'd', 'd1', 'd_lower',
        'n_lower', 'pin',
    )
    list_filter = ('dn_passage',)


class AdminGost33259SurfaceValues(admin.ModelAdmin):
    list_display = (
        'id', 'dn_passage', 'pn', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11',
        'b2_lower', 'h_lower', 'h1_lower', 'h2_lower', 'h3_lower', 'h4_lower', 'h5_lower',
    )
    empty_value_display = 'пусто'


class AdminGost33259Mass(admin.ModelAdmin):
    list_display = (
        'dn_passage', 'type_fl', 'pn_1', 'pn_2', 'pn_6', 'pn_10', 'pn_16', 'pn_25', 'pn_40',
        'pn_63', 'pn_100', 'pn_160', 'pn_200',
    )


class AdminGost33259TypeDrawing(admin.ModelAdmin):
    list_display = (
        'id', 'type_fl', 'flange_drawing',
    )


class AdminGost33259SurfaceDrawing(admin.ModelAdmin):
    list_display = (
        'id', 'surface_fl', 'surface_drawing',
    )


admin.site.register(Gost33259AvailabilityFlange, AdminGost33259AvailabilityFlange)
admin.site.register(Gost33259Type01, AdminGost33259Type01)
admin.site.register(Gost33259Type02, AdminGost33259Type02)
admin.site.register(Gost33259Type11, AdminGost33259Type11)
admin.site.register(Gost33259SurfaceValues, AdminGost33259SurfaceValues)
admin.site.register(Gost33259Mass, AdminGost33259Mass)
admin.site.register(Gost33259TypeDrawing, AdminGost33259TypeDrawing)
admin.site.register(Gost33259SurfaceDrawing, AdminGost33259SurfaceDrawing)
