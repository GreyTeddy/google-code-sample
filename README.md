# Google Coding Challenge - Youtube Player

### Coding challenge to code a CLI version of YouTube

- should edit video_player.py (mostly)
- files use underscode `_` naming scheme

#### Some Extra
- implemented some `.bat` files to more easily run python commands

### Part 1
- [x] NUMBER_OF_VIDEOS
  - already implemented
- [x] SHOW_ALL_VIDEOS
  - To show all the videos
  ```
  YT> SHOW_ALL_VIDEOS
    Here's a list of all available videos:
    Amazing cats (amazing_cats_video_id) [#cat #animal]
    Another Cat Video (another_cat_video_id) [#cat #animal]
    Funny Dogs (funny_dogs_video_id) [#dog #animal]
    Life at Google (life_at_google_video_id) [#google #career]
    Video about nothing (nothing_video_id) []
  ```
  - implemented ```get_number_of_videos()``` that returns the number of videos
    - edited ```number_of_videos()``` so it uses ```get_number_of_videos()```
  - used ```sorted()``` with ```key = lambda ... ``` to sort the videos in terms of title in lexicographical order (as [sort()](https://docs.python.org/3/howto/sorting.html#:~:text=This%20idiom%20works%20because%20tuples%20are%20compared%20lexicographically%3B%20the%20first%20items%20are%20compared%3B%20if%20they%20are%20the%20same%20then%20the%20second%20items%20are%20compared%2C%20and%20so%20on)) does
- [x] PLAY <video_id>
  - Play the specified video
    - If the same video is already playing, then stop and play again.
    - If video does not exist, show that it cannot be played.
  ```
  YT> PLAY amazing_cats_video_id
  Playing video: Amazing Cats

  YT> PLAY funny_dogs_video_id
  Stopping video: Amazing Cats
  Playing video: Funny Dogs

  YT> PLAY funny_dogs_video_id
  Stopping video: Funny Dogs
  Playing video: Funny Dogs

  YT> PLAY some_other_video_id
  Cannot play video: Video does not exist
  ```
  - added `_video_playing` attribute to the `video_player` class
  - used `get_video(video_id)` method from `video` class
- [x] STOP
  - Stop the current video playing
  ```
  YT> PLAY amazing_cats_video_id
  Playing video: Amazing Cats

  YT> STOP
  Stopping video: Amazing Cats

  YT> STOP
  Cannot stop video: No video is currently playing
  ```
- [x] PLAY_RANDOM
  - Play a random video
    - If a video is already playing, stop the video
  ```
  YT> PLAY_RANDOM
  Playing video: Life at Google

  YT> PLAY_RANDOM
  Stopping video: Life at Google
  Playing video: Funny Dogs
  ```
    - imported `random.randint()` 
      - outside of class: so it does not have to be imported for every instance (unless python caches it)
      - `randint()` is [both inclusive](https://docs.python.org/3/library/random.html#:~:text=Return%20a%20random%20integer%20N%20such%20that%20a%20%3C%3D%20N%20%3C%3D%20b.%20Alias%20for%20randrange(a%2C%20b%2B1)) so the arguments are `0` and `number_of_videos - 1`
- [x] PAUSE
  - Pause the current plaing video
    - If already paused, show a warning message
    - If no video, show a warning message
  ```
  YT> PLAY amazing_cats_video_id
  Playing video: Amazing Cats

  YT> PAUSE
  Pausing video: Amazing Cats

  YT> PAUSE
  Video already paused: Amazing Cats

  YT> STOP
  Stopping video: Amazing Cats

  YT> PAUSE
  Cannot pause video: No video is currently playing
  ```
  - If new video is played with one already paused
    - New video should play and ignore paused status
    - New video can be paused
  ```
  YT> PLAY amazing_cats_video_id
  Playing video: Amazing Cats

  YT> PAUSE
  Pausing video: Amazing Cats

  YT> PLAY another_cat_video_id
  Stopping video: Amazing Cats
  Playing video: Another Cat Video
  
  YT> PAUSE
  Pausing video: Another Cat Video
  ```
  - added `_video_status` to the class
    - with `"Stopped"`, `"Paused"` and `"Playing"` as possible values
      - could use integers `0`,`1` and `2` but for readability strings were used instead
- [x] CONTINUE
  - Continue a currently paused video
    - If not paused, display warning
    - If no video playing, display warning
  ```
  YT> PLAY amazing_cats_video_id
  Playing video: Amazing Cats

  YT> CONTINUE
  Cannot continue video: Video is not paused

  YT> PAUSE
  Pausing video: Amazing Cats
  
  YT> CONTINUE
  Continuing video: Amazing Cats
  
  YT> CONTINUE
  Cannot continue video: Video is not paused
  
  YT> STOP
  Stopping video: Amazing Cats
  
  YT> CONTINUE
  Cannot continue video: No video is currently playing
  ```
- [x] SHOW_PLAYING
  - Display the title, video id, video tags and paused status of the video currently playing
    - If no video playing, display a message
  ```
  YT> PLAY amazing_cats_video_id
  Playing video: Amazing Cats
  
  YT> SHOW_PLAYING
  Currently playing: Amazing Cats (amazing_cats_video_id) [#cat #animal]
  
  YT> PAUSE
  Pausing video: Amazing Cats
  
  YT> SHOW_PLAYING
  Currently playing: Amazing Cats (amazing_cats_video_id) [#cat #animal] - PAUSED
 
  YT> STOP
  Stopping video: Amazing Cats
  
  YT> SHOW_PLAYING
  No video is currently playing

  ```

### Part 2

This part is for creating playlist functionality. In this part the class `Playlist` is developed and used. 
  
For my implementation, I will be storing instances of `Playlist` in a `VideoPlayer` attribute [OrderedDict](https://docs.python.org/3/library/collections.html#collections.OrderedDict) called `playlists`. I will be using that type so that so 
- Hashing can be used to get/access and delete playlists in $O(1)$ 
- Keep the order the playlists were added.
    - An element of type `dict` can be used to keep the order [as of version 3.7](https://docs.python.org/3/library/stdtypes.html#:~:text=Changed%20in%20version%203.7%3A%20Dictionary%20order%20is%20guaranteed%20to%20be%20insertion%20order.%20This%20behavior%20was%20an%20implementation%20detail%20of%20CPython%20from%203.6.), however I wanted to make sure that the order is kept for lower version of python as well.

`Playlist` class
  - Attributes
    - `_playlist_name`: `string`
    - `_video_ids`: `OrderedList<None>`
  - Methods
    - add_video_id: None
      - Adds the video id to the playlist


- [x] CREATE_PLAYLIST <playlist_name>
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

- [x] ADD_TO_PLAYLIST <playlist_name> <video_id>
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

- [x] SHOW_ALL_PLAYLISTS
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

- [x] SHOW_PLAYLIST <playlist_name>
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

- [x] REMOVE_FROM_PLAYLIST <playlist_name> <video_id>
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

- [x] CLEAR_PLAYLIST <playlist_name>
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

- [x] DELETE_PLAYLIST <playlist_name>
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