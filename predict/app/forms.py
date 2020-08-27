from django import forms

TENN_CHOICES =(
    ("1", "Semi-Furnished"),
    ("2", "Unfurnished"),
    ("3", "Furnished"),
)
FURN_CHOICES =(
    ("1", "Bachelors/Family"),
    ("2", "Family"),
    ("3", "Bachelors"),
)

class UserForm(forms.Form):
    noofbedrooms= forms.IntegerField()
    noofbathrooms= forms.IntegerField()
    furnishing=forms.ChoiceField(choices=FURN_CHOICES)
    tenants=forms.ChoiceField(choices=TENN_CHOICES)
    area=forms.IntegerField()
    latitude=forms.FloatField()
    longitude=forms.FloatField()
