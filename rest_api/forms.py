from django import forms
from .models import moview_details

class Update_db(forms.ModelForm):

    class Meta:
        model = moview_details
        fields = ('imdbID','Title','Year','Genre','Ratings')
