# Import Tracks Directory

Place your JSON or CSV files here to import tracks into the music library.

## Supported Formats

### JSON Format
```json
[
    {
        "title": "Track Title",
        "artist": "Artist Name",
        "album": "Album Name",
        "duration": "mm:ss"
    },
    {
        "title": "Track with Multiple Artists",
        "artist": ["Artist 1", "Artist 2"],
        "album": "Album Name",
        "duration": "mm:ss"
    }
]
```

### CSV Format
```csv
title,artist,album,duration
Track Title,Artist Name,Album Name,mm:ss
Track with Multiple Artists,"Artist 1, Artist 2",Album Name,mm:ss
```

## Sample Files

- `sample_tracks.json` - 10 sample tracks in JSON format
- `sample_tracks.csv` - 10 sample tracks in CSV format

## Usage

1. Place your import file in this directory
2. Run Main.py
3. Go to Music Library → Import Tracks
4. Enter the filename (e.g., `sample_tracks.json`)
5. Tracks will be imported and albums will be automatically created!

## Notes

- All fields (title, artist, album, duration) are required
- Duration format must be "mm:ss" (e.g., "03:45")
- Invalid/incomplete tracks will be skipped
- Duplicate tracks (same title, artist, album, duration) will be skipped by the BST
