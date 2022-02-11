import numpy as np
import pandas as pd

### Simulation Exercises

#PROBLEM 1: How likely is it that you roll doubles when rolling two dice?
### Making the dataframe
n_trials = n_rows = 10_000
n_dice = n_cols = 2
rolls = np.random.choice([1,2,3,4,5,6], n_trials * n_dice).reshape(n_rows, n_cols)

#### This one gave me half the answer
rolls_mean = rolls.sum(axis =1) / 2
double = rolls_mean == rolls[:,:1]
double.mean()

#### This gave me the answer
doubles = rolls[:,:1] == rolls[:,1:]
doubles.mean()

#### Confused myself why they were different
roll = np.random.randint(1, 7, size = (n_rows, n_cols))

#### Working with Zack this worked and I'm still confused why
roll_mean = roll.sum(axis =1) / 2
double_ = roll_mean == roll[:,0]
double_.mean()

doubles_ = roll[:,:1] == roll[:,1:]
doubles_.mean()
#### Either way this works.

#PROBLEM 2: If you flip 8 coins, what is the probability of getting exactly 3 heads? 

n_trials = n_rows = 10_000
n_flips = n_cols = 8
flips = np.random.choice([1,0], n_trials * n_flips).reshape(n_rows,n_cols)
three_flips = flips.sum(axis=1) == 3
three_flips.mean()

# What is the probability of getting more than 3 heads?
greater_than_three_flips = flips.sum(axis=1) > 3
greater_than_three_flips.mean()

### For my own sanity
less_than_three_flips = flips.sum(axis=1) < 3
less_than_three_flips.mean()

#PROBLEM 3: There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards I drive past both have data science students on them?

n_trails = n_rows = 10_000
n_billboards = n_cols = 2

cohorts = np.random.randint([1,5], size = (n_rows,n_cols))
cohorts

bill_sum = cohorts.sum(axis=1)
bill_sum

both_bill = bill_sum == 8
both_bill

both_bill.mean()

#PROBLEM 4: Codeup students buy, on average, 3 poptart packages with a standard deviation of 1.5 a day from the snack vending machine. If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon? (Remember, if you have mean and standard deviation, use the np.random.normal)

#PROBLEM 5: Compare Heights:
# Men have an average height of 178 cm and standard deviation of 8cm.

# Women have a mean of 170, sd = 6cm.

# Since you have means and standard deviations, you can use np.random.normal to generate observations.

# If a man and woman are chosen at random, P(woman taller than man)?

#PROBLEM 6: When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails. 
# What are the odds that after having 50 students download anaconda, no one has an installation issue? 

# 100 students?

# What is the probability that we observe an installation issue within the first 150 students that download anaconda?

#How likely is it that 450 students all download anaconda without an issue? 

#PROBLEM 7: There's a 70% chance on any given day that there will be at least one food truck at Travis Park. However, you haven't seen a food truck there in 3 days. 
# How unlikely is this?

#How likely is it that a food truck will show up sometime this week?

#PROBLEM 8: If 23 people are in the same room, what are the odds that two of them share a birthday? 

# What if it's 20 people? 40?

#BONUS Mage Duel: https://gist.github.com/ryanorsinger/2996446f02c1bf30fcb3f8fdb88bd51d

#BONUS Chuck a Luck: https://gist.github.com/ryanorsinger/eac1d7b7e978f90b8390bdc056312123