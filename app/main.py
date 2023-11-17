"""pipeline principal do projeto."""

from pipeline.extract import extract_excel
from pipeline.load import load_em_um_novo_excel
from pipeline.transform import transforma_em_um_unico

if __name__ == '__main__':
    lista_df = extract_excel(input_folder='data/input')
    df = transforma_em_um_unico(lista_df)
    load_em_um_novo_excel(
        df, output_folder='data/output', output_file_name='output.xlsx'
    )
