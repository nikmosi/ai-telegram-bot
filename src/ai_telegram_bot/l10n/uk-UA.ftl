hello-msg =
    <b>👊 Привіт!</b>
    Якщо ви хочете підтримати автора донатом, скористайтеся наступними командами:

    • /donate [сума]: задонатити вказану кількість зірок (наприклад, /donate 100)
    • /paysupport: допомога з оплатами
    • /refund: повернення донату

donate-invoice-title =
    Донат автору

donate-invoice-description =
    На суму {$amount ->
        [one] {$amount} зірку
        [few] {$amount} зірки
       *[other] {$amount} зірок
    }

donate-button-pay =
    Сплатити {$amount} XTR

donate-button-cancel =
    Скасувати операцію

donate-input-error =
    Будь ласка, введіть суму у форматі <code>/donate [ЧИСЛО]</code>, де [ЧИСЛО] — це сума донату від ⭐️ 1 до ⭐️ 2500.

    Приклади:
    • <code>/donate 100</code> - задонатити 100 ⭐️
    • <code>/donate 500</code> - задонатити 500 ⭐️
    • <code>/donate 1000</code> - задонатити 1000 ⭐️

donate-paysupport-tid-tip =
    <blockquote>Ви можете отримати його після завершення донату.
    Просто натисніть на повідомлення <b>"Ви успішно відправили ⭐️ .."</b> і скопіюйте ID транзакції звідти.</blockquote>

donate-paysupport-message =
    Якщо ви хочете зробити повернення коштів, скористайтеся командою /refund.

    🤓 Вам знадобиться ID транзакції.
    {donate-paysupport-tid-tip}

donate-refund-input-error =
    Будь ласка, вкажіть ID транзакції у форматі <code>/refund [id]</code>, де [id] — це ID транзакції, який ви отримали після донату.

    {donate-paysupport-tid-tip}

donate-refund-success =
    Повернення коштів успішно виконано. Зірки повернено на ваш рахунок у Telegram.

donate-refund-code-not-found =
    Транзакція з вказаним ID не знайдена. Будь ласка, перевірте дані і спробуйте ще раз.

donate-refund-already-refunded =
    Повернення коштів за цією транзакцією вже було здійснено раніше.

donate-cancel-payment =
    😢 Донат скасовано.

donate-successful-payment =
    <b>🫡 Дякую!</b>
    Ваш донат успішно прийнято.

payment-none-error =
    помилка xz

hello-owner =
    <b>👊 Привіт, власнику!</b>

ping-msg =
    <b>👊 Усе працює!</b>

media-msg =
    <b>🫡 Гарний медіафайл <i>(мабуть)</i>!</b>
