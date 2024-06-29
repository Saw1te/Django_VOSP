from django.contrib import admin
from .models import InputData, FiberData, InputDataMux, DataMux, InputDataPower, PowerData


admin.site.register(InputData)
admin.site.register(FiberData)
admin.site.register(InputDataMux)
admin.site.register(DataMux)
admin.site.register(InputDataPower)
admin.site.register(PowerData)