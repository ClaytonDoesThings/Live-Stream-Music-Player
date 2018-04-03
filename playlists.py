import ytda
import random

class Track:
    def __init__(self, title, id, publisher, desc, credit):
        self.title = title
        self.id = id
        self.publisher = publisher
        self.desc = desc
        self.credit = credit

class Playlist:
    def __init__(self, items):
        self.items = items
    def shuffle(self):
        return random.choice(self.items)


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
        for track in response.get('items'):
            title = track.get('snippet').get('title')
            id = track.get('contentDetails').get('videoId')
            publisher = "Ninety9Lives"
            desc = track.get('snippet').get('description')
            credit = desc[desc.find('Track: '): -(len(desc)-(desc.find('Questions?')-22))]
            result = Track(title, id, publisher, desc, credit)
            results.append(result)
    return results

ninety9lives = Playlist(ninety9lives_get())