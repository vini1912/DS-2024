livros = float(input('quantos livros você deseja comprar?'))
print('[1]:R$0,25 por livro + R$7,50 fixo')
print('[2]:R$0,50 por livro + R$2,50 fixo')

if livros <= 20:
    print('a melhor opção de desconto é [1]')
else:
    print('a melhor opção de desconto é [2]')