"""A video player class."""

from collections import OrderedDict
from .video_playlist import Playlist
from .video_library import VideoLibrary

# import outside of class so it is not imported per instance
# (unless there is caching, I don't know)
from random import randint

class VideoPlayer:
    """A class used to represent a Video Player."""
    def __init__(self):
        self._video_library = VideoLibrary()
        self._video_playing = None
        # this could be indicated with numbers 0,1,2
        # but for readability strings are used: 
        # -> "Stopped", "Paused", "Playing"
        self._video_status = "Stopped"

        # the playlists are stored in an ordered dictionary
        # so they can be accessed in O(1)
        # and the keys will be uppercased!
        self._playlists = OrderedDict()

    def get_number_of_videos(self):
        """
        Returns
            number of videos: int
        """
        num_videos = len(self._video_library.get_all_videos())
        return num_videos

    def number_of_videos(self):
        num_videos = self.get_number_of_videos()
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        ## """Returns all videos."""
        """Shows all videos."""
        videos = self._video_library.get_all_videos()
        # https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index
        videos.sort(key= lambda tup: tup.title)
        print("Here's a list of all available videos:")
        for video_index in range(self.get_number_of_videos()):
            video_title = videos[video_index].title
            video_id = "("+ videos[video_index].video_id + ")"

            tags = videos[video_index].tags
            # print(tags)
            tags_string = "["
            num_tags = len(tags)
            if num_tags > 0:
                for tag_index in range(num_tags-1):
                    tags_string += tags[tag_index] + " "
                tags_string += tags[-1]
            tags_string += "]"

            print(video_title,video_id,tags_string)
        # exit()
        # print("show_all_videos needs implementation")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        # get the video to be played
        video_to_play = self._video_library.get_video(video_id)
        # if the video exists
        if (video_to_play):
            # to stop playing current video
            if (self._video_playing):
                print(f"Stopping video: {self._video_playing.title}")
            # set the video to be "played"
            self._video_playing = video_to_play
            self._video_status = "Playing"
            print(f"Playing video: {self._video_library.get_video(video_id).title}")
        else:
            print("Cannot play video: Video does not exist")


    def stop_video(self):
        """Stops the current video."""

        if (self._video_playing):
            print(f"Stopping video: {self._video_playing.title}")
            self._video_playing = None
            self._video_status = "Stopped"
        else:
            print(f"Cannot stop video: No video is currently playing")


    def play_random_video(self):
        """Plays a random video from the video library."""

        # some of the code can use already existing methods
        # but as the code is little and it saves a bit of time
        # some code will be somewhat reused
        
        # stop video if currently playing
        if (self._video_playing):
            print(f"Stopping video: {self._video_playing.title}")
            self._video_playing = None

        # get a number between 0 and the number of videos
        #    number_of_videos - 1: counting starts from zero and randint is both inclusive
        random_index = randint(0,self.get_number_of_videos()-1)

        # get the video id for a random video
        random_video_id = self._video_library.get_all_videos()[random_index].video_id
        self.play_video(random_video_id)

    def pause_video(self):
        """Pauses the current video."""
        
        if self._video_status == "Paused":
            print(f"Video already paused: {self._video_playing.title}")
        elif self._video_status == "Playing":
            print(f"Pausing video: {self._video_playing.title}")
            self._video_status = "Paused"
        else:
            print(f"Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""

        if self._video_status == "Playing":
            print("Cannot continue video: Video is not paused")
        elif not self._video_playing:
            print("Cannot continue video: No video is currently playing")
        else:
            print(f"Continuing video: {self._video_playing.title}")

    def show_playing(self):
        """Displays video currently playing."""
        if (self._video_playing):
            # create a tags string in the correct format
            tags = self._video_playing.tags
            tags_string = "["
            num_tags = len(tags)
            if num_tags > 0:
                for tag_index in range(num_tags-1):
                    tags_string += tags[tag_index] + " "
                tags_string += tags[-1]
            tags_string += "]"

            print(f"Currently playing: {self._video_playing.title} ({self._video_playing.video_id}) {tags_string}",end="")
            if self._video_status == "Paused":
                print(" - PAUSED",end="")
            print()
        else:
            print("No video is currently playing")
        
    def check_playlist_exists(self, playlist_name):
        """Checks if a playlist exists
        by comparing the "playlist_name" with the playlists stored
        regardless of casing
        """

        # this check is done in O(n) time
        # unless I use hashing/dictionary it will probably stay like that
        if playlist_name.upper() in self._playlists:
            return True
        return False


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if self.check_playlist_exists(playlist_name):
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            # add new instance of PlayList with key being in uppercase
            self._playlists[playlist_name.upper()] = Playlist(playlist_name)
            print(f"Successfully created new playlist: {playlist_name}")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """

        if not self.check_playlist_exists(playlist_name):
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
            return
        elif not self._video_library.get_video(video_id):
            print(f"Cannot add video to {playlist_name}: Video does not exist")
            return
        elif video_id in self._playlists[playlist_name.upper()]._video_ids:
            print(f"Cannot add video to {playlist_name}: Video already added")
            return
        else:
            self._playlists[playlist_name.upper()].add_video_id(video_id)
            print(f"Added video to {playlist_name}: {self._video_library.get_video(video_id).title}")

    def show_all_playlists(self):
        """Display all playlists."""

        if self._playlists:
            playlist_names = []
            print("Showing all playlists:")
            for key in self._playlists:
                playlist_names.append(self._playlists[key].playlist_name)
            for playlist_name in sorted(playlist_names):
                print(playlist_name)
        else:
            print("No playlists exist yet")
        
        # print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        # if the playlist exists 
        if playlist_name.upper() in self._playlists:
            print(f"Showing playlist: {playlist_name}")
            # if there are no videos on the playlist
            if len(self._playlists[playlist_name.upper()].video_ids) < 1:
                print("No videos here yet")
            else:
                # get each video using the video id stored and use to_string() to format
                for video_id in self._playlists[playlist_name.upper()].video_ids:
                    print(self._video_library.get_video(video_id).to_string())
        else:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        # if the playlist exists
        if playlist_name.upper() in self._playlists:
            if video_id in self._playlists[playlist_name.upper()].video_ids:
                # call remove_video_id from playlist._video_id
                self._playlists[playlist_name.upper()].remove_video_by_id(video_id)
                print(f"Removed video from {playlist_name}: {self._video_library.get_video(video_id).to_string()}")
            else:
                # if the video is on the playlist
                if self._video_library.get_video(video_id):
                    print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
                else:
                    print(f"Cannot remove video from {playlist_name}: Video does not exist")
        else:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        # if the playlist exists
        if playlist_name.upper() in self._playlists:
            self._playlists[playlist_name.upper()].remove_all_videos()
            print(f"Successfully removed all videos from {playlist_name}")
        else:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        # if the playlist exists
        if playlist_name.upper() in self._playlists:
            del self._playlists[playlist_name.upper()]
            print(f"Deleted playlist: {playlist_name}")
        else:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")


    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
