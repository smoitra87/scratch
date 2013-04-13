library(huge)


# ----- Define a function for plotting a matrix ----- #
myImagePlot <- function(x, ...){
     min <- min(x)
     max <- max(x)
     yLabels <- rownames(x)
     xLabels <- colnames(x)
     title <-c()
  # check for additional function arguments
  if( length(list(...)) ){
    Lst <- list(...)
    if( !is.null(Lst$zlim) ){
       min <- Lst$zlim[1]
       max <- Lst$zlim[2]
    }
    if( !is.null(Lst$yLabels) ){
       yLabels <- c(Lst$yLabels)
    }
    if( !is.null(Lst$xLabels) ){
       xLabels <- c(Lst$xLabels)
    }
    if( !is.null(Lst$title) ){
       title <- Lst$title
    }
  }
# check for null values
if( is.null(xLabels) ){
   xLabels <- c(1:ncol(x))
}
if( is.null(yLabels) ){
   yLabels <- c(1:nrow(x))
}

layout(matrix(data=c(1,2), nrow=1, ncol=2), widths=c(4,1), heights=c(1,1))

 # Red and green range from 0 to 1 while Blue ranges from 1 to 0
 ColorRamp <- rgb( seq(0,1,length=256),  # Red
                   seq(0,1,length=256),  # Green
                   seq(1,0,length=256))  # Blue
 ColorLevels <- seq(min, max, length=length(ColorRamp))

 # Reverse Y axis
 reverse <- nrow(x) : 1
 yLabels <- yLabels[reverse]
 x <- x[reverse,]

 # Data Map
 par(mar = c(3,5,2.5,2))
 image(1:length(xLabels), 1:length(yLabels), t(x), col=ColorRamp, xlab="",
 ylab="", axes=FALSE, zlim=c(min,max))
 if( !is.null(title) ){
    title(main=title)
 }
axis(BELOW<-1, at=1:length(xLabels), labels=xLabels, cex.axis=0.7)
 axis(LEFT <-2, at=1:length(yLabels), labels=yLabels, las= HORIZONTAL<-1,
 cex.axis=0.7)

 # Color Scale
 par(mar = c(3,2.5,2.5,2))
 image(1, ColorLevels,
      matrix(data=ColorLevels, ncol=length(ColorLevels),nrow=1),
      col=ColorRamp,
      xlab="",ylab="",
      xaxt="n")

 layout(1)
}
# ----- END plot function ----- #

######### function for plotting ROC values
plot_roc <- function(X,theta,substr) {

  X.npn <- huge.npn(X)
  out.mb <- huge(X,nlambda=50)
  out.npn <- huge(X.npn,nlambda=50)

  png(paste('out_mb_roc_',substr,sep=""))
  roc.mb = huge.roc(out.mb$path,theta)
  dev.off()

  png(paste('out_npn_roc_',substr,sep=""))
  roc.npn = huge.roc(out.npn$path,theta)
  dev.off()

  auc <- list(mb=roc.mb$AUC,npn=roc.npn$AUC)
  return(auc)
}

# ----- END ROC plotting function ----- #

run_ggm <- function(X,substr){
#X <- read.csv(fpath,header=FALSE)
#Y<-as.matrix(X)
sz <- dim(X)
#X <- as.matrix(Y)
X.npn = huge.npn(X) # Nonparanormal
out.mb = huge(X,nlambda=50) # Estimate the solution path
out.npn = huge(X.npn,nlambda=50)
#huge.roc(out.mb$path,L$theta) # Plot the ROC curve
#huge.roc(out.npn$path,L$theta)
mb.stars = huge.select(out.mb,criterion="stars") # Select the graph using StARS
npn.stars = huge.select(out.npn,criterion="stars")
mb.ric = huge.select(out.mb) # Select the graph using RIC
npn.ric = huge.select(out.npn)
png(paste("out_mb_",substr,sep=""))
plot(out.mb)
dev.off()
png(paste("out_npn_",substr,sep=""))
plot(out.npn)
dev.off()
png(paste("out_mb_ric_",substr,sep=""))
plot(mb.ric)
dev.off()
png(paste("out_npn_ric_",substr,sep=""))
plot(npn.ric)
dev.off()
png(paste("out_mb_stars_",substr,sep=""))
plot(mb.stars)
dev.off()
png(paste("out_npn_stars_",substr,sep=""))
plot(npn.stars)
dev.off()

#### Plot fitted matrices
png(paste("out_npn_stars_refit",substr,sep=""))
myImagePlot(as.matrix(npn.stars$refit),zlim=c(0,1)) 
dev.off()

png(paste("out_mb_stars_refit",substr,sep=""))
myImagePlot(as.matrix(mb.stars$refit),zlim=c(0,1)) 
dev.off()

png(paste("out_mb_ric_refit",substr,sep=""))
myImagePlot(as.matrix(mb.ric$refit),zlim=c(0,1)) 
dev.off()

png(paste("out_npn_ric_refit",substr,sep=""))
myImagePlot(as.matrix(npn.ric$refit),zlim=c(0,1))
dev.off()

return
}




######################################################################
# Experiments 04/09

# Create dataset 1 Sum
#L=huge.generator(n=200,d=20,graph="random",prob=0)
#X = L$data
#d=20
#X = cbind(X,X[,1:d-1]+X[,2:d])
#run_ggm(X,'test_corr1')
#
## Create dataset 1 Product
#X = L$data
#X = cbind(X,X[,1:d-1]*X[,2:d])
#run_ggm(X,'test_corr2')
#
## Create dataset 1 dist
#X = L$data
#X = cbind(X,abs(X[,1:d-1]-X[,2:d]))
#run_ggm(X,'test_corr3')
#

