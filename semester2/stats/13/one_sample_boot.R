x <- c(1.9833, 1.9749, 2.0014, 1.9830, 2.0212, 2.0609, 1.9750, 1.9754, 1.9844, 1.9442)
alpha <- 0.05
t_s_samples = c()

for (i in 1:10000) {
  x_s <- sample(x, length(x), replace=TRUE)
  t_s <- (mean(x_s)-mean(x)) / (sd(x_s) / sqrt(length(x_s)))
  t_s_samples <- c(t_s_samples, t_s)
}

quantile(t_s_samples, probs=c(alpha/2, 1-alpha/2))
mean(t_s_samples < -5.9579)