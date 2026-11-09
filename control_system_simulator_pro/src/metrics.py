import numpy as np

def calculate_metrics(t,y):

    y=np.array(y)

    final=y[-1]

    rise=np.where(y>=0.9*final)[0]

    rise_time=0

    if len(rise)>0:

        rise_time=t[rise[0]]

    peak=np.max(y)

    peak_time=t[np.argmax(y)]

    overshoot=(
        (peak-final)/final
    )*100

    return {

        "Rise Time":round(rise_time,3),

        "Peak Time":round(peak_time,3),

        "Overshoot":round(overshoot,3)
    }