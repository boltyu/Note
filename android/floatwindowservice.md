# in MainActivity.java

startService(new Intent(MainActivity.this, FloatWindowService.class));

# in FloatWindowService.java

package com.light.dict;
import android.app.Service;

# in FloatWindowService class
public class FloatWindowService extends Service {
    @Override
    public void onCreate() {
        super.onCreate();

    }

    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }
}

# add permission in AndroidManifest.xml(included in '<manifest')
<uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW"/>

# and add service in AndroidManifest.xml(included in '<application')
<service android:name=".FloatWindowService"
            tools:ignore="WrongManifestParent">
</service>

#### full code in onCreate(windowmanager)
    final WindowManager windowManager;
        windowManager = (WindowManager) getSystemService(WINDOW_SERVICE);
        linearLayout = new LinearLayout(this);
        LinearLayout.LayoutParams layoutParams = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.WRAP_CONTENT, LinearLayout.LayoutParams.WRAP_CONTENT);
        linearLayout.setBackgroundColor(Color.argb(150, 0, 0, 0));
        linearLayout.setLayoutParams(layoutParams);
        btView = new Button(this);
        btView.setText("screenshot");
        btView.setBackgroundColor(Color.BLACK);
        btView.setTextColor(Color.WHITE);
        btView.setGravity(Gravity.CENTER_VERTICAL);
        btView.setLayoutParams(layoutParams);
        linearLayout.addView(btView);
        //https://stackoverflow.com/questions/46208897/android-permission-denied-for-window-type-2038-using-type-application-overlay
        int LAYOUT_FLAG;
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            LAYOUT_FLAG = WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY;
        } else {
            LAYOUT_FLAG = WindowManager.LayoutParams.TYPE_PHONE;
        }
        final WindowManager.LayoutParams params = new WindowManager.LayoutParams(
                WindowManager.LayoutParams.MATCH_PARENT,
                WindowManager.LayoutParams.WRAP_CONTENT,
                LAYOUT_FLAG,
                WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE,
                PixelFormat.TRANSLUCENT);
        params.x = 0;
        params.y = 0;
        params.gravity = Gravity.CENTER;
        windowManager.addView(linearLayout, params);

# set flowwindow moveable 
