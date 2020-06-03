OzoneDiscretized<-table(discretize(AirQuality$Ozone, method = "interval",categories = 5,labels = c("bin1","bin2","bin3","bin4","bin5")), useNA = "always")

SolarDiscretized<-table(discretize(AirQuality$Solar.R , method = "interval",categories = 4,labels = c("bin1","bin2","bin3","bin4")), useNA = "always")

titanic[,6] <- 0

titanic[which(titanic[,1] == "Crew", arr.ind = TRUE), 6] <- 4
titanic[which(titanic[,1] == "1st", arr.ind = TRUE), 6] <- 3
titanic[which(titanic[,1] == "2nd", arr.ind = TRUE), 6] <- 2
titanic[which(titanic[,1] == "3rd", arr.ind = TRUE), 6] <- 1





