from django import forms

class AddTeam(forms.Form):
    name = forms.CharField(max_length=20, 
        widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Name'}))
    t_id = forms.CharField(max_length=20, 
        widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '2020-XX'}))
    members = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Team Members'}))