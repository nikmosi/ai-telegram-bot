hello-msg =
    <b>👊 Здравей!</b>
    Если хочешь поддержать автора донатом, используй следующие команды:

    • /donate [сумма]: передай указанное количество звёзд (например, /donate 100)
    • /paysupport: помощь с платежами
    • /refund: возврат доната

donate-invoice-title =
    Донат автору

donate-invoice-description =
    На сумму в {$amount ->
        [one] {$amount} звезда
        [few] {$amount} звезды
       *[other] {$amount} звёзд
    }

donate-button-pay =
    Оплати {$amount} XTR

donate-button-cancel =
    Отмени операцию

donate-input-error =
    Укажи сумму в формате <code>/donate [ЧИСЛО]</code>, где [ЧИСЛО] — это количество доната, от ⭐️ 1 до ⭐️ 2500.

    Примеры:
    • <code>/donate 100</code> - передать 100 ⭐️
    • <code>/donate 500</code> - передать 500 ⭐️
    • <code>/donate 1000</code> - передать 1000 ⭐️

donate-paysupport-tid-tip =
    <blockquote>Его можно найти после завершения доната.
    Просто нажми на сообщение <b>"Ты успешно отправил ⭐️ .."</b> и скопируй ID транзакции.</blockquote>

donate-paysupport-message =
    Если тебе нужен возврат, воспользуйся командой /refund.

    🤓 Для этого потребуется ID транзакции.
    {donate-paysupport-tid-tip}

donate-refund-input-error =
    Введи ID транзакции в формате <code>/refund [id]</code>, где [id] — это код, который ты получил после доната.

    {donate-paysupport-tid-tip}

donate-refund-success =
    Возврат выполнен успешно. Потраченные звёзды возвращены на твой счёт в Telegram.

donate-refund-code-not-found =
    Транзакция с указанным ID не найдена. Проверь данные и попробуй снова.

donate-refund-already-refunded =
    Возврат по этой транзакции уже был выполнен.

donate-cancel-payment =
    😢 Донат отменён.

donate-successful-payment =
    <b>🫡 Спасибо!</b>
    Твой донат успешно обработан.

payment-none-error =
    ошибка xz

hello-owner =
    <b>👊 Здравей, хозяин!</b>

ping-msg =
    <b>👊 Всё работает!</b>

media-msg =
    <b>🫡 Крутая медиа <i>(наверное)</i>!</b>
