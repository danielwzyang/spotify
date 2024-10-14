# to get your data, go to https://www.spotify.com/us/account/privacy/
# scroll down to the bottom to the download your data section
# select only your account data to get the last year of listening
# click request data and go to your email to confirm
# this will take up to 5 days to get sent to you
# you will get a zip file with a lot of .json files
# extract the zip and put this python file in the same folder as the .json files
# make sure you see something like StreamingHistory_music_0.json

# change the values below to your liking
# you need python and numpy to run the file

# default: StreamingHistory_music_0.json -> StreamingHistory_music
# if you're using jsons with different names for some reason make sure to update the prefix
# your files have to be in the form prefix0.json, prefix1.json, etc
filePrefix = "StreamingHistory_music_"

# default: wrapped for year 2024
year = "2024"

# set to false if you don't want the top artists to be printed
displayArtists = True
# default: top 5 artists
numOfArtists = 5

# set to false if you don't want the top songs to be printed
displaySongs = True
# default: top 5 songs
numOfSongs = 5

# set to false if you don't want the total minutes to be printed
displayTotalMinutes = True



# actual code

import json
import os.path
import numpy as np

# keeps an list of objects storing all the songs from the json files
allSongs = []

# loops through the files
counter = 0

# takes all the streaming history files and adds them to the songs list
while os.path.isfile(filePrefix + str(counter) + ".json"):
    allSongs = np.concatenate((allSongs, json.load(
        open(filePrefix + str(counter) + ".json", encoding="utf8"))))
    counter += 1

# initializes the object that will store all the data
data = {
    "artist": {

    },
    "track": {

    }
}

# loops through all the songs
for song in allSongs:
    # if the song was played in the year set
    if year in song["endTime"]:
        # if this is the first time seeing an artist, it will initialize the value to 0 minutes
        if song["artistName"] not in data["artist"].keys():
            data["artist"][song["artistName"]] = 0
        
        # adds the number of minutes to the artist
        # divide by 60000 because there are 60000 ms in 1 min
        data["artist"][song["artistName"]] += song["msPlayed"] / 60000
            
        # if this is the first time seeing a song, it will initialize the value to 0 plays
        if song["trackName"] not in data["track"].keys():
            data["track"][song["trackName"]] = 0

        # adds 1 to the number of plays for the song
        data["track"][song["trackName"]] += 1

print("----------------------------------------------")

# if the user wants to display the artists
if displayArtists:
    # takes all the artists and sorts them by decreasing number of minutes
    # takes the top n(value provided by user) artists
    topArtists = dict(reversed(sorted(data["artist"].items(), key=lambda item: item[1])[-numOfArtists:]))

    print(f"Your top {numOfArtists} artists this year are:\n")

    ranking = 1
    # loops through every artist
    for artist in topArtists:
        # prints ranking, artist, and number of minutes
        print(f"{ranking}. {artist} | {int(topArtists[artist])} minutes")
        ranking += 1

    print("----------------------------------------------")

# if the user wants to display the songs
if displaySongs:
    # takes all the songs and sorts them by decreasing number of plays
    # takes the top n(value provided by user) songs
    topSongs = dict(reversed(sorted(data["track"].items(), key=lambda item: item[1])[-numOfSongs:]))

    print(f"Your top {numOfSongs} songs this year are:\n")

    ranking = 1
    # loops through every song
    for song in topSongs:
        # prints ranking, song, and number of plays
        print(f"{ranking}. {song} | {topSongs[song]} plays")
        ranking += 1

    print("----------------------------------------------")

# if the user wants to display the songs
if displayTotalMinutes:
    # gets total of all the minutes by summing the minutes of all of the artists
    print(f"You listened to {int(sum(data["artist"].values()))} minutes this year!")
    print("----------------------------------------------")