import pandas as pd
import re

sep_dflt = ","
out_fmt = "%Y-%m-%d"

fpath = "~/temp.csv"

df = pd.read_csv(fpath, sep=sep_dflt)

rexp = re.compile(r'date', re.IGNORECASE)
date_cols = df.columns[df.columns.str.contains(rexp)]

df[date_cols] = df[date_cols].apply(
    pd.to_datetime,
    args=('coerce', False, False, None, None, True, None, False, 'unix', True)
    )

df[date_cols] = df[date_cols].apply(lambda t: t.dt.strftime(out_fmt))

df.to_csv(fpath)
