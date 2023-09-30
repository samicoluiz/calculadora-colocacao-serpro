from pdfminer.high_level import extract_text
import re
import pandas as pd
import string

pattern = re.compile(r'\/ \d+, \w+.+ \/')
# text = extract_text("./input_datasets/ED_6_SERPRO_RES_FINAL_PROVA_PRATICA_CONV_BIO_HETERO.pdf")
# with open('resultado2-1.txt', 'w') as f:
#     f.write(text)

# with open('resultado2.txt', 'r') as f:
#     text = f.read()

# text = text.replace('\n', '').replace('\x0c', '').replace('  ', ' ')
# text = text.split('/')
# text = [x.split(',') for x in text]	
# df = pd.DataFrame(text)
# df

text = extract_text("./clean_datasets/ED_3_SERPRO_RES_FIN_OBJ_CONV_PRAT.pdf")
with open('resultado1-1.txt', 'w') as f:
    f.write(text)