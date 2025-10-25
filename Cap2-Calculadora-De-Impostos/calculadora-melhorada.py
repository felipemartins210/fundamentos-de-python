# Faixas do IR (mensal 2025) como constantes
IR_FAIXAS = [
    {
        "min": 0.00,
        "max": 2259.20,
        "aliquota": 0.0,
        "deducao": 0.0
    },
    {
        "min": 2259.21,
        "max": 2826.65,
        "aliquota": 0.075,
        "deducao": 169.44
    },
    {
        "min": 2826.66,
        "max": 3751.05,
        "aliquota": 0.15,
        "deducao": 381.44
    },
    {
        "min": 3751.06,
        "max": 4664.68,
        "aliquota": 0.225,
        "deducao": 662.77
    },
    {
        "min": 4664.69,
        "max": float("inf"),  # Acima de 4664,68
        "aliquota": 0.275,
        "deducao": 896.00
    }
]

# Função para calcular o IR com base nas faixas definidas
def calcular_ir(salario):
    for faixa in IR_FAIXAS:
        if faixa["min"] <= salario <= faixa["max"]:
            return salario * faixa["aliquota"] - faixa["deducao"]
    return 0.0

# Teste
salario = 4000.0
imposto = calcular_ir(salario)
print(f"Salário: R$ {salario:.2f} - Imposto de Renda: R$ {imposto:.2f}")
