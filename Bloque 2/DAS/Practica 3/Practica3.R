libs <- c("dplyr", "lubridate")
sapply(.libs, require, character.only=TRUE)

#Ejercicio 1
estacion <- read.csv(file.choose(),sep=";")
estacion$date <- ymd(estacion$date)
dayweek<-wday(estacion$date)
estacion$dayweek<-dayweek
xdayweek <- group_by(estacion, dayweek)
xdayweek <- summarise(xdayweek, meanAvailable = mean (avg_available))
qplot(dayweek, meanAvailable, data=xdayweek, color="red", ylab="Free Bicycles",
      xlab="Days of week", xlim=c(1,7), main="Guillem de Castro. Dayweek Average", geom="line")+
  +     theme_light()+
  +     theme(plot.title = element_text(face="bold", size=22, hjust = 0.5), legend.position="none")
#Tras analizar el gráfico, comprobamos que el día de la semana con menos bicicletas disponibles es el domingo


#Ejercicio 2
xday <- group_by(estacion, date)
xday <- summarise(xday, meanAvailable = mean (avg_available)) 
day[ xday$meanAvailable == max(xday$meanAvailable), ]$date
#[1] "2014-06-12"
#El día con el mayor número de bicicletas disponibles es el 12 de junio de 2014.
xday[ xday$meanAvailable == max(xday$meanAvailable), ]
# A tibble: 1 x 2
#  date       meanAvailable
#  <date>             <dbl>
#1 2014-06-12          23.0
#Ese día hubo una media de 23 bicicletas disponibles.

lessbikes <- xday[ xday$meanAvailable == min(xday$meanAvailable), ]
lessbikes <- lessbikes[1,]
lessbikes$date
#[1] "2012-02-15"
#Uno de los días con menos bicicletas disponibles (cero) es el 15 de febrero de 2012.


#Ejercicio 3
month <- month(estacion$date)
estacion$month <- month
xmonth <- group_by(estacion, month)
xmonth <- summarise(xmonth, meanAvailable = mean (avg_available))
xmonth[ xmonth$meanAvailable == min(xmonth$meanAvailable), ]$month
#[1] 3
#El mes con el menor número de bicicletas disponibles de media es marzo.

xmonth[ xmonth$meanAvailable == min(xmonth$meanAvailable), ]
# A tibble: 1 x 2
#  month meanAvailable
#  <dbl>         <dbl>
#1     3          1.58
#Hubo una media de 1 bicicleta disponible.


#Ejercicio 4
qplot(month, meanAvailable, data=xmonth, color="red", ylab="Available Bicycles",
      +       xlab="Months", xlim=c(1,12), main="Guillem de Castro. Month Average", geom="line")+
  +     theme_light()+
  +     theme(plot.title = element_text(face="bold", size=22, hjust = 0.5), legend.position="none")
#Tras observar el gráfico creado, se concluye que en verano (de julio a septiembre) el número de bicicletas disponibles es superior al de los meses previos.


#Ejercicio 5
day <- day(estacion$date)
estacion$day <- day
estacion_marzo <- estacion[ estacion$month == 3, ]
xmarchday <- group_by(estacion_marzo, day)
xmarchday <- summarise(xmarchday, meanAvailable = mean (avg_available))
qplot(day, meanAvailable, data=xmarchday, color="red", ylab="Available Bicycles",xlab="Days", xlim=c(1,31), main="Guillem de Castro. March Average", geom="line")+
  +     theme_light()+
  +     theme(plot.title = element_text(face="bold", size=22, hjust = 0.5), legend.position="none")
#El gráfico muestra que en el periodo de Fallas (del 15 al 19 de marzo) no existen bicicletas disponibles en esa estación.
