
from django.views.generic import TemplateView


# Create your views here.
class UserPanelView(TemplateView):
    template_name = "user_panel_module/user_panel.html"
