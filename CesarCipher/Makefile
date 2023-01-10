.PHONY: all build clean

all: build clean-dev

build:
	pyinstaller -F prog.py --name CesarCipher
	mv dist/CesarCipher CesarCipher

clean-dev:
	rm -rf *.spec build dist
clean: clean-dev
	rm -rf CesarCipher