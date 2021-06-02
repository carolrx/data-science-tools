"""
Arquivos para tutorial
Exemplo de comentario multilinha para python
"""

# Comentarios em python podem ser realizados desse modo :

# declaracao de variaveis, podemos observar que não foi necessário definir o
# tipo
elemento_a = 20
elemento_b = 30

# Vamos a nosso primeiro tópico, como exibir para o usuário algo em python
# isso é feito através do metodo print
print("Alô mundo")

resultado = elemento_a + elemento_b
print("O resultado da soma é ", resultado)
# outra maneira de apresenta o resultado é através de um recurso
# chamado f string
print(f"O resultado da soma é {resultado}")

# Agora que tal checarmos o tipo presente no resultado
print(type(resultado))

# Agora se tentarmos somarmos variaveis de tipo distintos obtemos o seguinte
# resultado:
# Executando essa linha vai ocorrer um erro
print("Esse erro é proposital")
tipo_distintos = elemento_a + "laranja"

