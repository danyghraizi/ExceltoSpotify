# SpotifyExcel
Given an excel sheet with the columns (Title, Artist) you can create a spotify playlist with whatever songs are found on spotify.

Instructions to Use

Install Required Libraries:

Install Python libraries:
pip install spotipy pandas openpyxl

Set Up Spotify Developer Account:

Visit the Spotify Developer Dashboard (https://developer.spotify.com/dashboard/) and create an app.
You need to select Web API when creating the Spotify Developer App. The script leverages the Spotify Web API to search for tracks, create playlists, and add tracks to playlists.
No other SDKs or APIs are required for this script.

Obtain your CLIENT_ID and CLIENT_SECRET.

Update Script:

Replace your_client_id and your_client_secret in the script with your Spotify credentials.
Prepare Excel File:

Ensure your Excel file (Piano_Music_Collection.xlsx) is in the same directory as the script.
Run the Script:

Execute the script:
python ExceltoSpotify.py

Authenticate:

The script will open a browser for Spotify authentication. Log in and authorize the app.

Playlist Created:

A new Spotify playlist named "My Piano Music Playlist" will be created, containing the tracks found in the Excel file.

NOTE: Uncomment the line of code that has "edge" to use "edge" browser instead of the default browser you have.
