import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Set up the Spotify API client with your credentials
client_id = 'YOUR_CLIENT_ID'  # Replace with your Spotify client ID
client_secret = 'YOUR_CLIENT_SECRET'  # Replace with your Spotify client secret

# Authenticate with Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Function to get song features based on a song name
def get_song_features(song_name):
    # Search for the song on Spotify
    result = sp.search(q=song_name, limit=1)
    
    # Check if we found a song
    if not result['tracks']['items']:
        return None
    
    # Get the track ID for the first search result
    track_id = result['tracks']['items'][0]['id']
    
    # Get audio features for the song
    features = sp.audio_features(track_id)[0]
    
    return features

# Function to recommend similar songs based on a song's features
def recommend_songs(song_name, num_recommendations=5):
    # Get the features of the input song
    song_features = get_song_features(song_name)
    
    if not song_features:
        print(f"Song '{song_name}' not found on Spotify.")
        return []
    
    # Extract relevant features for similarity (e.g., danceability, energy, tempo, etc.)
    features = ['danceability', 'energy', 'tempo', 'valence', 'loudness', 'speechiness']
    song_values = {feature: song_features[feature] for feature in features}
    
    print(f"Features for '{song_name}':")
    for feature, value in song_values.items():
        print(f"  {feature}: {value}")

    # Use Spotify recommendations API to find similar tracks based on song features
    recommendations = sp.recommendations(seed_tracks=[song_features['id']], limit=num_recommendations)
    
    recommended_songs = []
    for track in recommendations['tracks']:
        song = {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'uri': track['uri'],
            'popularity': track['popularity']
        }
        recommended_songs.append(song)
    
    return recommended_songs

# Example usage
song_name = "Shape of You"  # Song to base recommendations on
recommended_songs = recommend_songs(song_name)

# Display the recommended songs
if recommended_songs:
    print(f"\nSongs similar to '{song_name}':")
    for song in recommended_songs:
        print(f"Song: {song['name']}, Artist: {song['artist']}, Popularity: {song['popularity']}")
        print(f"Listen on Spotify: {song['uri']}")
        print("------")
