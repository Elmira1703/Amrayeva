import request
import data
#Амраева Эльмира, 21 когорта
def test_get_track_order():
    response = request.post_new_order(data.body_order)
    print("Создание заказа в тесте:", response.status_code)
    if response.status_code == 201:
        track_number = response.json().get('track')
        print("Номер трека в тесте:", track_number)
        response1 = request.order_track(track_number)
        print("Получение заказа по треку в тесте:", response1.status_code)

        assert response1.status_code == 200
    else:
        print("Ошибка при создании заказа в тесте:", response.status_code)

test_get_track_order()
