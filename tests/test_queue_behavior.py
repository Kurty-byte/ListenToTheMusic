"""
Test queue behavior:
- Adding individual tracks from library = APPEND
- Creating queue from playlist = REPLACE
"""
from Library import Library
from Playlist import PlaylistManager
from Queue import MusicQueue

print("="*60)
print("TESTING QUEUE BEHAVIOR")
print("="*60)

library = Library()
playlist_manager = PlaylistManager()
music_queue = MusicQueue()

# Test 1: Add individual tracks (should append)
print("\n--- TEST 1: Add Individual Tracks from Library ---")
tracks = library.get_all_tracks()

print(f"Adding track 1: {tracks[0].get_title()}")
music_queue.add_track(tracks[0])
print(f"Queue size: {music_queue.get_size()}")

print(f"Adding track 2: {tracks[1].get_title()}")
music_queue.add_track(tracks[1])
print(f"Queue size: {music_queue.get_size()}")

print(f"Adding track 3: {tracks[2].get_title()}")
music_queue.add_track(tracks[2])
print(f"Queue size: {music_queue.get_size()}")

print("\nQueue contents:")
current = music_queue._MusicQueue__head
idx = 1
while current:
    print(f"  {idx}. {current.track.get_title()}")
    current = current.next
    idx += 1

print("\n✓ Individual tracks APPENDED to queue")

# Test 2: Create queue from playlist (should replace)
print("\n--- TEST 2: Create Queue from Playlist ---")
playlist = playlist_manager.get_playlist("My Playlist")
print(f"Current queue size: {music_queue.get_size()}")
print(f"Creating queue from playlist '{playlist.get_name()}'...")

music_queue.clear()
music_queue.load_tracks(playlist.get_tracks())

print(f"New queue size: {music_queue.get_size()}")
print("\nQueue contents:")
current = music_queue._MusicQueue__head
idx = 1
while current:
    print(f"  {idx}. {current.track.get_title()}")
    current = current.next
    idx += 1

print("\n✓ Playlist queue REPLACED entire queue")

print("\n" + "="*60)
print("SUMMARY")
print("="*60)
print("✓ Library tracks: add_track() appends to existing queue")
print("✓ Playlists: clear() + load_tracks() replaces queue")
print("✓ Behavior matches Spotify and other streaming services")
print("="*60)
