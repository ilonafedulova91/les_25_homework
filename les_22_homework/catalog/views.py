from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'catalog/home.html')

def contacts(request):
    success = None
    name = None
    phone = None
    message = None

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(name, phone, message)

        success = 'Сообщение успешно отправлено!'

    return render(request,'catalog/contacts.html', {
        'success': success,
        'name': name,
        'phone': phone,
        'message': message,
    })

#3. Configure the URLs