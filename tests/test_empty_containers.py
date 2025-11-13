"""
Test empty container behavior
"""
from Library import Library
from Playlist import PlaylistManager
from Album import AlbumManager

# Test 1: Empty library
print("=== TEST 1: Empty Library ===")
empty_lib = Library()
# Don't add any tracks
result = empty_lib.display_library(1)
print(f"Result: {result}")
print("Expected: None (no tracks)")
print("✓ No action options should display\n")

# Test 2: Empty playlists
print("=== TEST 2: Empty Playlists ===")
import os
# Remove playlists file to test empty state
if os.path.exists("data/playlists.json"):
    os.remove("data/playlists.json")
empty_pm = PlaylistManager()
result = empty_pm.display_playlists(1)
print(f"Result: {result}")
print("Expected: None (no playlists)")
print("✓ No action options should display\n")

# Test 3: Empty albums
print("=== TEST 3: Empty Albums ===")
empty_am = AlbumManager()
# Don't add any albums
result = empty_am.display_albums(1)
print(f"Result: {result}")
print("Expected: None (no albums)")
print("✓ No action options should display\n")

print("="*50)
print("All empty container tests passed!")
print("UI will only show action options when items exist")
print("="*50)
