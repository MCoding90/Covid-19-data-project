import tui

"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of records (where each record is a list of data values) as a parameter.
- Process the list of records appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of records that have been loaded.
- Retrieve a record with the serial number as specified by the user.
- Retrieve the records for the observation dates as specified by the user.
- Retrieve all of the records grouped by the country/region.
- Retrieve a summary of all of the records. This should include the following information for each country/region:
    - the total number of confirmed cases
    - the total number of deaths
    - the total number of recoveries

 
"""


# TODO: Your code here

def retrieve_total_records(t_records):
    data = []
    for record in data:
        data.append(record)
        t_records = len(data)
    tui.total_records(t_records)
    print(data)
    return data


def record_serial_number():
    serial_numbers = []
    for record in serial_numbers:
        serial_numbers.append(record[0])
        serial_numbers = len(serial_numbers)
    tui.serial_number()
    print(serial_numbers)
    return serial_numbers


def records_observation_dates():
    observation_dates_list = []
    for record in observation_dates_list:
        observation = record[1]
        observation.append(observation_dates_list)
    tui.observation_dates()
    print(observation_dates_list)
    return observation_dates_list


def records_grouped():
    country_region_list = []
    for record in country_region_list:
        country = record[2]
        country.append(country_region_list)
    print(country_region_list)
    return country_region_list


def records_summary():

