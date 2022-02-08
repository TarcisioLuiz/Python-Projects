
import fdescontos
func = 'josé'
salario = 500

desconto_inss = fdescontos.descinss(func, salario)
print(desconto_inss)
desconto_irpf = fdescontos.descirpf(func, salario)
print(desconto_irpf)
desconto_vt = fdescontos.descvt(func, salario)
print(desconto_vt)