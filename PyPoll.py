import csv
import os
#file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.
#election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
#election_data.close()
#with open(file_to_load) as election_data:
 #   print(election_data)
 # Create a filename variable to a direct or indirect path to the file.
#file_to_save = "Resources/analysis/election_analysis.txt"

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
 #   txt_file.write("Hello World")
  #  txt_file.write("Arapahoe")
   # txt_file.write("Denver")
    #txt_file.write("Jefferson")
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Resources", "analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    # Print each row in the CSV file.
    #for row in file_reader:
    #    print(row)
