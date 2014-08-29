TARGETDIRS = $(addprefix target/,classes)

all : targetdir classes

targetdir : 
	mkdir -p $(TARGETDIRS)

classes : src/Foo.java
	javac -d target/classes src/Foo.java

.PHONY : clean run test

clean : 
	rm -rf target/

run : 
	java -cp target/classes foopkg.Foo

