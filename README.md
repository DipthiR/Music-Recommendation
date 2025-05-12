# Music-Recommendation
### Spotify Music Recommendation System
This project uses the Spotify API to recommend songs similar to a given song. The recommendations are based on features such as danceability, energy, tempo, and more. The system uses the Spotipy library to interact with the Spotify API.

## Features:
Search for a song by name.

Fetch audio features like danceability, energy, loudness, etc., for the song.

Recommend songs based on the song's features.

Display recommended songs with their names, artists, popularity, and direct links to listen on Spotify.

## Requirements
Python 3.x

Spotipy library (Python library for the Spotify API)

You can install the required libraries using pip:

pip install spotipy
## Setup
1. Spotify Developer Account
To use the Spotify API, you need to have a Spotify Developer Account and create an application to get the necessary credentials (Client ID and Client Secret).

Go to the Spotify Developer Dashboard.

Log in with your Spotify account.

Create a new app to get your Client ID and Client Secret.

Replace the YOUR_CLIENT_ID and YOUR_CLIENT_SECRET placeholders in the MusicRecommendation.py file with your credentials.

## How to Run the Program
Clone or download this repository to your local machine.

Open the Python file MusicRecommendation.py and set your Client ID and Client Secret in the script.

Run the Python script:

python MusicRecommendation.py
The program will fetch audio features for a given song (e.g., "Shape of You") and recommend similar songs based on those features.

## Example Output
After running the program, you will get output similar to this:

Features for 'Shape of You':
  danceability: 0.822
  energy: 0.741
  tempo: 95.982
  valence: 0.568
  loudness: -4.136
  speechiness: 0.0809

Songs similar to 'Shape of You':
Song: Blinding Lights, Artist: The Weeknd, Popularity: 90
Listen on Spotify: spotify:track:0VjIjW4GlUZAMYd2vXMi3b
------
Song: Don't Start Now, Artist: Dua Lipa, Popularity: 88
Listen on Spotify: spotify:track:7jyY8d1u2W5y3lgFQy5mjX
------
Song: Levitating, Artist: Dua Lipa, Popularity: 88
Listen on Spotify: spotify:track:2nJrR5QsTfqVt5aV9Krfgb
------
...
## Troubleshooting
Invalid Client ID/Secret:

Ensure that you've copied the correct Client ID and Client Secret from your Spotify Developer Dashboard.

Double-check that there are no extra spaces or characters when copying and pasting.

API Errors:

If you encounter errors related to the API, ensure that your credentials are valid and that you are authenticated properly.

Refer to the Spotify API Documentation for more details on the API usage.

No Results Found:

If a song isn't found, it may not exist on Spotify. Try using a more popular song or verify the song's name.

