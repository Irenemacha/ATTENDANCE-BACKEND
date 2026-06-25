from django.http import JsonResponse

def login(request):
    return JsonResponse({"message": "login works"})

def register(request):
    return JsonResponse({"message": "register works"})