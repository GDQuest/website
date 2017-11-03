#!/usr/bin/python3

import os

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def get_channel_playlist(service, **kwargs):
    results = service.playlists().list(
        **kwargs
    ).execute()

    if results["pageInfo"]["totalResults"] > results["pageInfo"]["resultsPerPage"]:
        numItems = results["pageInfo"]["resultsPerPage"]
    else:
        numItems = results["pageInfo"]["totalResults"]

    for num in range(0, numItems):
        print(results['items'][num]['snippet']['title'])
        get_playlist_videos(service,
            part='snippet',
            playlistId=str(results['items'][num]["id"]),
            maxResults=50
        )

def get_playlist_videos(service, **kwargs):
    results = service.playlistItems().list(
        **kwargs
    ).execute()

    if results["pageInfo"]["totalResults"] > results["pageInfo"]["resultsPerPage"]:
        numItems = results["pageInfo"]["resultsPerPage"]
    else:
        numItems = results["pageInfo"]["totalResults"]
    
    print(numItems)

    for num in range(0, numItems):
        print(" - ", results['items'][num]['snippet']['title'])

if __name__ == "__main__":
    # When running locally, disable OAuthlib's HTTPs verification. When
    # running in production *do not* leave this option enabled.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    youtube = get_authenticated_service()
    get_channel_playlist(youtube,
        part='snippet',
        channelId='UCxboW7x0jZqFdvMdCFKTMsQ',
        maxResults=50
    )
