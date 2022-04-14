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

    # TODO: Write the results to a CSV file, following the specification in the instructions.
    # https://stackoverflow.com/questions/59291949/change-column-headers-using-dictwriter
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

    # TODO: Write the results to a JSON file, following the specification in the instructions.
    json_list = []
    with open(filename, 'w') as json_outfile:
        # for elem in results:
            # json_outfile.write(json.dumps(elem.__dict__, default=str))
            # json.dump(elem.__dict__,json_outfile, ensure_ascii=False, default=str)
            # json.dump(elem.__dict__, json_outfile, default=str, separators=(',', ':'))
            
            # jsonString = json.dumps(elem.__dict__,default=str)
            # json_outfile.write(jsonString)
            # print(elem.__dict__['neo'])

            # json_list.append(elem.__dict__)
       
        # rename dictionary keys
        new_dict_keys = []
        key_map = {'time': 'datetime_utc', 
                    'neo': 'neo', 
           '_designation': 'designation', 
               'distance': 'distance_au', 
               'velocity': 'velocity_km_s'} 

        # for i in range(len(json_list)):
        #     # d1 = dict(zip(list(json_list[i].keys()), fieldnames))
        #     # json_list[i] = json_list[i].serialize()

        #     # json_list[i]['time'] = str(json_list[i]['time'])
        #     # json_list[i]['time'] = datetime.datetime.strptime(json_list[i]['time'], '%Y-%m-%d %H:%M')
        #     json_list[i]['time'] = datetime_to_str(json_list[i]['time'])
        #     new_dict_keys.append({key_map[old_key]: value for old_key, value in json_list[i].items()})
    
        # json.dump(new_dict_keys, json_outfile, indent=4, default=str)
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


