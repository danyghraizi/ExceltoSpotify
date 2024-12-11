
# SpotifyExcel

This project allows you to create a Spotify playlist from an Excel sheet that contains song information in 2 columns (Title, Artist). The script searches for the tracks on Spotify and adds them to a newly created playlist.

## Instructions to Use

### 1. Install Required Libraries

To run the script, you need to install the required Python libraries. Run the following command to install them:

```bash
pip install spotipy pandas openpyxl
```

### 2. Set Up Spotify Developer Account

1. Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and create an app.
2. When creating the app, select **Web API**. The script uses the Spotify Web API to search for tracks, create playlists, and add tracks to playlists.
3. No other SDKs or APIs are required for this script.
4. Once the app is created, obtain your `CLIENT_ID` and `CLIENT_SECRET`.

### 3. Update Script with Your Credentials

Replace the `your_client_id` and `your_client_secret` in the script with your Spotify credentials.

### 4. Prepare Excel File

Ensure that your Excel file, such as `Piano_Music_Collection.xlsx`, is in the same directory as the script. The Excel file should have the following columns:

- **Title** (e.g., song name)
- **Artist** (e.g., artist name)

### 5. Run the Script

Execute the script with the following command:

```bash
python ExceltoSpotify.py
```

### 6. Authenticate

The script will open a browser for Spotify authentication. Log in and authorize the app to allow it to create playlists and add tracks.

### 7. Playlist Created

After successful authentication, a new Spotify playlist named **"My Piano Music Playlist"** will be created, containing the tracks found in the Excel file.

### NOTE

If you want to use a different browser for authentication, you can modify the webbrowser.get() function in the script:

```python
# Custom function to open URL with Edge
auth_url = sp.auth_manager.get_authorize_url()
webbrowser.get('edge').open(auth_url)  # Change 'edge' to your desired browser if needed
```

---

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
