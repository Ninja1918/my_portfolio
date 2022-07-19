from django.shortcuts import render
from django.views import View


class index(View):
    def get(self ,request):
        context = {
            "footer" : True
        }
        return render(request,'main/index.html', context)

class about(View):
    def get(self, request):
        context = {
            "footer" : False
        }
        return render(request, 'main/about.html' , context)