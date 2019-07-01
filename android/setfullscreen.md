# in MainActivity.java , remove title bar
    getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
                    WindowManager.LayoutParams.FLAG_FULLSCREEN);
# in AndroidMainfest.xml , remove action bar
    <application
        android:theme="@style/Theme.AppCompat.Light.NoActionBar"    
        ...                                                             

