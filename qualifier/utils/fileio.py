# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

# write a function named save_csv that uses the csv library to save the qualifying data as a file.
def save_csv(csvpath, data):
    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Then we can write the data rows
        for row in data:
            csvwriter.writerow(row.values())
