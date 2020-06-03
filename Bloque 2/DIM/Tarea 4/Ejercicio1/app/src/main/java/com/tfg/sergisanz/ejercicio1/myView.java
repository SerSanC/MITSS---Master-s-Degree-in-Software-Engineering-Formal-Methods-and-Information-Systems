package com.tfg.sergisanz.ejercicio1;

import android.view.MotionEvent;
import android.view.View;
import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.util.AttributeSet;
import android.view.View;

import java.util.Random;

public class myView extends View {

    // Generador de numeros aleatorios
    Random rdm = new Random();
    // Almacena las propiedades graficas de dibujo de la linea
    Paint paint = new Paint();
    // Almacenan la posicion inicial y final de la linea
    float prevX, prevY, newX, newY;
    // Almacena el color con el que se va a dibujar la linea actual
    int color = Color.BLACK;


    public myView(Context context, AttributeSet attrs){
        super(context,attrs);
        paint.setAntiAlias(true);
        paint.setStrokeWidth(6f);
        paint.setColor(Color.BLACK);
        paint.setStyle(Paint.Style.STROKE);
        paint.setStrokeJoin(Paint.Join.ROUND);
        System.out.println("Estoy en el constructor");
    }
    int cont = 0;
    @Override
    public boolean onTouchEvent(MotionEvent event) {
        // Procesar evento
        switch (event.getActionMasked()){
            case MotionEvent.ACTION_MOVE:

                newX = event.getX();
                newY = event.getY();
                this.invalidate();
                break;
            case MotionEvent.ACTION_DOWN:

                prevX = event.getX();
                prevY = event.getY();
                break;
            case MotionEvent.ACTION_UP:

                newX = -1;
                newY = -1;
                prevY = -1;
                prevX = -1;
                break;

        }

        return true;
    }
    @Override
    protected void onDraw(Canvas canvas)
    {
        //System.out.println(rdm.nextInt());
        // Establezco el color con el que se va a dibujar la linea en curso
        paint.setColor(rdm.nextInt());
        // Dibujo la linea en curso
        canvas.drawLine(this.prevX, this.prevY, this.newX,
                this.newY, this.paint);
    }
}


