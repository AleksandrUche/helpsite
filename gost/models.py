from django.db import models


class Documents(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True, db_index=True, verbose_name="URL")
    description = models.CharField(max_length=200)
    cat_id = models.ForeignKey('CategoryDoc', on_delete=models.PROTECT, verbose_name="Категории")

    def __str__(self):
        return self.title


class CategoryDoc(models.Model):
    name = models.CharField(max_length=20, db_index=True)

    def __str__(self):
        return self.name


'''
Начало описания моделей для ГОСТ 33259-2015
'''


# наличие фланца в ГОСТ 33259-2015
class Gost33259AvailabilityFlange(models.Model):
    pn = models.CharField(max_length=6, verbose_name='PN')
    type_fl = models.CharField(max_length=6, verbose_name='Тип фланца')
    dn_10 = models.BooleanField(default=False)
    dn_15 = models.BooleanField(default=False)
    dn_20 = models.BooleanField(default=False)
    dn_25 = models.BooleanField(default=False)
    dn_32 = models.BooleanField(default=False)
    dn_40 = models.BooleanField(default=False)
    dn_50 = models.BooleanField(default=False)
    dn_65 = models.BooleanField(default=False)
    dn_80 = models.BooleanField(default=False)
    dn_100 = models.BooleanField(default=False)
    dn_125 = models.BooleanField(default=False)
    dn_150 = models.BooleanField(default=False)
    dn_200 = models.BooleanField(default=False)
    dn_250 = models.BooleanField(default=False)
    dn_300 = models.BooleanField(default=False)
    dn_350 = models.BooleanField(default=False)
    dn_400 = models.BooleanField(default=False)
    dn_450 = models.BooleanField(default=False)
    dn_500 = models.BooleanField(default=False)
    dn_600 = models.BooleanField(default=False)
    dn_700 = models.BooleanField(default=False)
    dn_800 = models.BooleanField(default=False)
    dn_900 = models.BooleanField(default=False)
    dn_1000 = models.BooleanField(default=False)
    dn_1200 = models.BooleanField(default=False)
    dn_1400 = models.BooleanField(default=False)
    dn_1600 = models.BooleanField(default=False)
    dn_1800 = models.BooleanField(default=False)
    dn_2000 = models.BooleanField(default=False)
    dn_2200 = models.BooleanField(default=False)
    dn_2400 = models.BooleanField(default=False)
    dn_2600 = models.BooleanField(default=False)
    dn_2800 = models.BooleanField(default=False)
    dn_3000 = models.BooleanField(default=False)
    dn_3200 = models.BooleanField(default=False)
    dn_3400 = models.BooleanField(default=False)
    dn_3600 = models.BooleanField(default=False)
    dn_4000 = models.BooleanField(default=False)

    def __str__(self):
        return self.pn


# Тип 01
class Gost33259Type01(models.Model):
    dn_passage = models.CharField(max_length=6, verbose_name='DN')
    pn = models.CharField(max_length=6, verbose_name='PN')
    dv_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='dв')
    b_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='b')
    c1_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='c1')
    d = models.CharField(blank=True, null=True, max_length=6, verbose_name='D')
    d1 = models.CharField(blank=True, null=True, max_length=6, verbose_name='D1')
    d_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='d')
    n_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='n')
    pin = models.CharField(blank=True, null=True, max_length=6, verbose_name='Диаметр шпилек')


# Тип 02
class Gost33259Type02(models.Model):
    dn_passage = models.CharField(max_length=6, verbose_name='DN')
    pn = models.CharField(max_length=6, verbose_name='PN')
    d0 = models.CharField(blank=True, null=True, max_length=6, verbose_name='D0')
    d2 = models.CharField(blank=True, null=True, max_length=6, verbose_name='D2')
    dv_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='dв')
    b_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='b')
    b1_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='b1')
    c_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='c')
    c1_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='c1')
    d = models.CharField(blank=True, null=True, max_length=6, verbose_name='D')
    d1 = models.CharField(blank=True, null=True, max_length=6, verbose_name='D1')
    d_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='d')
    n = models.CharField(blank=True, null=True, max_length=6, verbose_name='n')
    pin = models.CharField(blank=True, null=True, max_length=6, verbose_name='Диаметр шпилек')


# Тип 11
class Gost33259Type11(models.Model):
    dn_passage = models.CharField(max_length=6, verbose_name='DN')
    pn = models.CharField(max_length=6, verbose_name='PN')
    dm = models.CharField(blank=True, null=True, max_length=6, verbose_name='Dm')
    dn = models.CharField(blank=True, null=True, max_length=6, verbose_name='Dn')
    d1_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='d1')
    b_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='b')
    h = models.CharField(blank=True, null=True, max_length=6, verbose_name='H')
    h1 = models.CharField(blank=True, null=True, max_length=6, verbose_name='H1')
    d = models.CharField(blank=True, null=True, max_length=6, verbose_name='D')
    d1 = models.CharField(blank=True, null=True, max_length=6, verbose_name='D1')
    d_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='d')
    n_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='n')
    pin = models.CharField(blank=True, null=True, max_length=6, verbose_name='Диаметр шпилек')

    def __str__(self):
        return self.dn_passage

    class Meta:
        verbose_name = 'ГОСТ 33259-2015'
        verbose_name_plural = 'ГОСТ 33259-2015'
        ordering = ['id']


