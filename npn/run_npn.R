library(huge) # Load the package huge
#L = huge.generator(n=200,d=200,graph="hub") # Generate data with hub structures
#X = L$data; X.pow = X^3/sqrt(15) # Power Transformation

X <- read.csv('data/distances174colsfirst2000.txt',header=FALSE)
Y<-as.matrix(X)
sz <- dim(Y)
for(i in 1:5) {
	X <- as.matrix(Y[((i-1)*sz[1]/5+1):(i*sz[1])/5,])
	X.npn = huge.npn(X) # Nonparanormal
	out.mb = huge(X,nlambda=50) # Estimate the solution path
	out.npn = huge(X.npn,nlambda=50)
	#huge.roc(out.mb$path,L$theta) # Plot the ROC curve
	#huge.roc(out.npn$path,L$theta)
	#mb.stars = huge.select(out.mb,criterion="stars") # Select the graph using StARS
	#npn.stars = huge.select(out.npn,criterion="stars")
	mb.ric = huge.select(out.mb) # Select the graph using RIC
	npn.ric = huge.select(out.npn)
	png(paste("out_mb_",i,sep=""))
	plot(out.mb)
	dev.off()
	png(paste("out_npn_",i,sep=""))
	plot(out.npn)
	dev.off()
	png(paste("out_mb_ric_",i,sep=""))
	plot(mb.ric)
	dev.off()
	png(paste("out_npn_ric",i,sep=""))
	plot(npn.ric)
	dev.off()

}



