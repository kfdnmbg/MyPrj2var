import g4f
from django.shortcuts import render
import markdown



def home(request):
    response = ''
    if request.method == 'POST':
        prompt = request.POST.get('lang')
        if prompt == None:
            prompt = ''
        input_text = request.POST.get('query')
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=[{"role":"system", "content":prompt},
                      {"role":"user", "content":input_text},
                      ],
            timeout=120,
        ) 
    response = markdown.markdown(response)
    return render(request, 'index.html', {'result': response})
