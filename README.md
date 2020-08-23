# Bank elevator

*Bank elevator*

## Algorithm

There are Primarily 4 steps in this algorithm

### step 1 : Calculate moves(floors) for each user input to users target floor

Calculate the floors(UP/DOWN) from Current floor to Target floor.

if the user are inputs from floor 3 to target floor 7(UP) - [4,5,6,7]

if the user are inputs from floor 9 to target floor 5(DOWN) - [8,7,6,5]

### step 2 : Calculate all moves(floors) for all users.

1. Calculate all the UP moves of each user and form a list
   
2. Calculate the highest floor from above step(Max of all UP floors chosen by users)
   
3. With that Highest floor as basis calculate all DOWN moves of each user and form a list


### step 3 : Creating instruction set(INSIDE Algo)

**Refer test cases and code for examples**

1. Take all the moves calculated in Step 2

2. Sort all the user in the ascending(UP)/descending(DOWN) order of destination

3. And keep track of all visited floors and if already visited do not add to instructions else add to instruction.
   
4. if one user moves are exhausted then add OPEN/CLOSE to instruction set.

  **Step3 gives all instructions set required for INSIDE algo**

### step 4 : Creating instruction set (OUTSIDE Algo)

**Refer test cases and code for examples**

1. Take all users inputs - their current floor and target floor(c,t)
   
2. Subtracting(t-c) current floor from target floor is going to give whether they want to UP or DOWN
   
3. Apply Step3 algo on up/DOWN lists created above

 **Step4 gives all instructions set required for OUTSIDE algo**


## Unit testing and testing

Please run `make test` to test all use cases. You can also use `tox` to run tests.
Make also uses `tox` to run tets cases.

Please `cli.py` for trying different inputs.


## Note

Please find the thought process and how i arrived at the algo in `pg.py` and please do not consider same for review.