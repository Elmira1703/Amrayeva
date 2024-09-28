import configuration
import requests
import data

def post_new_order(body_order):
    return requests.post(configuration.URL_SERVICE + configuration.NEW_ORDER_PATH, json=body_order)
response = post_new_order(data.body_order)
print("Создание заказа:", response.status_code)
print(response.json())

track_number = response.json().get('track')
print("Номер трека:", track_number)

def order_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK_PATH + str(track_number))

response_track = order_track(track_number)
print("Получение заказа по треку:", response_track.status_code)

