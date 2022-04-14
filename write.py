"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json
from helpers import datetime_to_str

def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )
    field_names = {'time': 'datetime_utc', 'distance': 'distance_au', 'velocity': 'velocity_km_s', '_designation': 'designation', 'name': 'name', 'diameter': 'diameter_km', 'hazardous': 'potentially_hazardous'}

    if not results:
        with open(filename, 'w') as csv_outfile:
            writer = csv.writer(csv_outfile)
            writer.writerow(fieldnames)

    # ELABORATE: https://stackoverflow.com/questions/59291949/change-column-headers-using-dictwriter
    with open(filename, 'w', newline='') as csv_outfile:
        writer = csv.DictWriter(csv_outfile, fieldnames=field_names, extrasaction='ignore')
        writer.writerow(field_names)

        for elem in results:
            writer.writerow(elem.__dict__)

def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'neo', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )

    json_list = []
    with open(filename, 'w') as json_outfile:
        for elem in results:
            print(elem.__dict__['neo'])
            result_dict = dict(datetime_utc=datetime_to_str(elem.__dict__['time']), distance_au=elem.__dict__['distance'],
                velocity_km_s=elem.__dict__['velocity'], neo={
                "designation": elem.__dict__['neo'].designation,
                "name": elem.__dict__['neo'].name,
                "diameter_km": elem.__dict__['neo'].diameter,
                "potentially_hazardous": elem.__dict__['neo'].hazardous
            })
            json_list.append(result_dict)
        json.dump(json_list, json_outfile, indent=4)


