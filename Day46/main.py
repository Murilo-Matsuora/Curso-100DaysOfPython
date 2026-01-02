from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

BILLBORD_ENDPOINT = "https://www.billboard.com/charts/hot-100/"

date = input("What date do you want to travel back to? (The format should be YYYY-MM-DD):\n")

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0"
}

response = requests.get(url=f"{BILLBORD_ENDPOINT}{date}", headers=header)
website = response.text

soup = BeautifulSoup(website, "html.parser")
song_tags = soup.find_all(
    name="h3",
    class_="c-title a-font-basic u-letter-spacing-0010 u-max-width-397 lrv-u-font-size-16 lrv-u-font-size-14@mobile-max u-line-height-22px u-word-spacing-0063 u-line-height-normal@mobile-max a-truncate-ellipsis-2line lrv-u-margin-b-025 lrv-u-margin-b-00@mobile-max",
    id="title-of-a-story"
)
song_names = [tag.getText().strip() for tag in song_tags]

with open(file=f"TopSongsFrom{date}.txt", mode="w") as f:
    for song_name in song_names:
        f.write(f"{song_name}\n")


# READ SENSITIVE DATA
senstive_data = {}
with open(file="sensitive_data.json",mode="r") as f:
    sensitive_data = json.load(f)

# CONNECTS TO SPOTIFY
scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id = sensitive_data["Spotify"]["client_id"],
    client_secret = sensitive_data["Spotify"]["client_secret"],
    redirect_uri = "https://example.com",
    scope = scope))

curent_user = sp.current_user()
print(curent_user)

# SEARCHES FOR THE SPOTIFY URLs
song_uris = []
print(date[:4])
for song_name in song_names:
    results = sp.search(q=f"track: {song_name} year: {date[:4]}", limit=10)['tracks']['items']
    if len(results) <= 0:
        raise LookupError
    else:
        print(results[0]['name'])
        print(results[0]['uri'])
        print("\n")
        song_uris.append(results[0]['uri'])

# CREATES PLAYLIST
print(f"user_id: {curent_user["id"]}")
playlist = sp.user_playlist_create(user=curent_user["id"], name=f"{date} Billboard 100", public=False)

# ADDS SONGS TO PLAYLIST
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
    
