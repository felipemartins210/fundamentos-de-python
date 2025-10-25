# Constantes
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

# Solicita as entradas do usuário
gross_income = float(input("Digite a renda bruta anual: "))
num_dependents = int(input("Digite o número de dependentes: "))

# Calcula o imposto de renda
taxable_income = gross_income - STANDARD_DEDUCTION - (DEPENDENT_DEDUCTION * num_dependents)

income_tax = taxable_income * TAX_RATE

# Exibe o resultado
print("A taxa é: R$ " + str(income_tax))

