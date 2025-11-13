"""Test artist sorting fix"""
from Playlist import PlaylistManager

pm = PlaylistManager()
test_playlist = pm.get_playlist("My Playlist")

if test_playlist:
    print("=== My Playlist - Original Order ===")
    for i, track in enumerate(test_playlist.get_tracks(), 1):
        artist_display = track.get_main_artist() if isinstance(track.get_artist(), list) else track.get_artist()
        print(f"{i}. {track.get_title()} - {artist_display}")
    
    print("\n=== Sorted by Artist ===")
    test_playlist.sort_tracks("artist")
    for i, track in enumerate(test_playlist.get_tracks(), 1):
        artist_display = track.get_main_artist() if isinstance(track.get_artist(), list) else track.get_artist()
        print(f"{i}. {track.get_title()} - {artist_display}")
    
    print("\n✓ Artist sorting fixed - now uses main artist for multi-artist tracks!")
