# CS 110
## Chapter 11 - Lab - Working with Pygame


### [Assignment Description](https://docs.google.com/document/d/1kFLQs7Lepb8hcYOrZq5scmRmdcNkIwWZ6Kb85_0bCVY/edit?usp=sharing)

***
Replace anything surrounded by the `< >` symbols._

## SUMMARY:
 < Herogame that spawns a Turtle hero controller by the user to defeat the enemies >
#### Unique Feature
 < Added a new damaged Hero sprite for when the Hero drops below 50% health. Uses a new spriteChange method in the hero class to change the sprite to the damaged hero sprite when it drops to 5 or less health. Also added a fun DnD style d20 attack pattern to the Hero. When a 1 is rolled, it is a critical failure and the Hero loses 2 HP instead of the usual 1 on a missed attack. Also added a critical success which heals the hero 1 health which the spriteChange function takes into account and can technically heal back above the threshold and change back into the undamaged sprite>

## GRACE DAYS
Grace days used for this assignment: < 0 >

Grace days remaining: < 0 >/5

## KNOWN BUGS AND INCOMPLETE PARTS:
 < What parts of the project you were not able to complete >
I wanted to use the "damaged_hero.png" file because it has a transparent background but whenever I attempted to use it, it would change to an empty sprite instead of the png file so I had to go with the lower quality jpg file instead

## REFERENCES:
 < List any outside resources used >
 pygame library

## MISCELLANEOUS COMMENTS:
 < Anything you would like the grader to know >
