## Conjunto de Dados
# Os dados estão disponíveis em formato csv (‘vendas_ficticias.csv’) e contêm as seguintes informações para cada venda:

#   •	Data da venda
#   •	Valor da venda
#   •	Vendedor
#   •	Quantidade vendida
#   •	Produto


# from tabulate import tabulate

# print(tabulate(arquivo.head(), headers='keys', tablefmt='fancy_grid'))

# f = open('vendas_ficticias.csv', 'r')

# data = f.read()

# rows = data.split('\n')

# print(rows)

# full_data = []

# for row in rows:
#     split_row = row.split(",")
#     full_data.append(split_row)

# print(full_data)

import pandas as pd

df = pd.read_csv('vendas_ficticias.csv', sheet_name = None)
display(df)
df.head()

# import imaplib
# import email
# import pandas as pd
# from openpyxl import load_workbook

# # Configurações do e-mail
# EMAIL = 'seu_email@example.com'
# PASSWORD = 'sua_senha'
# IMAP_SERVER = 'imap.exemplo.com'
# REMETENTE_ESPECIFICO = 'remetente@example.com'
# ASSUNTO_CONTEM = 'APLICACAO'

# # Conectar ao servidor de e-mail
# mail = imaplib.IMAP4_SSL(IMAP_SERVER)
# mail.login(EMAIL, PASSWORD)
# mail.select('inbox')

# # Buscar e-mails não lidos do remetente específico com assunto contendo "APLICACAO"
# status, messages = mail.search(None, f'(UNSEEN FROM "{REMETENTE_ESPECIFICO}" SUBJECT "{ASSUNTO_CONTEM}")')

# # Lista para armazenar os dados extraídos
# data = []

# # Processar cada e-mail
# for num in messages[0].split():
#     status, msg_data = mail.fetch(num, '(RFC822)')
#     msg = email.message_from_bytes(msg_data[0][1])
    
#     if msg.is_multipart():
#         for part in msg.walk():
#             if part.get_content_type() == 'text/plain':
#                 body = part.get_payload(decode=True).decode()
#                 data.append(body)
#     else:
#         body = msg.get_payload(decode=True).decode()
#         data.append(body)

# # Fechar a conexão com o servidor de e-mail
# mail.logout()

# # Criar ou atualizar a planilha Excel
# file_path = 'emails.xlsx'

# try:
#     # Se o arquivo existir, carregar e atualizar
#     book = load_workbook(file_path)
#     writer = pd.ExcelWriter(file_path, engine='openpyxl')
#     writer.book = book
# except FileNotFoundError:
#     # Se o arquivo não existir, criar um novo
#     writer = pd.ExcelWriter(file_path, engine='openpyxl')

# # Converter dados para DataFrame
# df = pd.DataFrame(data, columns=['Conteúdo'])

# # Escrever dados na planilha
# df.to_excel(writer, sheet_name='Emails', index=False)
# writer.save()
# writer.close()

# print("Processo concluído com sucesso!")