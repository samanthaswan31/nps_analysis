# QTON_BL_202502280718
import pyopenms as oms
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# load data
exp = oms.MSExperiment()
oms.MzMLFile().load("data/sample1.mzML", exp)

# convert to pandas dataframe
df = exp.get_df()
df.head(2)