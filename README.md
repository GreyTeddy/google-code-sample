# Youtube Player - Google Coding Challenge - Internship Experience Uk

### Coding challenge to code a CLI version of YouTube

- should edit `video_player.py` (mostly)
  - ended up changing `video_playlist`, `video` and `commande_parser`.py
- files use underscode `_` naming scheme

#### Some Extra
- implemented some `.bat` files to more easily run python commands
- implemented the want more functionalities in a different folder `more`

### Implemented/Augmented Classes
#### `Playlist` class
  - Attributes
    - `playlist_name`: `string`
    - `video_ids`: `OrderedList<None>`
  - Methods
    - `add_video_id`
      - Adds video with video id to the playlist
      - Args:
        - `video_id`: `string`
    - `remove_all_videos`
      - Removes all videos from the playlist

#### `Video` class
  - Attributes
    - `title`: `string`
    - `_video_id`: `String`
    - `tags`: `tuple<Sequence[string]>`
    - `flagged`: `bool`
    - `reason_flagged`: `String`
  - Methods
    - `to_string()`
      - Returns to string
        - `title`
        - `id`
        - `tags`
        - "Want More" extra
          - Average Rating
    - "Want More" extra
      - `add_rating`
        - Add a rating to the video
          - Args:
          - `video_id`: `string`
      - `get_average_rating`
        - Get the average value of the ratings

### Part 1
- [x] `NUMBER_OF_VIDEOS`
  - already implemented
