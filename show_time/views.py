from django.shortcuts import render_to_response

def current_datetime(request):
    return render_to_response("index.html")
