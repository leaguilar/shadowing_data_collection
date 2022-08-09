from django.http import HttpResponse
from django.shortcuts import render
from .forms import ObservationForm
from .models import ObservationType
from datetime import datetime
from django.utils import timezone


def index(request):
    observer = request.GET.get('observer')
    shift = request.GET.get('shift')
    zone = request.GET.get('zone')
    shadowing = request.GET.get('shadowing')
    error = ''

    context = {'error_message': '',
               'form': ObservationForm(),
               'observer': observer
               }

    if request.method == 'POST':
        print("REACTING TO POST")
        print(request.POST)
        form = ObservationForm(request.POST)

        if form.is_valid():
            print("SAVING")
            obs = form.save()

            if form.data['observation_type'] == ObservationType.Journey or form.data['observation_type'] == ObservationType.NewJourney:
                context['form'].fields['prev_observation'].initial = obs.pk
                context['form'].fields['observation_type'].initial = ObservationType.Journey

            if form.data['observation_type'] == ObservationType.Zonal:
                context['form'].fields['prev_observation'].initial = ""
                context['form'].fields['observation_type'].initial = ObservationType.Zonal
        else:
            context['error_message'] = "Observation Not Saved, invalid data"
            print(form.errors)

    context['form'].fields['page_load'].initial = timezone.now()

    print("----")
    print(context['form'].fields['page_load'].initial)
    print("----")
    #context['form'].fields['observation_start'].initial = timezone.now()
    if observer:
        context['form'].fields['observer_name'].initial = observer
    if shift:
        context['form'].fields['shift_type'].initial = shift

    if shadowing:
        shadowing = int(shadowing)
        context['form'].fields[f'badge_{shadowing}'].initial = True

        if request.method == 'GET':
            context['form'].fields['observation_type'].initial = ObservationType.NewJourney

    if zone:
        context['form'].fields['zone'].initial = zone
        context['form'].fields['observation_type'].initial = ObservationType.Zonal

    print("CONTEXT")
    print(context)
    #return render(request, 'collect/index_test.html', context)
    return render(request, 'collect/index.html', context)
