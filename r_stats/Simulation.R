# Final Exam: Simulation Study - 
# Comparing Wilson Score CI with Z-CI for proportion

##############
# Setting up #
##############
# Data Simulation #
###################

set.seed(12345);
p_true = c(0.1, 0.5);
n = c(30, 50);
N_sim = 100;
alpha = 0.10

# generate random numbers
x = matrix(0, N_sim, 4);
x[, 1] = rbinom(N_sim, size = n[1], p_true[1]);
x[, 2] = rbinom(N_sim, size = n[1], p_true[2]);
x[, 3] = rbinom(N_sim, size = n[2], p_true[1]);
x[, 4] = rbinom(N_sim, size = n[2], p_true[2]);

param = matrix(0, 4, 2);
param[1, ] = c(n[1], p_true[1]);
param[2, ] = c(n[1], p_true[2]);
param[3, ] = c(n[2], p_true[1]);
param[4, ] = c(n[2], p_true[2]);

SimDat = NULL;
SimDat$n30p0.1 = x[, 1];
SimDat$n30p0.5 = x[, 2];
SimDat$n50p0.1 = x[, 3];
SimDat$n50p0.5 = x[, 4];

SimDat = as.data.frame(SimDat);
save(SimDat, file="Simulation.RData");

library(mosaic);

panel.ci = function (x, y, mu, data2, ...) {
  panel.xyplot(x, y, ...)
  good = subset(data2, upper > mu & lower < mu)
  bad = subset(data2, upper < mu | lower > mu)
  with(good, panel.arrows(lower, .index, upper, .index, angle=90, length = 0.05, ends="both"))
  with(bad, panel.arrows(lower, .index, upper, .index, angle=90, length = 0.05, ends="both", 
                         col="red", lwd=3))
  panel.abline(v=mu, lty=2)
}

plot_ci = function (df, mu, ...) {  
  space = 0.1 * (max(df$lower) - min(df$upper))
  xyplot(.index ~ mean, data=df, data2 = df, panel=panel.ci, mu = mu, 
         xlim = c(min(df$lower) - space, max(df$upper) + space), ylab = NULL)
}

# Wilson score interval with continuity correction for single proportion
CI_Proportion_Wilson_vec = function(x, n, alpha){
  phat = x/n;
  z = abs(qnorm(alpha/2));
  CI_lower = 2 * n * phat + z^2 - 1 - (z * sqrt(z^2 - 2 - (1/n) + 4 * phat * (n * (1 - phat) + 1) ));
  CI_lower = CI_lower / (2 * n + 2 * z^2);
  CI_lower = CI_lower * (phat > 0);
  CI_upper = 2 * n * phat + z^2 + 1 + (z * sqrt(z^2 + 2 - (1/n) + 4 * phat * (n * (1 - phat) - 1) ));
  CI_upper = CI_upper / (2 * n + 2 * z^2);
  CI_upper = CI_upper * (phat < 1) + phat * (phat == 1);
  result = data.frame(lower = CI_lower, mean = phat, upper = CI_upper, .index=1:length(x));
  result
};

###################
# Part (a) Plot CI
###################

CI_Wilson = CI_Proportion_Wilson_vec(SimDat[, 1], n=30, alpha=0.1);
plot_ci(CI_Wilson, 0.1);



# Wilson Score CI

result = matrix(0, 4, 2);

for (i in 1:4){
    x = SimDat[, i];
    n = param[i, 1];
    p_true = param[i, 2];
    CI_Wilson = CI_Proportion_Wilson_vec(x, n, alpha);
    result[i, 1] = sum(CI_Wilson$lower < p_true & CI_Wilson$upper > p_true) / 100;

    # Z-interval
    phat_vec = x / n;
    s_vec = sqrt(phat_vec*(1-phat_vec));
    SE_vec = s_vec/sqrt(n)
    zstar = -qnorm(alpha/2)
    lower_vec = phat_vec - zstar * SE_vec;
    upper_vec = phat_vec + zstar * SE_vec;
    result[i, 2] = sum(lower_vec < p_true & upper_vec > p_true) / 100;
}

# Result 
# Wilson Z
# [,1] [,2]
# n = 30, p = 0.1, 
#[1,] 0.97 0.77
# n = 30, p = 0.5
#[2,] 0.94 0.89
# n = 50, p = 0.1
# [3,] 0.89 0.83
# n = 50, p = 0.5
#[4,] 0.96 0.88

# z-CI
plot_ci(CI_Z, p_true);
