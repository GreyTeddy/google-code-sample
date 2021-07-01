"""A video player class."""

from collections import OrderedDict
from .video_playlist import Playlist
from .video_library import VideoLibrary

# import outside of class so it is not imported per instance
# (unless there is caching, I don't know)
from random import sample

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
        
        self._current_playlist = ""
        self._current_playlist_video_ids = []
        self._current_track_index = 0
        self._last_track_index = -1

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
        for video in videos:
            print(video.to_string())

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
            if video_to_play.flagged:
                print(f"Cannot play video: Video is currently flagged (reason: {video_to_play.reason_flagged})")
                return
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
            # empty the current playlist variables
            # so it stops playing the playlist
            if (self._current_playlist):
                print(f"Stoping playlist: {self._current_playlist}")
                self._current_playlist = ""
                self._current_playlist_video_ids = []
                self._current_track_index = 0
                self._last_track_index = -1
            self._video_playing = None
            self._video_status = "Stopped"
        else:
            print(f"Cannot stop video: No video is currently playing")


    def play_random_video(self):
        """Plays a random video from the video library."""
        
        # stop video if currently playing
        if (self._video_playing):
            print(f"Stopping video: {self._video_playing.title}")
            self._video_playing = None

        # create a random sample of unique numbers
        # which represent the indices on the video library
        # this can become slow/combersome if too many videos are stored
        random_video_index = sample(range(0,self.get_number_of_videos()),self.get_number_of_videos())

        for video_index in random_video_index:
            video_id = self._video_library.get_all_videos()[video_index].video_id
            if not self._video_library.get_video(video_id).flagged:
                self.play_video(video_id)
                return
        print("No videos available")

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

            print(f"Currently playing: {self._video_playing.to_string()}",end="")
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
            print("Would you like to create that playlist?")
            print("Enter Y to create the playlist")
            user_input = input()
            if user_input.upper() == "Y":
                self.create_playlist(playlist_name)
                if self._video_library.get_video(video_id):
                    print("Would you like to add the video to that playlist?")
                    print("Enter Y to add the video")
                    user_input = input()
                    if user_input.upper() == "Y":
                        self.add_to_playlist(playlist_name,video_id)
                else:
                    print("Cannot add video to the playlist: Video does not exist")
            return
        elif not self._video_library.get_video(video_id):
            print(f"Cannot add video to {playlist_name}: Video does not exist")
            return
        elif self._video_library.get_video(video_id).flagged:
            print(f"Cannot add video to {playlist_name}: Video is currently flagged (reason: {self._video_library.get_video(video_id).reason_flagged})")
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

            number_of_videos_in_playlist = len(self._playlists[playlist_name.upper()].video_ids)
            string_number_of_videos_in_playlist = str(number_of_videos_in_playlist)
            # fix linguistic mistake
            if number_of_videos_in_playlist == 1:
                string_number_of_videos_in_playlist+= " video"
            else:
                string_number_of_videos_in_playlist+= " videos"
            print(f"Showing playlist: {playlist_name} ({string_number_of_videos_in_playlist})")

            # if there are no videos on the playlist
            if len(self._playlists[playlist_name.upper()].video_ids) < 1:
                print("No videos here yet")
            else:
                # get each video using the video id stored and use to_string() to format
                for video_id in self._playlists[playlist_name.upper()].video_ids:
                    print(self._video_library.get_video(video_id).to_string())
        else:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
            print("Would you like to create that playlist?")
            print("Enter Y to create the playlist")
            user_input = input()
            if user_input.upper() == "Y":
                self.create_playlist(playlist_name)

    def play_playlist(self,playlist_name):
        """Play the playlist with the provided name"""
        if playlist_name.upper() not in self._playlists:
            print(f"Cannot play playlist {playlist_name}: Playlist does not exist")
            return
        self._current_playlist = self._playlists[playlist_name.upper()].playlist_name
        self._current_playlist_video_ids = list(self._playlists[playlist_name.upper()].video_ids)
        self._current_playlist_length = len(self._current_playlist_video_ids)
        if (self._current_playlist_length > 0):
            # while 
            #   the current track index is in range
            #   the video to be played is flagged
            #   try the next video
            while self._current_track_index < self._current_playlist_length and (self._video_library.get_video(self._current_playlist_video_ids[self._current_track_index]).flagged):
                self._current_track_index+=1
            
            if(self._current_track_index >= self._current_playlist_length):
                print(f"Cannot play playlist {playlist_name}: All videos are flagged")
            else:
                print(f"Playing playlist: {playlist_name}")
                self.play_video(self._current_playlist_video_ids[self._current_track_index])
        else:
            print(f"Cannot play playlist {playlist_name}: Playlist is empty")
    
    def next(self):
        """Play the next song in the playlist, if a playlist is playing."""

        self._current_track_index += 1
        while self._current_track_index < self._current_playlist_length and (self._video_library.get_video(self._current_playlist_video_ids[self._current_track_index]).flagged):
            self._current_track_index+=1
        
        if(self._current_track_index >= self._current_playlist_length):
            print(f"Nothing playing: End of playlist")
            self.play_video(self._current_playlist_video_ids[self._current_track_index])

    def show_current_playlist(self):
        """Show current playlist playing"""
        if self._current_playlist:
            print(f"Currently Playlist: {self._current_playlist}")
        else:
            print("No playlist playing currently.")
    

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
        # get all the videos and sort them by title
        all_videos = self._video_library.get_all_videos()
        # put all the found videos on a temporary list
        search_results = []
        for video in all_videos:
            if search_term.upper() in video.title.upper() and not video.flagged:
                search_results.append(video.video_id)
        
        # if the resulting list is empty
        # then no solutions
        if not len(search_results):
            print(f"No search results for {search_term}")
            return
        
        # sort the search results by title
        search_results.sort(key= lambda tup: self._video_library.get_video(tup).title)
        print(f"Here are the results for {search_term}:")
        for index, video_id in enumerate(search_results):
            print(str(index+1)+") "+ self._video_library.get_video(video_id).to_string())

        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")
        # try and get user integer
        try:
            user_input = int(input())
        # if not an integer, do nothing and return to main command menu
        except ValueError:
            return
        
        if user_input <= len(search_results) and user_input > 0:
            # user input is offset by 1 as counting starts from 0 on lists
            self.play_video(search_results[user_input-1])

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        all_videos = self._video_library.get_all_videos()
        # put all the found videos on a temporary list
        search_results = []
        for video in all_videos:
            if video.flagged:
                continue
            # temporarly store all the tags for a video in uppercase
            temp_tags = [tag.upper() for tag in video.tags]
            if video_tag.upper() in temp_tags:
                search_results.append(video.video_id)

        # if the resulting list is empty
        # then no solutions
        if not len(search_results):
            print(f"No search results for {video_tag}")
            return

        # sort the search results by title
        search_results.sort(key= lambda tup: self._video_library.get_video(tup).title)
        print(f"Here are the results for {video_tag}:")
        for index, video_id in enumerate(search_results):
            print(str(index+1)+") "+ self._video_library.get_video(video_id).to_string())
        
        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")
        # try and get user integer
        try:
            user_input = int(input())
        # if not an integer, do nothing and return to main command menu
        except ValueError:
            return
        
        if user_input <= len(search_results) and user_input > 0:
            # user input is offset by 1 as counting starts from 0 on lists
            self.play_video(search_results[user_input-1])


    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        
        if not self._video_library.get_video(video_id):
            print("Cannot flag video: Video does not exist")
            return
        elif self._video_library.get_video(video_id).flagged:
            print("Cannot flag video: Video is already flagged")
            return

        if flag_reason:
            self._video_library.get_video(video_id).flag(flag_reason)
            if self._video_status in ["Playing","Paused"] and self._video_playing.flagged:
                self.stop_video()
            print(f"Successfully flagged video: {self._video_library.get_video(video_id).title} (reason: {flag_reason})")
        else:
            self._video_library.get_video(video_id).flag()
            if self._video_status in ["Playing","Paused"] and self._video_playing.flagged:
                self.stop_video()
            print(f"Successfully flagged video: {self._video_library.get_video(video_id).title} (reason: Not supplied)")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        if not self._video_library.get_video(video_id):
            print("Cannot remove flag from video: Video does not exist")
        elif not self._video_library.get_video(video_id).flagged:
            print("Cannot remove flag from video: Video is not flagged")
        else:
            self._video_library.get_video(video_id).allow()
            print(f"Successfully removed flag from video: {self._video_library.get_video(video_id).title}")

    def get_average_rating(self,video_id):
        video = self._video_library.get_video(video_id)
        average_rating = video.get_average_rating()
        if average_rating != -1:
            print(f"Average rating for {video.title}: {average_rating}")
        else:
            print(f"Video has not been rated yet")
    
    def rate(self,video_id,rating):
        if rating in ["1","2","3","4","5"]:
            self._video_library.get_video(video_id).add_rating(int(rating))
        else:
            print("Cannot rate video: Rating not between 1 to 5")
    
    def show_all_videos_by_rating(self):
        videos = self._video_library.get_all_videos()
        videos.sort(key=lambda video: video.get_average_rating(),reverse=True)
        for video in videos:
            print(video.to_string())