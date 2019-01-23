from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

#python3 manage.py makemigrations
#python3 manage.py makemigrations music
#python manage.py sqlmigrate music 0001
#python3 manage.py migrate
#python manage.py shell

#from music.models import Album, Song
#Album.objects.all()
#Album.objects.filter(artist__startswith='Taylor')

#album1 = Album.objects.get(pk=1)
# song = Song()
#song.save()
#album1.song_set.all()
# album1.song_set.create(song_title= 'I love bacon', file_type = 'mp3')
#album1.song_set.count()