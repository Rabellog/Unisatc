renda=float(input("Digite qual a sua renda anual: "))
educacao=float(input("Digite qual o seu gasto anual com educação: "))
dep=float(input("Digite qual o gasto de dispensas médicas anuais: "))

if renda < 27110.40:
    deducao=0
    aliquota=0
    base=renda-deducao
    imposto=(base/100)*aliquota

if (renda >= 27110.40) and (renda < 33919.80):
    deducao=dep+educacao+2033.28
    aliquota=7.5
    base=renda-deducao
    imposto=(base/100)*aliquota
    
if (renda >= 33919.81) and (renda < 45012.60):
    deducao=dep+educacao+4577.27
    aliquota=15
    base=renda-deducao
    imposto=(base/100)*aliquota

if (renda >= 450126.61) and (renda < 55976.16):
    deducao=dep+educacao+7953.21
    aliquota=22.5
    base=renda-deducao
    imposto=(base/100)*aliquota

if (renda > 55976.16):
    deducao=dep+educacao+10752.02
    aliquota=27.5
    base=renda-deducao
    imposto=(base/100)*aliquota

print(f"O imposto seu de renda anual é {imposto}")