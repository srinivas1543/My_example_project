from django.shortcuts import render,redirect

activities = []

def index(request):
    return render(request,'index.html',{'activities' : activities})


def add(request):
    if request.method == 'POST':
        activity = request.POST.get('activity')
        if(activity):
            activities.append(activity)
    return redirect('/')


def delete(request):
    if request.method == 'POST':
        index = request.POST.get('index')
        if index is not None:
            index = int(index)
            if index>=0 and index < len(activities):
                activities.pop(index)
    return redirect('/')

def update(request):
    if request.method == 'POST':
        index = int(request.POST.get('index'))
        new_activity = request.POST.get('new_activity')
        if index is not None and new_activity:
            if index>=0 and index<len(activities):
                activities[index] = new_activity
    return redirect('/')
