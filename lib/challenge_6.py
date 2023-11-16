class Music():
    def __init__(self): 
        self.tracks = {}
    
    def add_track(self, track_name, artist_name):
        if track_name == "":
            raise Exception("Track name empty.")
        elif artist_name == "":
            raise Exception("Artist name empty.")
        else:
            self.tracks[track_name] = artist_name
            return
        
    def get_tracks(self):
        if self.tracks == {}:
            raise Exception("No tracks listened to.")
        else:
            tracks_list = []
            for key in self.tracks:
                tracks_list.append(f"'{key}' by {self.tracks[key]}")
            track_string = '\n'.join(tracks_list)
            return track_string
            