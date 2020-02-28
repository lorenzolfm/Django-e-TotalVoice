from django.shortcuts import render
from cadastro.models import User
from cadastro.utils import sendSMS

def index(request):
    if request.method == 'POST':
        try:
            emailRegistered = User.objects.get(email = request.POST['email'])
            return render(request, 'cadastro/index.html', {'error': 'Email já registrado'})
        except User.DoesNotExist:
            try:
                phoneNumberRegistered = User.objects.get(phoneNumber = request.POST['phoneNumber'])
                return render(request, 'cadastro/index.html', {'error': 'Telefone já registrado'})
            except User.DoesNotExist:
                registeredUser = User(
                    name = request.POST['name'],
                    email = request.POST['email'],
                    phoneNumber = request.POST['phoneNumber'],
                    couponID = User.setCouponID()
                )
                registeredUser.save()
                sendSMS(registeredUser)
                return render(request, 'cadastro/index.html', {'success': 'Cadastro realizado com sucesso! Cupom de comida a caminho :D'})
    else:
        return render(request, 'cadastro/index.html')
