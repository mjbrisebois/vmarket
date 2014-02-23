
SHELL		= /bin/bash
PY2		= python
PYTESTOPTS	= -v --capture=no
PYTEST		= $(PY2) -m pytest $(PYTESTOPTS)

clean-vmarket.db:
	rm -f databases/vmarket.db

clean-pyc:
	find . -name '*.pyc' -exec rm {} \;

testclean:	clean-vmarket.db clean-pyc

test:		testclean
	$(PYTEST)

# Run only tests with a prefix containing the target string, eg test-blah
test-%:		testclean
	$(PYTEST) *$**.py

unit-%:		testclean
	$(PYTEST) -k $*
