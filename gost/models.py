from django.db import models


class Documents(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True, db_index=True, verbose_name="URL")
    description = models.CharField(max_length=200)
    cat_id = models.ForeignKey('Category_doc', on_delete=models.PROTECT, verbose_name="Категории")

    def __str__(self):
        return self.title


class Category_doc(models.Model):
    name = models.CharField(max_length=20, db_index=True)

    def __str__(self):
        return self.name


class Gost33259_flange(models.Model):
    dn_passage = models.CharField(max_length=6)
    pn = models.CharField(max_length=6)
    d2 = models.CharField(blank=True, null=True, max_length=6)
    d3 = models.CharField(blank=True, null=True, max_length=6)
    d4 = models.CharField(blank=True, null=True, max_length=6)
    d5 = models.CharField(blank=True, null=True, max_length=6)
    d6 = models.CharField(blank=True, null=True, max_length=6)
    d7 = models.CharField(blank=True, null=True, max_length=6)
    d8 = models.CharField(blank=True, null=True, max_length=6)
    d9 = models.CharField(blank=True, null=True, max_length=6)
    d10 = models.CharField(blank=True, null=True, max_length=6)
    d11 = models.CharField(blank=True, null=True, max_length=6)
    b2_lower = models.CharField(blank=True, null=True, max_length=6)
    h_lower = models.CharField(blank=True, null=True, max_length=6)
    h1_lower = models.CharField(blank=True, null=True, max_length=6)
    h2_lower = models.CharField(blank=True, null=True, max_length=6)
    h3_lower = models.CharField(blank=True, null=True, max_length=6)
    h4_lower = models.CharField(blank=True, null=True, max_length=6)
    h5_lower = models.CharField(blank=True, null=True, max_length=6)
    dm = models.CharField(blank=True, null=True, max_length=6)
    dn = models.CharField(blank=True, null=True, max_length=6)
    d1_lower = models.CharField(blank=True, null=True, max_length=6)
    b_lower = models.CharField(blank=True, null=True, max_length=6)
    h = models.CharField(blank=True, null=True, max_length=6)
    d = models.CharField(blank=True, null=True, max_length=6)
    d1 = models.CharField(blank=True, null=True, max_length=6)
    d_lower = models.CharField(blank=True, null=True, max_length=6)
    n_lower = models.CharField(blank=True, null=True, max_length=6)
    pin = models.CharField(blank=True, null=True, max_length=6)

    def __str__(self):
        return self.dn_passage

    class Meta:
        verbose_name = 'ГОСТ 33259-2015'
        verbose_name_plural = 'ГОСТ 33259-2015'
        ordering = ['id']


class Gost33259_type(models.Model):
    type_fl = models.CharField(max_length=6)
    flange_drawing = models.ImageField(upload_to="photos/%Y/%m/%d/")

    def __str__(self):
        return self.type_fl

    class Meta:
        verbose_name = 'типы'
        verbose_name_plural = 'Тип фланца'


class Gost33259_surface(models.Model):
    surface_fl = models.CharField(max_length=6)
    flange_surface = models.ImageField(upload_to="photos/%Y/%m/%d/")

    def __str__(self):
        return self.surface_fl

    class Meta:
        verbose_name = 'уплотнительные поверхности'
        verbose_name_plural = 'Уплотнительная поверхность'