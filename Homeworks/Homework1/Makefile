MDS=$(wildcard *.md)
TARGETS=$(MDS:.md=.pdf)

all: $(TARGETS)

%.pdf: %.md
	pandoc -o $@ $^

clean:
	rm -rf *.pdf