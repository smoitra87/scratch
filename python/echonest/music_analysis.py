import pyechonest 
from pyechonest import config
from pyechonest.track import track_from_file
import pickle
import numpy as np
import pylab as pl
import os


api_key = "DMSARFFYEZKLFL9LE"

config.ECHO_NEST_API_KEY = api_key

fpath = "02-Heir-Apparent.mp3"

if not os.path.exists("track.p") : 
	with open(fpath,'rb') as fin : 
		track = track_from_file(fin,'mp3')
	pickle.dump(track,open('track.p','wb'))
else : 
	track = pickle.load(open('track.p','rb'))

t = [seg['start'] for seg in track.segments]
loud = [seg['loudness_max'] for seg in track.segments]

pl.plot(t,loud)
#pl.xticks(t,np.arange(len(t)))
pl.xlabel("Time Segment")
pl.ylabel("Loudness")
pl.show()
