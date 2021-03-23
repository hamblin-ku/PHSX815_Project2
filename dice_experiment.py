# File:     dice_experiment.py
# Author:   Kurt Hamblin
# Description:  Utitlize the Random Class to:
# Simulate dice rolls where the dice weights are sampled from a Rayleigh Distribution

from Random import Random
import numpy as np
import argparse

# main function for this Python code
if __name__ == "__main__":
    
    # Set up parser to handle command line arguments
    # Run as 'python monopoly_experiment.py -h' to see all available commands
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", "-s", help="Seed number to use")
    parser.add_argument("--Nsides",  help="Number of sides on each die")
    parser.add_argument("--Nrolls",  help="Number of rolls")
    parser.add_argument("--Nexp",  help="Number of rolls")
    args = parser.parse_args()

    # default seed
    seed = 5555
    if args.seed:
        print("Set seed to %s" % args.seed)
        seed = args.seed
    random = Random(seed)
    
    # By default, roll 6 sided dice
    Nsides = 6
    if args.Nsides:
        print("Number sides per die: %s" % args.Nsides)
        Nsides = np.uint64(args.Nsides)

    Nrolls = 100
    if args.Nrolls:
        print("Number of rolls per experiment: %s" % args.Nrolls)
        Nrolls = np.uint64(args.Nrolls)
     
    Nexp = 1000
    if args.Nexp:
        print("Number of experiments: %s" % args.Nexp)
        Nexp = np.uint64(args.Nexp)

    
    # Create weights by pulling from a rayleigh distribution
    weights = np.array([ random.Rayleigh() for i in range(Nsides) ])

    # The weigths need to sum to one, so normalize them
    weights /= weights.sum()
    print(f'Weights: {weights}')
    
    rolls_test = np.zeros((Nexp, Nrolls))
    rolls_fair = np.zeros((Nexp, Nrolls))
    for i in range(Nexp):
        for j in range(Nrolls):
            rolls_test[i,j] = random.roll_die(Nsides = Nsides, weights = weights)
            rolls_fair[i,j] = random.roll_die(Nsides = Nsides)

    
    
    # Save the normalized results
    np.savetxt('data/dice_rolls.txt', rolls_test, delimiter = ',', fmt="%d")
    np.savetxt('data/fair_dice_rolls.txt', rolls_fair, delimiter = ',', fmt="%d")
    
