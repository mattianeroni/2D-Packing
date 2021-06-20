import packing
import utils
from packing import test

import itertools

orderlines = utils.read_problem("./testproblem.csv")

cases = tuple(itertools.chain(
    orderlines[0].cases,
    orderlines[1].cases,
    orderlines[2].cases,
    orderlines[3].cases,
    orderlines[6].cases,
))


test(packing.MRBL, cases, (120,80))
test(packing.GBAF, cases, (120,80), splitting="shorteraxis")
test(packing.SWWF, cases, (120,80))
