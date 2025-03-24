from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, welcome to your skincare app!")
