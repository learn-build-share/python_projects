import pandas as pd

def save_report(
        analysis,
        filename
):

    df = pd.DataFrame([analysis])

    df.to_csv(
        filename,
        index=False
    )