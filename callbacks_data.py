from aiogram.utils.callback_data import CallbackData


status_up_callback   = CallbackData('update', 'order_id')
delete_callback      = CallbackData('delete', 'order_id')
hide_callback        = CallbackData('hide', 'any')

edit_order_callback  = CallbackData('edit', 'order_id')

cancel_callback      = CallbackData('cancel', 'order_id')
split_callback       = CallbackData('split', 'order_id')
debs_lite_callback   = CallbackData('debs', 'user_id')
debs_ex_callback     = CallbackData('exdebs', 'deb_id')

goods_callback       = CallbackData('goods', 'user_id')



