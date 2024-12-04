hello-msg =
    <b>👊 Hei!</b>
    Jos haluat tukea tekijää lahjoituksella, käytä seuraavia komentoja:

    • /donate [määrä]: lahjoita määritelty määrä tähtiä (esim. /donate 100)
    • /paysupport: apua maksujen kanssa
    • /refund: lahjoituksen palautus

donate-invoice-title =
    Lahjoitus tekijälle

donate-invoice-description =
    Summalle {$amount ->
        [one] {$amount} tähti
        [few] {$amount} tähteä
       *[other] {$amount} tähteä
    }

donate-button-pay =
    Maksa {$amount} XTR

donate-button-cancel =
    Peru toiminto

donate-input-error =
    Kirjoita summa muodossa <code>/donate [LUKU]</code>, missä [LUKU] on lahjoituksen määrä, välillä ⭐️ 1 - ⭐️ 2500.

    Esimerkkejä:
    • <code>/donate 100</code> - lahjoita 100 ⭐️
    • <code>/donate 500</code> - lahjoita 500 ⭐️
    • <code>/donate 1000</code> - lahjoita 1000 ⭐️

donate-paysupport-tid-tip =
    <blockquote>Voit saada sen, kun lahjoitus on suoritettu.
    Napsauta viestiä <b>"Lähetit onnistuneesti ⭐️ .."</b> ja kopioi tapahtumatunnus siitä.</blockquote>

donate-paysupport-message =
    Jos haluat palauttaa lahjoituksen, käytä komentoa /refund.

    🤓 Tarvitset tapahtumatunnuksen.
    {donate-paysupport-tid-tip}

donate-refund-input-error =
    Ilmoita tapahtumatunnus muodossa <code>/refund [id]</code>, missä [id] on tunnus, jonka sait lahjoituksen jälkeen.

    {donate-paysupport-tid-tip}

donate-refund-success =
    Lahjoituksen palautus onnistui. Tähdet on palautettu Telegram-tilillesi.

donate-refund-code-not-found =
    Tapahtumaa annetulla tunnuksella ei löytynyt. Tarkista tiedot ja yritä uudelleen.

donate-refund-already-refunded =
    Tämän tapahtuman lahjoitus on jo palautettu.

donate-cancel-payment =
    😢 Lahjoitus peruttu.

donate-successful-payment =
    <b>🫡 Kiitos!</b>
    Lahjoituksesi on käsitelty onnistuneesti.

payment-none-error =
    virhe xz

hello-owner =
    <b>👊 Hei, omistaja!</b>

ping-msg =
    <b>👊 Kaikki toimii!</b>

media-msg =
    <b>🫡 Kiva media <i>(kai)</i>!</b>
