#### Runs all the imputation tests

library(huge)
library(circular)  # Load the package huge

# Calculate Cond mean
condmean <- function(mu1,mu2,a,sig12,sig22) {
   val = mu1 + sig12%*%sig22%*%(a-mu2)
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
    sse = sse + mean((Y-Yimp)^2)
	#sse_base = mean((Y-rep(mu1,n))^2)
   	return(list("sse"=sse))
}
#----------End Function------------------



#######################################################################
# Decompose matrix into parts required for inference
decompose_mat <- function(mu,sigma,v) {
   
	p = dim(sigma)[1]

	if(v==1) {
    sig12 = matrix(sigma[1,2:p],nrow=1,ncol=p-1)
	sig22 = matrix(sigma[2:p,2:p],nrow=p-1,ncol=p-1)
	sig22 = solve(sig22)
	mu1 = mu[1]	
	mu2 = matrix(mu[2:p],nrow=p-1,ncol=1)
    }

    if(v %in% 2:(p-1)) {
		#print(c("Imputing column",v))
		sig12 = matrix(sigma[v,c(1:(v-1),(v+1):p)],nrow=1,ncol=p-1)
		m1 = rbind(matrix(sigma[1:(v-1),1:(v-1)],nrow=v-1,ncol=v-1),matrix(sigma[(v+1):p,1:(v-1)],nrow=p-v,ncol=v-1))
		m2 = rbind(matrix(sigma[1:(v-1),(v+1):p],nrow=v-1,ncol=p-v),matrix(sigma[(v+1):p,(v+1):p],nrow=p-v,ncol=p-v))
		sig22 = cbind(m1,m2)
		sig22 = solve(sig22)
		mu1 = mu[v]		
		mu2 = matrix(c(mu[1:(v-1)],mu[(v+1):p]),nrow=(p-1),ncol=1)
    }

	if(v==p) {
      sig12 = matrix(sigma[p,1:(p-1)],nrow=1,ncol=p-1)
	  sig22 = matrix(sigma[1:(p-1),1:(p-1)],nrow=p-1,ncol=p-1)
	  sig22 = solve(sig22)
      mu1 = mu[p]
      mu2 = matrix(mu[1:(p-1)],nrow=(p-1),ncol=1)
    }

	return(list("mu1"=mu1,"mu2"=mu2,"sig12"=sig12,"sig22"=sig22))
}
#------ End Function -------------------------------------------


#####################################################################
### Log likelihood and Imputation Testing for a particular Dataset

test_glasso <- function(trainf,testf,dtype,metric,substr){
train <- read.csv(trainf,header=FALSE)
train<-as.matrix(train)
test <- read.csv(testf,header=FALSE)
test<-as.matrix(test)
class(train) <- "numeric"
class(test) <- "numeric"

# split substr to get temp and iid
parts <- unlist(strsplit(substr,"\\_"))
temp <- parts[1]
iid <- parts[2]

if(dtype=='angular') {
  train <- rad(train)
  for (j in 1:(dim(train)[2])) {
    train[,j] <- circular(train[,j] - mean.circular(train[,j]))
  }
  # project everything to -pi,pi
  train <- circular(train + pi,modulo="2pi")-pi
  train <- as.matrix(train)

  test <- rad(test)
  for (j in 1:(dim(test)[2])) {
    test[,j] <- circular(test[,j] - mean.circular(test[,j]))
  }
  # project everything to -pi,pi
  test <- circular(test + pi,modulo="2pi")-pi
  test <- as.matrix(test)
}

# Relabel and transform test
test.ggm <- test # relabeling test
test.npn <- huge.npn(test)

# Relabel and transform train
train.ggm <- train
train.npn <- huge.npn(train) # Nonparanormal


# Find solution path using Glasso
out.ggm <- huge(train.ggm,method="glasso",nlambda=50) 
out.ggm[["trans"]] <- "ggm"
out.npn <- huge(train.npn,method="glasso",nlambda=50)
out.npn[["trans"]] <- "npn"


####### Select models from solution path using different criteria
models <- list()

#### Use Stars
#model = huge.select(out.ggm,criterion="stars")  
#models[[paste(model$method,model$trans,model$criterion,sep="_")]] = model

#model = huge.select(out.npn,criterion="stars")
#models[[paste(model$method,model$trans,model$criterion,sep="_")]] = model

#### Use EBIC
model <- huge.select(out.ggm,criterion="ebic")
models[[paste(model$method,model$trans,model$criterion,sep="_")]] = model

model <- huge.select(out.npn,criterion="ebic")
models[[paste(model$method,model$trans,model$criterion,sep="_")]] = model


#### Use RIC
model <- huge.select(out.ggm,criterion="ric")
models[[paste(model$method,model$trans,model$criterion,sep="_")]] = model

model <- huge.select(out.npn,criterion="ric")
models[[paste(model$method,model$trans,model$criterion,sep="_")]] = model

#######################################################################
# Run log likelihood 

if(metric=='loglik') {
  sink("loglik.out",append=TRUE)

  if(model$trans=="npn") {
	test <- test.npn
  } else {
    test <- test.ggm
  }

  S_test <- cor(test)
  S_train <- cor(train)

  for( mname in  names(models)){
    text = paste(substr,dtype,mname,metric,sep="_")

	model <- models[[mname]]
	
	if("opt.icov" %in% names(model)){
    	Z <- model$opt.icov
    } else {
		Z <- solve(diag(diag(cor(model$data))))
    } 

	Z = as.matrix(Z)
	ll_train = log(det(Z)) - sum(diag(S_train%*%Z)) 
	ll_test = log(det(Z)) - sum(diag(S_test%*%Z)) 

    cat(text)
    cat("\n")		
    cat(paste("Train:",ll_train))
    cat("\t")		
    cat(paste("Test:",ll_test))
	cat("\n\n")
  }
  sink()
}

########################################################################
# Run Imputation test

if(metric=="impute") {

	sink("impute.R",append=TRUE)
	sink()

	n = dim(test)[1]
    p = dim(test)[2]

	test <- as.matrix(test.npn)

	for(mname in names(models))	 {
       model = models[[mname]]
	   if("opt.icov" %in% names(model)){
	        Z <- model$opt.icov
            Zinv <- solve(Z)
    	} else {
        Zinv <- diag(diag(cor(model$data)))
    	} 


	mu = colMeans(test)
	sse = 0
	sse_base <- 0

	## Run Main algo

	for(v in 1:p) {
  		d <- decompose_mat(mu,Zinv,v)
		imp =  impute_col(test,v,d$mu1,d$mu2,d$sig12,d$sig22)
		sse = sse + imp$sse
		sse_base = sse_base + imp$sse_base
	}

	rmse = sqrt(sse/p)
	model[['rmse']] = rmse


	## Run baseline 1 : Identity matrix
	sigma <- diag(p)
	sse = 0
	for(v in 1:p) {
  		d <- decompose_mat(mu,sigma,v)
		imp =  impute_col(test,v,d$mu1,d$mu2,d$sig12,d$sig22)
		sse = sse + imp$sse
	}
	rmse = sqrt(sse/p)
	model[['rmse_base1']] = rmse



	## Run baseline 2 : Full covariance matrix
	sigma <- cov(model$data)
	sse = 0

	for(v in 1:p) {
  		d <- decompose_mat(mu,sigma,v)
		imp =  impute_col(test,v,d$mu1,d$mu2,d$sig12,d$sig22)
		sse = sse + imp$sse
	}
	rmse = sqrt(sse/p)
	model[['rmse_base2']] = rmse

	print(c("rmse",model$criterion,model$trans,model[['rmse']]))
	print(c("rmse_base1",model$criterion,model$trans,model[['rmse_base1']]))
	print(c("rmse_base2",model$criterion,model$trans,model[['rmse_base2']]))
    }
}
return(models)
}