# уплотнительные поверхности для всех фланцев ГОСТ 33259
class Gost33259SurfaceValues(models.Model):
    dn_passage = models.CharField(max_length=6, verbose_name='DN')
    pn = models.CharField(max_length=6, verbose_name='PN')
    d2 = models.CharField(blank=True, null=True, max_length=6, verbose_name='D2')
    d3 = models.CharField(blank=True, null=True, max_length=6, verbose_name='D3')
    d4 = models.CharField(blank=True, null=True, max_length=6, verbose_name='D4')
    d5 = models.CharField(blank=True, null=True, max_length=6, verbose_name='D5')
    d6 = models.CharField(blank=True, null=True, max_length=6, verbose_name='D6')
    d7 = models.CharField(blank=True, null=True, max_length=6, verbose_name='D7')
    d8 = models.CharField(blank=True, null=True, max_length=6, verbose_name='D8')
    d9 = models.CharField(blank=True, null=True, max_length=6, verbose_name='D9')
    d10 = models.CharField(blank=True, null=True, max_length=6, verbose_name='D10')
    d11 = models.CharField(blank=True, null=True, max_length=6, verbose_name='D11')
    b2_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='b2')
    h_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='h')
    h1_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='h1')
    h2_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='h2')
    h3_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='h3')
    h4_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='h4')
    h5_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='h5')

    def __str__(self):
        return self.dn_passage


# чертеж типа фланца
class Gost33259TypeDrawing(models.Model):
    type_fl = models.CharField(max_length=6)
    flange_drawing = models.ImageField(upload_to="photos/%Y/%m/%d/")

    def __str__(self):
        return self.type_fl

    class Meta:
        verbose_name = 'типы'
        verbose_name_plural = 'Типы фланцев ГОСТ 33259-2015'


# чертеж уплотнительной поверхности фланца
class Gost33259SurfaceDrawing(models.Model):
    surface_fl = models.CharField(max_length=6)
    flange_surface = models.ImageField(upload_to="photos/%Y/%m/%d/")

    def __str__(self):
        return self.surface_fl

    class Meta:
        verbose_name = 'уплотнительные поверхности'
        verbose_name_plural = 'Уплотнительная поверхность ГОСТ 33259-2015'


'''
Конец описания моделей для ГОСТ 33259-2015
'''

'''
Начало описания моделей для АТК 26-18-13-96
'''


# Исполнение 1
class Atk261813FlangeExec1(models.Model):
    dn_passage = models.CharField(max_length=6, verbose_name='DN')
    pn = models.CharField(max_length=6, verbose_name='PN')
    d = models.CharField(max_length=6, verbose_name='D')
    d1 = models.CharField(max_length=6, verbose_name='D1')
    d2 = models.CharField(max_length=6, verbose_name='D2')
    d1_lower = models.CharField(max_length=6, verbose_name='d1')
    b_lower = models.CharField(max_length=6, verbose_name='b')
    h_lower = models.CharField(max_length=6, verbose_name='h')
    h1_lower = models.CharField(max_length=6, verbose_name='h1')
    dm = models.CharField(max_length=6, verbose_name='Dm')
    dn = models.CharField(max_length=6, verbose_name='Dn')
    d_lower = models.CharField(max_length=6, verbose_name='d')
    n_lower = models.CharField(max_length=6, verbose_name='n')
    m = models.CharField(max_length=6, verbose_name='Масса')


# Исполнение 2
class Atk261813FlangeExec2(models.Model):
    dn_passage = models.CharField(max_length=6, verbose_name='DN')
    pn = models.CharField(max_length=6, verbose_name='PN')
    d = models.CharField(max_length=6, verbose_name='D')
    d1 = models.CharField(max_length=6, verbose_name='D1')
    d4 = models.CharField(max_length=6, verbose_name='D4')
    d1_lower = models.CharField(max_length=6, verbose_name='d1')
    b_lower = models.CharField(max_length=6, verbose_name='b')
    h_lower = models.CharField(max_length=6, verbose_name='h')
    h2_lower = models.CharField(max_length=6, verbose_name='h2')
    dm = models.CharField(max_length=6, verbose_name='Dm')
    dn = models.CharField(max_length=6, verbose_name='Dn')
    d_lower = models.CharField(max_length=6, verbose_name='d')
    n_lower = models.CharField(max_length=6, verbose_name='n')
    m = models.CharField(max_length=6, verbose_name='Масса')


