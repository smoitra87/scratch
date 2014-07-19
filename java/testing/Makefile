TARGETDIRS = $(addprefix target/,classes test)

all : targetdir classes testclasses

targetdir : 
	mkdir -p $(TARGETDIRS)

target_test_dir : 
	mkdir -p target/test

classes : src/Foo.java
	javac -d target/classes src/Foo.java

testclasses : test/FooTest.java test/FooTest2.java
	javac -cp target/classes:/usr/share/java/junit4.jar -d target/test test/Foo*.java

.PHONY : clean run test

clean : 
	rm -rf target/

run : 
	java -cp target/classes foopkg.Foo

test : 
	java -cp target/classes:target/test:/usr/share/java/junit4.jar org.junit.runner.JUnitCore foopkg.FooTest foopkg.FooTest2

