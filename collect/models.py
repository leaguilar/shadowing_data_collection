# import the standard Django Model
# from built-in library
from django.db import models


class ObservationType(models.TextChoices):
    NewJourney = 'NJ', 'New Journey'
    Journey = 'JO', 'Journey'
    Zonal = 'ZO', 'Zonal'


class ObservationModel(models.Model):
    class Shifts(models.TextChoices):
        Morning = 'MO', 'Morning'
        Afternoon = 'AF', 'Afternoon'

    class Interactions(models.TextChoices):
        int_phy = 'INTPHY', 'Interaction with physician'
        int_pat = 'INTPAT', 'Interaction with patient'
        int_nur = 'INTNUR', 'Interaction with nurse'
        int_oth = 'INTOTH', 'Interaction with other'
        phone_call = 'PHONEC', 'Phone call'
        charting = 'CHARTI', 'Charting'
        procedure = 'PROCED', 'Procedure'
        discharge = 'DISCHA', 'Discharge'
        personal = 'PERSON', 'Personal'
        waiting = 'WAITIN', 'Waiting'
        other = 'OTHER1', 'Other'
        moving = 'MOVING', 'Moving'

    class Zones(models.TextChoices):
        nurse_station_open = 'NUROPE', 'Nurse station open'
        nurse_station = 'NURSTA', 'Nurse station'
        neuro_offices = 'NEUOFF', 'Neuro offices'
        cockpit = 'COCPIT', 'Cockpit'

        corr_ft = 'CORRFT', 'Corridor Fast Track'
        corr_1 = 'CORR01', 'Corridor 1'
        corr_2 = 'CORR02', 'Corridor 2'
        corr_3 = 'CORR03', 'Corridor 3'
        corr_4 = 'CORR04', 'Corridor 4'
        corr_5 = 'CORR05', 'Corridor 5'
        corr_6 = 'CORR06', 'Corridor 6'
        corr_7 = 'CORR07', 'Corridor 7'

    # fields of the model
    observer_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=100, blank=True)

    shift_type = models.CharField(
        max_length=2,
        choices=Shifts.choices,
    )

    observation_type = models.CharField(
        max_length=2,
        choices=ObservationType.choices,
    )

    interaction_type = models.CharField(
        max_length=6,
        choices=Interactions.choices,
        default=None,
    )

    zone = models.CharField(
        max_length=6,
        choices=Zones.choices,
        default=None,
    )

    prev_observation = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    observation_start = models.DateTimeField()
    observation_end = models.DateTimeField(auto_now=True)

    # BADGES
    badge_1 = models.BooleanField()
    badge_2 = models.BooleanField()
    badge_3 = models.BooleanField()
    badge_4 = models.BooleanField()
    badge_5 = models.BooleanField()
    badge_6 = models.BooleanField()
    badge_7 = models.BooleanField()
    badge_8 = models.BooleanField()
    badge_9 = models.BooleanField()
    badge_10 = models.BooleanField()
    badge_11 = models.BooleanField()
    badge_12 = models.BooleanField()
    badge_13 = models.BooleanField()
    badge_14 = models.BooleanField()
    badge_15 = models.BooleanField()
    badge_16 = models.BooleanField()
    badge_17 = models.BooleanField()
    badge_18 = models.BooleanField()
    badge_19 = models.BooleanField()
    badge_20 = models.BooleanField()
    badge_21 = models.BooleanField()
    badge_22 = models.BooleanField()
    badge_23 = models.BooleanField()
    badge_24 = models.BooleanField()
    badge_25 = models.BooleanField()

    class Meta:
        verbose_name = 'Observation'
        verbose_name_plural = 'Observations'
