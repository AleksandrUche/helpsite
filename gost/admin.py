from django.contrib import admin

from .models import *


@admin.register(Gost33259AvailabilityFlange)
class AdminGost33259AvailabilityFlange(admin.ModelAdmin):
    # list_display = (
    #     'id', 'pn', 'type_fl', 'dn_10', 'dn_15', 'dn_20', 'dn_25', 'dn_32', 'dn_40', 'dn_50',
    #     'dn_65', 'dn_80', 'dn_100', 'dn_125', 'dn_150', 'dn_200', 'dn_250', 'dn_300',
    #     'dn_350', 'dn_400', 'dn_450', 'dn_500', 'dn_600', 'dn_700', 'dn_800', 'dn_900',
    #     'dn_1000', 'dn_1200', 'dn_1400', 'dn_1600', 'dn_1800', 'dn_2000', 'dn_2200',
    #     'dn_2400', 'dn_2600', 'dn_2800', 'dn_3000', 'dn_3200', 'dn_3400', 'dn_3600', 'dn_4000',
    # )
    list_display = [field.name for field in Gost33259AvailabilityFlange._meta.get_fields()]


@admin.register(Gost33259Type01)
class AdminGost33259Type01(admin.ModelAdmin):
    # list_display = (
    #     'id', 'dn_passage', 'dn_passage', 'pn', 'dv_lower', 'b_lower', 'c1_lower', 'd',
    #     'd1', 'd_lower', 'n_lower', 'pin',
    # )
    list_display = [field.name for field in Gost33259Type01._meta.get_fields()]
    list_filter = ('dn_passage',)


@admin.register(Gost33259Type02)
class AdminGost33259Type02(admin.ModelAdmin):
    # list_display = (
    #     'id', 'dn_passage', 'pn', 'd0', 'd2', 'dv_lower', 'b_lower', 'b1_lower', 'c_lower',
    #     'c1_lower', 'd', 'd1', 'd_lower', 'n_lower', 'pin',
    # )
    list_display = [field.name for field in Gost33259Type02._meta.get_fields()]
    list_filter = ('dn_passage',)


@admin.register(Gost33259Type11)
class AdminGost33259Type11(admin.ModelAdmin):
    # list_display = (
    #     'id', 'dn_passage', 'dm', 'dn', 'd1_lower', 'b_lower', 'h', 'h1', 'd', 'd1', 'd_lower',
    #     'n_lower', 'pin',
    # )
    list_display = [field.name for field in Gost33259Type11._meta.get_fields()]
    list_filter = ('dn_passage',)


@admin.register(Gost33259SurfaceValues)
class AdminGost33259SurfaceValues(admin.ModelAdmin):
    # list_display = (
    #     'id', 'dn_passage', 'pn', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11',
    #     'b2_lower', 'h_lower', 'h1_lower', 'h2_lower', 'h3_lower', 'h4_lower', 'h5_lower',
    # )
    list_display = [field.name for field in Gost33259SurfaceValues._meta.get_fields()]
    empty_value_display = 'пусто'


@admin.register(Gost33259Mass)
class AdminGost33259Mass(admin.ModelAdmin):
    # list_display = (
    #     'id', 'dn_passage', 'type_fl', 'pn_1', 'pn_2', 'pn_6', 'pn_10', 'pn_16', 'pn_25', 'pn_40',
    #     'pn_63', 'pn_100', 'pn_160', 'pn_200',
    # )
    list_display = [field.name for field in Gost33259Mass._meta.get_fields()]


@admin.register(Gost33259TypeDrawing)
class AdminGost33259TypeDrawing(admin.ModelAdmin):
    # list_display = (
    #     'id', 'type_fl', 'flange_drawing',
    # )
    list_display = [field.name for field in Gost33259TypeDrawing._meta.get_fields()]


@admin.register(Gost33259SurfaceDrawing)
class AdminGost33259SurfaceDrawing(admin.ModelAdmin):
    # list_display = (
    #     'id', 'surface_fl', 'surface_drawing',
    # )
    list_display = [field.name for field in Gost33259SurfaceDrawing._meta.get_fields()]


@admin.register(Atk261813FlangeExec1)
class AdminAtk261813FlangeExec1(admin.ModelAdmin):
    list_display = [field.name for field in Atk261813FlangeExec1._meta.get_fields()]


@admin.register(Atk261813FlangeExec2)
class AdminAtk261813FlangeExec2(admin.ModelAdmin):
    list_display = [field.name for field in Atk261813FlangeExec2._meta.get_fields()]


@admin.register(Atk261813FlangeExec3)
class AdminAtk261813FlangeExec3(admin.ModelAdmin):
    list_display = [field.name for field in Atk261813FlangeExec3._meta.get_fields()]


@admin.register(Atk261813FlangeExec4)
class AdminAtk261813FlangeExec4(admin.ModelAdmin):
    list_display = [field.name for field in Atk261813FlangeExec4._meta.get_fields()]


@admin.register(Atk261813FlangeExec5)
class AdminAtk261813FlangeExec5(admin.ModelAdmin):
    list_display = [field.name for field in Atk261813FlangeExec5._meta.get_fields()]


@admin.register(Atk261813FlangeExec6)
class AdminAtk261813FlangeExec6(admin.ModelAdmin):
    list_display = [field.name for field in Atk261813FlangeExec6._meta.get_fields()]


@admin.register(Atk261813FlangeDrawing)
class AdminAtk261813FlangeDrawing(admin.ModelAdmin):
    list_display = [field.name for field in Atk261813FlangeDrawing._meta.get_fields()]
