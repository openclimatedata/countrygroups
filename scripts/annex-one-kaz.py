# Annex I parties

import pandas as pd

from util import to_code, root

annex_one = pd.read_csv(root / "data/annex-one.csv", index_col=0)

assert len(annex_one) == 43

# In accordance with the COP conclusion (FCCC/CP/2001/13/Add.4, section V.C.)
# and following ratification by Kazakhstan of the Kyoto Protocol on 19 June
# 2009 and its entry into force on 17 September 2009, Kazakhstan is considered
# an Annex I Party for the purposes of the Protocol but remains to be a
# non-Annex I Party for the purposes of the Convention.

annex_one.loc[to_code("Kazakhstan")] = "Kazakhstan"
annex_one = annex_one.sort_index()
annex_one.to_csv(root / "data/annex-one-kaz.csv")
