1. Design the Problem

    As a user
    So that I can keep track of my music listening
    I want to add tracks I've listened to and see a list of them.

    Assumptions made:
    - user wants to see both track title and artist name
    
    Further possible functionality:
    - does user want to see when track was listened to?

2. Design the Class Interface

    class Music():
        def __init__(self):
            # Parameters:
            #   None other than self
            # Side effects:
            #   Initializes self.tracks to be a new empty dictionary 
            pass # No code here yet

        def add_track(self, track_name, artist_name)
            # Parameters:
            #   track_name: string representing name of track
            #   artist_name: string representing music artists's name
            # Returns:
            #   Nothing
            # Side-effects
            #    Throws an exception if either track_name or artist_name are an empty string
            #   Throws an exception if either track_name or artist_name are non-string inputs
            #    Saves the track to the self object
            pass # No code here yet

        def get_tracks(self):
            # Parameters:
            #   None other than self
            # Returns:
            #   A list of tracks user has listened to
            # Side-effects:
            #   Throws an exception if no tracks have been listened to
            pass # No code here yet

3. Create Examples as Tests

    """
    Class initializes new Music object
    """
    music_tracker = Music()
    
    """
    Object stores dictionary of music tracks
    """
    music_tracker = Music()
    music_tracker.tracks = {}

    """
    Given track name and artist name
    add_track saves the track to object
    """

    """
    Given artist name but no track name
    add_track returns error "Track name empty."
    """

    """
    Given track name but no artist name
    add_track returns error "Arist name empty."
    """

    """
    Given user has added three tracks,
    get_track returns list of three tracks,
    formatted as such:

    "Track Title 1" by "Arist A"
    "Track Title 2" by "Artist B"
    "Track Title 3" by "Artist C"

    etc.
    """

    """
    Given self.tracks is empty,
    get_track returns error "No music listened to."
    """




4. Implement the Behaviour