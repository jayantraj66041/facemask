from django.shortcuts import render
from django.views import View

# Create your views here.


class Landing(View):
    def get(self, request):
        return render(request, "landing.html")

    def post(self, request):
        pass
