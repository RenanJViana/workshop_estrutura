"""modulo com todas as transformações necessárias para consolidar os dados de entrada."""

from typing import List

import pandas as pd


def transforma_em_um_unico(all_data: List[pd.DataFrame]) -> pd.DataFrame:
    """Função para consolidar os dados de arquivos Excel.

    Parameters
    ----------
    all_data: List[pd.DataFrame]
        Lista de DataFrames

    Returns
    -------
    consolidated_df : pd.DataFrame
        DataFrame consolidado

    Raises
    ------
    ValueError
        Não há arquivos Excel para concatenar
    """
    if not all_data:
        raise ValueError("No data to transform")

    consolidated_df = pd.concat(all_data, axis=0, ignore_index=True)
    return consolidated_df
