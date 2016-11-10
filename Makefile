all: help

help:
	@echo "Commands: package"

package:
	@-rm -r dist/* 2>/dev/null
	@-rm -r build/* 2>/dev/null
	python setup.py sdist bdist_wheel
	for file in dist/*; do gpg --detach-sign -a $$file; done
