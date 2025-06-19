package com.scsa.android.haginhae;


public class Player {
    private float y;

    public Player(float screenHeight) {
        y = screenHeight - 600;  // 바 위치
    }

    public float getY() {
        return y;
    }

    public boolean isTouchWithin(float touchY) {
        return touchY >= y;  // 바보다 아래에서만 터치 가능
    }
}
