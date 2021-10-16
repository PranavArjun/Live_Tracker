from django import forms
from .models import TrackerScanner
  
  
# creating a form
class ScannerForm(forms.ModelForm):
  
    # create meta class
    class Meta:
        # specify model to be used
        model = TrackerScanner
  
        # specify fields to be used
        fields = [
            "package_id"
        ]
        
        widgets = { 'package_id' : forms.NumberInput(attrs={'id':'cust'}) 
                        
                       } 

        

    



	