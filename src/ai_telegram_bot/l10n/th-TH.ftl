hello-msg =
    <b>👊 สวัสดี!</b>
    หากคุณต้องการสนับสนุนผู้เขียนด้วยการบริจาค โปรดใช้คำสั่งต่อไปนี้:

    • /donate [จำนวน]: บริจาคจำนวนดาวที่ระบุ (ตัวอย่าง: /donate 100)
    • /paysupport: ช่วยเหลือด้านการชำระเงิน
    • /refund: ขอคืนเงินบริจาค

donate-invoice-title =
    บริจาคให้กับผู้เขียน

donate-invoice-description =
    จำนวนเงิน {$amount ->
        [one] {$amount} ดาว
        [few] {$amount} ดวงดาว
       *[other] {$amount} ดวงดาว
    }

donate-button-pay =
    ชำระเงิน {$amount} XTR

donate-button-cancel =
    ยกเลิกการดำเนินการ

donate-input-error =
    โปรดกรอกจำนวนเงินในรูปแบบ <code>/donate [ตัวเลข]</code> โดยที่ [ตัวเลข] คือจำนวนเงินบริจาค ตั้งแต่ ⭐️ 1 ถึง ⭐️ 2500

    ตัวอย่าง:
    • <code>/donate 100</code> - บริจาค 100 ⭐️
    • <code>/donate 500</code> - บริจาค 500 ⭐️
    • <code>/donate 1000</code> - บริจาค 1000 ⭐️

donate-paysupport-tid-tip =
    <blockquote>คุณสามารถได้รับมันหลังจากที่คุณทำการบริจาคเสร็จ
    เพียงแค่คลิกที่ข้อความ <b>"คุณได้โอน ⭐️ สำเร็จ .."</b> และคัดลอก ID การทำธุรกรรมจากที่นั่น</blockquote>

donate-paysupport-message =
    หากคุณต้องการขอคืนเงิน โปรดใช้คำสั่ง /refund

    🤓 คุณจะต้องใช้ ID การทำธุรกรรม
    {donate-paysupport-tid-tip}

donate-refund-input-error =
    โปรดกรอก ID การทำธุรกรรมในรูปแบบ <code>/refund [id]</code> โดยที่ [id] คือ ID ที่คุณได้รับหลังจากการบริจาค

    {donate-paysupport-tid-tip}

donate-refund-success =
    การคืนเงินสำเร็จแล้ว ดาวที่ใช้จ่ายไปได้รับการคืนเงินในบัญชี Telegram ของคุณ

donate-refund-code-not-found =
    ไม่พบธุรกรรมที่มี ID ที่ระบุ โปรดตรวจสอบข้อมูลและลองอีกครั้ง

donate-refund-already-refunded =
    การคืนเงินสำหรับธุรกรรมนี้ได้ดำเนินการไปแล้ว

donate-cancel-payment =
    😢 การบริจาคถูกยกเลิก

donate-successful-payment =
    <b>🫡 ขอบคุณ!</b>
    การบริจาคของคุณได้รับการยอมรับเรียบร้อยแล้ว

payment-none-error =
    ข้อผิดพลาด xz

hello-owner =
    <b>👊 สวัสดีเจ้าของ!</b>

ping-msg =
    <b>👊 ระบบทำงานอยู่!</b>

media-msg =
    <b>🫡 สื่อเจ๋ง <i>(อาจจะ)</i>!</b>
