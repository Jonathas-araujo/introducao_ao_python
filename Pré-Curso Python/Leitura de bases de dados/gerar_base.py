import pandas as pd
import numpy as np

# Base ficticia de atendimentos ambulatoriais em UBS (Unidade Basica de Saude)
# Propositalmente "suja": duplicatas, ausentes, outliers, texto com espacos e
# codigos inconsistentes -- para servir de estudo de caso do pipeline completo.

dados = {
    "NOME": [
        "Maria da Silva", "Joao Pedro Souza", "Ana Paula Lima", "Carlos Eduardo",
        "  Francisca Alves  ", "Jose Ferreira", "Maria da Silva", "Rita de Cassia",
        "Antonio Carlos", "Juliana Santos", "Pedro Henrique", "  Marcos Vinicius",
        "Sandra Regina", "Luiz Gonzaga", "Patricia Gomes", "Roberto Carlos",
        "Fernanda Dias", "Joao Pedro Souza", "Camila Ribeiro", "Bruno Costa",
        "Vera Lucia", "Marcos Vinicius", "Aline Cristina", "Rafael Nunes",
        "Silvia Helena", "Eduardo Pires", "Tatiane Moraes", "Gabriel Rocha",
        "Larissa Melo", "Diego Fernandes", "Monica Barbosa", "Thiago Araujo",
        "Cristina Farias", "Vinicius Teixeira", "Adriana Castro", "Renato Lopes",
        "Beatriz Cardoso", "Felipe Andrade", "Simone Ramos", "Wagner Duarte",
    ],
    "SEXO": [
        "F", "M", "F", "M", "F", "M", "F", "F", "M", "F", "M", "M", "F", "M",
        "F", "M", "F", "M", "F", "M", "F", "M", "F", "M", "F", "M", "F", "M",
        "F", "M", "F", "M", "F", "M", "F", "M", "F", "M", "F", 9,
    ],
    "IDADE": [
        34, 45, 200, 29, 61, np.nan, 34, 52, 8, 27, 39, 71, 44, np.nan, 19,
        33, 58, 45, 22, 47, 66, 71, 31, 15, 49, -5, 60, 26, 38, 42, 55, 30,
        24, 68, 37, 41, 12, 53, 46, 63,
    ],
    "PESO_KG": [
        68.5, 82.0, 75.3, np.nan, 59.8, 90.1, 68.5, 71.2, 30.4, 62.0, 77.5,
        0.0, 65.9, 88.3, 54.2, 79.0, 61.7, 82.0, 58.4, 95.6, 66.3, 84.1,
        63.5, 45.0, 70.2, 78.9, 60.1, 33.7, 57.8, 81.4, 69.9, 74.6, np.nan,
        87.2, 64.0, 76.3, 40.2, 80.5, 67.8, 72.1,
    ],
    "UBS": [
        "UBS Central", "UBS Central", "UBS Norte", " UBS Sul", "UBS Norte",
        "UBS Central", "UBS Central", "UBS Sul", "UBS Norte", "UBS Central",
        "UBS Sul", "UBS Norte", "UBS Central", "UBS Sul", "UBS Norte",
        "UBS Central", "UBS Sul", "UBS Central", "UBS Norte", "UBS Central",
        "UBS Sul", "UBS Norte", "UBS Central", "UBS Sul", "UBS Norte",
        "UBS Central", "UBS Sul", "UBS Norte", "UBS Central", "UBS Sul",
        "UBS Norte", "UBS Central", "UBS Sul", "UBS Norte", "UBS Central",
        "UBS Sul", "UBS Norte", "UBS Central", "UBS Sul", "UBS Norte",
    ],
    "DT_ATENDIMENTO": [
        "2026-03-02", "2026-03-02", "2026-03-03", "2026-03-03", "2026-03-04",
        "2026-03-04", "2026-03-02", "2026-03-05", "2026-03-05", "2026-03-06",
        "2026-03-06", "2026-03-07", "2026-03-07", "2026-03-08", "2026-03-08",
        "2026-03-09", "2026-03-09", "2026-03-02", "2026-03-10", "2026-03-10",
        "2026-03-11", "2026-03-07", "2026-03-12", "2026-03-12", "2026-03-13",
        "2026-03-13", "2026-03-14", "2026-03-14", "2026-03-15", "2026-03-15",
        "2026-03-16", "2026-03-16", "2026-03-17", "2026-03-17", "2026-03-18",
        "2026-03-18", "2026-03-19", "2026-03-19", "2026-03-20", "2026-03-20",
    ],
}

df = pd.DataFrame(dados)
df.to_csv("pacientes.csv", index=False, sep=";", encoding="utf-8")
print(df.shape)
print(df.head())
