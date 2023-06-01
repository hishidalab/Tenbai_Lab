from django.shortcuts import render

def testView(request):
    return render(request, 'pengin/test.html')

