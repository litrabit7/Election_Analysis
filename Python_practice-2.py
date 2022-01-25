# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

# import csv functions
import csv  

# use to see the options

# dir(csv)

# import the operating system
import os
# dir(os)

# submodule with useful funciton joining path
# dir(os.path)
# alternative for geting the file path
# file_to_load = os.path.join("Resources", "election_results.csv")


# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
# election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
# election_data.close()

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    # txt_file.write("Hello World")
    # Write three counties to the file.
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson")

    # Write three counties to the file.
    #  txt_file.write("Arapahoe, Denver, Jefferson")
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")