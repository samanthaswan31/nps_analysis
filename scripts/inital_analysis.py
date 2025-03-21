# QTON_BL_202502280718
import pyopenms as oms
import numpy as np
import matplotlib.pyplot as plt

# load data
exp = oms.MSExperiment()
oms.MzMLFile().load("data/sample1.mzML", exp)

# inspect properties
def plot_spectra_2D_overview(experiment):
    rows = 200.0
    cols = 200.0
    exp.updateRanges()

    bilip = oms.BilinearInterpolation()
    tmp = bilip.getData()
    tmp.resize(int(rows), int(cols))
    bilip.setData(tmp)
    bilip.setMapping_0(0.0, exp.getMinRT(), rows - 1, exp.getMaxRT())
    bilip.setMapping_1(0.0, exp.getMinMZ(), cols - 1, exp.getMaxMZ())
    for spec in exp:
        if spec.getMSLevel() == 1:
            mzs, ints = spec.get_peaks()
            rt = spec.getRT()
            for i in range(0, len(mzs)):
                bilip.addValue(rt, mzs[i], ints[i])

    data = np.ndarray(shape=(int(cols), int(rows)), dtype=np.float64)
    for i in range(int(rows)):
        for j in range(int(cols)):
            data[i][j] = bilip.getData().getValue(i, j)

    plt.imshow(np.rot90(data), cmap="gist_heat_r")
    plt.xlabel("retention time (s)")
    plt.ylabel("m/z")
    plt.xticks(
        np.linspace(0, int(rows), 20, dtype=int),
        np.linspace(exp.getMinRT(), exp.getMaxRT(), 20, dtype=int),
    )
    plt.yticks(
        np.linspace(0, int(cols), 20, dtype=int),
        np.linspace(exp.getMinMZ(), exp.getMaxMZ(), 20, dtype=int)[::-1],
    )
    plt.show()


plot_spectra_2D_overview(exp)