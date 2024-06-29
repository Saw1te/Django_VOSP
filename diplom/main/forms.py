from .models import InputData, InputDataMux, InputDataPower
from django.forms import ModelForm, NumberInput


class InputDataForm(ModelForm):
    class Meta:
        model = InputData
        fields = ['type_fibers', 'count_fibers', 'fading', 'dispersion', 'diameter']

        widgets = {
            'count_fibers': NumberInput(attrs={
                'class': 'form',
                'placeholder': 'Кол-во ОВ в кабеле, до'
            }),

            'fading': NumberInput(attrs={
                'class': 'form',
                'placeholder': 'Диаметр сердцевины, мкм'
            }),

            'dispersion': NumberInput(attrs={
                'class': 'form',
                'placeholder': 'Рабочая длина волны, нм'
            }),

            'diameter': NumberInput(attrs={
                'class': 'form',
                'placeholder': 'Коэффициент затухания, дБ/км, не более'
            })
        }


class InputDataMuxForm(ModelForm):
    class Meta:
        model = InputDataMux
        fields = ['count_fibers', 'count_canals', 'max_decay']

        widgets = {
            'count_fibers': NumberInput(attrs={
                'class': 'form',
                'placeholder': 'Количество волокон'
            }),

            'count_canals': NumberInput(attrs={
                'class': 'form',
                'placeholder': 'Количество каналов'
            }),

            'max_decay': NumberInput(attrs={
                'class': 'form',
                'placeholder': 'Максимальные вносимые затухания, дБ'
            })
        }


class InputDataPowerForm(ModelForm):
    class Meta:
        model = InputDataPower
        fields = ['output_power', 'gain_factor', 'noise_factor']

        widgets = {
            'output_power': NumberInput(attrs={
                'class': 'form',
                'placeholder': 'Выходная мощность, дБм'
            }),

            'gain_factor': NumberInput(attrs={
                'class': 'form',
                'placeholder': 'Коэффициент усиления, дБ'
            }),

            'noise_factor': NumberInput(attrs={
                'class': 'form',
                'placeholder': 'Коэффициент шума, дБ'
            })
        }
