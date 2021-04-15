par(mfrow=c(5, 1))
for (n in c(10, 20, 100, 500, 10000)) {
    norm_samples <- rnorm(n, mean=50)    
    hist(norm_samples, freq=F)
    curve(dnorm(x, mean=50), col='red', add=T)
}