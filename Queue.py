import json
import os
import random
from Track import Track

# Doubly linked list node for queue
class QueueNode:
    def __init__(self, track):
        self.track = track
        self.next = None
        self.prev = None

class MusicQueue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__current = None  # Currently playing track
        self.__size = 0
        self.__is_shuffled = False
        self.__is_repeat = False
        self.__is_playing = False
        self.__original_order = []  # For unshuffling
        self.__file_path = "data/queue_state.json"
    
    # Add track to queue
    def add_track(self, track):
        new_node = QueueNode(track)
        
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
            self.__current = new_node
        else:
            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node
        
        self.__size += 1
        self.__original_order.append(track)
    
    # Load tracks from a list (for creating queue from playlist/library)
    def load_tracks(self, tracks):
        for track in tracks:
            self.add_track(track)
        self.save_state()  # Save after loading tracks
    
    # Play (resume)
    def play(self):
        self.__is_playing = True
        self.save_state()
    
    # Pause
    def pause(self):
        self.__is_playing = False
        self.save_state()
    
    # Next track - O(1)
    def next_track(self):
        if not self.__current:
            return None
        
        if self.__current.next:
            self.__current = self.__current.next
        elif self.__is_repeat:
            # If repeat is on, go back to first track
            self.__current = self.__head
        else:
            # No repeat, stop at last track
            self.__is_playing = False
            self.save_state()
            return None
        
        self.save_state()
        return self.__current.track
    
    # Previous track - O(1)
    def previous_track(self):
        if not self.__current:
            return None
        
        if self.__current.prev:
            self.__current = self.__current.prev
        elif self.__is_repeat:
            # If repeat is on and at first track, go to last
            self.__current = self.__tail
        
        self.save_state()
        return self.__current.track
    
    # Shuffle queue
    def shuffle(self):
        if self.__is_shuffled or self.__size <= 1:
            return
        
        # Get all tracks
        tracks = []
        current = self.__head
        while current:
            tracks.append(current.track)
            current = current.next
        
        # Remember current track
        current_track = self.__current.track if self.__current else None
        
        # Shuffle
        random.shuffle(tracks)
        
        # Rebuild queue
        self.__head = None
        self.__tail = None
        self.__size = 0
        
        for track in tracks:
            new_node = QueueNode(track)
            if self.__head is None:
                self.__head = new_node
                self.__tail = new_node
            else:
                self.__tail.next = new_node
                new_node.prev = self.__tail
                self.__tail = new_node
            self.__size += 1
        
        # Find and set current track
        self.__current = None  # Reset first
        if current_track:
            current = self.__head
            while current:
                if current.track == current_track:
                    self.__current = current
                    break
                current = current.next
        
        # If current track wasn't found, default to head
        if not self.__current:
            self.__current = self.__head
        
        self.__is_shuffled = True
        self.save_state()
    
    # Helper to check if a node exists in the queue
    def __find_node(self, target_node):
        current = self.__head
        while current:
            if current == target_node:
                return True
            current = current.next
        return False
    
    # Unshuffle (restore original order)
    def unshuffle(self):
        if not self.__is_shuffled:
            return
        
        # Remember current track
        current_track = self.__current.track if self.__current else None
        
        # Rebuild queue with original order
        self.__head = None
        self.__tail = None
        self.__size = 0
        
        for track in self.__original_order:
            new_node = QueueNode(track)
            if self.__head is None:
                self.__head = new_node
                self.__tail = new_node
            else:
                self.__tail.next = new_node
                new_node.prev = self.__tail
                self.__tail = new_node
            self.__size += 1
        
        # Find and set current track
        self.__current = None  # Reset first
        if current_track:
            current = self.__head
            while current:
                if current.track == current_track:
                    self.__current = current
                    break
                current = current.next
        
        # If current track wasn't found, default to head
        if not self.__current:
            self.__current = self.__head
        
        self.__is_shuffled = False
        self.save_state()
    
    # Toggle repeat
    def toggle_repeat(self):
        self.__is_repeat = not self.__is_repeat
        self.save_state()
        return self.__is_repeat
    
    # Clear queue
    def clear(self):
        self.__head = None
        self.__tail = None
        self.__current = None
        self.__size = 0
        self.__is_shuffled = False
        self.__is_repeat = False
        self.__is_playing = False
        self.__original_order = []
        self.save_state()
    
    # Get current track
    def get_current_track(self):
        return self.__current.track if self.__current else None
    
    # Get total duration
    def get_total_duration(self):
        total_seconds = 0
        current = self.__head
        while current:
            total_seconds += current.track.duration_to_seconds()
            current = current.next
        
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        return f"{hours} hr {minutes} min"
    
    # Get current page number
    def get_current_page(self):
        if not self.__current:
            return 1
        
        count = 0
        current = self.__head
        while current and current != self.__current:
            count += 1
            current = current.next
        
        return (count // 10) + 1
    
    # Display queue (first 10 tracks)
    def display(self, page=1):
        if self.__size == 0:
            print("Queue is empty!")
            return
        
        print("\n=== MUSIC QUEUE ===")
        print(f"Total Duration: {self.get_total_duration()}")
        print(f"Shuffled: {'Yes' if self.__is_shuffled else 'No'}")
        print(f"Repeat: {'Yes' if self.__is_repeat else 'No'}")
        print("Tracks:")
        
        # Show current playing
        if self.__current:
            status = "Playing" if self.__is_playing else "Paused"
            print(f"\nCurrently {status}:")
            print(f"    {self.__current.track.display()}")
        
        print("\nNext:")
        
        # Calculate page
        items_per_page = 10
        total_pages = (self.__size + items_per_page - 1) // items_per_page
        
        # Get tracks to display
        tracks_list = []
        current = self.__head
        while current:
            tracks_list.append(current)
            current = current.next
        
        start_idx = (page - 1) * items_per_page
        end_idx = min(start_idx + items_per_page, self.__size)
        
        for i in range(start_idx, end_idx):
            node = tracks_list[i]
            marker = " -> " if node == self.__current else "    "
            print(f"{marker}({i + 1}) {node.track.display()}")
        
        print(f"\n<Page {page} of {total_pages}>")
        print()
    
    # Save queue state
    def save_state(self):
        tracks_data = []
        current = self.__head
        current_index = -1
        idx = 0
        
        while current:
            tracks_data.append(current.track.to_dict())
            if current == self.__current:
                current_index = idx
            current = current.next
            idx += 1
        
        original_data = [t.to_dict() for t in self.__original_order]
        
        state = {
            "tracks": tracks_data,
            "current_index": current_index,
            "is_shuffled": self.__is_shuffled,
            "is_repeat": self.__is_repeat,
            "is_playing": self.__is_playing,
            "original_order": original_data
        }
        
        os.makedirs(os.path.dirname(self.__file_path), exist_ok=True)
        
        with open(self.__file_path, 'w') as f:
            json.dump(state, f, indent=4)
    
    # Load queue state
    def load_state(self):
        if not os.path.exists(self.__file_path):
            return False
        
        try:
            with open(self.__file_path, 'r') as f:
                state = json.load(f)
                
                # Clear current queue
                self.__head = None
                self.__tail = None
                self.__size = 0
                
                # Load tracks
                for track_data in state["tracks"]:
                    track = Track.from_dict(track_data)
                    new_node = QueueNode(track)
                    if self.__head is None:
                        self.__head = new_node
                        self.__tail = new_node
                    else:
                        self.__tail.next = new_node
                        new_node.prev = self.__tail
                        self.__tail = new_node
                    self.__size += 1
                
                # Set current track
                current_index = state["current_index"]
                if current_index >= 0:
                    current = self.__head
                    for i in range(current_index):
                        if current:
                            current = current.next
                    self.__current = current
                
                # Restore state
                self.__is_shuffled = state["is_shuffled"]
                self.__is_repeat = state["is_repeat"]
                self.__is_playing = state["is_playing"]
                
                # Load original order
                self.__original_order = []
                for track_data in state["original_order"]:
                    track = Track.from_dict(track_data)
                    self.__original_order.append(track)
                
                return True
        except:
            return False
    
    # Getters for state
    def is_playing(self):
        return self.__is_playing
    
    def is_shuffled(self):
        return self.__is_shuffled
    
    def is_repeat_on(self):
        return self.__is_repeat
    
    def get_size(self):
        return self.__size
