CFLAGS=-Wall -g

all: newex19

newex19: object.o ex19.o

clean:
	rm -f ex19 object.o ex19.o

test:
	./test.sh && echo "##### Tests Pass #####" || echo "##### Tests fail #####"
