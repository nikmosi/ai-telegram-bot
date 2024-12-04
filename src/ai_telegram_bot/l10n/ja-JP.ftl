hello-msg =
    <b>👊 こんにちは!</b>
    作者を支援したい場合は、以下のコマンドを使用してください:

    • /donate [金額]: 指定された星の数を寄付する (例: /donate 100)
    • /paysupport: 支払いサポート
    • /refund: 寄付の返金

donate-invoice-title =
    作者への寄付

donate-invoice-description =
    {$amount ->
        [one] {$amount} 星
        [few] {$amount} 星
       *[other] {$amount} 星
    }

donate-button-pay =
    {$amount} XTR 支払う

donate-button-cancel =
    操作をキャンセル

donate-input-error =
    <code>/donate [数字]</code> という形式で金額を入力してください。[数字]は寄付金額で、⭐️ 1から⭐️ 2500の範囲です。

    例:
    • <code>/donate 100</code> - 100 ⭐️ 寄付
    • <code>/donate 500</code> - 500 ⭐️ 寄付
    • <code>/donate 1000</code> - 1000 ⭐️ 寄付

donate-paysupport-tid-tip =
    <blockquote>寄付が完了した後に確認できます。
    「⭐️ を正常に送信しました..」というメッセージをタップし、そこからトランザクションIDをコピーしてください。</blockquote>

donate-paysupport-message =
    返金を希望する場合は、/refund コマンドを使用してください。

    🤓 トランザクションIDが必要です。
    {donate-paysupport-tid-tip}

donate-refund-input-error =
    トランザクションIDを<code>/refund [id]</code> の形式で入力してください。[id]は寄付後に受け取ったトランザクションIDです。

    {donate-paysupport-tid-tip}

donate-refund-success =
    返金が正常に処理されました。使った星があなたのTelegramアカウントに返還されました。

donate-refund-code-not-found =
    指定されたIDのトランザクションが見つかりませんでした。情報を確認して再試行してください。

donate-refund-already-refunded =
    このトランザクションの返金はすでに処理されています。

donate-cancel-payment =
    😢 寄付がキャンセルされました。

donate-successful-payment =
    <b>🫡 ありがとうございます!</b>
    あなたの寄付は正常に処理されました。

payment-none-error =
    エラー xz

hello-owner =
    <b>👊 こんにちは、オーナー!</b>

ping-msg =
    <b>👊 正常に動作しています!</b>

media-msg =
    <b>🫡 素晴らしいメディア <i>(たぶん)</i>!</b>
