# in MainActivity.java 
    getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
                        WindowManager.LayoutParams.FLAG_FULLSCREEN);    // remove title bar
# in AndroidMainfest.xml
    <application
        android:theme="@style/Theme.AppCompat.Light.NoActionBar"        // remove action bar
        ...                                                             

# set screen landscape
    in <application
        <activity
           android:screenOrientation="landscape"