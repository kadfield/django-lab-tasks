from django.http import HttpResponse


def home(request):
    return HttpResponse("Ana səhifə - University Portal")


def about(request):
    return HttpResponse("Haqqımızda - Layihə haqqında məlumat")


def contact(request):
    return HttpResponse("Əlaqə - Bizimlə əlaqə səhifəsi")
