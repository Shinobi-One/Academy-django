from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.urls import reverse
from django.utils.decorators import method_decorator

from apps.user_module.forms import EditPasswordForm
from apps.user_module.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from apps.user_panel_module.forms import EditUserPanel
import apps.user_module.models

from apps.user_panel_module.forms import EditUserPanel


# Create your views here.

@method_decorator(login_required, name="dispatch")
class UserPanelView(View):

    def get(self, request):
        user = request.user
        context = {
            "user": user

        }
        return render(request, 'user_panel_module/user_panel.html', context)


@login_required()
def user_panel_partial(request):
    return render(request, 'user_panel_module/include/user_panel_partial.html', context={})


@method_decorator(login_required, name="dispatch")
class EditUserPanelView(View):
    def get(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        form = EditUserPanel(instance=current_user)
        context = {"edit_form": form,
                   "current_user": current_user
                   }
        return render(request, 'user_panel_module/edit_user_panel.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        form = EditUserPanel(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)

        context = {"edit_form": form,
                   "current_user": current_user
                   }
        return render(request, 'user_panel_module/edit_user_panel.html', context)


@method_decorator(login_required, name="dispatch")
class EditPasswordView(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditPasswordForm()

        context = {
            "user": current_user,
            "edit_form": edit_form
        }
        return render(request, 'user_panel_module/edit_password_panel.html', context)

    def post(self, request):
        current_user: User = User.objects.filter(id=request.user.id).first()
        edit_form = EditPasswordForm(request.POST)
        if edit_form.is_valid():

            if current_user.check_password(edit_form.cleaned_data.get("current_password")):
                current_user.set_password(edit_form.cleaned_data.get('password'))
                current_user.save()
                logout(request)
                return redirect(reverse('user:login'))
            else:
                edit_form.add_error('password', 'رمز وارد شده نادرست است ')
        context = {
            "edit_form": edit_form
        }
        return render(request, 'user_panel_module/edit_password_panel.html', context)
