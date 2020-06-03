package com.tfg.sergisanz.ejercicio3;


import android.graphics.Path;
import android.view.View;
import java.util.Random;
import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.util.AttributeSet;
import android.view.MotionEvent;


public class myView extends View{
    // Generador de numeros aleatorios
    Random random = new Random();
    // Almacena las propiedades graficas de dibujo de la linea
    Paint paint = new Paint();
    // Almacenan la posicion inicial posY final de la linea
    float posX, posY;
    // Almacena el color con el que se va a dibujar la linea actual
    int color = Color.BLACK;
    String accion;
    Path path = new Path();

    public myView(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    @Override
    public boolean onTouchEvent(MotionEvent event) {
        posX = event.getX();
        posY = event.getY();
        switch(event.getAction()) {
            case MotionEvent.ACTION_DOWN :
                path.reset();
                this.color = Color.rgb(random.nextInt(255), random.nextInt(255), random.nextInt(255));
                accion = "down";
                break;

            case MotionEvent.ACTION_MOVE :
                accion = "move";
                break;

            case MotionEvent.ACTION_UP :
                break;
        }
        this.invalidate();
        return true;
    }
    @Override
    protected void onDraw(Canvas canvas) {
        paint.setAntiAlias(true);
        paint.setStrokeWidth(6f);
        //paint.setColor(Color.BLACK);
        paint.setStyle(Paint.Style.STROKE);
        paint.setStrokeJoin(Paint.Join.ROUND);
        // Establezco el color con el que se va a dibujar la lonea en curso
        paint.setColor(this.color);
        // Dibujo la linea
        if(accion == "down") path.moveTo(posX, posY);
        if(accion == "move") path.lineTo(posX, posY);
        canvas.drawPath(path, paint);
    }
}