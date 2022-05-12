# from django import forms
# from event.models import Event
# from dal import autocomplete
# from django.forms.widgets import TextInput, Textarea,FileInput,NumberInput,Select
	
# class EventForm(forms.ModelForm):
# 	class Meta:
# 		model = Event
# 		fields = ['title','class_teacher','description',"department",'semester']
# 		widgets= {
# 			'title' : TextInput(attrs={'class': 'form-control',}),	
# 			'class_teacher' : Select(attrs={'class': 'required form-control',}),	
# 			'description' : TextInput(attrs={'class': 'required form-control',}),	
# 			'semester' : Select(attrs={'class': 'required form-control',}),	
# 			'department' : Select(attrs={'class': 'required form-control',}),	
# 		}