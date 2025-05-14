all: libPlay.so

test: libPlay.so PlayTest.py
	python3 PlayTest.py

libPlay.so: Play.h Play.cpp Play.json PlaySm.h PlaySm.cpp PlaySm.json PlaySm.tin
	g++ -shared -std=c++20 -fPIC -ltac -lArk Play.cpp PlaySm.cpp -o libPlay.so

Play.h Play.cpp Play.json: Play.tac
	tacc Play.tac

PlaySm.h PlaySm.cpp PlaySm.json: PlaySm.tac Play.h Play.cpp Play.json
	tacc PlaySm.tac

clean:
	rm -f *.h *.cpp *.json *.transients *.so
