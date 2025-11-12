import json
import os
from Track import Track

# Simple linked list node for playlist tracks
class PlaylistNode:
    def __init__(self, track):
        self.track = track
        self.next = None

class Playlist:
    def __init__(self, name):
        self.__name = name
        self.__head = None  # Linked list of tracks
        self.__track_set = set()  # Hash set for duplicate checking (stores titles)
        self.__size = 0
    
    # Getters
    def get_name(self):
        return self.__name
    
    def get_size(self):
        return self.__size
    
    # Check if track already exists in playlist
    def __has_track(self, track):
        # Simple duplicate check using title + artist
        track_id = track.get_title().lower() + str(track.get_artist()).lower()
        return track_id in self.__track_set
    
    # Add track to playlist
    def add_track(self, track):
        if self.__has_track(track):
            return False  # Track already exists
        
        new_node = PlaylistNode(track)
        track_id = track.get_title().lower() + str(track.get_artist()).lower()
        self.__track_set.add(track_id)
        
        # Add to end of linked list
        if self.__head is None:
            self.__head = new_node
        else:
            current = self.__head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.__size += 1
        return True
    
    # Get all tracks as a list
    def get_tracks(self):
        tracks = []
        current = self.__head
        while current:
            tracks.append(current.track)
            current = current.next
        return tracks
    
    # Calculate total duration
    def get_total_duration(self):
        total_seconds = 0
        current = self.__head
        while current:
            total_seconds += current.track.duration_to_seconds()
            current = current.next
        
        # Convert back to readable format
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        if hours > 0:
            return f"{hours} hr {minutes} min {seconds} sec"
        else:
            return f"{minutes} min {seconds} sec"
    
    # Display playlist
    def display(self):
        print(f"\n=== Playlist: {self.__name} ===")
        print(f"Total Duration: {self.get_total_duration()}")
        print("Tracks:")
        
        current = self.__head
        index = 1
        while current:
            print(f"    [{index}] {current.track.display()}")
            current = current.next
            index += 1
        print()
    
    # Convert to dictionary for saving
    def to_dict(self):
        tracks_data = []
        current = self.__head
        while current:
            tracks_data.append(current.track.to_dict())
            current = current.next
        
        return {
            "name": self.__name,
            "tracks": tracks_data
        }
    
    # Create playlist from dictionary
    @staticmethod
    def from_dict(data):
        playlist = Playlist(data["name"])
        for track_data in data["tracks"]:
            track = Track.from_dict(track_data)
            playlist.add_track(track)
        return playlist

# Playlist Manager to handle multiple playlists
class PlaylistManager:
    def __init__(self):
        self.__playlists = {}  # Hash map: name -> Playlist
        self.__file_path = "data/playlists.json"
        self.__load_from_file()
    
    # Create new playlist
    def create_playlist(self, name):
        if name in self.__playlists:
            return None  # Playlist name already exists
        
        playlist = Playlist(name)
        self.__playlists[name] = playlist
        self.__save_to_file()
        return playlist
    
    # Get playlist by name
    def get_playlist(self, name):
        return self.__playlists.get(name)
    
    # Get all playlist names
    def get_playlist_names(self):
        return list(self.__playlists.keys())
    
    # Display all playlists with pagination
    def display_playlists(self, page=1):
        names = self.get_playlist_names()
        if not names:
            print("No playlists created yet!")
            return
        
        items_per_page = 10
        total_pages = (len(names) + items_per_page - 1) // items_per_page
        
        start_idx = (page - 1) * items_per_page
        end_idx = min(start_idx + items_per_page, len(names))
        
        print("\n=== PLAYLISTS ===")
        for i in range(start_idx, end_idx):
            print(f"[{i + 1}] {names[i]}")
        
        if total_pages > 1:
            print(f"\n<Page {page} of {total_pages}>")
        print()
        
        return total_pages
    
    # Get playlist by index (for selection)
    def get_playlist_by_index(self, index):
        names = self.get_playlist_names()
        if 0 <= index < len(names):
            return self.__playlists[names[index]]
        return None
    
    # Add track to specific playlist
    def add_track_to_playlist(self, playlist_name, track):
        playlist = self.get_playlist(playlist_name)
        if playlist:
            result = playlist.add_track(track)
            if result:
                self.__save_to_file()
            return result
        return False
    
    # Save all playlists to file
    def __save_to_file(self):
        data = []
        for playlist in self.__playlists.values():
            data.append(playlist.to_dict())
        
        os.makedirs(os.path.dirname(self.__file_path), exist_ok=True)
        
        with open(self.__file_path, 'w') as f:
            json.dump(data, f, indent=4)
    
    # Load playlists from file
    def __load_from_file(self):
        if not os.path.exists(self.__file_path):
            return
        
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for playlist_data in data:
                    playlist = Playlist.from_dict(playlist_data)
                    self.__playlists[playlist.get_name()] = playlist
        except:
            print("Error loading playlists file")
