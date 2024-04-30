MARKDOWNS=$(wildcard *.md)
TARGETS=$(MARKDOWNS:.md=.pdf)

all: $(TARGETS)

%.pdf: %.md
	pandoc -o $@ $^

clean:
	rm -rf *.pdf