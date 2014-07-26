#!/bin/sh

[ ! -d lib/ ] && mkdir -p lib/
wget -O lib/guava.jar http://central.maven.org/maven2/com/google/guava/guava/17.0/guava-17.0.jar
wget -O lib/args4j.jar http://search.maven.org/remotecontent?filepath=args4j/args4j/2.0.29/args4j-2.0.29.jar

[ ! -d target/ ] && mkdir -p target/
echo javac -d target/ src/com/deepmoitra/Util.java
javac -d target/ src/com/deepmoitra/Util.java
echo javac -d target/ -cp target/:lib/ src/com/deepmoitra/Main.java
javac -d target/ -cp target/:lib/guava.jar src/com/deepmoitra/Main.java

#java -cp target/ com.deepmoitra.Util
echo java -cp target/:lib/guava.jar com.deepmoitra.Main
java -cp target/:lib/guava.jar com.deepmoitra.Main
