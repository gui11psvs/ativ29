# Crie um programa que receba uma lista com os nomes dos alunos presentes em uma aula e exiba quantos alunos estão presentes e a lista dos nomes. Se o total de alunos presentes for menor que 5, exiba uma mensagem sugerindo uma revisão da lista de chamada.

# Exemplo de entrada:
# Alunos presentes: ['Ana', 'Bruno', 'Carlos', 'Daniela']

# Exemplo de saída:
# Alunos presentes: 4
# Lista de alunos presentes: Ana, Bruno, Carlos, Daniela
# Aviso: Poucos alunos presentes. Revisar lista de chamada.

lunos_presentes = ['Ana', 'Bruno', 'Carlos', 'Daniela']

# Calcula o número de alunos presentes
numero_alunos_presentes = len(alunos_presentes)

# Exibe o número de alunos presentes e a lista de nomes
print(f"Alunos presentes: {numero_alunos_presentes}")
print(f"Lista de alunos presentes: {', '.join(alunos_presentes)}")

# Verifica se o número de alunos presentes é menor que 5
if numero_alunos_presentes < 5:
    print("Aviso: Poucos alunos presentes. Revisar lista de chamada.")