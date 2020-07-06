# traffic_signals

#### meant for one source-destination pair
input.txt - Each line in this file contains space separated Latitude Longitude values of a place. The first line corresponding to the origin and the second corresponds with the destination. To roughly imagine, here I've considered the road from after Natural's Icecream to Essex Farms so that exactly one intersection on ring road is covered. 

code.py - It has following mentioned functions each doing it's tasks as described below:
1. main() - It reads the Latitude Longitude values from the input file (here input.txt) as a string format and calls get_api_request_list after every 5 minutes for 24 hours. Each API request answer obtained is added as a new line in result file (result.csv here)

2. get_api_request_list(source_lat, source_long, dest_lat, dest_long) - This function takes latitude longitude values of source and destination as parameters and calls google's distance matrix api to get the answer for the query. A list of the API's reply's parameters is formed and returned.

3. append_list_as_row(file_name, list_of_elem) - The api request list obtained is appended as a row in the result csv file using this function. 

result.csv - Its results are obtained in result.csv file 

To run this section, use the command : python3 code.py

#### meant for 4 source-destination pair crossing a single intersection
input_1.txt - Each line in this file contains space separated Latitude Longitude values of a place. Each alternate line corresponds to the source and destination alternatively. For eg. 1st line is the source and 2nd its corresponding destination, 3rd line is the source and 4th its corresponding destination and so on. Each source destination path crosses a single intersection only. 

code_1.py - It has following mentioned functions each doing it's tasks as described below:
1. main() - It reads the Latitude Longitude values from the input file (here input.txt) as a string format and calls get_api_request_list for all source destination pairs, after every 5 minutes for 7 days. Each API request answer obtained is added as a new line in result file (result.csv here). So, after every 5 minutes, 4 lines are added in the result file each corresponding to a single source destination pair.

Rest functions in this file are exactly the same as code.py.

result_1.csv - Its results are obtained in result_1.csv file.

To run this section, use the command : python3 code_1.py
