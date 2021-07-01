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

        # if the video is flagged
        # with placeholder 
        self._flagged = False
        self._reason_flagged = "Not supplied"

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

        string_flagged = ""
        if self.flagged:
            string_flagged = f" - FLAGGED (reason: {self._reason_flagged})"
        string_average_rating = ""
        if len(self._ratings):
            string_average_rating+= f" Rating: {self.get_average_rating()}"
        return self._title+" "+string_video_id+" "+tags_string+string_average_rating+string_flagged

    @property
    def flagged(self) -> bool:
        """Returns "True" if video is flagged."""
        return self._flagged

    @property
    def reason_flagged(self) -> str:
        """Returns the reason why a video is flagged, if the video is flagged.
        If not, it returns "Not Flagged"
        """
        if self.flagged == True:
            return self._reason_flagged
        return "Not Flagged"

    def flag(self,reason=""):
        """Sets the video to flagged"

        Args: 
            reason: str
                Reason the video is flagged
                    If not provided, reason set to "Not supplied"
        """
        self._flagged = True
        if reason:
            self._reason_flagged = reason
        else:
            self._reason_flagged = "Not supplied"
    
    def allow(self,reason=""):
        """Sets the video to allowed"
        """
        self._flagged = False
        self._reason_flagged = ""

    @property
    def rating(self) -> int:
        """Returns the rating of the video.
        Returns -1 if there is no rating"""
        return self._ratings

    def add_rating(self,rating):
        """Add a rating to the video"""
        self._ratings.append(rating)
    
    def get_average_rating(self) -> int:
        """Get the average value of the ratings
        If no ratings: -1 """
        if len(self._ratings):
            return round(sum(self._ratings)/len(self._ratings),1)
        else:
            return -1

