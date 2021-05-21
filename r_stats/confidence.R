setwd("~/cs152/python-linear-algebra/r_stats")

# why normal, not uniform
x <- seq(-4,4,by=0.1)
# normal density curve 
plot(x, dnorm(x), type="l", lty=1)
# t-distri with degree of freedom
lines(x,dt(x,1), col="yellow")
lines(x,dt(x,5), col="red")
lines(x,dt(x,10), col="orange")

# construct CI
#t-based confidence interval
n <- 10
alpha <- 0.05
x <- rnorm(n,0,1) #iid sample from N(0,1)
c(mean(x) - qt(1-alpha/2,n-1)*sd(x)/sqrt(n),mean(x) + qt(1-alpha/2,n-1)*sd(x)/sqrt(n))

#check coverage rate
M <- 1000
CI_matrix <- matrix(0,nrow=M,ncol=2)
for(i in 1:M)
{
  x <- rnorm(n,0,1) #iid sample from N(0,1)
  CI_matrix[i,] <- c(mean(x) - qt(1-alpha/2,n-1)*sd(x)/sqrt(n),mean(x) + qt(1-alpha/2,n-1)*sd(x)/sqrt(n))
}

mean(CI_matrix[,1]<=0 & CI_matrix[,2]>=0) #coverage rate

a = acos(16/sqrt(826))

