# Resocake

My friend made this really cool design language/simulator called [Reso!](https://gitlab.com/lynnpepin/reso) Essentially, if you use *just* the right colors, you can build logical circuits that look really pretty. While tinkering with it, I wondered if I could adapt an old graph art project, Cheescake, to make circuits that run in the Reso simulator. It took some tuning, but I made it work!

## Installation

step 1) go get [Reso!](https://gitlab.com/lynnpepin/reso)

step 2) drag every .py file here into Reso's main directory, as well as our clock node, `new_clock.png`.

step 3) Windows users don't have to do this, but Mac and Linux users may have to check if Reso is recognizing colors generated by Resocake. To check, go through every step in Usage and check if at least the clock circuits are flashing in the final result. If they are, you're done, but if not, in resoboard.py, swap every instance of `from palette` to `from hack_palette`. Don't forget to swap it back if you are using reso outside of Resocake! 

## Usage

step 1) In the Reso directory, run `python3 resocake.py`.

step 2) make a lovely image in the larger window by clicking around! You can click when the smaller window is green, but when that window is red Resocake is drawing wires and nodes.

step 3) when you feel you've put your all into it, take a screenshot of your circuit. it must be a png!

step 4) reso time now! I like to do something along the lines of this, but tweak as needed.

```
python3 reso.py ~/filepath-to-screenshot.png -n 12 -s hello_ -v
```
If all -n of your reso progressions look exactly the same, check step 3 in Installation. 

---
_seriously super special thanks to my friend Lynn who made reso!_ 