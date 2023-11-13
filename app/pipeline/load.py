"""modulo com todas as transformações necessárias para consolidar os dados de entrada."""

import os

import pandas as pd


def load_em_um_novo_excel(
    df: pd.DataFrame, output_folder: str, output_file_name: str
) -> None:
    """Salva um DataFrame em um arquivo Excel.

    Parameters
    ----------

    df: pd.DataFrame
        Data frame para exportar

    output_folder: str
        Pasta onde será salvo o arquivo

    output_file_name: str
        Nome do arquivo a ser salvo

    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    df.to_excel(
        os.path.join(output_folder, output_file_name), index=False
    )  # Retirado engine='openpyxl'
