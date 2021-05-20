x <- c(1.9833, 1.9749, 2.0014, 1.9830, 2.0212, 2.0609, 1.9750, 1.9754, 1.9844, 1.9442)
y <- c(2.0752, 2.2755, 2.0935, 2.1227, 2.0424, 2.1561, 2.1400, 2.0885, 2.0401, 1.9832)

s_d <- sqrt(var(x)/length(x) + var(y)/length(y))
t_d <- (mean(x) - mean(y)) / s_d; t_d;

alpha <- 0.05; t_d_s_samples = c();x
for (i in 1:10000) {
  x_s <- sample(x, length(x), replace=TRUE)
  y_s <- sample(y, length(y), replace=TRUE)
  s_d_s <- sqrt(var(x_s)/length(x) + var(y_s)/length(y))
  t_d_s <- ( (mean(x_s)-mean(y_s)) - (mean(x)-mean(y)) ) / s_d_s
  t_d_s_samples <- c(t_d_s_samples, t_d_s)
}
quantile(t_d_s_samples, probs=c(alpha/2, 1-alpha/2))
mean(t_d_s_samples < t_d)
