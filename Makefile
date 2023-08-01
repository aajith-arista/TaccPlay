all: libPlay.so test

test: libPlay.so PlayTest.py
	python3 PlayTest.py

libPlay.so: Play.h Play.cpp Play.json
	g++ -shared -std=c++20 -fPIC -ltac Play.cpp -o libPlay.so

Play.h Play.cpp Play.json: Play.tac
	tacc Play.tac

clean:
	rm -f Play.h Play.cpp Play.json libPlay.so
