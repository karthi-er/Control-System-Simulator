from scipy.optimize import minimize

def tune():

    def objective(x):

        kp,ki,kd=x

        return (
            kp-2
        )**2 + (
            ki-0.5
        )**2 + (
            kd-0.1
        )**2

    result=minimize(
        objective,
        [1,1,1]
    )

    return result.x