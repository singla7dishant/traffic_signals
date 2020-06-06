import googlemaps
import requests
import json
import time
from csv import writer
import pandas as pd

API_key = ""
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial"

# function to add new row in the result csv file
def append_list_as_row(file_name, list_of_elem):
	with open(file_name, 'a', newline='') as write_obj:
		csv_writer = writer(write_obj)
		csv_writer.writerow(list_of_elem)

# function calls the api for source and destination and returns the api return parameters in the form of a list
def get_api_request_list(source_lat, source_long, dest_lat, dest_long):
	originPoint = source_lat + "," + source_long
	destinationPoint = dest_lat + "," + dest_long
	api_call = url + "&origins=" + originPoint + "&destinations=" + destinationPoint + "&departure_time=now" + "&key=" + API_key
	query_time = time.ctime()
	r = requests.get(api_call)
	res = r.json()
	distance_text = res['rows'][0]['elements'][0]['distance']['text']
	distance_value = res['rows'][0]['elements'][0]['distance']['value']
	duration_text = res['rows'][0]['elements'][0]['duration']['text']
	duration_value = res['rows'][0]['elements'][0]['duration']['value']
	duration_in_traffic_text = res['rows'][0]['elements'][0]['duration_in_traffic']['text']
	duration_in_traffic_value = res['rows'][0]['elements'][0]['duration_in_traffic']['value']
	return [source_lat, source_long, dest_lat, dest_long, query_time, distance_text, distance_value, duration_text, duration_value, duration_in_traffic_text, duration_in_traffic_value]


# reads space separated latitude longitude coordinates from a file and passes them as string to get_api_request_list func
def main():
	coordinates = pd.read_csv('input.txt', sep='\s+', header=None, converters={i: str for i in range(4)})
	for i in range(0, 188):
		result_list = get_api_request_list(coordinates[0][0], coordinates[1][0], coordinates[0][1], coordinates[1][1])
		print(result_list)
		append_list_as_row('result.csv', result_list)
		time.sleep(300)


if __name__ == '__main__':
	main()

