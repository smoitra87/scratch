library(huge) # Load the package huge
#L = huge.generator(n=200,d=200,graph="hub") # Generate data with hub structures
#X = L$data; X.pow = X^3/sqrt(15) # Power Transformation

run_ggm <- function(fpath,substr){
X <- read.csv(fpath,header=FALSE)
Y<-as.matrix(X)
sz <- dim(Y)

X <- as.matrix(Y)
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

return
}

run_ggm_split <- function(fpath,substr,nsplit){
X <- read.csv(fpath,header=FALSE)
Y<-as.matrix(X)
sz <- dim(Y)

for(i in 1:nsplit) {
	X <- as.matrix(Y[((i-1)*sz[1]/nsplit+1):(i*sz[1])/nsplit,])
	X.npn = huge.npn(X) # Nonparanormal
	out.mb = huge(X,nlambda=50) # Estimate the solution path
	out.npn = huge(X.npn,nlambda=50)
	#huge.roc(out.mb$path,L$theta) # Plot the ROC curve
	#huge.roc(out.npn$path,L$theta)
	mb.stars = huge.select(out.mb,criterion="stars") # Select the graph using StARS
	npn.stars = huge.select(out.npn,criterion="stars")
	mb.ric = huge.select(out.mb) # Select the graph using RIC
	npn.ric = huge.select(out.npn)
	png(paste("out_mb_",substr,"_",i,sep=""))
	plot(out.mb)
	dev.off()
	png(paste("out_npn_",substr,"_",i,sep=""))
	plot(out.npn)
	dev.off()
	png(paste("out_mb_ric_",substr,"_",i,sep=""))
	plot(mb.ric)
	dev.off()
	png(paste("out_npn_ric_",substr,"_",i,sep=""))
	plot(npn.ric)
	dev.off()
	png(paste("out_mb_stars_",substr,"_",i,sep=""))
	plot(mb.stars)
	dev.off()
	png(paste("out_npn_stars_",substr,"_",i,sep=""))
	plot(npn.stars)
	dev.off()
}
return
}

### Distances split trajectory
#run_ggm_split('data/distances174colsfirst2000.txt','dist2000',5)

###### Distances whole trajectory
#run_ggm('data/distances174colsfirst2000.txt','dist2000')

#### Distances Subsampled trajectory
#run_ggm('data/distances174colssub1000.txt','sub1000')
#run_ggm('data/distances174colssub200.txt','sub200')

### Thetatau split
#run_ggm_split('data/theta44tau43_first5000.txt','tt5000',5)

##### Thetatau whole
#run_ggm('data/theta44tau43_first5000.txt','tt5000')

#### ThetaTau subsampled
#run_ggm('data/theta44tau43_sub1000.txt','sub1000')
#run_ggm('data/theta44tau43_sub50.txt','sub50')



#######################################################################
# 300 K

#run_ggm_split('data/X_2000_300K.dat','300_dist2000',5)

###### Distances whole trajectory
run_ggm('data/distances174_300K.dat','300_dist2000')

#### Distances Subsampled trajectory
run_ggm('data/distances174_sub_300K.dat','300_sub')


#### Thetatau split
#run_ggm_split('data/theta44tau43_300_5000.dat','tt_300K_5000',5)
#
###### Thetatau whole
#run_ggm('data/theta44tau43_300_5000.dat','tt_300K_5000')
#
##### ThetaTau subsampled
#run_ggm('data/theta44tau43_300_sub1000.dat','tt_300K_sub1000')
#run_ggm('data/theta44tau43_300_sub50.dat','tt_300K_sub50')

#######################################################################
# 350 K

#run_ggm_split('data/X_2000_350K.dat','350_dist2000',5)

###### Distances whole trajectory
run_ggm('data/distances174_350K.dat','350_dist2000')

#### Distances Subsampled trajectory
run_ggm('data/distances174_sub_350K.dat','350_sub')

#### Thetatau split
#run_ggm_split('data/theta44tau43_350_5000.dat','tt_350K_5000',5)
#
###### Thetatau whole
#run_ggm('data/theta44tau43_350_5000.dat','tt_350K_5000')
#
##### ThetaTau subsampled
#run_ggm('data/theta44tau43_350_sub1000.dat','tt_350K_sub1000')
#run_ggm('data/theta44tau43_350_sub50.dat','tt_350K_sub50')
#



