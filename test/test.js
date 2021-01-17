require("isomorphic-unfetch");

const API_KEY = process.env.API_KEY
const USER = process.env.USER

const API_ROOT = "http://ws.audioscrobbler.com/2.0/"

const RECENT_URL = `${API_ROOT}?method=user.getrecenttracks&user=${USER}&limit=1&api_key=${API_KEY}&format=json`

const SONG_URL = `${API_ROOT}?method=user.gettoptracks&user=${USER}&limit=1&api_key=${API_KEY}&format=json`

const ARTIST_URL = `${API_ROOT}?method=user.gettopartists&user=${USER}&limit=1&api_key=${API_KEY}&format=json`

const USER_URL = `${API_ROOT}?method=user.getinfo&user=${USER}&api_key=${API_KEY}&format=json`

const WEEKLY_ARTIST_URL = `${API_ROOT}?method=user.getweeklyartistchart&user=${USER}&api_key=${API_KEY}&format=json`

const WEEKLY_ALBUM_URL = `${API_ROOT}?method=user.getweeklyalbumchart&user=${USER}&limit=10&api_key=${API_KEY}&format=json`

async function main() {
    
    const get = async (url) => {
        const r = await fetch(url);
        return await r.json();
    }

    const getTopTrack = async (artist) => {
        const url = `${API_ROOT}?method=artist.gettoptracks&artist=${artist}&limit=1&api_key=${API_KEY}&format=json`
        const r = await fetch(url);
        trackJSON = await r.json();
        return trackJSON.toptracks.track[0].image[2]['#text']
    }

    async function show_weekly_album() {
        songJSON = await get(WEEKLY_ALBUM_URL)
        songJSON = songJSON.weeklyalbumchart.album
        console.log(songJSON)
        for (let i = 0; i < 10; i++) {
            artistObj = songJSON[i]
            // console.log(artistObj)
            const artist = artistObj.name
            const count = artistObj.playcount
            let body = i+1 + ': ' + " [" + count + "] " + artist
            // console.log(body)
        }
    }   
    show_weekly_album()

    // weeklyJSON = await get(WEEKLY_ARTIST_URL)
    // console.log(weeklyJSON.weeklyartistchart.artist)
    
}


main();