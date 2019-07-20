from mp3_converter.celery import app
from youtube_dl import YoutubeDL
from django.core.mail import send_mail
from django.conf import settings


@app.task
def download_mp3(url, email, protocol, host):
    print(settings.MEDIA_ROOT)
    options = {
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': 'media/%(id)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with YoutubeDL(options) as youtube_dl:
        extracted_info = youtube_dl.extract_info(url, download=True)
        id = extracted_info['id']
        download_link = protocol + '://' + host + '/media/' + id + '.mp3'

        send_email.delay(download_link, email)


@app.task
def send_email(url, email):
    send_mail(subject='mp3_converter', message=url, from_email=settings.EMAIL_HOST_USER, recipient_list=[email], fail_silently=False)