######################################################################
# Experiments 04/11



# Pregenerate the data
L_list <- list()
d = 20
for (i in 0:5){
   n = 50*2^i
   L=huge.generator(n=n,d=d,graph="random",prob=0) 
   L_list[[i+1]] <- L
}

# Define original dependency matrix
m1 = diag(20)
m1[2:20,1:19] = m1[2:20,1:19] + diag(19)
m1 = m1[,1:19]
m2 = diag(20)
m2[1:19,2:20] = m2[1:19,2:20] + diag(19)
m2 = m2[1:19,]
theta = matrix(data=0,nrow=39,ncol=39)
theta[1:20,21:39] = m1
theta[21:39,1:20] = m2

###### Sum 
#
#auc.sum.mb <- list()
#auc.sum.npn <- list()
#for (i in 0:5) {
#  X = L_list[[i+1]]$data
#  n = 50*2^i
#  X = cbind(X,X[,1:d-1]+X[,2:d])
#  run_ggm(X,paste('test_sum_n',n,sep="")) 
#  auc <- plot_roc(X,theta,paste('test_sum_n',n,sep=""))
#  auc.sum.mb[[i+1]] <- auc$mb
#  auc.sum.npn[[i+1]] <- auc$npn
#
#}
#
###### Product
#auc.prod.mb <- list()
#auc.prod.npn <- list()
#for (i in 0:5) {
#  X = L_list[[i+1]]$data
#  n = 50*2^i
#  X = cbind(X,X[,1:d-1]*X[,2:d])
#  run_ggm(X,paste('test_prod_n',n,sep=""))
#  auc <- plot_roc(X,theta,paste('test_prod_n',n,sep=""))
#  auc.prod.mb[[i+1]] <- auc$mb
#  auc.prod.npn[[i+1]] <- auc$npn
#}
#
###### 1D Distance
#auc.l1.mb <- list()
#auc.l1.npn <- list()
#for (i in 0:5) {
#  X = L_list[[i+1]]$data
#  n = 50*2^i
#  X = cbind(X,abs(X[,1:d-1]-X[,2:d]))
#  run_ggm(X,paste('test_l1_n',n,sep=""))
#  auc <- plot_roc(X,theta,paste('test_l1_n',n,sep=""))
#  auc.l1.mb[[i+1]] <- auc$mb
#  auc.l1.npn[[i+1]] <- auc$npn
#
#}

###### 3D distances

L_list <- list()
d = 10
for (i in 0:5){
   n = 50*2^i
   L=huge.generator(n=n,d=3*d,graph="random",prob=0) 
   L_list[[i+1]] <- L
}

#define theta
m <- matrix(data=0,nrow=30,ncol=d*(d-1)/2)
colid = 0
for(i in 1:d) {
 j=i+1
 while(j<=d) {
   colid = colid + 1
   m[i,colid] = 1
   m[i+d,colid] = 1
   m[i+2*d,colid] = 1
   m[j,colid] = 1
   m[j+d,colid] = 1
   m[j+2*d,colid] = 1
   j = j + 1
 }

}

theta = matrix(data=0,nrow=3*d+d*(d-1)/2,ncol=3*d+d*(d-1)/2)
theta[1:30,31:75] <- m
theta[31:75,1:30] <- t(m)
png(paste("3dtheta1.png",sep=""))
myImagePlot(theta)
dev.off()

# Edges between the different distance measres 

#define theta
m <- matrix(data=0,nrow=d*(d-1)/2,ncol=d*(d-1)/2)
colid = 0
for(i in 1:d) {
 nbr = NULL
 j = i+1
 while(j <= d) {
  colid = d*(d-1)/2 - (d-i)*(d-i+1)/2 + j-i
  nbr = c(nbr,colid)
  j = j+1
 } 
 for(p in 1:(d-1)) {
  for(q in 1:(d-1)) {
   if(q==p) { next } 
   m[nbr[p],nbr[q]] = 1
  }
 }
}

theta2 = matrix(data=0,nrow=3*d+d*(d-1)/2,ncol=3*d+d*(d-1)/2)
theta2[31:75,31:75] <- m
png(paste("3dtheta2.png",sep=""))
myImagePlot(theta2)
dev.off()

auc.3d.mb <- list()
auc.3d.npn <- list()
auc2.3d.mb <- list()
auc2.3d.npn <- list()

for (i in 0:5) {
  X = L_list[[i+1]]$data
  n = 50*2^i

  m <- matrix(data=0,nrow=n,ncol=d*(d-1)/2)
  for(p in 1:n){
   colid=0
   for (j in 1:d) {
    k = j+1
    while(k <=d){
       colid = colid + 1
       m[p,colid] <- sqrt((X[p,j]-X[p,k])^2+(X[p,d+j]-X[p,d+k])^2 + 
                     (X[p,2*d+j]-X[p,2*d+k])^2)
       k = k + 1
    }
   }
  }
  
  X = cbind(X,m)
  run_ggm(X,paste('test_3d_n',n,sep="")) 
  auc <- plot_roc(X,theta,paste('test_3d_n',n,sep=""))
  auc.3d.mb[[i+1]] <- auc$mb
  auc.3d.npn[[i+1]] <- auc$npn

  auc2 <- plot_roc(X,theta2,paste('test_3d2_n',n,sep=""))
  auc2.3d.mb[[i+1]] <- auc2$mb
  auc2.3d.npn[[i+1]] <- auc2$npn

}


