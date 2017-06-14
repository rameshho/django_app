from django.http import HttpResponse
from django.http import Http404
from .models import Album, Song
# Create your views here.

'''
def index(request):
    #Connect to DataBase, look at albums table, and get all albums from there
    all_albums = Album.objects.all()

    html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html)
'''

'''
def index(request):
    from django.template import loader
    all_albums = Album.objects.all()

    #By default django looks for templates directory in your app directory
    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }
    return HttpResponse(template.render(context, request))
'''


def index(request):
    from django.shortcuts import render
    all_albums = Album.objects.all()

#   By default django looks for templates directory in your app directory
    context = {'all_albums': all_albums }


#   render function will automatically send httpresponse as return
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    from django.shortcuts import render, get_object_or_404
    '''
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    '''
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})


def favorite(request, album_id):
    from django.shortcuts import render, get_object_or_404
    '''
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    '''
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "You did not select a valid song",
        })
    else:
        selected_song.is_favourite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})

