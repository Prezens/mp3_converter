from django.shortcuts import render, redirect
from .forms import UrlForm
from .models import RequestVideo
from .tasks import download_mp3


def index_view(request):
    form = UrlForm()

    if request.method == 'POST':
        form = UrlForm(request.POST)

        if form.is_valid():
            url = form.cleaned_data['url']

            new_url = form.save(commit=False)
            new_url.url = url
            new_url.save()

            download_mp3.delay(url, form.cleaned_data['email'], request.scheme, request.META['HTTP_HOST'])

            return redirect('/')

    return render(request, 'converter/index.html', {'form': form})
