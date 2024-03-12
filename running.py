import pandas as pd
import gpxpy
import gpxpy.gpx


def main():
    activities = pd.read_csv('cardioActivities.csv')

    to_drop = ['Route Name',
               'Average Heart Rate (bpm)',
               'Friend\'s Tagged',
            'Notes']
    activities.drop(to_drop, inplace=True, axis=1)

    filtered_df = activities['Type'] == 'Running'

    running = activities[filtered_df]

    listInTrack = []

    for index, row in running.iterrows():
        file ='data/'+str(row["GPX File"])
        gpx_file = open(file, 'r')
        gpx = gpxpy.parse(gpx_file)

        for track in gpx.tracks:
            laps = 0
            for segment in track.segments:
                initialLatitude = segment.points[0].latitude
                initialLongitude = segment.points[0].longitude
                initialPoint = True
                for point in segment.points:
                    if not initialPoint:
                        if round(initialLatitude,4) == round(point.latitude,4) and round(initialLongitude,4) == round(point.longitude,4):
                            laps += 1
                    initialPoint = False
        if laps > 4:
            listInTrack.append(file.replace('data/',''))
        booleanSeries = running["GPX File"].isin(listInTrack)
        trackActivities = running[booleanSeries]   
    print(trackActivities[["Date", "Distance (km)","Duration","Average Pace"]])

if __name__ == '__main__':
    main()
