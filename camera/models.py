from django.db import models
from jsonfield import JSONField
from django.contrib.auth import get_user_model

User = get_user_model()

from django.db.models.signals import post_delete
from django.dispatch import receiver



class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class Camera(models.Model):
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, related_name='camera')
    camera_name = models.CharField(max_length=64, unique=True, default="")
    camera_def = models.CharField(max_length=100, default="")
    camera_cost = models.IntegerField(default="0")
    
    def __str__(self):
        template = '{0.camera_name} {0.camera_def} '
        return template.format(self)

    camera_image = models.ImageField(upload_to='images/',blank=False,null=True)
    
    @property
    def characteristics(self):
        return self.characteristic_set.all()

    


class Characteristic(models.Model):
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)

    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)



class ShortDefenition(models.Model):
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)

    camera_short_def = models.CharField(max_length=200)

class ShortDefenitionImage(models.Model):
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)

    defenition_image = models.ImageField(upload_to='short-def-images/',blank=False,null=True)

class Filter(models.Model):
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)

    BRAND_CHOICES = (
        ('a', 'Hikvision'),
        ('b', 'HiWatch'),
        ('c', 'Ezviz'),
    )
    brand_filter = models.CharField(max_length=1, verbose_name='Бренды', choices=BRAND_CHOICES, blank=True)

    CAMERA_TYPE_CHOICES = (
        ('a', 'IP'),
        ('b', 'HD-TVI'),
        ('c', 'Аналог'),
        ('d', 'Уличная'),
        ('e', 'Купольная'),
        ('f', 'Офисная'),
        ('g', 'Встраиваемая'),
        ('h', 'Офисная'),
    )
    camera_filter = models.CharField(max_length=1, verbose_name='Тип камеры',choices=CAMERA_TYPE_CHOICES, blank=True)

    FRAME_TYPE_CHOICES = (
        ('a', 'Стандартный корпус'),
        ('b', 'Купольная'),
        ('c', 'Цилиндрическая'),
        ('d', 'Компактная'),
        ('e', 'Мини-купольная'),
        ('f', 'Панорамная'),
        ('g', 'Поворотная'),
    )
    frame_filter = models.CharField(max_length=1, verbose_name='Тип корпуса',choices=FRAME_TYPE_CHOICES, blank=True)

    POS_CHOICES = (
        ('a', 'Wi-Fi'),
        ('b', 'Встроенный микрофон'),
        ('c', 'Аудио вход для микрофона'),
        ('d', 'слот для SD карта'),
        ('e', 'ColorVu'),
    )
    pos_filter = models.CharField(max_length=1, verbose_name='Возможности', choices=POS_CHOICES, blank=True)

    USE_CHOICES = (
        ('a', 'Внутреннее'),
        ('b', 'Уличное'),
        ('c', 'Антикоррозионное'),
    )
    use_filter = models.CharField(max_length=1, verbose_name='Исполнение', choices=USE_CHOICES, blank=True)

    ZOOM_CHOICES = (
        ('a', 'Нет'),
        ('b', '4х'),
        ('c', '10х'),
        ('d', '20х'),
        ('e', '23х'),
        ('g', '25х'),
        ('g', '30х'),
        ('h', '32х'),
        ('i', '36х'),
    )
    zoom_filter = models.CharField(max_length=1, verbose_name='Оптическое увеличение', choices=ZOOM_CHOICES, blank=True)

    SENS_CHOICES = (
        ('a', 'CMOS 1/1.7"'),
        ('b', 'CMOS 1/1.8"'),
        ('c', 'CMOS 1/1.9"'),
        ('d', 'CMOS 1/2.5"'),
        ('e', 'CMOS 1/2.7"'),
        ('f', 'CMOS 1/2.8"'),
        ('g', 'CMOS 1/3"'),
        ('h', 'CMOS 1/4"'),
        ('i', 'CMOS'),
    )
    sens_filter = models.CharField(max_length=1, verbose_name='Оптический сенсор', choices=SENS_CHOICES, blank=True)

    MP_CHOICES = (
        ('a', '1 Мп'),
        ('b', '1,3 Мп'),
        ('c', '2 Мп'),
        ('d', '3 Мп'),
        ('e', '4 Мп'),
        ('f', '5 Мп'),
        ('g', '6 Мп'),
        ('h', '8 Мп'),
        ('i', '12 Мп'),
        ('j', '16 Мп'),
        ('k', '18 Мп'),
    )
    mp_filter = models.CharField(max_length=1, verbose_name='Кол-во мегапикселей', choices=MP_CHOICES, blank=True)

    IK_CHOICES = (
        ('a', 'Нет'),
        ('b', 'До 3 м'),
        ('c', 'До 10 м'),
        ('d', 'До 15 м'),
        ('e', 'До 20 м'),
        ('f', 'До 30 м'),
        ('g', 'До 40 м'),
        ('h', 'До 50 м'),
        ('i', 'До 70 м'),
        ('j', 'До 80 м'),
        ('k', 'До 100 м'),
        ('l', 'До 110 м'),
        ('m', 'До 120 м'),
        ('n', 'До 150 м'),
        ('o', 'До 200 м'),
        ('p', 'До 500 м (лазер)'),
        ('r', 'До 800 м (лазер)'),
        ('s', 'До 1000 м (лазер)'),
    )
    ik_filter = models.CharField(max_length=1, verbose_name='ИК-подсветка', choices=IK_CHOICES, blank=True)

    PROT_CHOICES = (
        ('a', 'Нет'),
        ('b', 'IP66'),
        ('c', 'IP67'),
        ('d', 'IP68'),
        ('e', 'NEMA4X C5-M'),
    )
    prot_filter = models.CharField(max_length=1, verbose_name='Защита от пыли/влаги', choices=PROT_CHOICES, blank=True)

    SUP_CHOICES = (
        ('a', '12VDC'),
        ('b', '24VAC'),
        ('c', 'PoE 802.3aF'),
        ('d', 'High-PoE 802.3at'),
        ('e', 'PoC (TVI)'),
        ('f', '36VDC'),
    )
    sup_filter = models.CharField(max_length=1, verbose_name='Питание', choices=SUP_CHOICES, blank=True)

    WDR_CHOICES = (
        ('a', 'DWDR'),
        ('b', 'WDR 120дб'),
        ('c', 'WDR 140дб'),
    )
    wdr_filter = models.CharField(max_length=1, verbose_name='WDR', choices=WDR_CHOICES, blank=True)

    VAR_CHOICES = (
        ('a', 'Да'),
    )
    var_filter = models.CharField(max_length=1, verbose_name='Вариофокальный объектив', choices=VAR_CHOICES, blank=True)


class Accessory(models.Model):
    camera = models.ForeignKey(Camera, on_delete=models.DO_NOTHING)
    accessory_name = models.CharField(max_length=50)
    accessory_description = models.CharField(max_length=150)
    accessory_image = models.ImageField(upload_to='accessory-images/',blank=False,null=True)



class Shop(models.Model):
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    working_hour = models.CharField(max_length=200)
    day_off = models.CharField(max_length=200)
    phones = models.CharField(max_length=200)


# delelte file with objects
@receiver(post_delete, sender=Camera)
def submission_delete(sender, instance, **kwargs):
    instance.camera_image.delete(False) 

@receiver(post_delete, sender=ShortDefenitionImage)
def submission_delete(sender, instance, **kwargs):
    instance.defenition_image.delete(False) 

@receiver(post_delete, sender=Accessory)
def submission_delete(sender, instance, **kwargs):
    instance.accessory_image.delete(False) 