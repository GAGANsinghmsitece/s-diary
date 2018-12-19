from django.shortcuts import render,redirect,get_object_or_404
from .forms import CreateDiaryUser, SUserLoginForm, MakeADiaryForm,UpdateProfileForm
from .models import DiaryUser,DiaryText,Profile
from django.http import Http404


def CreateDiaryUserView(request):
	if request.method == 'POST':
		form=CreateDiaryUser(request.POST)
		if form.is_valid():
			form.save()
			return redirect('MyEntries')
	else:
		form=CreateDiaryUser()
	if request.user_agent.is_mobile==True:
		return render(request,'Mobile/CreateDiaryUser.html',{'form':form})
	else:
	    return render(request,'CreateDiaryUser.html',{'form':form})

def SUserLoginFormView(request):
	if request.method=='POST':
		form1=SUserLoginForm(request.POST)
		if form1.is_valid():
			UserInfo=form1.save(commit=False)
			return redirect('Display',**{'slug':UserInfo.Username})
	else:
		form1=SUserLoginForm()
	return render(request,'FormLoginTemplate.html',{'form1':form1})

def Display(request,slug):
	UserPresent=get_object_or_404(DiaryUser,Username=slug)
	UserName=slug
	Results=DiaryText.objects.filter(DiaryUser=UserName)
	if request.user_agent.is_mobile==True:
		return render(request,'Mobile/MainDiaryDisplay.html',{'Results':Results,'slug':slug})
	else:
		ProfileResults=Profile.objects.filter(DiaryUser=slug)
		if request.method=='POST':
			if Profile.objects.filter(DiaryUser=slug).exists():
				ProfileAlready=get_object_or_404(Profile,DiaryUser=slug)
				form=UpdateProfileForm(request.POST,request.FILES,instance=ProfileAlready)
				if form.is_valid():
					form.save()
			else:
				form=UpdateProfileForm(request.POST,request.FILES)
				if form.is_valid():
					ProfileUpdate=form.save(commit=False)
					ProfileUpdate.DiaryUser=slug
					ProfileUpdate.save()
			return redirect('Display',**{'slug':slug})
		else:
			form=UpdateProfileForm()
		return render(request,'MainDiaryDisplay.html',{'Results':Results,'slug':slug,'ProfileResults':ProfileResults,'form':form})




# Create your views here.

def ViewProfile(request,slug):
	ProfileResults=Profile.objects.filter(DiaryUser=slug)
	if request.method=='POST':
		if Profile.objects.filter(DiaryUser=slug).exists():
			ProfileAlready=get_object_or_404(Profile,DiaryUser=slug)
			form=UpdateProfileForm(request.POST,request.FILES,instance=ProfileAlready)
			if form.is_valid():
				form.save()
		else:
			form=UpdateProfileForm(request.POST,request.FILES)
			if form.is_valid():
				ProfileUpdate=form.save(commit=False)
				ProfileUpdate.DiaryUser=slug
				ProfileUpdate.save()
		return redirect('Display',**{'slug':slug})
	else:
		form=UpdateProfileForm()
		if request.user_agent.is_mobile==True:
			return render(request,'Mobile/ViewProfile.html',{'form':form,'slug':slug,'ProfileResults':ProfileResults})
		else:
			raise Http404('The link seems to be broken')

def NewEntryView(request,slug):
	UserPresent=get_object_or_404(DiaryUser,Username=slug)
	if request.method=='POST':
		form=MakeADiaryForm(request.POST)
		if form.is_valid():
			BlogEntry=form.save(commit=False)
			BlogEntry.DiaryUser=slug
			BlogEntry.save()
			return redirect('Display',**{'slug':slug})
	else:
		form=MakeADiaryForm()
		return render(request,'Mobile/AddNewEntry.html',{'form':form,'slug':slug})

def ViewFeatures(request):
	return render(request,'FeaturesTemplate.html')

def ViewPrivacy(request):
	return render(request,'PrivacyTemplate.html')

def ViewAboutUs(request):
	return render(request,'AboutUsTemplate.html')

def ViewSaporaInc(request):
	return render(request,'SaporaIncTemplate.html')

def ViewDiary(request,slug,pk):
	Profile=get_object_or_404(DiaryUser,Username=slug)
	DiaryEntry=get_object_or_404(DiaryText,id=pk)
	return render(request,'Mobile/ViewDiary.html',{'DiaryEntry':DiaryEntry})
