import argparse

args = argparse.ArgumentParser()

args.add_argument('-x','--xVal',required=True)
# args.add_argument('-y','--yVal',required=False)

argvar = vars(args.parse_args())

pass