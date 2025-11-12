import sys
import os

# Add parent directory to path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Library import Library
from Playlist import PlaylistManager
from Track import Track

def populate_library():
    print("Populating library...")
    library = Library()
    
    # Sample tracks
    tracks_data = [
        ("Gangnam Style", "PSY", "Psy 6 (Six Rules), Part 1", "03:39"),
        ("GAS GAS GAS EXTENDED MIX", "Manuel", "Initial D", "04:21"),
        ("Counting Stars", "OneRepublic", "Native", "04:17"),
        ("Feel This Moment", ["Pitbull", "Christina Aguilera"], "Global Warming", "03:50"),
        ("Call Me Maybe", "Carly Rae Jepsen", "Kiss", "03:13"),
        ("Timber", "Kesha", "The Party Don't Stop", "03:24"),
        ("Roar", "Katy Perry", "Prism", "03:44"),
        ("I Knew You Were Trouble", "Taylor Swift", "Red", "03:40"),
        ("Just Dance", ["Lady Gaga", "Colby O'Donis"], "The Fame", "04:02"),
        ("Domino", "Jessie J", "Who You Are", "03:52"),
        ("Payphone", ["Maroon 5", "Wiz Khalifa"], "Overexposed", "03:51"),
        ("Blinded in Chains", "Avenged Sevenfold", "City of Evil", "06:34"),
        ("Bad Romance", "Lady Gaga", "The Fame Monster", "04:55"),
        ("Dynamite", "BTS", "BE", "03:19"),
        ("Butter", "BTS", "Butter - Single", "02:44"),
        ("Shape of You", "Ed Sheeran", "÷ (Divide)", "03:53"),
        ("Blank Space", "Taylor Swift", "1989", "03:51"),
        ("Uptown Funk", ["Mark Ronson", "Bruno Mars"], "Uptown Special", "04:30"),
        ("Someone Like You", "Adele", "21", "04:45"),
        ("Rolling in the Deep", "Adele", "21", "03:48"),
        ("Closer", ["The Chainsmokers", "Halsey"], "Collage", "04:04"),
        ("Wake Me Up", "Avicii", "True", "04:09"),
        ("Radioactive", "Imagine Dragons", "Night Visions", "03:06"),
        ("Demons", "Imagine Dragons", "Night Visions", "02:57"),
        ("Believer", "Imagine Dragons", "Evolve", "03:24"),
    ]
    
    for track_data in tracks_data:
        track = Track(track_data[0], track_data[1], track_data[2], track_data[3])
        library.add_track(track)
    
    print(f"Added {len(tracks_data)} tracks to library!")
    return library

def populate_playlists(library):
    print("\nPopulating playlists...")
    playlist_manager = PlaylistManager()
    
    # Get all tracks from library
    all_tracks = library.get_all_tracks()
    
    # Create sample playlists
    playlists_config = [
        ("My Playlist", [0, 3, 6, 9]),  # Some random tracks
        ("Tempo", [1, 11, 21, 22]),
        ("NewLove", [4, 5, 7, 15]),
        ("K-PaPop", [0, 13, 14]),
        ("JPop", [1, 8]),
        ("Anime", [11, 22, 23]),
        ("G(OLD)", [3, 4, 8, 9, 12, 18, 19]),
        ("Pinoy Classic", [16, 17, 20]),
        ("HeartBr3@k", [6, 7, 18]),
        ("HearBre@k2", [4, 15, 19, 21]),
        ("Workout Mix", [1, 11, 17, 22, 24]),
        ("Chill Vibes", [18, 19, 21]),
    ]
    
    for playlist_name, track_indices in playlists_config:
        playlist = playlist_manager.create_playlist(playlist_name)
        if playlist:
            for idx in track_indices:
                if idx < len(all_tracks):
                    playlist_manager.add_track_to_playlist(playlist_name, all_tracks[idx])
            print(f"Created playlist: {playlist_name}")
    
    print(f"Added {len(playlists_config)} playlists!")

def main():
    print("="*50)
    print("  POPULATING LISTEN TO THE MUSIC SYSTEM")
    print("="*50)
    print()
    
    # Populate library first
    library = populate_library()
    
    # Then populate playlists
    populate_playlists(library)
    
    print("\n" + "="*50)
    print("  POPULATION COMPLETE!")
    print("="*50)
    print("\nYou can now run Main.py to explore the system!")

if __name__ == "__main__":
    main()
