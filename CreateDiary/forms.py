from django import forms
from .models import DiaryUser, DiaryText,Profile
from django.forms import ModelForm

class CreateDiaryUser(forms.ModelForm):
	class Meta:
		model=DiaryUser
		fields={'Username','Password','CheckPassword'}
		widgets={
		  'Username':forms.TextInput(attrs={'placeholder':'Username','class':'Username',}),
		  'Password':forms.PasswordInput(attrs={'placeholder':'Password','class':'password'}),
		  'CheckPassword':forms.PasswordInput(attrs={'placeholder':'Re-enter Password','class':'password1'})
		}

	def CheckUserExist(self):
		Username=self.cleaned_data['Username']
		if DiaryUser.objects.filter(Username=Username):
			 raise ValidationError("This Username Already Exists")
		return Username

	def clean(self):
		form_data = self.cleaned_data
		if form_data['Password'] !=form_data['CheckPassword']:
			self._errors["Password"]="Both Password Do Not Match"
			del form_data['Password']
		return form_data

class SUserLoginForm(forms.ModelForm):
	class Meta:
		model=DiaryUser
		fields={'Username','Password'}
		widgets={
			'Username':forms.TextInput(attrs={'placeholder':'Username','class':'LoginUsername'}),
			'Password':forms.PasswordInput(attrs={'placeholder':'Password','class':'LoginPassword'})
		}
	
	def clean(self):
		form_data=self.cleaned_data
		LoginUsername=form_data['Username']
		LoginPassword=form_data['Password']
		if DiaryUser.objects.filter(Username=LoginUsername,Password=LoginPassword).exists():
			pass
		else:
			self._errors["Username"]="The User Credentials entered is not present in our database"
			return form_data

class UpdateProfileForm(forms.ModelForm):

	class Meta:
		model=Profile
		fields={'Name','Hobbies','LivesAt','WorksAt','ProfilePic'}
		widgets={
			'Name':forms.TextInput(attrs={'placeholder':'Name','class':'Headline'}),
			'Hobbies':forms.Textarea(attrs={'placeholder':'Enter your hobbies...','class':'BodyDiary'}),
			'LivesAt':forms.TextInput(attrs={'placeholder':'Lives in','class':'Headline'}),
			'WorksAt':forms.TextInput(attrs={'placeholder':'Works at','class':'Headline'}),
		}

class MakeADiaryForm(forms.ModelForm):

	class Meta:
		model=DiaryText
		fields={'DiaryHeading','DiaryBody'}
		widgets={
			'DiaryHeading':forms.TextInput(attrs={'placeholder':'Enter Title','class':'Headline'}),
			'DiaryBody':forms.Textarea(attrs={'placeholder':'Start Writing','class':'BodyDiary'}),
		}