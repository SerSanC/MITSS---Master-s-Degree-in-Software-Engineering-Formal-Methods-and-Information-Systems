.lib<- c("ggplot2","gstat","hydroGOF","rpart","rpart.plot","nnet")
.inst <- .lib %in% installed.packages()
if (length(.lib[!.inst])>0) install.packages(.lib[!.inst])
lapply(.lib, require, character.only=TRUE)



#Ejercicio1
autoColumns = c("mpg","cyl","disp","hp","wt","acc","myear","orig","carname")
car <- read.table("./auto.txt",header=F, col.name = autoColumns)

car$cyl <- as.factor(car$cyl)
car$myear <- as.factor(car$myear)
car$orig <- as.factor(car$orig)
car <- car[,1:8]

#Ejercicio 2 
car <- na.omit(car)

#Ejercicio 3
set.seed(800)
samp_size <- floor(0.75*nrow(car))
train_ind <- sample(seq_len(nrow(car)), size = samp_size)
train <- car[train_ind, ]
test <- car[-train_ind, ]

#Ejercicio 4
linearmodel <- lm(mpg~cyl+disp+hp+wt+acc+myear+orig,train)
regressiontree <- rpart(formula = mpg~cyl+disp+hp+wt+acc+myear+orig, data = train, method = "anova")
neuralnetwork <- nnet(mpg~cyl+disp+hp+wt+acc+myear+orig, data = train, skip = TRUE, linout = TRUE, size = 12)

#Ejercicio 5
summary(linearmodel)
summary(regressiontree)
summary(neuralnetwork)

rpart.plot(regressiontree)
prediction <- predict(neuralnetwork)
plot(prediction)
plot(linearmodel)

##Cual es menos informativo?
## La red neuronal debido a su complejidad es el que menos información aporta


#Ejercicio 6 
printcp(regressiontree)
plotcp(regressiontree)

tree_pruned <- prune(regressiontree,cp = 0.05 )
rpart.plot(tree_pruned)

#Ejercicio 7 
prediccionLm=predict(linearmodel, train)
#Hare uso del pruned tree con el fin de evitar overfitting en el test data.
prediccionRegTree=predict(tree_pruned, train)
prediccionNeuralNet=predict(neuralnetwork, train)

maeTrainingDataLm = mae(train$mpg, prediccionLm)
maeTrainingDataRegTree = mae(train$mpg, prediccionRegTree)
maeTrainingDataNeuralNet= mae(train$mpg, as.vector(prediccionNeuralNet))

rmseTrainingDataLm = rmse(train$mpg, prediccionLm)
rmseTrainingDataRegTree = rmse(train$mpg, prediccionRegTree)
rmseTrainingDataNeuralNet= rmse(train$mpg, as.vector(prediccionNeuralNet))

resultadosTrainingData = data.frame(MAE=c(maeTrainingDataLm, maeTrainingDataRegTree, maeTrainingDataNeuralNet), RMSE=c(rmseTrainingDataLm,rmseTrainingDataRegTree,rmseTrainingDataNeuralNet ))


modelos = c("lm", "regTree", "NeuralNetwork")
resultadosTrainingData=cbind(modelos, resultadosTrainingData)
resultadosTrainingData


#Ejercicio 8 


prediccionLm=predict(linearmodel, test)
#Hare uso del pruned tree con el fin de evitar overfitting en el test data.
prediccionRegTree=predict(tree_pruned, test)
prediccionNeuralNet=predict(neuralnetwork, test)


maeTestDataLm = mae(test$mpg, prediccionLm)
maeTestDataRegTree = mae(test$mpg, prediccionRegTree)
maeTestDataNeuralNet= mae(test$mpg, as.vector(prediccionNeuralNet))


rmseTestDataLm = rmse(test$mpg, prediccionLm)
rmseTestDataRegTree = rmse(test$mpg, prediccionRegTree)
rmseTestDataNeuralNet= rmse(test$mpg, as.vector(prediccionNeuralNet))


resultadosTestData = data.frame(MAE=c(maeTestDataLm, maeTestDataRegTree, maeTestDataNeuralNet), RMSE=c(rmseTestDataLm,rmseTestDataRegTree,rmseTestDataNeuralNet))                              


resultadosTestData=cbind(modelos, resultadosTestData)
resultadosTestData


