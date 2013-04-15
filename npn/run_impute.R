#### Runs all the imputation tests

library(huge)
library(circular)  # Load the package huge

test_glasso <- function(trainf,testf,dtype,metric,substr){
train <- read.csv(trainf,header=FALSE)
train<-as.matrix(train)
test <- read.csv(testf,header=FALSE)
test<-as.matrix(test)

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

train.npn = huge.npn(train) # Nonparanormal
out.ggm = huge(train,method="glasso",nlambda=50) # Estimate the solution path
out.ggm[["trans"]] = "ggm"
out.npn = huge(train.npn,method="glasso",nlambda=50)
out.npn[["trans"]] = "npn"


####### The models
models = list()
model = huge.select(out.ggm,criterion="stars")  
models[[paste(model$method,model$trans,model$criterion,sep="_")]] = model

model = huge.select(out.npn,criterion="stars")
models[[paste(model$method,model$trans,model$criterion,sep="_")]] = model

model = huge.select(out.ggm,criterion="ebic")
models[[paste(model$method,model$trans,model$criterion,sep="_")]] = model

model = huge.select(out.npn,criterion="ebic")
models[[paste(model$method,model$trans,model$criterion,sep="_")]] = model

model = huge.select(out.ggm,criterion="ric") # Select the graph using RIC
models[[paste(model$method,model$trans,model$criterion,sep="_")]] = model

model = huge.select(out.npn,criterion="ric")
models[[paste(model$method,model$trans,model$criterion,sep="_")]] = model

if(metric=='loglik') {
  sink("loglik.out",append=TRUE)
  S_test <- cov(test)
  S_train <- cov(train)

  for( mname in  names(models)){
    text = paste(substr,dtype,mname,metric,sep="_")

	model = models[[mname]]
  
	if("opt.icov" %in% names(model)){
    	Z <- model$opt.icov
    } else {
		Z <- solve(diag(diag(cov(model$data))))
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

if(metric=="impute") {

	sink("impute.R",append=TRUE)
	sink()

	n,p = dim(s)

	for(mname in names(models))	 {
       model = models[[mname]]

       

    }



}


return(models)
}

#######################################################################
# 300 K

#run_ggm_split('data/X_2000_300K.dat','300_dist2000',5)

###### Distances whole trajectory
#run_ggm('data/distances174_300K.dat','300_dist2000')
#test_glasso('data/distances174_300K_train.dat','data/distances174_300K_test.dat','dist','loglik','300K_noniid')

#### Distances Subsampled trajectory
#run_ggm('data/distances174_sub_300K.dat','300_sub')
#run_ggm_glasso('data/distances174_sub_300K.dat','300_glasso_sub')

###### Thetatau whole
#run_ggm_angles('data/theta44tau43_300_5000.dat','tt_300K_5000')
#run_ggm_angles_glasso('data/theta44tau43_300_5000.dat','tt_glasso_300K_5000')

##### ThetaTau subsampled
#run_ggm_angles('data/tt_300K_sub.dat','tt_300K_sub')
#run_ggm_angles_glasso('data/tt_300K_sub.dat','tt_glasso_300K_sub')

#######################################################################
# 350 K

#run_ggm_split('data/X_2000_350K.dat','350_dist2000',5)

###### Distances whole trajectory
#run_ggm('data/distances174_350K.dat','350_dist2000')
#run_ggm_glasso('data/distances174_350K.dat','350_glasso_dist2000')

#### Distances Subsampled trajectory
#run_ggm('data/distances174_sub_350K.dat','350_sub')
#run_ggm_glasso('data/distances174_sub_350K.dat','350_glasso_sub')

###### Thetatau whole
#run_ggm_angles('data/theta44tau43_300_5000.dat','tt_350K_5000')
#run_ggm_angles_glasso('data/theta44tau43_300_5000.dat','tt_glasso_350K_5000')

##### ThetaTau subsampled
#run_ggm_angles('data/tt_350K_sub.dat','tt_350K_sub')
#run_ggm_angles_glasso('data/tt_350K_sub.dat','tt_glasso_350K_sub')



######################################################################
# File handling and prelims

# delete previous results
sink("loglik.out")
sink()
sink("impute.out")
sink()

models = test_glasso('data/distances174_300K_train.dat','data/distances174_300K_test.dat','dist','loglik','300K_noniid')

#### Subsample
models = test_glasso('data/distances174_sub_300K_train.dat','data/distances174_sub_300K_test.dat','dist','loglik','300K_iid')

#### Whole theta tau
models = test_glasso('data/theta44tau43_300_5000_train.dat','data/theta44tau43_300_5000_test.dat','angles','loglik','300K_noniid')

##### ThetaTau subsampled
models = test_glasso('data/tt_300K_sub_train.dat','data/tt_300K_sub_test.dat','angles','loglik','300K_iid')

#######################################################################
# 350 K

models = test_glasso('data/distances174_350K_train.dat','data/distances174_350K_test.dat','dist','loglik','350K_noniid')

#### Subsample
models = test_glasso('data/distances174_sub_350K_train.dat','data/distances174_sub_350K_test.dat','dist','loglik','350K_iid')

#### Whole theta tau
models = test_glasso('data/theta44tau43_350_5000_train.dat','theta44tau43_350_5000_test.dat','angles','loglik','350K_noniid')

##### ThetaTau subsampled
models = test_glasso('data/tt_350K_sub_train.dat','data/tt_350K_sub_test.dat','angles','loglik','350K_iid')




