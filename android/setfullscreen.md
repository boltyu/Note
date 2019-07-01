<<<<<<< HEAD
# in MainActivity.java , remove title bar
    getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
                    WindowManager.LayoutParams.FLAG_FULLSCREEN);
# in AndroidMainfest.xml , remove action bar
    <application
        android:theme="@style/Theme.AppCompat.Light.NoActionBar"    
=======
# in MainActivity.java 
    getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
                        WindowManager.LayoutParams.FLAG_FULLSCREEN);    // remove title bar
# in AndroidMainfest.xml
    <application
        android:theme="@style/Theme.AppCompat.Light.NoActionBar"        // remove action bar
>>>>>>> 747a0876cc67c8be45b1b7c3ff93dde5bd379e91
        ...                                                             

