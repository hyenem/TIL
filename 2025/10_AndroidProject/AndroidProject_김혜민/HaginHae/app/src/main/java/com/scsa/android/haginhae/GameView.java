package com.scsa.android.haginhae;

import android.app.Activity;
import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.view.MotionEvent;
import android.view.View;

public class GameView extends View {

    private Ball ball;
    private Player player;
    private Paint paint;

    private boolean isGameOver = false;
    private Context context;

    public GameView(Context context, int screenWidth, int screenHeight) {
        super(context);
        this.context = context;

        ball = new Ball(context, screenWidth / 2f, 100, 50, screenWidth, screenHeight);
        player = new Player(screenHeight);
        paint = new Paint();

        Runnable loop = new Runnable() {
            @Override
            public void run() {
                invalidate();
                postDelayed(this, 16);
            }
        };
        post(loop);
    }

    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);

        if (!isGameOver) {
            ball.update();
        }

        // 배경
        canvas.drawColor(Color.WHITE);

        // 공
        canvas.drawBitmap(
                ball.getImage(),
                ball.getX() - ball.getRadius(),  // 중심 정렬
                ball.getY() - ball.getRadius(),
                paint
        );
        // 바
        paint.setColor(Color.GRAY);
        canvas.drawRect(0, player.getY(), getWidth(), player.getY() + 10, paint);
        // 점수 표시
        paint.setColor(Color.BLACK);
        paint.setTextSize(50f);
        paint.setTextAlign(Paint.Align.LEFT);
        canvas.drawText("Bounce: " + ball.getBounceCount(), 50, 100, paint);

        // "TOUCH" 텍스트
        paint.setColor(Color.LTGRAY);
        paint.setTextSize(40f);
        paint.setTextAlign(Paint.Align.CENTER);
        canvas.drawText("TOUCH!", getWidth() / 2f, player.getY() + 80, paint);

        // GameOver
        if (ball.isOutOfScreen()) {
            isGameOver = true;

            paint.setColor(Color.RED);
            paint.setTextSize(100f);
            paint.setTextAlign(Paint.Align.CENTER);
            canvas.drawText("Game Over", getWidth() / 2f, getHeight() / 2f - 100, paint);

            // 버튼
            paint.setColor(Color.BLACK);
            paint.setTextSize(60f);
            canvas.drawText("▶ 다시 시작", getWidth() / 2f, getHeight() / 2f + 20, paint);
            canvas.drawText("◀ 뒤로 가기", getWidth() / 2f, getHeight() / 2f + 120, paint);
        }
    }

    @Override
    public boolean onTouchEvent(MotionEvent event) {
        float x = event.getX();
        float y = event.getY();

        if (!isGameOver && player.isTouchWithin(y)) {
            if (ball.isTouchingBall(x, y)) {
                ball.bounce(x);
            }
        } else if (isGameOver) {
            float centerX = getWidth() / 2f;

            if (y > getHeight() / 2f && y < getHeight() / 2f + 60) {
                // ▶ 다시 시작
                resetGame();
            } else if (y > getHeight() / 2f + 100 && y < getHeight() / 2f + 160) {
                // ◀ 뒤로 가기
                if (context instanceof Activity) {
                    ((Activity) context).finish();
                }
            }
        }

        return true;
    }


    private void resetGame() {
        ball = new Ball(context, getWidth() / 2f, 100, 50, getWidth(), getHeight());
        isGameOver = false;
    }
}
