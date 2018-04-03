import ytda
import random

class Playlist:
    def __init__(self, items, shuffle):
        self.items = items
        self.shuffle = shuffle

def ninety9lives_get():
    results = []
    pageToken = None
    working = True
    while working:
        response = ytda.playlist_items_list_by_playlist_id(ytda.client,
            part='snippet,contentDetails',
            maxResults=50,
            pageToken=pageToken,
            playlistId='PLiqQaVH2Y0AclIaiZzfdu1JEQmGeGah8A'
        )
        if 'nextPageToken' in response:
            pageToken = response.get('nextPageToken')
        else:
            working = False
        results = results+response.get('items')
    return results

def ninety9lives_shuffle (playlist):
    return random.choice(playlist.items).get('contentDetails').get('videoId')

ninety9lives = Playlist(ninety9lives_get(), ninety9lives_shuffle)