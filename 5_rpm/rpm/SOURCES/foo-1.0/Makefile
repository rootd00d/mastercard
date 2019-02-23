DESTDIR ?=
PREFIX ?= /usr/local
CC=gcc
foo: foo.c
	gcc -o foo foo.c

clean:
	rm foo

install:
	install -m 0755 -d $(DESTDIR)$(PREFIX)/bin
	install -m 0755 foo $(DESTDIR)$(PREFIX)/bin
