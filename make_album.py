album = {}
def make_album(artist, title, tracks=''):
	if tracks:
		album[title] = (artist, tracks)
	else:
		album[title] = artist

while True:
	artist = input("artist? ")
	if artist.lower() == 'q':
		break
	title = input("title? ")
	if title.lower() == 'q':
		break
	tracks = input("tracks? ")
	if tracks.lower() == 'q':
		break	
	if tracks:
		make_album(artist,title,tracks)
	else:
		make_album(artist,title)

print(album)
