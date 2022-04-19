from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class chatbot(TemplateView):
    template_name = 'chatbot.html'
    def get(self,request):
        return render(request,self.template_name)

    def post(self,request):
        if request.method == 'POST':
            user = request.POST.get('input',False)
            print(user)
            
            # context={"user":user,"bot":chat(request)}
        return render(request,self.template_name)