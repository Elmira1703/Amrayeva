import configuration
import requests
import data

def post_new_order(body_order):
    return requests.post(configuration.URL_SERVICE + configuration.NEW_ORDER_PATH, json=body_order)

def order_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK_PATH + str(track_number))

response = post_new_order(data.body_order)

track_number = response.json().get('track')
response_track = order_track(track_number)



