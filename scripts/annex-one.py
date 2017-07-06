# Annex I parties

import os

import pandas as pd

from util import to_code, to_short_name

path = os.path.dirname(os.path.realpath(__file__))

url = "http://unfccc.int/parties_and_observers/parties/annex_i/items/2774.php"

annex_one = pd.read_html(url, attrs = {'class': "list_table"})[0]

annex_one = annex_one.iloc[1:, 1]

annex_one.name = "Name"

annex_one = annex_one.apply(lambda x: x.replace(" **", ""))

annex_one.index = annex_one.apply(to_code)

annex_one = pd.Series(
    [to_short_name(code) for code in annex_one.index],
    index=annex_one.index
)

annex_one.index.name = "Code"
annex_one.name = "Name"

assert len(annex_one) == 43

annex_one.to_csv(os.path.join(path, "../data/annex-one.csv"), header=True)
