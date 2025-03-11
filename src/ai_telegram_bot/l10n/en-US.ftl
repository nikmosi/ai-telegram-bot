hello-msg =
    <b>👊 Hello!</b>
    If you want to support the author with a donation, use the following commands:

    • /donate [amount]: donate the specified number of stars (e.g., /donate 100)
    • /paysupport: assistance with payments
    • /refund: donation refund

donate-invoice-title =
    Donate to the author

donate-invoice-description =
    For an amount of {$amount ->
        [one] {$amount} star
        [few] {$amount} stars
       *[other] {$amount} stars
    }

donate-button-pay =
    Pay {$amount} XTR

donate-button-cancel =
    Cancel operation

donate-input-error =
    Please enter the amount in the format <code>/donate [NUMBER]</code>, where [NUMBER] is the donation amount, from ⭐️ 1 to ⭐️ 2500.

    Examples:
    • <code>/donate 100</code> - donate 100 ⭐️
    • <code>/donate 500</code> - donate 500 ⭐️
    • <code>/donate 1000</code> - donate 1000 ⭐️

donate-paysupport-tid-tip =
    <blockquote>You can get it after completing your donation.
    Just tap on the message <b>"You successfully sent ⭐️ .."</b> and copy the transaction ID from there.</blockquote>

donate-paysupport-message =
    If you want a refund, use the /refund command.

    🤓 You will need the transaction ID.
    {donate-paysupport-tid-tip}

donate-refund-input-error =
    Please provide the transaction ID in the format <code>/refund [id]</code>, where [id] is the transaction ID you received after making a donation.

    {donate-paysupport-tid-tip}

donate-refund-success =
    Refund successfully processed. The stars have been returned to your Telegram account.

donate-refund-code-not-found =
    Transaction with the specified ID not found. Please check the data and try again.

donate-refund-already-refunded =
    A refund for this transaction has already been issued.

donate-cancel-payment =
    😢 Donation canceled.

donate-successful-payment =
    <b>🫡 Thank you!</b>
    Your donation has been successfully processed.

payment-none-error =
    error xz

hello-owner =
    <b>👊 Hello, owner!</b>

ping-msg =
    <b>👊 Up & Running!</b>

media-msg =
    <b>🫡 Nice media <i>(I guess)</i>!</b>
