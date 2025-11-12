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
    
    # Sample tracks - expanded with more tracks from same albums
    tracks_data = [
        # Adele - 21 (multiple tracks from same album)
        ("Someone Like You", "Adele", "21", "04:45"),
        ("Rolling in the Deep", "Adele", "21", "03:48"),
        ("Set Fire to the Rain", "Adele", "21", "04:01"),
        ("Rumour Has It", "Adele", "21", "03:43"),
        ("Turning Tables", "Adele", "21", "04:10"),
        
        # Adele - 25
        ("Hello", "Adele", "25", "04:55"),
        ("When We Were Young", "Adele", "25", "04:50"),
        
        # Imagine Dragons - Night Visions (multiple tracks)
        ("Radioactive", "Imagine Dragons", "Night Visions", "03:06"),
        ("Demons", "Imagine Dragons", "Night Visions", "02:57"),
        ("It's Time", "Imagine Dragons", "Night Visions", "04:00"),
        ("On Top of the World", "Imagine Dragons", "Night Visions", "03:12"),
        
        # Imagine Dragons - Evolve
        ("Believer", "Imagine Dragons", "Evolve", "03:24"),
        ("Thunder", "Imagine Dragons", "Evolve", "03:07"),
        ("Whatever It Takes", "Imagine Dragons", "Evolve", "03:21"),
        
        # Taylor Swift - Red
        ("I Knew You Were Trouble", "Taylor Swift", "Red", "03:40"),
        ("We Are Never Getting Back Together", "Taylor Swift", "Red", "03:13"),
        ("22", "Taylor Swift", "Red", "03:52"),
        
        # Taylor Swift - 1989
        ("Blank Space", "Taylor Swift", "1989", "03:51"),
        ("Shake It Off", "Taylor Swift", "1989", "03:39"),
        ("Style", "Taylor Swift", "1989", "03:51"),
        
        # Lady Gaga - The Fame
        ("Just Dance", ["Lady Gaga", "Colby O'Donis"], "The Fame", "04:02"),
        ("Poker Face", "Lady Gaga", "The Fame", "03:57"),
        ("Paparazzi", "Lady Gaga", "The Fame", "03:28"),
        
        # Lady Gaga - The Fame Monster
        ("Bad Romance", "Lady Gaga", "The Fame Monster", "04:55"),
        ("Telephone", ["Lady Gaga", "Beyoncé"], "The Fame Monster", "03:40"),
        ("Alejandro", "Lady Gaga", "The Fame Monster", "04:34"),
        
        # BTS - BE
        ("Dynamite", "BTS", "BE", "03:19"),
        ("Life Goes On", "BTS", "BE", "03:27"),
        
        # BTS - Butter - Single
        ("Butter", "BTS", "Butter - Single", "02:44"),
        ("Permission to Dance", "BTS", "Butter - Single", "03:07"),
        
        # OneRepublic - Native
        ("Counting Stars", "OneRepublic", "Native", "04:17"),
        ("If I Lose Myself", "OneRepublic", "Native", "04:02"),
        ("Love Runs Out", "OneRepublic", "Native", "03:43"),
        
        # Ed Sheeran - ÷ (Divide)
        ("Shape of You", "Ed Sheeran", "÷ (Divide)", "03:53"),
        ("Castle on the Hill", "Ed Sheeran", "÷ (Divide)", "04:21"),
        ("Perfect", "Ed Sheeran", "÷ (Divide)", "04:23"),
        
        # Maroon 5 - Overexposed
        ("Payphone", ["Maroon 5", "Wiz Khalifa"], "Overexposed", "03:51"),
        ("One More Night", "Maroon 5", "Overexposed", "03:39"),
        
        # Single tracks from various albums
        ("Gangnam Style", "PSY", "Psy 6 (Six Rules), Part 1", "03:39"),
        ("GAS GAS GAS EXTENDED MIX", "Manuel", "Initial D", "04:21"),
        ("Feel This Moment", ["Pitbull", "Christina Aguilera"], "Global Warming", "03:50"),
        ("Call Me Maybe", "Carly Rae Jepsen", "Kiss", "03:13"),
        ("Timber", "Kesha", "The Party Don't Stop", "03:24"),
        ("Roar", "Katy Perry", "Prism", "03:44"),
        ("Domino", "Jessie J", "Who You Are", "03:52"),
        ("Blinded in Chains", "Avenged Sevenfold", "City of Evil", "06:34"),
        ("Uptown Funk", ["Mark Ronson", "Bruno Mars"], "Uptown Special", "04:30"),
        ("Closer", ["The Chainsmokers", "Halsey"], "Collage", "04:04"),
        ("Wake Me Up", "Avicii", "True", "04:09"),
    ]
    
    for track_data in tracks_data:
        track = Track(track_data[0], track_data[1], track_data[2], track_data[3])
        library.add_track(track)
    
    print(f"Added {len(tracks_data)} tracks to library!")
    
    # Display album statistics
    album_manager = library.get_album_manager()
    albums = album_manager.get_all_albums()
    print(f"Created {len(albums)} albums automatically!")
    
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
