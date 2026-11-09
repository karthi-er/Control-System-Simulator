import pandas as pd

def export_csv(
        time,
        response,
        filename
):

    df=pd.DataFrame({

        "Time":time,

        "Response":response

    })

    df.to_csv(
        filename,
        index=False
    )