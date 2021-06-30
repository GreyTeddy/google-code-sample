"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags

    def to_string(self):
        string_video_id = "("+ self._video_id + ")"

        tags_string = "["
        num_tags = len(self._tags)
        if num_tags > 0:
            for tag_index in range(num_tags-1):
                tags_string += self._tags[tag_index] + " "
            tags_string += self._tags[-1]
        tags_string += "]"

        return self._title+" "+string_video_id+" "+tags_string