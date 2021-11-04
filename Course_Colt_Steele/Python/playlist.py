playlist = {
	'title':'tidal wave',
	'author': 'Victor Souza',
	'songs': [
		{'Title': 'Australia Street', 'Artist': ['Sticky Fingers'], 'duration': 2.5},
		{'Title': 'Hyper', 'Artist': ['Sticky Fingers', 'God'], 'duration': 3.2},
		{'Title': 'Blinding Lights', 'Artist': ['The Weekend'], 'duration': 4.1},
		{'Title': 'Ou va le monde', 'Artist': ['La Femme'], 'duration': 1.5}
	]
}

for song in playlist['songs']:
	print(song['Title'])