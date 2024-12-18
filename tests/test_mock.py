from pay_client.clients.mock import MockPayClient
from pay_client.configs.mock import MockConfig
from pay_client.enums.order import DisplayMode, Status
from pay_client.models.order import OrderUnified

def test_func():
    config = MockConfig()
    client = MockPayClient(config=config)
    order_unified_data = {
        'out_trade_no': '123456',
        'subject': 'test',
        'body': 'test',
        'notify_url': 'http://test.com/notify',
        'return_url': 'http://test.com/return',
        'price': 0.01,
        'expire_time': '2022-01-01 00:00:00',
    }

    order = client.unified_order(data=OrderUnified(**order_unified_data))
    correct_order = {
        'status': Status.SUCCESS,
        'channel_order_no': 'MOCK-P-123456',
        'channel_user_id': '',
        'out_trade_no': '123456',
        'raw_data': 'MOCK_SUCCESS',
        'success_time': order.success_time,
        'display_mode': DisplayMode.DEFAULT,
        'display_content': None,
        'channel_error_code': None,
        'channel_error_message': None,
    }
    assert order.model_dump() == correct_order