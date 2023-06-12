import pandas as pd

arq = 'planilha.xlsx'

tb = pd.ExcelFile(arq)
print(tb.sheet_names)

if 'Planilha1' in tb.sheet_names:
    print(tb.parse('Planilha1'))
else:
    print('não existe')