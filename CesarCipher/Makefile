.PHONY: all build clean clean-dev

all: build clean-dev

build:
	pyinstaller -F cesar.py --name CesarCipher
	mv dist/CesarCipher CesarCipher

clean-dev:
	rm -rf *.spec build dist
clean: clean-dev
	rm -rf CesarCipher