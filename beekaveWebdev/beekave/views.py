from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from beekave.forms import UserCreationForm

# Create your views here.


#--- User Creation
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'
    