# Исполнение 3
class Atk261813FlangeExec3(models.Model):
    dn_passage = models.CharField(max_length=6, verbose_name='DN')
    pn = models.CharField(max_length=6, verbose_name='PN')
    d = models.CharField(max_length=6, verbose_name='D')
    d1 = models.CharField(max_length=6, verbose_name='D1')
    d2 = models.CharField(max_length=6, verbose_name='D2')
    d6 = models.CharField(max_length=6, verbose_name='D6')
    d1_lower = models.CharField(max_length=6, verbose_name='d1')
    b_lower = models.CharField(max_length=6, verbose_name='b')
    h_lower = models.CharField(max_length=6, verbose_name='h')
    h1_lower = models.CharField(max_length=6, verbose_name='h1')
    h2_lower = models.CharField(max_length=6, verbose_name='h2')
    dm = models.CharField(max_length=6, verbose_name='Dm')
    dn = models.CharField(max_length=6, verbose_name='Dn')
    d_lower = models.CharField(max_length=6, verbose_name='d')
    n_lower = models.CharField(max_length=6, verbose_name='n')
    m = models.CharField(max_length=6, verbose_name='Масса')


# Исполнение 4
class Atk261813FlangeExec4(models.Model):
    dn_passage = models.CharField(max_length=6, verbose_name='DN')
    pn = models.CharField(max_length=6, verbose_name='PN')
    d = models.CharField(max_length=6, verbose_name='D')
    d1 = models.CharField(max_length=6, verbose_name='D1')
    d2 = models.CharField(max_length=6, verbose_name='D2')
    d4 = models.CharField(max_length=6, verbose_name='D4')
    d1_lower = models.CharField(max_length=6, verbose_name='d1')
    b_lower = models.CharField(max_length=6, verbose_name='b')
    h_lower = models.CharField(max_length=6, verbose_name='h')
    h2_lower = models.CharField(max_length=6, verbose_name='h2')
    dm = models.CharField(max_length=6, verbose_name='Dm')
    dn = models.CharField(max_length=6, verbose_name='Dn')
    d_lower = models.CharField(max_length=6, verbose_name='d')
    n_lower = models.CharField(max_length=6, verbose_name='n')
    m = models.CharField(max_length=6, verbose_name='Масса')


# Исполнение 5
class Atk261813FlangeExec5(models.Model):
    dn_passage = models.CharField(max_length=6, verbose_name='DN')
    pn = models.CharField(max_length=6, verbose_name='PN')
    d = models.CharField(max_length=6, verbose_name='D')
    d1 = models.CharField(max_length=6, verbose_name='D1')
    d2 = models.CharField(max_length=6, verbose_name='D2')
    d5 = models.CharField(max_length=6, verbose_name='D5')
    d6 = models.CharField(max_length=6, verbose_name='D6')
    d1_lower = models.CharField(max_length=6, verbose_name='d1')
    b_lower = models.CharField(max_length=6, verbose_name='b')
    h_lower = models.CharField(max_length=6, verbose_name='h')
    h1_lower = models.CharField(max_length=6, verbose_name='h1')
    h2_lower = models.CharField(max_length=6, verbose_name='h2')
    dm = models.CharField(max_length=6, verbose_name='Dm')
    dn = models.CharField(max_length=6, verbose_name='Dn')
    d_lower = models.CharField(max_length=6, verbose_name='d')
    n_lower = models.CharField(max_length=6, verbose_name='n')
    m = models.CharField(max_length=6, verbose_name='Масса')


# Исполнение 6
class Atk261813FlangeExec6(models.Model):
    dn_passage = models.CharField(max_length=6, verbose_name='DN')
    pn = models.CharField(max_length=6, verbose_name='PN')
    d = models.CharField(max_length=6, verbose_name='D')
    d1 = models.CharField(max_length=6, verbose_name='D1')
    d8 = models.CharField(max_length=6, verbose_name='D8')
    d9 = models.CharField(max_length=6, verbose_name='D9')
    d1_lower = models.CharField(max_length=6, verbose_name='d1')
    b_lower = models.CharField(max_length=6, verbose_name='b')
    h_lower = models.CharField(max_length=6, verbose_name='h')
    h1_lower = models.CharField(max_length=6, verbose_name='h1')
    h3_lower = models.CharField(max_length=6, verbose_name='h3')
    b1_lower = models.CharField(max_length=6, verbose_name='b1')
    dm = models.CharField(max_length=6, verbose_name='Dm')
    dn = models.CharField(max_length=6, verbose_name='Dn')
    r_lower = models.CharField(max_length=6, verbose_name='r')
    d_lower = models.CharField(max_length=6, verbose_name='d')
    n_lower = models.CharField(max_length=6, verbose_name='n')
    m = models.CharField(max_length=6, verbose_name='Масса')


'''
Конец описания моделей для АТК 26-18-13-96
'''
