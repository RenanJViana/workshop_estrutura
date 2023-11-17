"""modulo de extract necessárias para consolidar os dados de entrada."""

import glob
import os
from typing import List

import pandas as pd


def extract_excel(input_folder: str) -> List[pd.DataFrame]:
    """Função para extrair dados de arquivos Excel.

    Parameters
    ----------
    input_folder : str
        Pasta onde estão os arquivos Excel

    Returns
    -------
    List[pd.DataFrame]
        Lista de DataFrames

    Raises
    ------
    ValueError
        Não há arquivos Excel na pasta especificada
    """
    files = glob.glob(os.path.join(input_folder, "*.xlsx"))

    if not files:
        raise ValueError("No Excel files found in the specified folder")

    all_data = [pd.read_excel(file) for file in files]
    return all_data
