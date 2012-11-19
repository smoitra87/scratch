from multiprocessing import Pool
import time,random

class Parents(object) :
	pass

class SubhodeepMoitra(object) : 
	def __init__(self,mom,dad) : 
		self.mom = mom
		self.dad = dad
		self.alive = True
		self.age = 0

def updateProteinArchitect(me) : 
	stufftodo= ['MSLTI','Proteins2012','PyMol','BioPython'] # more later
	for stuff in stufftodo  :
		time.sleep(random.expovariate(0.5))	
		me.__setattr__(stuff,True)

def updatePythonista(me) : 
	stufftodo= ['Pycon2012','string','stdlib'] # more later
	for stuff in stufftodo  :
		time.sleep(random.expovariate(0.25))	
		me.__setattr__(stuff,True)

def updateTriathlete(me) : 
	stufftodo= ['PittMarathon2012','IMTexas70_3','MS150'] # more later
	for stuff in stufftodo  :
		time.sleep(random.expovariate(0.25))	
		me.__setattr__(stuff,True)

def updateClimber(me) : 
	stufftodo= ['RockSchool2012','Seneca','V2'] # more later
	for stuff in stufftodo  :
		time.sleep(random.expovariate(0.5))	
		me.__setattr__(stuff,True)


if __name__ == '__main__' : 
	mamma,baba = Parents(),Parents()
	me = SubhodeepMoitra(mamma,baba)
	lifeStart = time.time()
	gradSchoolStart = 21 # Life begins at gradschool ?
	
	# Don't want to live beyond 70
	lifeEnd = lifeStart + 70 - random.expovariate(lambd=1.0)
	life  = Pool(processes=4)
	life.apply_async(updateProteinArchitect,me)
	life.apply_async(updatePythonista,me)
	life.apply_async(updateTriathlete,me)
	life.apply_async(updateClimber,me)

	while time.time() + gradSchoolStart < lifeEnd  : 
		time.sleep(1) # Check anually if I am alive
	me.alive = False
	life.terminate()	
	print("What a ride..!!")


