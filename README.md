# Running track activities

This solution allowed me to search for which cardio activities I have done of Running on a race track. For this I used my activities registered in [Runkeeper] (https://runkeeper.com/) and it allowed me to export the data.
The files are:
* cardioActivities.csv: file with the list of activities with the following fields: 
Activity Id	
Date	
Type	
Route Name	
Distance (km)	
Duration	
Average Pace	
Average Speed (km/h)	
Calories Burned	Climb (m)	
Average Heart Rate (bpm)	
Friend's Tagged	Notes	
GPX File

* data: folder with each gpx file of each activity

## Solution
 
To obtain only the running activities that were on a track I did the following:

1. Create a dataframe with the information in cardioActivities.csv
2. Remove unnecessary columns
3. Filter only running activities
4. Open each gpx file from the running dataframe and search according to the coordinates in which activity I ran more than 4 times through the same point. This is because generally in other types of running activities other than the track we pass through the same point more than 2 or 3 times, this only happens on the track because it is circular.


## Built With

* [Pandas](https://pandas.pydata.org/) - Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data.
* [gpxpy](https://pypi.org/project/gpxpy/) - Python library for parsing and manipulating GPX files