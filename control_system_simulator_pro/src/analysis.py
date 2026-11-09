import control
import matplotlib.pyplot as plt

def bode_plot():

    G=control.TransferFunction(
        [1],
        [1,2,1]
    )

    control.bode_plot(
        G,
        dB=True
    )

    plt.show()