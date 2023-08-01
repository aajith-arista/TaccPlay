# TaccPlay
Playground to build TACC code

Compiles a tac model defined in `Play.tac` and instantiates the object in `PlayTest.py`
```
% make test
tacc Play.tac
g++ -shared -std=c++20 -fPIC -ltac Play.cpp -o libPlay.so
python3 PlayTest.py
% % echo $?
0
```
