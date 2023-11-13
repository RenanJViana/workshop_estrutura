"""pipeline principal do projeto."""

from pipeline.extract import extract_excel

lista_df = extract_excel(input_folder="data/input")
print(*lista_df, sep="\n\n")
