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
for (i in 0:5){
   n = 50*2^i
   L=huge.generator(n=n,d=20,graph="random",prob=0) 
#   L_list
   print(i)
}


# Sum 





# Product


# Distance


# Distance 2D 


# Distance 3D



