from models import clases
from  django import forms



class formulario(forms.ModelForm):
    class meta:
        model = clases 
        fields = "_all_"
       