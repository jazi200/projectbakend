
from distutils.log import error
import email
from email.message import EmailMessage
from django.shortcuts import render,redirect
from django.urls import reverse_lazy 
from .models import Tagam
from .models import Makal
from .models import Pikir
from .forms import TagamForm,UserRegistrationForm,LoginUserForm
from django.views.generic import DetailView, UpdateView, DeleteView,CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.core.mail import send_mail
from django.core.mail import EmailMessage



def send_message(request): 
    send_mail("Welcome to testing page","My content","200103073@stu.sdu.edu.kz",["200103073@stu.sdu.edu.kz","200103073@stu.sdu.edu.kz"], 
              fail_silently=False,html_message="<b>Bold text </b> <i>Italic text </i>" )
    return render (request,'project/successfull.html') 
    '''
   email = EmailMessage(
       'Hello',
       'Body goes here',
       '200103073@stu.sdu.edu.kz',
       ['200103073@stu.sdu.edu.kz','200103073@stu.sdu.edu.kz'],
       headers={'Message-ID':'foo'},
   )
   email.attach_file('/Users/acer/Desktop/AaTe06MJoq4.png')

   email.send(fail_silently=False)
   '''
 

# Create your views here.
def home(request):
    tagam = Tagam.objects.all()
    return render(request,'project/first.html',{'tagam': tagam})

class NewsDetailView(DetailView):
    model = Tagam
    template_name = 'project/details_view.html'
    context_object_name = 'tagam'

class NewsUpdateView(UpdateView):
    model = Tagam
    success_url = '/project/'
    template_name = 'project/update.html'
    form_class = TagamForm

class NewsDeleteView(DeleteView):
    model = Tagam
    success_url = '/project/'
    template_name = 'project/news-delete.html'


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'project/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')

def pikir(request):
    pik = Pikir.objects.all()
    return render(request,'project/pikir.html',{'title':'Пікірлер','pik': pik}) 

def makal(request):
    makal = Makal.objects.all()
    return render(request,'project/third.html',{'title':'Мақал','makal': makal}) 

def create(request):
    if request.method == 'POST':
          form = TagamForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('home')

    form = TagamForm()
    data = {
      'form': form
    }
    return render(request,'project/create.html', data) 
    
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'project/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'project/registor.html', {'user_form': user_form})
  

