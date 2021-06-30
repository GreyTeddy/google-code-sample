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