- [x] `SHOW_ALL_VIDEOS`
  - To show all the videos
  ##### Notes at implementing the functionality
  - implemented ```get_number_of_videos()``` that returns the number of videos
    - edited ```number_of_videos()``` so it uses ```get_number_of_videos()```
  - used ```sorted()``` with ```key = lambda ... ``` to sort the videos in terms of title in lexicographical order (as [sort()](https://docs.python.org/3/howto/sorting.html#:~:text=This%20idiom%20works%20because%20tuples%20are%20compared%20lexicographically%3B%20the%20first%20items%20are%20compared%3B%20if%20they%20are%20the%20same%20then%20the%20second%20items%20are%20compared%2C%20and%20so%20on)) does
- [x] `PLAY <video_id>`
  - Play the specified video
    - If the same video is already playing, then stop and play again.
    - If video does not exist, show that it cannot be played.
  ##### Notes at implementing the functionalityt play video: Video does not exist
  - added `_video_playing` attribute to the `video_player` class
  - used `get_video(video_id)` method from `video` class
- [x] `STOP`
  - Stop the current video playing
- [x] `PLAY_RANDOM`
  - Play a random video
    - If a video is already playing, stop the video
  ##### Notes at implementing the functionality
    - imported `random.sample()` 
      - outside of class: so it does not have to be imported for every instance (unless python caches it)
      - `sample()` is [both inclusive](https://docs.python.org/3/library/random.html#:~:text=Return%20a%20random%20integer%20N%20such%20that%20a%20%3C%3D%20N%20%3C%3D%20b.%20Alias%20for%20randrange(a%2C%20b%2B1)) so the arguments are `0` and `number_of_videos - 1`
      - `sample()` is used so if a video is unavailable, another video is chosen
        - similar to shuffling a playlist
- [x] `PAUSE`
  - Pause the current plaing video
    - If already paused, show a warning message
    - If no video, show a warning message
  - If new video is played with one already paused
    - New video should play and ignore paused status
    - New video can be paused
  ##### Notes at implementing the functionality
  - added `_video_status` to the class
    - with `"Stopped"`, `"Paused"` and `"Playing"` as possible values
      - could use integers `0`,`1` and `2` but for readability strings were used instead
- [x] `CONTINUE`
  - Continue a currently paused video
    - If not paused, display warning
    - If no video playing, display warning
- [x] `SHOW_PLAYING`
  - Display the title, video id, video tags and paused status of the video currently playing
    - If no video playing, display a message

### Part 2

This part is for creating playlist functionality. In this part the class `Playlist` is developed and used. 
  
For my implementation, I will be storing instances of `Playlist` in a `VideoPlayer` attribute [OrderedDict](https://docs.python.org/3/library/collections.html#collections.OrderedDict) called `playlists`. I will be using that type so that so 
- Hashing can be used to get/access and delete playlists in $O(1)$ 
- Keep the order the playlists were added.
    - An element of type `dict` can be used to keep the order [as of version 3.7](https://docs.python.org/3/library/stdtypes.html#:~:text=Changed%20in%20version%203.7%3A%20Dictionary%20order%20is%20guaranteed%20to%20be%20insertion%20order.%20This%20behavior%20was%20an%20implementation%20detail%20of%20CPython%20from%203.6.), however I wanted to make sure that the order is kept for lower version of python as well.

- [x] `CREATE_PLAYLIST <playlist_name>`
  - Create a new (empty) playlist
    - Unique Name
    - No Whitespace
    - Not Case Sensitive
  ```
  YT> CREATE_PLAYLIST my_PLAYlist
  Successfully created new playlist: my_PLAYlist

  YT> CREATE_PLAYLIST my_PLAYLIST
  Cannot create playlist: A playlist with the same name already exists
  ```

- [x] `ADD_TO_PLAYLIST <playlist_name> <video_id>`
  - Add the specified video the a playlist.
    - If playlist or video does not exist, show warning
    - If both don't exist, show playlist warning first
    - No duplicate videos
    - Respond to user with playlist name they have typed
  ```
  YT> CREATE_PLAYLIST my_playLIST
  Successfully created new playlist: my_playLIST

  YT> ADD_TO_PLAYLIST my_playlist amazing_cats_video_id
  Added video to my_playlist: Amazing Cats

  YT> ADD_TO_PLAYLIST my_PLAYlist amazing_cats_video_id
  Cannot add video to my_PLAYlist: Video already added

  YT> ADD_TO_PLAYLIST my_playlist some_other_video_id
  Cannot add video to my_playlist: Video does not exist
  
  YT> ADD_TO_PLAYLIST another_playlist some_other_video_id
  Cannot add video to another_playlist: Playlist does not exist
  ``` 

- [x] `SHOW_ALL_PLAYLISTS`
  - Show all available playlists (name only)
    - If no playlists, display “No playlists exist yet”
    - Playlists should be shown in lexicographical order, ignoring casing
  ```
  YT> SHOW_ALL_PLAYLISTS
  No playlists exist yet
  
  YT> CREATE_PLAYLIST MY_playlist
  Successfully created new playlist: MY_playlist
  
  YT> SHOW_ALL_PLAYLISTS
  Showing all playlists:
  MY_playlist
  ```

- [x] `SHOW_PLAYLIST <playlist_name>`
  - Show all videos in a playlist
    - In the format: “title (video_id) [tags]”
    - If it doesn'st exists, display warning message
    - If it's empty, display “No videos here yet"
    - List videos in the same order they were added
    - Display name in the same case as user inputted it
  ```
  YT> CREATE_PLAYLIST my_playlist
  Successfully created new playlist: my_playlist

  YT> SHOW_PLAYLIST my_PLAYLIST
  Showing playlist: my_PLAYLIST
  No videos here yet
  
  YT> ADD_TO_PLAYLIST my_playlist amazing_cats_video_id
  Added video to my_playlist: Amazing Cats
  
  YT> SHOW_PLAYLIST my_playlist
  Showing playlist: my_playlist
  Amazing Cats (amazing_cats_video_id) [#cat #animal]
  
  YT> SHOW_PLAYLIST another_playlist
  Cannot show playlist another_playlist: Playlist does not exist
  ```

  - Added method `to_string` to `Video` class
    - Uses string format used in `show_all_videos`

- [x] `REMOVE_FROM_PLAYLIST <playlist_name> <video_id>`
  - Remove the specified vdieo from the specified playlist
    - If either does not exist, display relevant warning
    - Keep the case of the playlist name
  ```
  YT> CREATE_PLAYLIST my_playlist
  Successfully created new playlist: my_playlist

  YT> ADD_TO_PLAYLIST my_PLAYlist amazing_cats_video_id
  Added video to my_PLAYlist: Amazing Cats

  YT> REMOVE_FROM_PLAYLIST my_playLIST amazing_cats_video_id
  Removed video from my_playLIST: Amazing Cats

  YT> REMOVE_FROM_PLAYLIST my_playlist amazing_cats_video_id
  Cannot remove video from my_playlist: Video is not in playlist

  YT> REMOVE_FROM_PLAYLIST my_playlist some_other_video_id
  Cannot remove video from my_playlist: Video does not exist

  YT> REMOVE_FROM_PLAYLIST another_playlist amazing_cats_video_id
  Cannot remove video from another_playlist: Playlist does not exist

  YT> REMOVE_FROM_PLAYLIST another_playlist some_other_video_id
  Cannot remove video from another_playlist: Playlist does not exist
  ```

  - Added method `remove_video_by_id` to `Playlist` class
    - Just deletes the `video_id` key element from `._video_ids`

- [x] `CLEAR_PLAYLIST <playlist_name>`
  - Remove all the videos from the playlist
    - Don't delete the playlist
    - If playlist doesn't exist, display warning
  ```
  YT> CREATE_PLAYLIST my_playlist
  Successfully created new playlist: my_playlist
  
  YT> ADD_TO_PLAYLIST my_playlist amazing_cats_video_id
  Added video to my_playlist: Amazing Cats
  
  YT> CLEAR_PLAYLIST my_playlist
  Successfully removed all videos from my_playlist
  
  YT> SHOW_PLAYLIST my_playlist
  Showing playlist: my_playlist
  No videos here yet.
  
  YT> CLEAR_PLAYLIST another_playlist
  Cannot clear playlist another_playlist: Playlist does not exist
  ```
  - Added method `remove_all_videos` to `Playlist` class
    - Assigns new `OrderedDict` to `._video_ids`

- [x] `DELETE_PLAYLIST <playlist_name>`
  - Delete the specified playlist
    - If playlist doesn't exist, display warning
  ```
  YT> CREATE_PLAYLIST my_playlist
  Successfully created new playlist: my_playlist

  YT> DELETE_PLAYLIST my_playlist
  Deleted playlist: my_playlist
  
  YT> DELETE_PLAYLIST my_playlist
  Cannot delete playlist my_playlist: Playlist does not exist
  ```


### Part 3

#### Searching Videos.

- [x] `SEARCH_VIDEOS <search_term>`
  - Display all videos in the library whose title contain the specified search term
    - Not case sensitive
    - No whitespace or special characters
    - Lexicographical order (by title)
  - Ask the user to play one of the videos
    - Read the answer in standard input
    - If valid number, play video
    - If not, do nothing
  ```
  YT> SEARCH_VIDEOS cat
    Here are the results for cat:
    1) Amazing Cats (amazing_cats_video_id) [#cat #animal]
    2) Another Cat Video (another_cat_video_id) [#cat #animal]
    Would you like to play any of the above? If yes, specify the number of the video.
    If your answer is not a valid number, we will assume it's a no.
    Nope!

  YT> SEARCH_VIDEOS cat
    Here are the results for cat:
    1) Amazing Cats (amazing_cats_video_id) [#cat #animal]
    2) Another Cat Video (another_cat_video_id) [#cat #animal]
    Would you like to play any of the above? If yes, specify the number of the video.
    If your answer is not a valid number, we will assume it's a no.
    2
    Playing video: Another Cat Video

  YT> SEARCH_VIDEOS blah
    No search results for blah
  ```

  As we are looking for videos that include the words specifically (not case sensitive), we shouldn't use tricks utilising distance measurement or machine learning models, as their purpose is for find text that might be similar but not the same as the input. 
  
  So, python functions and/or regular expressions can be used. For this implementation the python keyword `in` will be used, where similarly to handling non-case sensitive terms in other functions, `upper()` will be used to "normalise" the comparisons.

- [x] `SEARCH_VIDEOS_WITH_TAG <tag_name>`
  - Show all videos whose list of tags contains the specified hashtag
    - Not case sensitive
    - In lexicographical order by titel
    - No results shown, if user forgets hashtag
  - Ask the user to play one of the videos
    - Read the answer in standard input
    - If valid number, play video
    - If not, do nothing 

  ```
  YT> SEARCH_VIDEOS_WITH_TAG #cat
  Here are the results for #cat:
  1) Amazing Cats (amazing_cats_video_id) [#cat #animal]
  2) Another Cat Video (another_cat_video_id) [#cat #animal]
  Would you like to play any of the above? If yes, specify the number of the video.
  If your answer is not a valid number, we will assume it's a no.
  No
  
  YT> SEARCH_VIDEOS_WITH_TAG #cat
  Here are the results for #cat:
  1) Amazing Cats (amazing_cats_video_id) [#cat #animal]
  2) Another Cat Video (another_cat_video_id) [#cat #animal]
  Would you like to play any of the above? If yes, specify the number of the video.
  If your answer is not a valid number, we will assume it's a no.
  2
  Playing video: Another Cat Video
  
  YT> SEARCH_VIDEOS_WITH_TAG #blah
  No search results for #blah
  
  YT> SEARCH_VIDEOS_WITH_TAG cat
  No search results for cat
  ```

  This is very similar to the previous search method but now tupples have to be traversed as well. So the tags are stored temporarily in uppercase, to disregard case sensitivity, and traversed. 


### Part 4

- [x] `FLAG_VIDEO <video_id> <flag_reason>`
  Mark a video as flagged with a supplied reason

  - Reason is optional, default "Not Supplied"
    - A string with no whitespace
  - If already flagged, display warning message
  - Display warning message when:
    - user tries to play flagged video
    - user tires to add flagged video to playlist
      - show error even if video already exists in playlist
  - Don't randomly play flagged videos
  - When showing all videos or videos on playlist
    - Show flagged status
  - Don't show flagged videos in search results
  - Stop video when flagged video was already playing or paused

  Notes at implementing the functionality
  - additional functionality to `video` class
    - added `flagged` and `reason_flagged` attributes
      - `flagged`: `bool`
      - `reason_flagged`: `string`
    - added `flag` method

- [x] `ALLOW_VIDEO <video_id>`
  Allow a video by un-flagging it
  - If video does not exist, display a warning message
  - Will now be shown on
    - SHOW_ALL_VIDEOS
    - SHOW_PLAYLIST
    - SEARCH_VIDEOS
    - SEARCH_VIDEOS_WITH_TAG

  Notes at impleneting the functionality
  - additional functionality to `video` class
    - added `allow` method


### Want More?

#### Implemented the more changes to a a different directory, to not interfere with the tests provided.
##### To run the app with the implemented changes, run `./run_app_more.bat`

- [x] If a playlist doesn't exist yet
  - Ask user
    - Creat a playlist with the name given
      - Also add video if used from with command `ADD_VIDEO_TO_PLAYLIST`
- [x] Show number of videos on playlist
  - Implement fix where
    - "1 video" instead of "1 videos"
- [x] Command to play a whole playlist and command to advance to the next video
  -  PLAY_PLAYLIST <playlist_name>
  -  NEXT command
     -  Print warning
        -  if no playlist is playing
        -  if there is no other song in the queue 
  -  Should work with PLAY <id>, STOP, PAUSE, CONTINUE
  - SHOW_CURRENT_PLAYLIST
  - Edit `command_parser`
    - Parse the commands
    - Show the commands on help
- [x] Rating System
  - RATE_VIDEO <video_id> <rating>
  - rating can only be in a certain range (e.g. 1-5)
  Implemented:
    - Rate a video
    - Get Average rating
    - Show all videos by rating (descending)
- [ ] UNDO command
  - A stack could be used to enter all commands
    - But due to time constraints only one UNDO can be done
- [ ] Add real URL to video
- [x] How to optimise the search when there are multiple videos and tags
  Hashing is a way of optimising the search and in case of python dictionaries are the built in answer. In my implemenatations I have used an extension of dictionaries called `OrderedDict`, which are dictionaries which keep the order in which they add elements. Python have this feature since version 3.6, so `OrderedDict` are not needed for >=3.6
```

GreyTeddy - Dennis (Dionysios Ntouka)
Art by Joan G. Stark
          ___   .--.
    .--.-"   "-' .- |
   / .-,`          .'
   \   `           \
    '.            ! \
      |     !  .--.  |
      \        '--'  /.____
     /`-.     \__,'.'      `\
  __/   \`-.____.-' `\      /
  | `---`'-'._/-`     \----'    _ 
  |,-'`  /             |    _.-' `\
 .'     /              |--'`     / |
/      /\              `         | |
|   .\/  \      .--. __          \ |
 '-'      '._       /  `\         /
    jgs      `\    '     |------'`
               \  |      |
                \        /
                 '._  _.'

```