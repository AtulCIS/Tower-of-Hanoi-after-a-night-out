# Tower of Hanoi - after a night out!

* Bob is very familiar with the famous mathematical puzzle/game, "Tower of Hanoi". Bob is drunk, but in this stage, he is still capable of following the rules of the game itself, as well as choosing when to pick up or put down a disk.
* Bob standing in a rectangular room where k is the number of squares. 3 poles are standing on a, b, c are positions of poles.
* n is the number of disks.
* Since Bob is drunk, on a given move, Bob will either stumble one square to the left or one square to the right with equal probability, unless Bob is at either end of the room.
* This expression E(n, k, a, b, c) evaluates the number of squares that Bob travels during a single optimally-played game. A game is played optimally if the number of disk-pickups is minimized.
* In this problem we have to find the last nine digits of ∑1≤n≤10000 E(n,10n,3n,6n,9n).

## Installation

The program is written in python 3.6 and Flask framework is used.
* Clone this repo.
* In the cloned folder. Create a virtual environment for python3.
* Activate this environment.
* Install all the dependencies of requirements.txt file by below-given command.

```bash
pip install -r requirements.txt
```

## To run the Program

```python
python run.py
```
## To run the test cases

```python
python Test.py
```
## 