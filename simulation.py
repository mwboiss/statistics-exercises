import matplotlib as plt
import numpy as np
import pandas as pd

### Simulation Exercises

#PROBLEM 1: How likely is it that you roll doubles when rolling two dice?

n_trials = n_rows = 10_000
n_dice = n_cols = 2
rolls = np.random.choice([1,2,3,4,5,6], n_trials * n_dice).reshape(n_rows, n_cols)

doubles = 

#PROBLEM 2: If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting more than 3 heads?

#PROBLEM 3: There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards I drive past both have data science students on them?

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