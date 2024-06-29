from django.shortcuts import render, redirect
from .forms import InputDataForm, InputDataMuxForm, InputDataPowerForm
from .models import InputData, FiberData, InputDataMux, DataMux, InputDataPower, PowerData


def index(request):
    error = ''
    if request.method == 'POST':
        form = InputDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(step2)
        else:
            error = 'Ошибка в заполнении формы'

    form = InputDataForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/index.html', data)


def result(request):
    fiber_data = FiberData.objects.all()
    fiber_verbose = {}
    for i in fiber_data:
        if i.name_fibers not in fiber_verbose:
            fiber_verbose[i.name_fibers] = []
            fiber_verbose[i.name_fibers].append(i.type_fibers)
            fiber_verbose[i.name_fibers].append(i.count_fibers)
            fiber_verbose[i.name_fibers].append(i.fading)
            fiber_verbose[i.name_fibers].append(i.dispersion)
            fiber_verbose[i.name_fibers].append(i.diameter)
    input_fiber = InputData.objects.order_by("-id")[:1]
    list_fiber = []
    for i in input_fiber:
        list_fiber.append(i.type_fibers)
        list_fiber.append(i.count_fibers)
        list_fiber.append(i.fading)
        list_fiber.append(i.dispersion)
        list_fiber.append(i.diameter)
    step_1 = {}
    for i in fiber_verbose:
        if fiber_verbose[i] == list_fiber:
            step_1[i] = fiber_verbose[i]
            name_1 = i
    mux_data = DataMux.objects.all()
    mux_verbose = {}
    for i in mux_data:
        if i.name not in mux_verbose:
            mux_verbose[i.name] = []
            mux_verbose[i.name].append(i.count_fibers)
            mux_verbose[i.name].append(i.count_canals)
            mux_verbose[i.name].append(i.max_decay)
    input_mux = InputDataMux.objects.order_by("-id")[:1]
    list_mux = []
    for i in input_mux:
        list_mux.append(i.count_fibers)
        list_mux.append(i.count_canals)
        list_mux.append(i.max_decay)
    step_2 = {}
    for i in mux_verbose:
        if mux_verbose[i] == list_mux:
            step_2[i] = mux_verbose[i]
            name_2 = i
    power_data = PowerData.objects.all()
    power_verbose = {}
    for i in power_data:
        if i.name_power not in power_verbose:
            power_verbose[i.name_power] = []
            power_verbose[i.name_power].append(i.output_power)
            power_verbose[i.name_power].append(i.gain_factor)
            power_verbose[i.name_power].append(i.noise_factor)
    input_power = InputDataPower.objects.order_by("-id")[:1]
    list_power = []
    for i in input_power:
        list_power.append(i.output_power)
        list_power.append(i.gain_factor)
        list_power.append(i.noise_factor)
    step_3 = {}
    for i in power_verbose:
        if power_verbose[i] == list_power:
            step_3[i] = power_verbose[i]
            name_3 = i
    varr = {
        "step_1": step_1,
        "name_1": name_1,
        "step_2": step_2,
        "name_2": name_2,
        "step_3": step_3,
        "name_3": name_3
    }

    return render(request, 'main/result.html', varr)


def step2(request):
    error = ''
    if request.method == 'POST':
        form = InputDataMuxForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(step3)
        else:
            error = 'Ошибка в заполнении формы'

    form = InputDataMuxForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/step2.html', data)


def step3(request):
    error = ''
    if request.method == 'POST':
        form = InputDataPowerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(result)
        else:
            error = 'Ошибка в заполнении формы'

    form = InputDataPowerForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/step3.html', data)
