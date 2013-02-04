.PHONY: test

test:
	python test/hello.py
	python test/python_js.py
	python test/division.py
	python test/equals.py
	python test/zero_division.py
	python test/tuple_unpacking.py
	cd test; python embedded_output.py
	cd test; python dontcare.py

test-all: test booktest

booktest:
	cd ../book/section1/; python test.py
	cd ../book/section3/; python test.py
	cd ../book/section4/; python test.py
	cd ../book/section5/; python test.py
	cd ../book/section6/; python test.py
	cd ../book/section7/; python test.py
	cd ../book/section8/; python test.py
	cd ../book/section9/; python test.py
	cd ../book/section11/; python test.py
	cd ../book/section12/; python test.py