from django.shortcuts import render
from . import forms


def page_count(request):
    count = request.session.get('count', 0)
    newcount = count + 1
    request.session['count'] = newcount
    print(request.session.set_expiry(120))
    # print(request.session.get_expiry_age())
    # print(request.session.set_expiry_date())
    return render(request, 'result.html', {'count': newcount})

def regform(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        html = 'we have recieved this form again'
    else:
        html = 'welcome for first time'
    return render(request, 'signup.html', {'html': html, 'form': form})

#Form #View Functions
def regform(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        html = 'we have recieved this form again'
        if form.is_valid():
            html = html + "The Form is Valid"
    else:
        html = 'welcome for first time'
    return render(request, 'signup.html', {'html': html, 'form': form})