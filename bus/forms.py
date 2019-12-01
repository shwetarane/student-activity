from django import forms

zone_choices = [
    ('','None'),
    ('zone1-buda','Zone1 - [Buda Tx to San Marcos TX]'),
    ('zone2-kyle', 'Zone2 - [Kyle Tx to San Marcos TX]'),
    ('zone2-austin', 'Zone3 - [Austin Tx to San Marcos TX]'),

    ]

class TicketForm(forms.Form):
    zone = forms.CharField(required=False, label='Seelect Zone',
            widget=forms.Select(choices=zone_choices))
            
    
