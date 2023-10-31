from django.shortcuts import render
from django.http import JsonResponse
from email.message import EmailMessage
import smtplib
import environ
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

def home(request):
    return render(request, 'index.html')

def form(request):
    if request.method == 'POST':
        remitente = env('EMAIL')
        destinatario = env('EMAIL')

        email = EmailMessage()
        email["From"] = remitente
        email["To"] = destinatario
        email["Subject"] = 'Email Contact'

        smtp = smtplib.SMTP_SSL('smtp.gmail.com')
        smtp.login(remitente, env('PASSWORD'))
        nombre = request.POST.get("Nombre")
        email_de_contacto = request.POST.get("E-mail")
        telefono = request.POST.get("Telefono")
        mensaje_de_contacto = request.POST.get("Mensaje")

        mensaje = """Nombre: """+nombre+"""
E-mail: """+email_de_contacto+"""
Teléfono: """+telefono+"""
Mensaje: 
"""+mensaje_de_contacto

        email.set_content(mensaje)

        smtp.sendmail(remitente, destinatario, email.as_string())
        smtp.quit()

        return JsonResponse({'status':"Mensaje de contacto enviado!"})