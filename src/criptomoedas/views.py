from django.shortcuts import render

# Create your views here.
def example(request):
    return HttpResponseRedirect(reverse('news-year-archive', args=(year,)))