bad_greet = 'Привет! Я облачный список покупок, отправь мне любое сообщение, и я сохраню его. Когда будешь в ' \
            'магазине, не забудь отправить мне /goods, и я покажу всё, что необходимо купить. По умолчанию покупки, ' \
            'добавленные тобой, просматривать и удалять можешь только ты. Чтобы это изменить, просто отправь мне имя ' \
            'пользователя в формате\n@имя_пользователя\nТогда он получит доступ к твоим покупкам. Поле username у ' \
            'вашего аккаунта не заполнено, оно необходимо для более комфортного кооперативного использования бота, ' \
            'чтобы обновить username в моей базе данных,просто отправь мне /start ещё раз '

good_greet = 'Привет! Я облачный список покупок, отправь мне любое сообщение, и я сохраню его. Когда будешь в ' \
             'магазине, не забудь отправить мне /goods, и я покажу всё, что необходимо купить. По умолчанию покупки, ' \
             'добавленные тобой, просматривать и удалять можешь только ты. Чтобы это изменить, просто отправь мне имя ' \
             'пользователя в формате\n@имя_пользователя\nТогда он получит доступ к твоим покупкам.'

help_msg = '/goods - показать весь список, нажми на номер заказа, чтобы изменить его статус.\n/delete - вывести меню ' \
           'удаления.\n/start - обновить твой username.\n/edit - изменить текст заказа\n/lite - изменить режим, ' \
           'в лайт версии я не спрашиваю стоимость покупки при её ' \
           'завершении.\n/split - разделить стоимость покупки между пользователями.\n/debs - посмотреть ' \
           'долги.\n/stats - статистика покупок.\nЧтобы добавить покупку в список, просто отправь мне ' \
           'сообщение.\nПо умолчанию покупки, добавленные тобой, просматривать и удалять можешь только ты. Чтобы это ' \
           'изменить, просто отправь мне имя пользователя в формате @имя_пользователя\nТогда он получит доступ к ' \
           'твоим покупкам. Чтобы удалить доступ пользователя к твоим покупкам, отправь мне его юзернейм'

token = '1778262030:AAFYe10ZYdHSXRW5DZ1l_mB__P1TasLAXks'

admin = 'YOUR_ID'

tec = 'Привет! Добавил новый функционал, теперь можно смотреть статистику покупок, пофиксил баги, постарался сделать ' \
      'интерфейс максимально удобным и понятным. Пользуйся на здоровье, советуй друзьям и родственникам 🤣🤣🤣! Не ' \
      'забывай про расширенную версию (/lite), ' \
      'в ней бот спрашивает цену, при завершении покупки, это позволяет просматривать статистику трат, ' \
      'а также разделять стоимость покупки между пользователями. '

squirrels = ['CAACAgIAAxkBAAECKuBgdA7PIiGM4Or3lOAKGppu_RFCbAACowAD9wLID977KA9x6YmlHgQ',
             'CAACAgIAAxkBAAECKuJgdA7RSLgzavoSx-t4qUeN_Ri8_wACoQAD9wLID3k4mJr5Qz72HgQ',
             'CAACAgIAAxkBAAECKuRgdA7VQcbNqtYyqv87HhMtiktUQwACoAAD9wLID8NHHQGgm8AaHgQ',
             'CAACAgIAAxkBAAECKuVgdA7WkhFHW6qmd9gdb6YMRgd37wACmQAD9wLIDwrFMSvLc6BpHgQ',
             'CAACAgIAAxkBAAECKudgdA7XHRNFHkZiIqewq1lzYrz69wACmgAD9wLID9HVBvL9etQ4HgQ',
             'CAACAgIAAxkBAAECKuhgdA7XGeDPiMh9CooQlbNyONGANgACmwAD9wLID687ftTB4dOYHgQ',
             'CAACAgIAAxkBAAECKupgdA7YJYplG4GnEhqBhSjKtQpavgACnwAD9wLID8ve8ZYAAQzT_h4E',
             'CAACAgIAAxkBAAECKutgdA7ZjoZreKkp6SRBrdTg8a9LVQACoQAD9wLID3k4mJr5Qz72HgQ',
             'CAACAgIAAxkBAAECKu1gdA7aUD2lguB2y0jyvf9TfmmfBQACmAAD9wLID26aCmxF9ps7HgQ',
             'CAACAgIAAxkBAAECKu9gdA7cMLhmqJ3WErZPErBRMAgwVQACpQAD9wLID-xfZCDwOI5LHgQ',
             'CAACAgIAAxkBAAECKvBgdA7dCJX-DO5PEBZDgwAB_yXr9x8AAo8AA_cCyA_8LYxF0C17zx4E',
             'CAACAgIAAxkBAAECKvJgdA7dtMPVi-mNZ9_nPMKzN9wo7gACpgAD9wLID6sM5POpKsZYHgQ',
             'CAACAgIAAxkBAAECKvNgdA7e4NftoVPrPW3doiczGwABi90AAqcAA_cCyA_LmDZA3UdgQR4E',
             'CAACAgIAAxkBAAECKvVgdA7f0U5OqxcxaVZgv-Zkg2qtiAACqAAD9wLID6iv6Bm2o-fnHgQ',
             'CAACAgIAAxkBAAECKvZgdA7gv-gevih1TbXHpQ6TxNJTpwACqQAD9wLIDxrF_2d1FFb4HgQ',
             'CAACAgIAAxkBAAECKvlgdA7iQPkuCDfDZ_mTrTz-U2PjkwACrgAD9wLID1_vtWxyDS0cHgQ',
             'CAACAgIAAxkBAAECKvpgdA7j4zl6MxLUrqNGfHE6QNpcHQACsAAD9wLID2j04ssMRn4kHgQ',
             'CAACAgIAAxkBAAECKvxgdA7kX2Hdnw9s1srcTq8P0A_lEAACrQAD9wLID7aV4gPQ-IA2HgQ',
             'CAACAgIAAxkBAAECKv1gdA7lZ1cWuU0bgNfZ5LgdnkeuQwACrAAD9wLID7sfK_VIr8n_HgQ',
             'CAACAgIAAxkBAAECKv9gdA7m6Rih_ll2_N6uGRZ7GoM_AwACqwAD9wLIDzE2ZuCskJUTHgQ',
             'CAACAgIAAxkBAAECKwFgdA7ooR4AAUDv2fMmcwNFoHMjpeoAAq8AA_cCyA-sCY3fq8aviR4E',
             'CAACAgIAAxkBAAECKwJgdA7olYleSYMNmorbTwzkf0cGzAACsQAD9wLID0cy0eKJOA2nHgQ',
             'CAACAgIAAxkBAAECKwRgdA7pR7gbrNiM6Q7nHqr_W21erAACsgAD9wLIDzOrIv3wX5RYHgQ',
             'CAACAgIAAxkBAAECKwVgdA7qRMKW3TiMKBVCPpS_ULu6dgACswAD9wLID6eWFTHTpw2zHgQ',
             'CAACAgIAAxkBAAECKwdgdA7rOfVzdSXQCxc9Z480ToUooQACtAAD9wLID2Uu3kpwpiGRHgQ']
