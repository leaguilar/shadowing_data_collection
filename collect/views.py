from django.http import HttpResponse
from django.shortcuts import render
from .forms import ObservationForm
from .models import ObservationType
from datetime import datetime


def index(request):
    observer = request.GET.get('observer')
    shift = request.GET.get('shift')
    context = {'latest_question_list': [1, 2],
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

    context['form'].fields['observation_start'].initial = datetime.now()
    if observer:
        context['form'].fields['observer_name'].initial = observer
    if shift:
        context['form'].fields['shift_type'].initial = shift
    #return render(request, 'collect/index_test.html', context)
    return render(request, 'collect/index.html', context)
