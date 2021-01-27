from django.shortcuts import render,redirect,reverse
from .forms import Contactform
from django.core.mail import EmailMessage
# Create your views here.
def contacto(request):
    contact_form = Contactform()
    if request.method == "POST":  
        contact_form = Contactform(data=request.POST)
        if contact_form.is_valid(): 
            name= request.POST.get('name')
            email= request.POST.get('email')
            content= request.POST.get('content')
            
            mail = EmailMessage(
                "Ignacio Vidondo Blog : Nuevo Mensaje de Contacto ",
                "De {} {}\n\nEscribio:\n\n {}".format(name ,email,content),
                "ignaciovidondo.pythonanywhere.com", ["ignaciovidondo@hotmail.com"],
              
                reply_to = [email]
                )
            try:
                mail.send() #Si esta todo ok redireccionar
                return redirect(reverse("contacto")+"?ok")
            except:
                return redirect(reverse("contacto")+"?fail")
            
    return render (request, 'Contacto/contacto.html', {'form':contact_form })
