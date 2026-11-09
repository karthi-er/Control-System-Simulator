import numpy as np

def simulate_first_order(pid):

    dt = 0.01

    time = np.arange(0,10,dt)

    response = []

    y = 0

    setpoint = 1

    for t in time:

        error = setpoint - y

        control = pid.update(error,dt)

        tau = 1.5

        dy = (
            -y + control
        ) / tau

        y += dy * dt

        response.append(y)

    return time,response