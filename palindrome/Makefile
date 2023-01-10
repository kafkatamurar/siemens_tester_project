.PHONY: all build clean clean-dev

all: build clean-dev

build:
	pyinstaller -F palindrome.py --name palindrome
	mv dist/palindrome palindrome

clean-dev:
	rm -rf *.spec build dist
clean: clean-dev
	rm -rf palindrome