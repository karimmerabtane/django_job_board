from django import forms 


# creat contact form 

class ContactForm(forms.Form):
    name     = forms.CharField( max_length= 50)
    email    = forms.EmailField()
    subject = forms.CharField(max_length=120)
    message = forms.CharField(widget=forms.Textarea)


    
