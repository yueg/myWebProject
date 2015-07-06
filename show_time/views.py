from django.shortcuts import render_to_response

time = 0
def current_datetime(request):
    time = 1
    return render_to_response("index.html")