#---------------End Function------------------





######################################################################
# Loglikelihood tests

# delete previous results
#sink("loglik.out")
#sink()
models = test_glasso('data/distances174_300K_train.dat','data/distances174_300K_test.dat','dist','loglik','300K_noniid')

#### Subsample
#models = test_glasso('data/distances174_sub_300K_train.dat','data/distances174_sub_300K_test.dat','dist','loglik','300K_iid')

#### Whole theta tau
i#models = test_glasso('data/theta44tau43_300_5000_train.dat','data/theta44tau43_300_5000_test.dat','angular','loglik','300K_noniid')

##### ThetaTau subsampled
#models = test_glasso('data/tt_300K_sub_train.dat','data/tt_300K_sub_test.dat','angular','loglik','300K_iid')

#######################################################################
# 350 K

#models = test_glasso('data/distances174_350K_train.dat','data/distances174_350K_test.dat','dist','loglik','350K_noniid')

#### Subsample
#models = test_glasso('data/distances174_sub_350K_train.dat','data/distances174_sub_350K_test.dat','dist','loglik','350K_iid')

#### Whole theta tau
#models = test_glasso('data/theta44tau43_350_5000_train.dat','data/theta44tau43_350_5000_test.dat','angular','loglik','350K_noniid')

##### ThetaTau subsampled
#models = test_glasso('data/tt_350K_sub_train.dat','data/tt_350K_sub_test.dat','angular','loglik','350K_iid')


#####################################################################
# Imputation tests
sink("impute.out")
sink()

sink("impute.out",append=TRUE)
cat(paste("Dtype","Temp","IID/Non-IID","Transform","M.select","RMSE","RMSE_base1","RMSE_base2",sep=","))
cat('\n')


#models = test_glasso('data/distances174_300K_train.dat','data/distances174_300K_test.dat','dist','impute','300K_noniid')

#### Subsample
#models = test_glasso('data/distances174_sub_300K_train.dat','data/distances174_sub_300K_test.dat','dist','impute','300K_iid')

#### Whole theta tau
#models = test_glasso('data/theta44tau43_300_5000_train.dat','data/theta44tau43_300_5000_test.dat','angular','impute','300K_noniid')

##### ThetaTau subsampled
#models = test_glasso('data/tt_300K_sub_train.dat','data/tt_300K_sub_test.dat','angular','impute','300K_iid')

#######################################################################
# 350 K

#models = test_glasso('data/distances174_350K_train.dat','data/distances174_350K_test.dat','dist','impute','350K_noniid')

#### Subsample
#models = test_glasso('data/distances174_sub_350K_train.dat','data/distances174_sub_350K_test.dat','dist','impute','350K_iid')

#### Whole theta tau
#models = test_glasso('data/theta44tau43_350_5000_train.dat','data/theta44tau43_350_5000_test.dat','angular','impute','350K_noniid')

##### ThetaTau subsampled
#models = test_glasso('data/tt_350K_sub_train.dat','data/tt_350K_sub_test.dat','angular','impute','350K_iid')


sink()




