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

    class Meta:
        verbose_name = 'наличе фланцев ГОСТ 33259-2015'
        verbose_name_plural = 'ГОСТ 33259-2015 наличе фланцев '
        ordering = ['id']


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

    def __str__(self):
        return self.dn_passage

    class Meta:
        verbose_name = 'тип 01 ГОСТ 33259-2015'
        verbose_name_plural = 'ГОСТ 33259-2015 тип 01'
        ordering = ['id']


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
    n_lower = models.CharField(blank=True, null=True, max_length=6, verbose_name='n')
    pin = models.CharField(blank=True, null=True, max_length=6, verbose_name='Диаметр шпилек')

    def __str__(self):
        return self.dn_passage

    class Meta:
        verbose_name = 'тип 02 ГОСТ 33259-2015'
        verbose_name_plural = 'ГОСТ 33259-2015 тип 02 '
        ordering = ['id']


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
        # field_values = []
        # for field in self._meta.get_fields():
        #     field_values.append(str(getattr(self, field.name, '')))
        # return ' '.join(field_values)
        return self.dn_passage

    class Meta:
        verbose_name = 'тип 11 ГОСТ 33259-2015'
        verbose_name_plural = 'ГОСТ 33259-2015 тип 11'
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

    class Meta:
        verbose_name = 'уплотнительные поверхности'
        verbose_name_plural = 'ГОСТ 33259-2015 уплотнительная поверхность '
        ordering = ['id']


# Масса фланцев ГОСТ 33259
class Gost33259Mass(models.Model):
    dn_passage = models.CharField(max_length=6, verbose_name='DN')
    type_fl = models.CharField(max_length=6, verbose_name='Тип')
    pn_1 = models.CharField(max_length=6, verbose_name='PN 1')
    pn_2 = models.CharField(max_length=6, verbose_name='PN 2,5')
    pn_6 = models.CharField(max_length=6, verbose_name='PN 6')
    pn_10 = models.CharField(max_length=6, verbose_name='PN 10')
    pn_16 = models.CharField(max_length=6, verbose_name='PN 16')
    pn_25 = models.CharField(max_length=6, verbose_name='PN 25')
    pn_40 = models.CharField(max_length=6, verbose_name='PN 40')
    pn_63 = models.CharField(max_length=6, verbose_name='PN 63')
    pn_100 = models.CharField(max_length=6, verbose_name='PN 100')
    pn_160 = models.CharField(max_length=6, verbose_name='PN 160')
    pn_200 = models.CharField(max_length=6, verbose_name='PN 200')

    def __str__(self):
        return self.dn_passage

    class Meta:
        verbose_name = 'массы'
        verbose_name_plural = 'ГОСТ 33259-2015 массы'
        ordering = ['id']


# чертеж типа фланца
class Gost33259TypeDrawing(models.Model):
    type_fl = models.CharField(max_length=6, verbose_name='Тип фланца')
    flange_drawing = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Чертеж')

    def __str__(self):
        return self.type_fl

    class Meta:
        verbose_name = 'типы'
        verbose_name_plural = 'ГОСТ 33259-2015 чертежи типов фланцев '


# чертеж уплотнительной поверхности фланца
class Gost33259SurfaceDrawing(models.Model):
    surface_fl = models.CharField(max_length=6, verbose_name='Уплотнительная поверхность')
    surface_drawing = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Чертеж')

    def __str__(self):
        return self.surface_fl

    class Meta:
        verbose_name = 'уплотнительные поверхности'
        verbose_name_plural = 'ГОСТ 33259-2015 чертежи уплотнительной поверхность'


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

    def __str__(self):
        return self.dn_passage


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

    def __str__(self):
        return self.dn_passage


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

    def __str__(self):
        return self.dn_passage


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

    def __str__(self):
        return self.dn_passage


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

    def __str__(self):
        return self.dn_passage


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

    def __str__(self):
        return self.dn_passage


'''
Конец описания моделей для АТК 26-18-13-96
'''
