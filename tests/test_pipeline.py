"""Tests for unit functionalities."""

import pandas as pd

from app.pipeline.transform import transforma_em_um_unico

# Sample data for testing
df1 = pd.DataFrame({"A": [1, 2, 3], "B": ["a", "b", "c"]})
df2 = pd.DataFrame({"A": [4, 5, 6], "B": ["d", "e", "f"]})


def test_transform() -> None:
    """Test the transformation of dataframes."""
    data = [df1, df2]
    consolidated_df = transforma_em_um_unico(data)
    assert len(consolidated_df) == 6  # 3 rows from df1 + 3 rows from df2
    assert list(consolidated_df.columns) == ["A", "B"]
