
# Calculate Cond mean
condmean <- function(mu1,mu2,a,sig12,sig22) {
   val = mu1 + sig12%*%solve(sig22)%*%(a-mu2)
   return(val)
}

# Run imputation for a particular col
impute_col <- function(dat,v,mu1,mu2,sig12,sig22) {

	n = dim(dat)[1]
	p <- dim(dat)[2]
    sse <- 0
	  
	mu1 = rep(mu1,n)
	mu2 = matrix(rep(mu2,n),nrow=p-1,ncol=n)


    Y <- dat[,v]
    if(v==1) {
    	a <- t(dat[,2:p])
    } else if(v==p) {
    	a  <- t(dat[,1:(p-1)])
    } else {
		a1 <- matrix(dat[,1:(v-1)],nrow=n,ncol=v-1)
        a2 <- matrix(dat[,(v+1):p],nrow=n,ncol=p-v)
        a <- t(cbind(a1,a2))
    } 
    Yimp <- condmean(mu1,mu2,a,sig12,sig22) 
#	print(c("Y",Y))
#	print(c("Yimp",Yimp))
#	print(c("Baseline",rep(mu1,n)))
    sse = sse + mean((Y-Yimp)^2)
   
	sse_base = mean((Y-rep(mu1,n))^2)
 
	return(list("sse"=sse,"sse_base"=sse_base))
}
#----------End Function------------------

 sigma = matrix(c(1,-0.5,0,-0.5,2,0.5,0,0.5,3),nrow=3,ncol=3)
 n = 1000
 mu = c(0,2,-1)
 dat = mvrnorm(n,mu,sigma)


	n = dim(dat)[1]
    p = dim(dat)[2]


	Zinv <- sigma


	mu = colMeans(dat)
	sse = 0
	sse_base <- 0

    #for v = 1
	v=1
    sig12 = matrix(Zinv[1,2:p],nrow=1,ncol=p-1)
	sig22 = matrix(Zinv[2:p,2:p],nrow=p-1,ncol=p-1)
	mu1 = mu[1]	
	mu2 = matrix(mu[2:p],nrow=p-1,ncol=1)

    imp = impute_col(dat,v,mu1,mu2,sig12,sig22)
	sse = sse +imp$sse
	sse_base = sse_base + imp$sse_base


	# for 2 to p-1
    for(v in 2:(p-1)) {
		#print(c("Imputing column",v))
		sig12 = matrix(Zinv[v,c(1:(v-1),(v+1):p)],nrow=1,ncol=p-1)
		m1 = rbind(matrix(Zinv[1:(v-1),1:(v-1)],nrow=v-1,ncol=v-1),matrix(Zinv[(v+1):p,1:(v-1)],nrow=p-v,ncol=v-1))
		m2 = rbind(matrix(Zinv[1:(v-1),(v+1):p],nrow=v-1,ncol=p-v),matrix(Zinv[(v+1):p,(v+1):p],nrow=p-v,ncol=p-v))
		sig22 = cbind(m1,m2)
		mu1 = mu[v]		
		mu2 = matrix(c(mu[1:(v-1)],mu[(v+1):p]),nrow=(p-1),ncol=1)
		imp = impute_col(dat,v,mu1,mu2,sig12,sig22)
		sse = sse + imp$sse
		sse_base = sse_base + imp$sse_base
		#print(c("sse is",sse))
    }
	# for v = p
	v=p
    sig12 = matrix(Zinv[p,1:(p-1)],nrow=1,ncol=p-1)
	sig22 = matrix(Zinv[1:(p-1),1:(p-1)],nrow=p-1,ncol=p-1)
    mu1 = mu[p]
    mu2 = matrix(mu[1:(p-1)],nrow=(p-1),ncol=1)
	imp =  impute_col(dat,v,mu1,mu2,sig12,sig22)
	sse = sse + imp$sse
	sse_base = sse_base + imp$sse_base


	rmse = sqrt(sse/p)
	rmse_base = sqrt(sse_base/p)


	print(c("rmse",rmse))
	print(c("rmse_base",rmse_base))





