dados = ['nome', 'logradouro', 'numero', 'complemento', 'bairro', 'cep', 'cidade', 'uf']
dados_usuario = {}

for dado in dados:
    pergunta = "Por favor insira seu {}: ".format(dado)
    dados_usuario[dado] = input(pergunta)

formatCep = dados_usuario['cep']
cep = '{}-{}'.format(formatCep[:5], formatCep[5:])
dados_usuario['cep'] = cep

carta = """
{}
{}, {} {}
{}
{} {}/{}"""

print(carta.format(
    dados_usuario['nome'],
    dados_usuario['logradouro'],
    dados_usuario['numero'],
    dados_usuario['complemento'],
    dados_usuario['bairro'],
    dados_usuario['cep'],
    dados_usuario['cidade'],
    dados_usuario['uf']
))