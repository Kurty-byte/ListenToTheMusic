# Listen to the Music - Music Playlist Management System

**A Course Project for ITCC45 (Object-Oriented Programming) and ITCC47 (Data Structures and Algorithms)**

## Table of Contents
1. [Overview](#overview)
2. [Project Requirements](#project-requirements)
3. [System Features](#system-features)
4. [Data Structures Used](#data-structures-used)
5. [Object-Oriented Programming Concepts](#object-oriented-programming-concepts)
6. [Additional Features (Beyond Requirements)](#additional-features-beyond-requirements)
7. [File Structure](#file-structure)
8. [Files and Their Purposes](#files-and-their-purposes)
9. [How to Launch the System](#how-to-launch-the-system)
10. [How to Populate the System](#how-to-populate-the-system)
11. [System Navigation Guide](#system-navigation-guide)

---

## Overview

Listen to the Music is a comprehensive music playlist management system developed as a course project for **ITCC45 (Computer Programming 3)** and **ITCC47 (Data Structures and Algorithms)**. Built entirely in Python, this system demonstrates the practical application of fundamental computer science concepts including Binary Search Trees, Doubly Linked Lists, Hash Maps, and object-oriented design principles.

The system allows users to manage a music library, create and organize playlists, maintain a playback queue, and import tracks and playlists from external files. It serves as a practical implementation of core programming concepts taught in both courses, showcasing data structure selection, algorithm optimization, and proper software design.

**Course Information:**
- **ITCC47** - Data Structures and Algorithms: Implements BST, Doubly Linked List, Hash Maps, and various algorithms
- **ITCC45** - Object-Oriented Programming: Demonstrates encapsulation, abstraction, class design, and object relationships

---

## Project Requirements

### Core Requirements
1. **Track Management**
   - Add tracks with title, artist(s), album, and duration
   - Store track information with data encapsulation
   - Support for multiple artists per track

2. **Music Library**
   - Maintain a sorted collection of all tracks
   - Search tracks by title
   - Display library contents

3. **Playlist Management**
   - Create named playlists
   - Add tracks to playlists
   - View playlist contents with total duration
   - Prevent duplicate tracks in playlists

4. **Music Queue**
   - Add tracks to playback queue
   - Navigate queue (next/previous)
   - Display current track indicator
   - Play/pause functionality
   - Clear queue

5. **Data Persistence**
   - Save library, playlists, and queue state to files
   - Load data on system restart

### Optional Challenges Implemented
1. **Shuffle and Repeat (8 points)**
   - Shuffle queue while maintaining current track
   - Toggle repeat mode
   - Restore original order when unshuffling

2. **Album Tracking (6 points)**
   - Automatic album creation when tracks are added
   - View all albums with track counts
   - Create queue from albums

3. **Importing Tracks (12 points)**
   - Import tracks from JSON files
   - Import tracks from CSV files
   - Duplicate detection
   - Error handling and reporting

4. **Sorter (20 points)**
   - Sort playlists by date created, name, or duration
   - Sort tracks within playlists by date added, title, artist, or duration
   - Five-level tie-breaker hierarchy
   - Temporary sorting (does not persist)

**Total Bonus Points Achieved: 46/46 (100%)**

---

## System Features

### Music Library
- Add individual tracks manually
- View library with pagination (10 tracks per page)
- Search tracks by title
- View all albums organized automatically
- Import tracks from JSON/CSV files
- Add tracks from library to queue
- Binary Search Tree maintains sorted order

### Playlists
- Create named playlists
- View all playlists with pagination
- Add tracks to playlists from library
- View playlist details with track list
- Sort playlists by multiple criteria
- Sort tracks within playlists
- Create queue from playlists
- Import playlists from JSON/CSV files
- Timestamps track creation and track additions

### Music Queue
- Create queue from playlists or albums
- Add individual tracks from library
- Play/Pause controls
- Next/Previous track navigation (O(1) complexity)
- Shuffle mode with original order preservation
- Repeat mode
- Current track indicator with arrow
- Queue state persistence
- Display with pagination

### Albums
- Automatic album creation from tracks
- View all albums with pagination
- Display album details (track count, duration)
- Create queue directly from albums

### Import System
- Organized import directories (tracks/, playlists/)
- Support for JSON and CSV formats
- Automatic format detection
- Duplicate detection
- Comprehensive error reporting
- Multi-artist support in CSV

---

## Data Structures Used

### 1. Binary Search Tree (BST)
**Implementation:** `Library` class
- **Purpose:** Maintain sorted track collection with efficient insertion and search
- **Complexity:** O(log n) average for insert, search, and traversal
- **Sorting Criteria:** title -> artist -> album -> duration -> date added
- **Location:** `Library.py`

### 2. Doubly Linked List
**Implementations:**
- **Music Queue** (`Queue.py`): Enables O(1) next/previous navigation
- **Playlists** (`Playlist.py`): Maintains track order within playlists
- **Advantages:**
  - Constant time forward/backward traversal
  - Efficient insertion at tail
  - Maintains pointer to current track

### 3. Hash Maps (Python dict)
**Implementations:**
- **PlaylistManager:** O(1) playlist lookup by name
- **AlbumManager:** O(1) album lookup by name
- **Playlist duplicate checking:** O(1) track existence verification using track_id
- **Purpose:** Fast lookups and duplicate detection

### 4. Hash Set (Python set)
**Implementation:** Playlist track duplicate detection
- **Purpose:** O(1) duplicate checking using track identifier
- **Location:** `Playlist.__track_set`

### 5. Arrays (Python list)
**Uses:**
- Temporary storage for sorting operations
- Search results
- Import data processing
- Pagination calculations

---

## Object-Oriented Programming Concepts

### 1. Data Encapsulation
All classes use private attributes with double underscore prefix:
```python
class Track:
    def __init__(self, title, artist, album, duration):
        self.__title = title      # Private attribute
        self.__artist = artist    # Private attribute
        # ... with public getters/setters
```
**Classes with encapsulation:**
- Track
- Library
- Playlist
- PlaylistManager
- MusicQueue
- Album
- AlbumManager

### 2. Abstraction
- Users interact with public methods without knowing internal implementation
- Complex data structure operations hidden behind simple interfaces
- Example: `library.add_track(track)` hides BST insertion logic

### 3. Class Design
**Core Classes:**
- `Track`: Represents a music track with metadata
- `Library`: Manages track collection using BST
- `Playlist` / `PlaylistManager`: Manages playlist collections
- `MusicQueue`: Manages playback queue
- `Album` / `AlbumManager`: Manages album collections

**Node Classes:**
- `BSTNode`: Binary Search Tree node for library
- `PlaylistNode`: Linked list node for playlists
- `QueueNode`: Doubly linked list node for queue

### 4. Static Methods
- `Track.from_dict()`: Create track from dictionary
- `Playlist.from_dict()`: Create playlist from dictionary

### 5. Object Relationships
- **Composition:** Library contains Tracks, Playlists contain Tracks
- **Aggregation:** Queue references Tracks without ownership
- **Association:** AlbumManager manages Albums

### 6. Method Overloading
- `__eq__` method in Track class for content-based comparison
- Enables proper duplicate detection and sorting

---

## Additional Features (Beyond Requirements)

### User Experience Enhancements
1. **Pagination System**
   - All list views support pagination (10 items per page)
   - Navigation: [n] Next, [p] Previous, [b] Back
   - Page indicator: "<Page X of Y>"

2. **Dynamic Menu Options**
   - Play/Pause toggle based on state
   - Repeat On/Off toggle
   - Shuffle On/Off toggle
   - Context-sensitive options

3. **Enhanced Queue Creation**
   - Create queue from playlists
   - Create queue from albums
   - Add individual tracks to existing queue

4. **Improved Import System**
   - Organized directory structure (tracks/, playlists/)
   - Separate duplicate and error counts
   - Detailed error messages
   - Multi-artist CSV support

5. **Sort Functionality**
   - Multiple sorting criteria for playlists
   - Multiple sorting criteria for tracks
   - Option to restore original order
   - Integrated into viewing screens

6. **Empty State Handling**
   - Action options hidden when containers are empty
   - Clear "empty" messages displayed
   - User-friendly navigation

7. **Consistent UI Format**
   - Standardized navigation prompts
   - Format: [letter] Action | [letter] Action | [letter] Action
   - "Enter choice:" prompts throughout

### Technical Enhancements
1. **Artist Handling**
   - Support for multiple artists (stored as list)
   - CSV import handles comma-separated artists
   - get_main_artist() method for display/sorting

2. **Timestamp Tracking**
   - Playlist creation timestamps
   - Track addition timestamps (per playlist)
   - ISO format storage for cross-platform compatibility

3. **State Persistence**
   - Queue state saved automatically
   - Library saved on modifications
   - Playlists saved on modifications

4. **Error Handling**
   - Try-catch blocks throughout
   - Graceful degradation on file errors
   - User-friendly error messages

---

## File Structure

```
ListenToTheMusic/
├── Main.py                      # Main application entry point
├── Track.py                     # Track class definition
├── Library.py                   # Library with BST implementation
├── Playlist.py                  # Playlist and PlaylistManager classes
├── Queue.py                     # MusicQueue with doubly linked list
├── Album.py                     # Album and AlbumManager classes
├── populate_system.py           # Sample data population script
├── README.md                    # This file
├── .gitignore                   # Git ignore rules
│
├── data/                        # Runtime data (excluded from git)
│   ├── library.json            # Persisted library data
│   ├── playlists.json          # Persisted playlists
│   ├── albums.json             # Persisted albums
│   └── queue_state.json        # Persisted queue state
│
└── import/                      # Import files directory
    ├── tracks/                  # Track import files
    │   ├── tracks1.json        # Eminem tracks
    │   ├── tracks1.csv
    │   ├── tracks2.json        # Michael Jackson tracks
    │   ├── tracks2.csv
    │   ├── tracks3.json        # Nirvana tracks
    │   ├── tracks3.csv
    │   ├── tracks4.json        # Led Zeppelin tracks
    │   ├── tracks4.csv
    │   ├── tracks5.json        # Guns N' Roses tracks
    │   └── tracks5.csv
    │
    └── playlists/               # Playlist import files
        ├── playlist1.json      # Eminem Classics
        ├── playlist1.csv
        ├── playlist2.json      # MJ Hits
        ├── playlist2.csv
        ├── playlist3.json      # Rock Legends
        └── playlist3.csv
```

**Excluded from Git (via .gitignore):**
- `data/` - Runtime generated data
- `*.pyc` - Python compiled files
- `__pycache__/` - Python cache directory
- `ListenToTheMusic Project Requirements/` - Project requirement documents

---

## Files and Their Purposes

### Core System Files

**Main.py**
- Application entry point and main menu
- Handles user input and navigation
- Coordinates interaction between all components
- Implements UI menus and pagination logic

**Track.py**
- Track class definition
- Data encapsulation for track metadata
- Methods: getters, setters, to_dict(), from_dict(), display()
- Supports single or multiple artists
- Duration parsing and conversion

**Library.py**
- Binary Search Tree implementation for track storage
- Automatic sorting and duplicate detection
- Search functionality by title
- Import functionality (JSON/CSV)
- Integration with AlbumManager

**Playlist.py**
- Playlist class using singly linked list
- PlaylistManager class using hash map
- Track addition with duplicate prevention
- Sorting functionality (date, title, artist, duration)
- Timestamp tracking (created_at, added_at)
- Import functionality (JSON/CSV)

**Queue.py**
- MusicQueue class using doubly linked list
- O(1) next/previous navigation
- Shuffle/unshuffle with order preservation
- Repeat mode toggle
- Play/pause state management
- State persistence to JSON

**Album.py**
- Album class for grouping tracks
- AlbumManager class for album collection
- Automatic album creation from tracks
- get_or_create_album() pattern
- Display with track count and duration

### Data Files (Generated at Runtime)

**data/library.json**
- Persisted track library in JSON format
- BST structure flattened to sorted array
- Auto-generated on first track addition

**data/playlists.json**
- Persisted playlists with timestamps
- Includes created_at and added_at timestamps
- Track data embedded in each playlist

**data/albums.json**
- Automatically generated album collection
- Updated when tracks are added to library

**data/queue_state.json**
- Current queue state persistence
- Includes current track position
- Shuffle state and original order
- Play/pause and repeat states

### Import Files

**import/tracks/tracks[1-5].json**
- Sample track import files in JSON format
- Each file contains 5-6 tracks from specific artists
- Demonstrates JSON import structure

**import/tracks/tracks[1-5].csv**
- Sample track import files in CSV format
- Same content as JSON files
- Demonstrates CSV import with headers

**import/playlists/playlist[1-3].json**
- Sample playlist import files in JSON format
- Each contains a themed playlist with 3 tracks
- Demonstrates playlist import structure

**import/playlists/playlist[1-3].csv**
- Sample playlist import files in CSV format
- Same content as JSON files
- Demonstrates playlist name grouping in CSV

---

## How to Launch the System

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses standard library only)

### Steps to Launch

1. **Open Terminal/Command Prompt**
   ```bash
   cd path/to/ListenToTheMusic
   ```

2. **Run the Main Application**
   ```bash
   python Main.py
   ```

3. **System Startup**
   - The system will load existing data from `data/` directory
   - If no data exists, it starts with empty collections
   - Main menu will be displayed

### First Time Setup (Optional)
If starting fresh, you can either:
- Manually add tracks through the UI
- Import tracks from the sample files

---

## How to Populate the System

### Import Functionality

**Import Tracks:**
1. Launch Main.py
2. Select [1] Music Library
3. Select [5] Import Tracks
4. Enter filename: `tracks1.json` (or any tracks1-5.json/csv)
5. Tracks are imported and albums auto-created

**Import Playlists:**
1. Launch Main.py
2. Select [2] Playlists
3. Select [5] Import Playlists
4. Enter filename: `playlist1.json` (or any playlist1-3.json/csv)
5. Playlists are imported with tracks

**Available Sample Files:**
- Tracks: tracks1.json through tracks5.json (also .csv versions)
- Playlists: playlist1.json through playlist3.json (also .csv versions)

### Method 3: Manual Entry

1. Launch Main.py
2. Select [1] Music Library
3. Select [1] Add Track
4. Enter track details:
   - Title
   - Artist (comma-separated for multiple artists)
   - Album
   - Duration (mm:ss format)
5. Repeat for each track
6. Create playlists via [2] Playlists menu

---

## System Navigation Guide

### Main Menu
```
========================================
    LISTEN TO THE MUSIC
========================================
[1] Music Library
[2] Playlists
[3] Music Queue
[4] Exit
========================================
```

### Music Library Menu
```
--- MUSIC LIBRARY ---
[1] Add Track              - Manually add a new track
[2] View Library           - Browse all tracks (paginated)
[3] Search Track           - Search tracks by title
[4] View Albums            - Browse all albums
[5] Import Tracks          - Import from JSON/CSV files
[6] Back                   - Return to main menu
```

**View Library Navigation:**
- `[n]` Next page
- `[p]` Previous page
- `[a]` Add track to queue
- `[b]` Back to library menu

**View Albums Navigation:**
- `[n]` Next page
- `[p]` Previous page
- `[v]` View album details
- `[q]` Create queue from album
- `[b]` Back to library menu

### Playlists Menu
```
--- PLAYLISTS ---
[1] Create Playlist        - Create a new empty playlist
[2] View Playlists         - Browse all playlists
[3] Add Track to Playlist  - Add tracks from library
[4] Create Queue from Playlist - Load playlist into queue
[5] Import Playlists       - Import from JSON/CSV files
[6] Back                   - Return to main menu
```

**View Playlists Navigation:**
- `[n]` Next page
- `[p]` Previous page
- `[v]` View playlist details
- `[q]` Create queue from playlist
- `[s]` Sort playlists (by date, name, or duration)
- `[b]` Back to playlists menu

**View Playlist Details:**
- Playlist displays with all tracks
- Options: `[s] Sort | [q] Queue | [b] Back`
- Sort options: date added, title, artist, duration
- Queue option: Load tracks into queue in current order

### Music Queue Menu
```
--- MUSIC QUEUE ---
[1] Play/Pause            - Toggle playback state
[2] Next                  - Move to next track
[3] Previous              - Move to previous track
[4] Turn on/off repeat    - Toggle repeat mode
[5] Turn on/off shuffle   - Toggle shuffle mode
[6] Clear queue           - Remove all tracks
[7] Exit queue            - Return to main menu
```

**Queue Display:**
- Shows current track with "Playing" or "Paused" status
- Arrow (->) indicates current track in list
- Displays: total duration, shuffle state, repeat state
- Pagination for large queues

**Queue State:**
- Automatically saved on changes
- Restored when returning to queue
- Persists across application restarts

### Navigation Tips

1. **Pagination Controls:**
   - Most lists show 10 items per page
   - Use `[n]` and `[p]` to navigate pages
   - Current page shown as "<Page X of Y>"

2. **Action Shortcuts:**
   - Single letter commands for quick navigation
   - Commands are case-insensitive (n or N both work)
   - Format: `[letter] Action | [letter] Action`

3. **Back Navigation:**
   - `[b]` always returns to previous menu
   - Can navigate back through multiple levels
   - `[4]` or `Exit` in main menu closes application

4. **Empty States:**
   - Action options hidden when no items exist
   - Clear messages displayed (e.g., "Library is empty!")
   - Prompts guide user to add content

5. **Queue Creation:**
   - From Playlist: replaces entire queue
   - From Album: replaces entire queue
   - From Library (individual): appends to existing queue
   - Matches standard music player behavior (Spotify-like)

6. **Sorting:**
   - Sorting is temporary (view-only)
   - Original order preserved in files
   - Can re-sort or restore original at any time
   - Queue creation uses currently displayed order

### Common Workflows

**Create and Play a Playlist:**
1. Main Menu -> [2] Playlists
2. [1] Create Playlist -> Enter name
3. [3] Add Track to Playlist -> Select playlist
4. Browse library and add tracks with `[x]`
5. [2] View Playlists -> Select playlist with `[v]`
6. Press `[q]` to queue -> Returns to main menu
7. [3] Music Queue -> [1] Play

**Import and Browse Music:**
1. Main Menu -> [1] Music Library
2. [5] Import Tracks -> Enter "tracks1.json"
3. [2] View Library -> Browse imported tracks
4. [4] View Albums -> See auto-created albums

**Build Custom Queue:**
1. Main Menu -> [1] Music Library
2. [2] View Library
3. Select tracks with `[a]` to add to queue
4. Navigate pages with `[n]`/`[p]`, add more tracks
5. [b] Back -> [b] Back to main menu
6. [3] Music Queue -> View and play

**Sort and Organize:**
1. Main Menu -> [2] Playlists
2. [2] View Playlists
3. Press `[s]` to sort by name, date, or duration
4. Press `[v]` to view a playlist
5. Press `[s]` to sort tracks within playlist
6. Choose sort criteria (title, artist, duration, date)
7. Press `[q]` to queue in sorted order

---

## Technical Notes

### Data Persistence
- All data automatically saved on modifications
- JSON format for human-readable storage
- ISO 8601 timestamps for cross-platform compatibility
- Graceful handling of missing or corrupt files

### Performance Characteristics
- Library operations: O(log n) average (BST)
- Queue navigation: O(1) (doubly linked list)
- Playlist/Album lookup: O(1) (hash map)
- Duplicate checking: O(1) (hash set)
- Sorting: O(n log n) (Python's Timsort)

### Error Handling
- File I/O errors caught and reported
- Invalid input handled gracefully
- Duplicate detection prevents data corruption
- User-friendly error messages throughout

### Code Style
- PEP 8 compliant (Python style guide)
- Private attributes with double underscore
- Clear method and variable naming
- Comprehensive comments in code
- Modular design with separation of concerns

---

## Project Statistics

- **Total Lines of Code:** ~2500+
- **Classes Implemented:** 10
- **Data Structures Used:** 5
- **Bonus Points Achieved:** 46/46 (100%)
- **Features Implemented:** 50+
- **Import Samples Included:** 16 files

## Credits

**Developed for:**
- ITCC47 Data Structures and Algorithms
- ITCC45 Object-Oriented Programming

**Implementation Date:** November 2025

**Key Technologies:**
- Python 3.x
- Standard Library Only (json, os, csv, datetime, random)
