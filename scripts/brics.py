# BRICS

import pandas as pd
from util import to_code, root

brics = ["Brazil", "Russian Federation", "India", "China", "South Africa"]

index = [to_code(name) for name in brics]

df = pd.DataFrame({"Name": brics}, index=index)
df.index.name = "Code"

assert len(df) == 5
assert len(df.index.unique()) == len(df)
assert len(df.Name.unique()) == len(df)

df.to_csv(root / "data/brics.csv")
