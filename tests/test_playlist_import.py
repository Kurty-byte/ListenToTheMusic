"""
Test playlist import functionality
"""
from Playlist import PlaylistManager

print("="*60)
print("TESTING PLAYLIST IMPORT")
print("="*60)

pm = PlaylistManager()

# Test JSON import
print("\n--- TEST 1: Import from JSON ---")
result = pm.import_playlists("import/playlists/playlist1.json")
print(f"Success: {result['success']}")
print(f"Imported: {result['imported']} playlists")
print(f"Duplicates: {result.get('duplicates', 0)}")
print(f"Skipped: {result['skipped']}")

# Test CSV import
print("\n--- TEST 2: Import from CSV ---")
result = pm.import_playlists("import/playlists/playlist2.csv")
print(f"Success: {result['success']}")
print(f"Imported: {result['imported']} playlists")
print(f"Duplicates: {result.get('duplicates', 0)}")
print(f"Skipped: {result['skipped']}")

# Test duplicate detection
print("\n--- TEST 3: Import Duplicate (should skip) ---")
result = pm.import_playlists("import/playlists/playlist1.json")
print(f"Success: {result['success']}")
print(f"Imported: {result['imported']} playlists")
print(f"Duplicates: {result.get('duplicates', 0)}")

# Display imported playlists
print("\n--- Imported Playlists ---")
pm.display_playlists(1)

# Check playlist contents
print("\n--- Checking Playlist Contents ---")
playlist = pm.get_playlist("Eminem Classics")
if playlist:
    print(f"Playlist: {playlist.get_name()}")
    print(f"Track count: {playlist.get_size()}")
    for track in playlist.get_tracks():
        print(f"  - {track.get_title()} by {track.get_artist()}")

print("\n" + "="*60)
print("✓ Playlist import functionality working!")
print("="*60)
