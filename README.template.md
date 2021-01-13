# Last.fm pulling data from Spotify TEST repo

Using Python & JavaScript to access last.fm and view my most recently listened to tracks on Spotify. This is a repo only for **testing** and setting up my profile readme. Check out my profile's README with this integrated!

Currently I am only using the JavaScript integration which avoids using redis.

## Most recent song

I really enjoy listening to music! My current playcount is {playcount} 🤯 . Here is my top artist and who I am listening to now!

| Last Listened              | Top Artist                       | Top Song                          |
| -------------------------- | -------------------------------- | --------------------------------- |
| ![Song Cover Photo]({img}) | ![Song Cover Photo]({artistImg}) | ![Song Cover Photo]({topSongImg}) |
| Artist: **{artist}**       | Artist: **{topArtist}**          | Artist: **{topSongArtist}**       |
| Title: **{song}**          | Streams: **{topArtistStreams}**  | Title: **{topSongName}**          |

## Works Cited

- Checkout a page for how to get the workflow going [here](https://dev.to/gargakshit/how-i-added-my-spotify-statistics-to-my-github-readme-4jdd)
- I use last.fm API since Spotify API would require token to get read only data which last.fm does not
- Checkout [last.fm/api](https://www.last.fm/api)
