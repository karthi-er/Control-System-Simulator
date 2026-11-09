import numpy as np

def calculate_metrics(t,r,target=1.0):
    rise=float(t[np.argmax(r>=0.9*target)]) if np.any(r>=0.9*target) else None
    overshoot=float((r.max()-target)/target*100)
    return {'rise_time':rise,'overshoot_percent':overshoot}
