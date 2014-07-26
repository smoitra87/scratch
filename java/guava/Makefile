LIBDIR = lib
TARGETDIR = target

DIRS : $(LIBDIR) $(TARGETDIR)
	mkdir -p $(LIBDIR) $(TARGETDIR)

LIBS : guavalib args4jlib
   
args4jlib : $(LIBDIR)/args4j-2.0.29.jar 
	wget -O $(LIBDIR)/args4j-2.0.29.jar http://search.maven.org/remotecontent?filepath=args4j/args4j/2.0.29/args4j-2.0.29.jar \
	touch "$@"

guavalib : $(LIBDIR)/guava-17.0.jar 
	 wget -O $(LIBDIR)/guava-17.0.jar http://central.maven.org/maven2/com/google/guava/guava/17.0/guava-17.0.jar \
	 touch "$@"

all : $(DIRS) $(LIBS)



