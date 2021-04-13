from django.shortcuts import render,redirect

def index(request):
    context = {
        "languages":[
            'HTML',
            'CSS',
            'JavaScript',
            'Python',
            'Mern',
            'Java',
            'C#']
        }

    return render(request,'index.html', context)


def success(request):
    language = " , ".join(request.POST.getlist('language'))
    print(request.POST.getlist('language'))
    context={
        "name":getSet(request, 'name'),
        "location": getSet(request, 'location'),
        "language":language,
        "message":getSet(request, 'message'),
        "refer":getSet(request, 'refer')

    }
    return render(request,'success.html',context)

def close(request):
   
    request.session.delete()
    return redirect('/index')


def getSet(request, name):
    response = None
    try:
        try:
            if request.POST[name]:
                response = request.POST[name]
                request.session[name] = response
        except:
            pass
        for key, value in request.session.items():
            if key == name:
                response = value
    except:
        pass
    return response