all: HIST2

HIST2: HIST2.cc
	g++ -g -ggdb3 -o HIST2 HIST2.cc

.PHONY: test
test: 
	./HIST2 < infile

.PHONY: debug
debug:
	gdb HIST2

.PHONY: clean
clean:
	rm HIST2

