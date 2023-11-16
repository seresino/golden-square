import pytest
from lib.challenge_6 import *

"""
Class initializes new Music object
"""
def test_initialization():
    music_tracker = Music()
    assert isinstance(music_tracker, Music)

"""
Object stores dictionary of music tracks
"""
def test_object_stores_music_tracks():
    music_tracker = Music()
    assert music_tracker.tracks == {}

"""
Given track name and artist name
add_track saves the track to object
"""
def test_add_track_saves_track_with_full_input():
    music_tracker = Music()
    music_tracker.add_track("Is it over now", "Taylor Swift")
    assert music_tracker.tracks == {"Is it over now": "Taylor Swift"}

"""
Given artist name but no track name
add_track returns error "Track name empty."
"""
def test_add_track_without_track_name():
    music_tracker = Music()
    with pytest.raises(Exception) as e:
        music_tracker.add_track("", "Taylor Swift")
    error = str(e.value)
    assert error == "Track name empty."

"""
Given track name but no artist name
add_track returns error "Arist name empty."
"""
def test_add_track_without_artist_name():
    music_tracker = Music()
    with pytest.raises(Exception) as e:
        music_tracker.add_track("Is it over now", "")
    error = str(e.value)
    assert error == "Artist name empty."

"""
Given self.tracks is empty,
get_tracks returns error "No music listened to."
"""
def test_get_track_when_tracks_empty():
    music_tracker = Music()
    with pytest.raises(Exception) as e:
        music_tracker.get_tracks()
    error = str(e.value)
    assert error == "No tracks listened to."

"""
Given user has added three tracks,
get_track returns list of three tracks,
formatted as such:

"Track Title 1" by Arist A
"Track Title 2" by Artist B
"Track Title 3" by Artist C

etc.
"""
def test_get_tracks_when_tracks_added():
    music_tracker = Music()
    music_tracker.add_track("Track Title 1", "Artist A")
    music_tracker.add_track("Track Title 2", "Artist B")
    music_tracker.add_track("Track Title 3", "Artist C")
    assert music_tracker.get_tracks() == ''''Track Title 1' by Artist A
'Track Title 2' by Artist B
'Track Title 3' by Artist C'''
