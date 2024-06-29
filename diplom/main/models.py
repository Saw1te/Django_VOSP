from django.db import models


fibers = (
    ('в грунт', 'В грунт'),
    ('в каналах кабельной канализации', 'В каналах кабельной канализации'),
    ('Подвесной самонесущий', 'Подвесной самонесущий'),
)


class InputData(models.Model):
    type_fibers = models.CharField('Тип прокладки кабеля', max_length=255, choices=fibers)
    count_fibers = models.IntegerField('Кол-во ОВ в кабеле, до')
    fading = models.FloatField('Диаметр сердцевины, мкм')
    dispersion = models.FloatField('Рабочая длина волны, нм')
    diameter = models.FloatField('Коэффициент затухания, дБ/км, не более')

    def __str__(self):
        return self.type_fibers

    class Meta:
        verbose_name = 'Входные данные кабель'
        verbose_name_plural = 'Входные данные кабель'


class FiberData(models.Model):
    name_fibers = models.CharField('Название кабеля', max_length=255)
    type_fibers = models.CharField('Тип прокладки кабеля', max_length=255, choices=fibers)
    count_fibers = models.IntegerField('Кол-во ОВ в кабеле, до')
    fading = models.FloatField('Диаметр сердцевины, мкм')
    dispersion = models.FloatField('Рабочая длина волны, нм')
    diameter = models.FloatField('Коэффициент затухания, дБ/км, не более')

    def __str__(self):
        return self.name_fibers

    class Meta:
        verbose_name = 'Кабель'
        verbose_name_plural = 'Кабели'


class InputDataMux(models.Model):
    count_fibers = models.IntegerField('Количество волокон')
    count_canals = models.IntegerField('Количество каналов')
    max_decay = models.FloatField('Максимальные вносимые затухания, дБ')

    class Meta:
        verbose_name = 'Входные данные мультиплексор'
        verbose_name_plural = 'Входные данные мультиплексор'


class DataMux(models.Model):
    name = models.CharField('Название устройства', max_length=255)
    count_fibers = models.IntegerField('Количество волокон')
    count_canals = models.IntegerField('Количество каналов')
    max_decay = models.FloatField('Максимальные вносимые затухания, дБ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'мультиплексор'
        verbose_name_plural = 'мультиплексоры'


class InputDataPower(models.Model):
    output_power = models.IntegerField('Выходная мощность, дБм')
    gain_factor = models.FloatField('Коэффициент усиления, дБ')
    noise_factor = models.FloatField('Коэффициент шума, дБ')

    class Meta:
        verbose_name = 'Входные данные усилитель'
        verbose_name_plural = 'Входные данные усилитель'


class PowerData(models.Model):
    name_power = models.CharField('Название устройства', max_length=255)
    output_power = models.IntegerField('Выходная мощность, дБм')
    gain_factor = models.FloatField('Коэффициент усиления, дБ')
    noise_factor = models.FloatField('Коэффициент шума, дБ')

    def __str__(self):
        return self.name_power

    class Meta:
        verbose_name = 'усилитель'
        verbose_name_plural = 'усилители'


