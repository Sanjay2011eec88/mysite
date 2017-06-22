from .models import Album, Song
from django.shortcuts import render, get_object_or_404

#
def index(request):
    all_albums = Album.objects.all()
    #template = loader.get_template('index.html')
    context = {
        'all_albums': all_albums,
    }
    return render(request, 'music/index.html',context)
    #return HttpResponse(template.render(context, request))
# def index(request):
#     all_objects = Album.objects.all()
#     html = ''
#     for album in all_objects:
#         url = "/music/" + str(album.id) + "/"
#         html += '<a href = "' + url + '">' + album.album_title + '</a><br>'
#     return HttpResponse(html)


def detail(request, album_id):
    #album = Album.objects.get(pk=album_id)
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album':album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError,Song.DoesNotExist):
        return render(request,'music/detail.html',{
            'album':album,
            'error_message':"You did not select a valid song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})