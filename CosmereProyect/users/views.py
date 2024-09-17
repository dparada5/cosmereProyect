from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test #admin
from django.contrib.admin.views.decorators import staff_member_required #staff

def	registration(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = UserCreationForm()
	return render(request, 'registration.html', {'form': form})

#ejemplos de niveles de usuario
def	is_admin(user):
	return user.is_superuser

@user_passes_test(is_admin)
def	admin_view(request):
	return render(request, 'admin.html')

@staff_member_required
def	staff_view(request):
	return render(request, 'staff.html')