from django.shortcuts import render

def resetActiveLink():
	home_active = 0
	projects_active = 0
	create_effect_active = 0
	import_file_active = 0
	sign_in_active = 0
	sign_out_active = 0
	register_active = 0
	context = {
		'home_active':home_active,
		'projects_active':projects_active,
		'create_effect_active': create_effect_active,
		'import_file_active': import_file_active,		
		'sign_in_active': sign_in_active,
		'sign_out_active': sign_out_active,
		'register_active': register_active
	}
	return context
	

def home(request):
	context = resetActiveLink()
	context['home_active'] = 1
	return render(request, 'wvy/wvy_home.html', context)

#TODO: Create urls and html files for the following functions
def projects(request):
	context = resetActiveLink()
	context['projects_active'] = 1
	return render(request, 'wvy/wvy_home.html', context)

def create_effect(request):
	context = resetActiveLink()
	context['create_effect_active'] = 1	
	return render(request, 'wvy/wvy_home.html', context)

def import_file(request):
	context = resetActiveLink()
	context['import_file_active'] = 1	
	try:
		context['file_type'] = request.POST['file_type']
	except:
		context['file_type'] = 'Choose your file type!'
	return render(request, 'wvy/wvy_import_file.html', context)

def sign_in(request):
	context = resetActiveLink()
	context['sign_in_active'] = 1	
	return render(request, 'wvy/wvy_home.html', context)

def sign_out(request):
	context = resetActiveLink()
	context['sign_out_active'] = 1	
	return render(request, 'wvy/wvy_home.html', context)

def register(request):
	context = resetActiveLink()
	context['register_active'] = 1	
	return render(request, 'wvy/wvy_home.html', context)
