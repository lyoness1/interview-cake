"""
A building has 100 floors. One of the floors is the highest floor an egg can be 
dropped from without breaking.
If an egg is dropped from above that floor, it will break. If it is dropped from
that floor or below, it will be completely undamaged and you can drop the egg 
again.

Given two eggs, find the highest floor an egg can be dropped from without 
breaking, with as few drops as possible.

Step 1: floor 2
Step 2: floor 4... etc.
Step n: when the first egg breaks, go down a floor. 
        if second egg intact, that's it. Else, it's the floor down. 
        
Worst case by 2's: 50 drops (floor 100)
Worst case by 3's: 33 drops to floor 99, 34 on floor 97, 35 on floor 98, 36: 100

OK, let's keep up this process... what happens by 4 floors? 
    4, 8, 12,... 96, 100: oops! (25 drops)
    97, 98, 99 (28, worst case)

What about by 5's?
    5, 10,... 95, 100 (20 drops)
    96, 97, 98, 99 (24 worst case)

6's? 
    6, 12,... 90, 96 (16 drops so far)
        case 1: 97, 98, 99, 100 (20 total)
        case 2: 91, 92, 93, 94, 95 (21 worst case)

7's? 
    7, 14,... 91, 98 (14 so far)
        case 1: 99, 100 (16 total)
        case 2: 92, 93, 94, 95, 96, 97 (20 worst case)

8's? ... 96 (12 so far)
        97, 98, 99, 10 (16 total)
        12 + 7 = 19 worst case

9's? 11 + 1 = 12 or 11 + 10 = 21 (going back up!)

10's? 10 + 9 = 19 worst case

11's? 9 + 10 = 19 worst case

12's? 8 + 11 = 19 worst case

13's? 7 + 12 = 19, 14: 7 + 13 = 20, 15: 6 + 14, etc.

What if we didn't go up constantly? 

What about a binary approach? 
Start at 50. 
    Option 1: go to 75 with that egg, etc.. 
    Option 2: have to iterate 49 floors with second egg. Still 50 tries. 
Start at 25? Worst case 25 tries. 
Start at 12? Worst case 19 (see above). 

OK, let's go back to 8's (first increment with worst case 19)
    Start at floor 8. If it breaks, 8 tries worst case. If it doesn't breaks...
    But what about jumping to more than 16 the next time? Skip 10 this time...
    If it breaks on the second drop, it would be 2 + 9 = 11, or: 
    8, 18, 28,... 98 --> 19 still. 

Let's try starting big and getting smaller with jumps (sort of binary). 
    Start at 13 (largest worst case 19 scenario). 
        Option 1: breaks first time --> 1 + 12 = 13 drops
        Option 2: jump 12 (now floor 25)
            a) breaks: 2 + 11 = 13
            b) jump 11 (to 36): 3 + 10 = 13

    OK, this is working. Mathematically: 
    Jump 13 to floor 13: 1 drop
        breaks: 1 + 12 = 13
    Jump 12 to floor 25: 2 drops
        breaks: 2 + 11 = 13
    Jump 11 to floor 36: 3 drops
        breaks: 3 + 10 = 13
    Jump 10 to floor 46: 4
        breaks: 4 + 9 = 13
    Floor 55: 5 + 8 = 13
    Floor 63: 6 + 7 = 13
    Floor 70: 7 + 6 = 13
    Floor 76: 8 + 5 = 13
    Floor 81: 13
    Floor 85, 88, now we're not getting to 100. When do we stop the pattern? 

    Let's try 14's:
    14: 1 + 13 = 14
    27: 2 + 12 = 14
    39: 3 + 11 = 14
    50: 4 + 10 = 14
    60: 5 + 9 = 14
    69: 6 + 8 = 14
    77: 7 + 7 = 14
    84: 8 + 6 = 14
    90: 9 + 5 = 14
    95: 10 + 4 = 14
    99: 11 + 3 = 14
    DAMN. 14 drops. just buy more eggs. But these are weird eggs that don't 
                    break from even floor one. I wouldn't eat them. 

Mathematically: 
1 + 2 + ... (n-2) + (n-1) + n = 100
[1 + n] + [2 + (n-1)] + [3 + (n-2)] + ... = 100
(n + 1) * (n / 2) = 100
n^2 + n - 200 = 0
n = 13.6 --> 14

Fucking triangular series. Would have liked to have known this for stacking 
coins on that Hackerrank challenge yesterday... 

"""


