test-all:
	cd coderunner/test; \
	python tiny.py; \
	python hello.py; \
	python division.py; \
	python zero_division.py; \
	python embedded_output.py; \
	python dontcare.py;
	cd int_and_float; python test.py
	cd python; python errors.py
	cd webdbpress60; python test.py
	cd webdbpress60/perloop; python test.py
	cd webdbpress60/scope; python test.py
	cd webdbpress60/syntax; python test.py
	cd webdbpress60/virtual; python test.py

