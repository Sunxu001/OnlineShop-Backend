from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from shop import models as shop_models
from shop import serializers as shop_serializers
from .forms import LoginForm




# Create your views here.
class GoodsViewSets(viewsets.ModelViewSet):
    queryset = shop_models.Goods.objects.all()
    serializer_class = shop_serializers.GoodsSerializer
   
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)

def home_page(request):
    return render(request, 'index.html')

def new_page(request):
    return render(request, 'new.html')
    
def cloes_page(request):
    return render(request, 'cloes.html')

def login_page(request):
    return render(request, 'login.html')

def message_page(request):
    return render(request, 'message.html')

def order_page(request):
    return render(request, 'order.html')

def regiter_page(request):
    return render(request, 'regiter.html')


