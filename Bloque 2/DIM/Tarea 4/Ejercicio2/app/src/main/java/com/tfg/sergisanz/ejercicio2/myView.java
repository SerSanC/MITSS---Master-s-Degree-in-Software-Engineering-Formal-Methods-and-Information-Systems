package com.tfg.sergisanz.ejercicio2;

import android.view.MotionEvent;
import android.view.View;
import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.util.AttributeSet;
import android.view.View;

import java.lang.reflect.Array;
import java.util.ArrayList;
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
    //almaceno las coordenadas en distintas listas
    ArrayList<Float> listPrevX = new ArrayList<Float>();
    ArrayList<Float> listPrevY = new ArrayList<Float>();
    ArrayList<Float> listnewX = new ArrayList<Float>();
    ArrayList<Float> listNewY = new ArrayList<Float>();
    ArrayList<Integer> listColor = new ArrayList<Integer>();

    public myView(Context context, AttributeSet attrs){
        super(context,attrs);
        paint.setAntiAlias(true);
        paint.setStrokeWidth(6f);
        paint.setColor(Color.BLACK);
        paint.setStyle(Paint.Style.STROKE);
        paint.setStrokeJoin(Paint.Join.ROUND);
    }
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
                //Generamos el color aleatorio y lo añadimos a una lista
                this.color = Color.rgb(rdm.nextInt(255),rdm.nextInt(255),rdm.nextInt(255));
                listColor.add(this.color);
                break;
            case MotionEvent.ACTION_UP:

                listPrevX.add(prevX);
                listPrevY.add(prevY);
                listnewX.add(newX);
                listNewY.add(newY);
                break;

        }


        return true;
    }
    @Override
    protected void onDraw(Canvas canvas) {
        // Establezco el color con el que se va a dibujar la linea en curso
        paint.setColor(this.color);
        canvas.drawLine(this.prevX, this.prevY, this.newX,
                this.newY, this.paint);
        // Dibujo la linea en curso
        if (listPrevY.size() > 0) {
            for (int i = 0; i < listPrevY.size(); i++) {
                paint.setColor(listColor.get(i));
                canvas.drawLine(listPrevX.get(i), listPrevY.get(i), listnewX.get(i),
                        listNewY.get(i), this.paint);

            }
        }
    }
}


