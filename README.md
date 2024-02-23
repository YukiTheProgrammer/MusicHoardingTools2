# Music Hoarding Tools 2 (Version 0.1)

A collection of Python programs to make the collection of offstreaming and leaked releases easier.

## Dependencies:
- python 3.12
## Instalation Guide:

## Setup Guide:

## Usage Guide:
## Documentation:
### B_DownloadFromSoundcloud.py
#### BaseSoundcloudDownloader(soundcloudUrl, path)
```
soundcloudUrl: url of track to download
path: path to directory where to download to (default: "E:\Soundcloud Downloads")

Downloads a track from SoundCloud.

path
|-song.mp3
```
#### MassBaseSoundcloudDownloader(soundcloudUrls, path)
```
soundcloudUrls: list of track urls to download
path: path to directory where to download to (default: "E:\Soundcloud Downloads")

Downloads a list of tracks from Soundcloud.

path
|-song1.mp3
|-song2.mp3
```
#### AlbumSoundcloudDownloader(albumUrl, path)
```
albumUrl: url of album to download
path: path to directory where to download to (default: "E:\Soundcloud Downloads")

Downloads an album from SoundCloud.

path
|-album
  |-albumSong1.mp3
  |-albumSong2.mp3
```
#### AllArtistAlbumsSoundloucdDownloader(artistUrl, path)
```
artistUrl: url of artist whos albums to download
path: path to directory where to download to (default: "E:\Soundcloud Downloads")

Downloads all albums from an artist.

path
|-album1
| |-album1Song1.mp3
| |-album1Song2.mp3
|
|-album2
  |-album2Song1.mp3
  |-album2Song2.mp3
```
#### AllArtistPlaylistsSoundloucdDownloader(artistUrl, path)
```
artistUrl: url of artist whos playlists to download
path: path to directory where to download to (default: "E:\Soundcloud Downloads")

Downloads all playlists from an artist.
path
|-playlist1
| |-playlist1Song1.mp3
| |-playlist1Song2.mp3
|
|-playlist2
  |-playlist2Song1.mp3
  |-playlist2Song2.mp3
```
#### AllArtistSoundloucdDownloader(artistUrl, path)
```
artistUrl: url of artist to download everything from
path: path to directory where to download to (default: "E:\Soundcloud Downloads")

Downloads everything from an artist.

path
|-artist
  |-album1
  | |-album1Song1.mp3
  | |-album1Song2.mp3
  |
  |-album2
  | |-album2Song1.mp3
  | |-album2Song2.mp3
  |
  |-playlist1
  | |-playlist1Song1.mp3
  | |-playlist1Song2.mp3
  |
  |-playlist2
  | |-playlist2Song1.mp3
  | |-playlist2Song2.mp3
  |
  |-song1.mp3
  |-song2.mp3
```
#### MassAllArtistSoundcloudDownloader(artistUrls,path)
```
artistUrls: list of artist urls to download from
path: path to directory where to download to (default: "E:\Soundcloud Downloads")

Downloads everything from a list of artists.

path
|-artist1
| |-album1
| | |-album1Song1.mp3
| | |-album1Song2.mp3
| |
| |-album2
| | |-album2Song1.mp3
| | |-album2Song2.mp3
| |
| |-playlist1
| | |-playlist1Song1.mp3
| | |-playlist1Song2.mp3
| |
| |-playlist2
| | |-playlist2Song1.mp3
| | |-playlist2Song2.mp3
| |
| |-song1.mp3
| |-song2.mp3
|
|-artist2
  |-album1
  | |-album1Song1.mp3
  | |-album1Song2.mp3
  |
  |-album2
  | |-album2Song1.mp3
  | |-album2Song2.mp3
  |
  |-playlist1
  | |-playlist1Song1.mp3
  | |-playlist1Song2.mp3
  |
  |-playlist2
  | |-playlist2Song1.mp3
  | |-playlist2Song2.mp3
  |
  |-song1.mp3
  |-song2.mp3
```

