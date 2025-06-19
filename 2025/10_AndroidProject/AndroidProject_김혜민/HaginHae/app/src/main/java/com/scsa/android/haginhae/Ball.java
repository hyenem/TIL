package com.scsa.android.haginhae;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;

public class Ball {
    private float x, y, radius;
    private float speedX = 0, speedY = 0;
    private float gravity = 0.6f;
    private float bouncePower = -35f;
    private int screenWidth, screenHeight;
    private Bitmap image;
    private int bounceCount = 0;



    public Ball(Context context, float x, float y, float radius, int screenWidth, int screenHeight) {
        this.x = x;
        this.y = y;
        this.radius = radius;
        this.screenWidth = screenWidth;
        this.screenHeight = screenHeight;

        // 배구공 이미지 로딩
        image = BitmapFactory.decodeResource(context.getResources(), R.drawable.volleyball);
        image = Bitmap.createScaledBitmap(image, (int)(radius * 2), (int)(radius * 2), true);
    }



    public void update() {
        speedY += gravity;
        x += speedX;
        y += speedY;

        // 좌우 벽 반사
        if (x - radius <= 0 || x + radius >= screenWidth) {
            speedX *= -1;
        }
    }

    public void bounce(float touchX) {
        speedY = bouncePower;

        // 터치 위치에 따라 좌우 방향 튕기기 조절
        float centerDiff = (touchX - x) / 50f;
        speedX += centerDiff;


        bounceCount++;
        gravity += 0.05f;      // 중력 증가 = 점점 빨라짐
        bouncePower -= 0.5f;   // 반발력도 점점 더 강하게 (공 더 튀게)
    }


    public boolean isOutOfScreen() {
        return y - radius > screenHeight;
    }

    // Getter
    public float getX() { return x; }
    public float getY() { return y; }
    public float getRadius() { return radius; }

    public boolean isTouchingBall(float touchX, float touchY) {
        float dx = touchX - x;
        float dy = touchY - y;
        float distanceSquared = dx * dx + dy * dy;
        return distanceSquared <= radius * radius;
    }

    public int getBounceCount() {
        return bounceCount;
    }

    public Bitmap getImage() {
        return image;
    }


}


