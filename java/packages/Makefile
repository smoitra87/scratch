JC			= javac
TARGET		= target
CLASSPATH	= target
JCFLAGS		= -d $(TARGET)/ -cp $(TARGET)/
SRCDIR		= src/com/deepmoitra/scratch/packages
PACKAGE		= com/deepmoitra/scratch/packages
JR			= java
JRFLAGS		= -cp $(TARGET)/

.SUFFIXES: .java .class

.java.class:
	$(JC) $(JCFLAGS) $*.java

CLASSES = \
        $(SRCDIR)/Add.java 

MAIN = \
        $(SRCDIR)/Main.java 

default : classes main

main : $(MAIN:.java=.class)

classes : $(CLASSES:.java=.class)

clean :
	$(RM) $(TARGET)/$(PACKAGE)/*.class

run : 
	$(JR) $(JRFLAGS) com.deepmoitra.scratch.packages.Main
