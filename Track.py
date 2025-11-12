import json

class Track:
    def __init__(self, title, artist, album, duration):
        # Private attributes with data encapsulation
        self.__title = title
        self.__artist = artist  # can be string or list for multiple artists
        self.__album = album
        self.__duration = duration  # format: "mm:ss"
    
    # Getters for encapsulation
    def get_title(self):
        return self.__title
    
    def get_artist(self):
        return self.__artist
    
    def get_album(self):
        return self.__album
    
    def get_duration(self):
        return self.__duration
    
    # Setters (in case we need to modify later)
    def set_title(self, title):
        self.__title = title
    
    def set_artist(self, artist):
        self.__artist = artist
    
    def set_album(self, album):
        self.__album = album
    
    def set_duration(self, duration):
        self.__duration = duration
    
    # Convert duration to seconds for calculations
    def duration_to_seconds(self):
        parts = self.__duration.split(":")
        minutes = int(parts[0])
        seconds = int(parts[1])
        return minutes * 60 + seconds
    
    # Get main artist (for sorting when multiple artists)
    def get_main_artist(self):
        if isinstance(self.__artist, list):
            return self.__artist[0]
        return self.__artist
    
    # Display format
    def display(self):
        artist_str = self.__artist
        if isinstance(self.__artist, list):
            artist_str = ", ".join(self.__artist)
        return f"{self.__title} - {artist_str} ({self.__duration})"
    
    # For saving to JSON
    def to_dict(self):
        return {
            "title": self.__title,
            "artist": self.__artist,
            "album": self.__album,
            "duration": self.__duration
        }
    
    # For loading from JSON
    @staticmethod
    def from_dict(data):
        return Track(data["title"], data["artist"], data["album"], data["duration"])
    
    # String representation
    def __str__(self):
        return self.display()
