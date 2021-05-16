data(iris)
str(iris)

par(mfrow=c(1,1))
hist(iris$Sepal.Width, breaks=50)
boxplot(iris$Sepal.Width, xlab="Sepal Width")

set1 = iris$Sepal.Width [iris$Species == "setosa"]
set2 = iris$Sepal.Width[iris$Species == "virginica"]
set3 = iris$Sepal.Width[iris$Species == "versicolor"]


boxplot(set1, set2, set3, 
        names=c("setosa", "virginica", "versicolor"), 
        ylab="Sepal Width")

