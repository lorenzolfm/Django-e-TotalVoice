from totalvoice.cliente import Cliente

def sendSMS(cadastro):
    if ' ' in cadastro.name:
        name = cadastro.name
        firstName = name[0]

    client = Cliente("<APIKey>", "api2.totalvoice.com.br")

    messageText = f"Parabéns, {cadastro.name}. Aqui está seu cupom de comida grátis: {cadastro.couponID}"
    client.sms.enviar(f"{cadastro.phoneNumber}", messageText)

