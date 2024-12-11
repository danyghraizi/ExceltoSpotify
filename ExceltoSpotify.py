import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser

# Define Spotify API credentials
SPOTIFY_CLIENT_ID = 'SPOTIFY_CLIENT_ID'
SPOTIFY_CLIENT_SECRET = 'SPOTIFY_CLIENT_SECRET'
SPOTIFY_REDIRECT_URI = 'http://localhost:8080'

# Set Microsoft Edge as the default browser
# webbrowser.register('edge', None, webbrowser.BackgroundBrowser(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'))

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="playlist-modify-private",
    open_browser=False  # Disable default browser open
))

# Custom function to open URL with Edge
auth_url = sp.auth_manager.get_authorize_url()
webbrowser.get('edge').open(auth_url)


# Load the Excel file
def load_excel(file_path):
    df = pd.read_excel(file_path, engine='openpyxl')
    return df

# Search for a track on Spotify
def search_track(track_name, artist_name):
    query = f"{track_name} {artist_name}"
    results = sp.search(q=query, type='track', limit=1)
    if results['tracks']['items']:
        return results['tracks']['items'][0]['id']
    return None

# Create a new playlist
def create_playlist(playlist_name):
    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
    return playlist['id']

# Add tracks to the playlist in chunks of 100
def add_tracks_to_playlist(playlist_id, track_ids):
    chunk_size = 100  # Spotify API limit
    for i in range(0, len(track_ids), chunk_size):
        chunk = track_ids[i:i + chunk_size]
        sp.playlist_add_items(playlist_id, chunk)
        print(f"Added {len(chunk)} tracks to the playlist.")


# Main Function
def main():
    # Path to your Excel file
    excel_file = "Piano_Music_Collection.xlsx"

    # Load data from Excel
    music_data = load_excel(excel_file)

    # Create a Spotify playlist
    playlist_name = "My Piano Music Playlist"
    playlist_id = create_playlist(playlist_name)
    print(f"Created playlist: {playlist_name}")

    # Search for tracks and collect Spotify IDs
    track_ids = []
    for _, row in music_data.iterrows():
        track_name = row[0]  # Assuming the track name is in the first column
        artist_name = row[1]  # Assuming the artist name is in the second column
        track_id = search_track(track_name, artist_name)
        if track_id:
            track_ids.append(track_id)
            print(f"Found: {track_name} by {artist_name}")
        else:
            print(f"Not Found: {track_name} by {artist_name}")

    # Add found tracks to the playlist
    if track_ids:
        add_tracks_to_playlist(playlist_id, track_ids)
        print("Tracks added to playlist successfully!")
    else:
        print("No tracks were added to the playlist.")

if __name__ == "__main__":
    main()
