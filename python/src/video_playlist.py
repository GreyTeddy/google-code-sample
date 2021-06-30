"""A video playlist class."""


from collections import OrderedDict


class Playlist:
    """A class used to represent a Playlist."""

    """
        Args:
            name: The playlist's name.
    """
    def __init__(self,playlist_name):
        self._playlist_name = playlist_name
        # ordered dict 
        # so the video id can be retrieved in O(1)
        # with the video id being the key and the value
        self._video_ids = OrderedDict()


    @property
    def playlist_name(self) -> str:
        """Returns the title of a video."""
        return self._playlist_name

    @property
    def video_ids(self) -> str:
        """Returns the video id of a video."""
        return self._video_ids

    def add_video_id(self,video_id):
        self._video_ids[video_id] = video_id
