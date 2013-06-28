library(huge)
library(circular)  # Load the package huge
library(mclust)
library(mix)


#####################################################################
### Log likelihood and Imputation Testing for a particular Dataset

mixmodel <- function(trainf,testf,dtype,metric,substr){
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

# Find Mixture model 

####### Run GMM 
models <- list()

S <- sample(1:nrow(train),size=100)
ggm <- Mclust(train.ggm,initialization=list(subset=S),modelNames=c('VVI','VEI'))
models$ggm <- ggm

ggm_f2 <- Mclust(train.ggm[,1:2],initialization=list(subset=S),modelNames=c('VVI','VEI'))
models$ggm_f2 <- ggm_f2

s = paste(substr,'ggm',dtype,'clus',sep="_")
png(paste("out_mix_",s,".png",sep=""))
plot(models$ggm_f2,what="classification")
dev.off()

npn <- Mclust(train.npn,initialization=list(subset=S),modelNames=c('VVI','VEI'))
models$npn <- npn

npn_f2 <-  Mclust(train.npn[,1:2],initialization=list(subset=S),modelNames=c('VVI','VEI'))
models$npn_f2 <- npn_f2

s = paste(substr,'npn',dtype,'clus',sep="_")
png(paste("out_mix_",s,".png",sep=""))
plot(models$npn_f2,what="classification")
dev.off()

s = paste(substr,'ggm',dtype,sep="_")
png(paste("out_mix_",s,".png",sep=""))
plot(models$ggm,what="BIC")
dev.off()

s = paste(substr,'npn',dtype,sep="_")
png(paste("out_mix_",s,".png",sep=""))
plot(models$npn,what="BIC")
dev.off()
#

#######################################################################
# Run log likelihood 
return(models)
}



######################################################################
# Mixture Models

# delete previous results

sink("loglik.csv")
cat(paste("Dtype","Temp","IID/Non-IID","Transform","M.select","Sparsity","TrainLL","TestLL",sep=","))
cat('\n')
sink()


models = mixmodel('data/distances174_300K_train.dat','data/distances174_300K_test.dat','dist','loglik','300K_noniid')

### Subsample
models = mixmodel('data/distances174_sub_300K_train.dat','data/distances174_sub_300K_test.dat','dist','loglik','300K_iid')

### Whole theta tau
models = mixmodel('data/theta44tau43_300_5000_train.dat','data/theta44tau43_300_5000_test.dat','angular','loglik','300K_noniid')

#### ThetaTau subsampled
models = mixmodel('data/tt_300K_sub_train.dat','data/tt_300K_sub_test.dat','angular','loglik','300K_iid')


