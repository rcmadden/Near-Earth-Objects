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

    # field_names = (
    #     'time', 'distance', 'velocity',
    #     '_designation', 'name', 'diameter', 'hazardous', 'neo'
    # )
    # if results == None or results == '':
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
            print(elem.__dict__)
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
    with open(filename, 'w', encoding='utf8') as json_outfile:
        for elem in results:
            # json_outfile.write(json.dumps(elem.__dict__, default=str))
            # json.dump(elem.__dict__,json_outfile, ensure_ascii=False, default=str)
            # json.dump(elem.__dict__, json_outfile, default=str, separators=(',', ':'))
            
            # jsonString = json.dumps(elem.__dict__,default=str)
            # json_outfile.write(jsonString)
            
            json_list.append(elem.__dict__)
        # rename dictionary keys
        # print(json_list)
        new_dict = []
        d1 = dict(zip(list(json_list[0].keys()), fieldnames))
        for i in range(len(json_list)):
            # d1 = dict(zip(list(json_list[i].keys()), fieldnames))
            new_dict.append({d1[old_key]: value for old_key, value in json_list[i].items()})

        json.dump(new_dict, json_outfile, indent=4, default=str)


