def optimize(df, show = True):
    
    import numpy as np
    import pandas as pd

    start_mem = np.sum(df.memory_usage()) / 1024**2
    
    ## Work on floats
    floats = df.select_dtypes(include=['float64']).columns.tolist()
    df[floats] = df[floats].apply(pd.to_numeric, downcast='float')

    ## Work o ints
    ints = df.select_dtypes(include=['int64']).columns.tolist()
    df[ints] = df[ints].apply(pd.to_numeric, downcast='integer')

    ## Work on objects
    obj = [i for i in df.columns if df[i].dtypes.name == 'object']
    
    for i in obj:
        try:
            df[i] = pd.to_datetime(df[i])
        except:
            if len(df[i].unique())/len(df[i]) < 0.5:
                df[i] = df[i].astype('category')
    
    end_mem = np.sum(df.memory_usage()) / 1024**2

    if show:
        print(('Original memory usage: {:.2f} MB').format(start_mem))    
        print(('Optimized memory usage: {:.2f} MB').format(end_mem))
        print('Optimization {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))       

    return df
