import pandas as pd
from src.pipeline import transform

def test_conc_dfs():
    df1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    df2 = pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]})
    
    arrange = pd.concat([df1, df2], ignore_index=True)
    act = transform.concat_data_frames([df1, df2])

    assert arrange.equals(act)

