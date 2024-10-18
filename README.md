# Wrapped Predictor

## setup
go to the spotify privacy settings: https://www.spotify.com/us/account/privacy/
scroll down to the bottom to the download your data section
select only your account data to get the last year of listening
you will get a zip file with a lot of .json files
extract the streaming history .json files and put the python file in the same folder
example setup folder:

    ... / Spotify Account Data
	    StreamingHistory_music_0.json
	    StreamingHistory_music_1.json
	    StreamingHistory_music_2.json
	    StreamingHistory_music_3.json
	    ...
	    wrapper.py

## usage
change these variables to your liking to adjust what's printed
|var|info|
|--|--|
|filePrefix|string<br><br>if for some reason your data isn't in the default StreamingHistory_music_ prefix, you can change it to match the file names<br><br>ex: file names => test0.json, test1.json, test2.json; prefix => "test"|
|year|string<br><br>the year to predict|
|displayArtists|boolean<br><br>whether you want the top artists to be printed or not|
|numOrArtists|int<br><br>how many artists do you want to be displayed|
|displaySongs|boolean<br><br>whether you want the top songs to be printed or not|
|numOfSongs|int<br><br>how many songs do you want to be displayed|
|displayTotalMinutes|boolean<br><br>whether you want the number of minutes to be printed or not|

run the file and see the output in the terminal; you need numPy to run this

