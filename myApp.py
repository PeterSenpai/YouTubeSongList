from Search import *
from addVideo import *
from listSongs import *
from deleteSongs import *

# initialize some vars
playlistId = 'PLh7jOgIfINLNziVOJf-OIFgUGv9CL_lRT'
maxR = 50

# open local file and read all the songs
with open('song.txt', encoding='UTF-8') as f:
    keywords = f.readlines()
keywords = [k.strip() for k in keywords]

k1 = keywords[:50]
k2 = keywords[50:]


# Auth
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
client = get_authenticated_service()

# list all the current song in the list
curr_songs = playlist_items_list_by_playlist_id(client, part='snippet,contentDetails', maxResults=maxR,
                                                playlistId=playlistId)
# delete all the songs
for song in curr_songs:
    playlist_items_delete(client, id=song, onBehalfOfContentOwner='')

# add all the songs
for k in k1:
    vId = search_list_by_keyword(client, part='snippet', maxResults=maxR, q=k, type='youtube#video')

    playlist_items_insert(client,
                          {'snippet.playlistId': playlistId,
                           'snippet.resourceId.kind': 'youtube#video',
                           'snippet.resourceId.videoId': vId,
                           'snippet.position': ''},
                          part='snippet',
                          onBehalfOfContentOwner='')

for k in k2:
    vId = search_list_by_keyword(client, part='snippet', maxResults=maxR, q=k, type='youtube#video')

    playlist_items_insert(client,
                          {'snippet.playlistId': playlistId,
                           'snippet.resourceId.kind': 'youtube#video',
                           'snippet.resourceId.videoId': vId,
                           'snippet.position': ''},
                          part='snippet',
                          onBehalfOfContentOwner='')