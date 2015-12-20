package com.android.test;
public class AndroidSMS4Activity extends android.app.Activity {

    public AndroidSMS4Activity()
    {
        return;
    }

    public void onCreate(android.os.Bundle p7)
    {
        super.onCreate(p7);
        this.setContentView(2130903040);
        this.sendSMS("12345678912", "hello");
        android.telephony.SmsManager.getDefault().sendTextMessage("12345678912", 0, "test", 0, 0);
        return;
    }

    public void sendSMS(String p7, String p8)
    {
        android.telephony.SmsManager.getDefault().sendTextMessage(p7, 0, p8, 0, 0);
        return;
    }
}
