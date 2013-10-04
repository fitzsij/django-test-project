# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from form_app.models import Package
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render

def search_form(request):
    return render(request, 'form_app/contact.html')

def showPackages(request):
	pkglist = Package.objects.all()
	return render_to_response('form_app/packages.html', {'packages': pkglist})


def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        pkglist = Package.objects.all()
        return render_to_response('form_app/search_results.html', {'packages': pkglist, 'query': q})
        #books = Book.objects.filter(title__icontains=q)
        #return render(request, 'form_app/search_results.html', {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')