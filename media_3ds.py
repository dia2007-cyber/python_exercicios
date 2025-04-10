import webbrowser
import os

materias = ["Português", "Matemática", "História", "Geografia", "Ciências"]
num_bimestres = 4
alunos = []

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para terminar): ")
    if nome.lower() == "sair":
        break
    alunos.append({"nome": nome, "notas": {materia: [0] * num_bimestres for materia in materias}})

for aluno in alunos:
    for materia in materias:
        for i in range(num_bimestres):
            while True:
                entrada = input(f"Digite a nota do aluno {aluno['nome']} na matéria de {materia} no bimestre {i + 1}: ")
                try:
                    nota = float(entrada)
                    if 0 <= nota <= 10:
                        aluno["notas"][materia][i] = nota
                        break
                    else:
                        print("Por favor, digite uma nota entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número válido.")

html_path = "notas_alunos.html"
with open(html_path, "w", encoding="utf-8") as pagina:
    pagina.write("""
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="utf-8">
            <title>Notas dos Alunos</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                h1 { color: #2c3e50; }
                table { border-collapse: collapse; width: 100%; margin-top: 20px; }
                th, td { border: 1px solid #ddd; padding: 8px; text-align: center; }
                th { background-color: #f2f2f2; }
                tr:nth-child(even) { background-color: #f9f9f9; }
                tr:hover { background-color: #f1f1f1; }
            </style>
        </head>
        <body>
            <h1>Notas dos Alunos</h1>
    """)

    for aluno in alunos:
        pagina.write(f"<h2>{aluno['nome']}</h2>")
        pagina.write("""
            <table>
                <tr>
                    <th>Matéria</th>
                    <th>1º Bimestre</th>
                    <th>2º Bimestre</th>
                    <th>3º Bimestre</th>
                    <th>4º Bimestre</th>
                    <th>Média</th>
                </tr>
        """)

        for materia in materias:
            notas = aluno["notas"][materia]                                           
            media = sum(notas) / num_bimestres                                     
            notas_html = []

            for nota in notas:                                                                                                                                                                
                notas_html.append(f"<td>{nota:.2f}</td>")

            media_color = 'red' if media < 6 else 'green'
            notas_html.append(f"<td style='color: {media_color};'>{media:.2f}</td>")
            
            pagina.write(f"<tr><td>{materia}</td>{''.join(notas_html)}</tr>")

        pagina.write("""
            </table>
        """)

    pagina.write("""
        </body>
        </html>
    """)                   
webbrowser.open('file://' + os.path.realpath(html_path))