hello-msg =
    <b>👊 Cześć!</b>
    Jeśli chcesz wesprzeć autora darowizną, skorzystaj z następujących poleceń:

    • /donate [kwota]: przekaż określoną liczbę gwiazdek (np. /donate 100)
    • /paysupport: pomoc z płatnościami
    • /refund: zwrot darowizny

donate-invoice-title =
    Wspieraj autora

donate-invoice-description =
    Na kwotę {$amount ->
        [one] {$amount} gwiazdkę
        [few] {$amount} gwiazdki
       *[other] {$amount} gwiazdek
    }

donate-button-pay =
    Zapłać {$amount} XTR

donate-button-cancel =
    Anuluj operację

donate-input-error =
    Proszę podać kwotę w formacie <code>/donate [LICZBA]</code>, gdzie [LICZBA] to kwota darowizny od ⭐️ 1 do ⭐️ 2500.

    Przykłady:
    • <code>/donate 100</code> - przekaż 100 ⭐️
    • <code>/donate 500</code> - przekaż 500 ⭐️
    • <code>/donate 1000</code> - przekaż 1000 ⭐️

donate-paysupport-tid-tip =
    <blockquote>Możesz go uzyskać po zakończeniu darowizny.
    Po prostu kliknij wiadomość <b>"Pomyślnie wysłano ⭐️ .."</b> i skopiuj z niej ID transakcji.</blockquote>

donate-paysupport-message =
    Jeśli chcesz dokonać zwrotu, użyj polecenia /refund.

    🤓 Będziesz potrzebować ID transakcji.
    {donate-paysupport-tid-tip}

donate-refund-input-error =
    Proszę podać ID transakcji w formacie <code>/refund [id]</code>, gdzie [id] to ID transakcji, które otrzymałeś po dokonaniu darowizny.

    {donate-paysupport-tid-tip}

donate-refund-success =
    Zwrot pomyślnie przetworzony. Gwiazdki zostały zwrócone na Twoje konto w Telegramie.

donate-refund-code-not-found =
    Nie znaleziono transakcji o podanym ID. Proszę sprawdzić dane i spróbować ponownie.

donate-refund-already-refunded =
    Zwrot dla tej transakcji został już wcześniej dokonany.

donate-cancel-payment =
    😢 Darowizna anulowana.

donate-successful-payment =
    <b>🫡 Dziękuję!</b>
    Twoja darowizna została pomyślnie zrealizowana.

payment-none-error =
    błąd xz

hello-owner =
    <b>👊 Cześć, właścicielu!</b>

ping-msg =
    <b>👊 Wszystko działa!</b>

media-msg =
    <b>🫡 Fajne media <i>(chyba)</i>!</b>
