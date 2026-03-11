from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

# Public lobby view
def home(request):
    return render(request, "club/home.html")

# Member-only lounge
@login_required
def member_lounge(request):
    return render(request, "club/lounge.html")

@permission_required('auth.view_user', raise_exception=True)
def manager_office(request):
    return render(request, "club/office.html")