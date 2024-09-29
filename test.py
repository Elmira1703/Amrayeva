import request
import data

# Амраева Эльмира, 21 когорта
def test_get_track_order():
    response = request.post_new_order(data.body_order)
    track_number = response.json().get('track')
    response1 = request.order_track(track_number)
    assert response1.status_code == 200, "Ошибка при получении заказа по треку"

test_get_track_order()



