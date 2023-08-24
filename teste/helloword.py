# informacaodoteclado = int (input()) #usa a hashtag pra comentar e saber o que fez CTRL e ; ou CTRL / caso vc queira comentar uma linha do código --> O pg não ler isso
# print(informacaodoteclado==2)


peso = float(input('digite seu peso (kg):'))
altura = float(input('digite sua altura (m):'))
IMC = peso/(altura**2)   
print("Seu IMC é: ", IMC)       #iimc isso é uma forma de dar uma entrada      
print ("Muito abaixo do peso?", IMC  < 17)            
print ("Estou abaixo do peso?", 17 <= IMC < 18.5)
print ("Peso dentro do normal?", 18.5 <= IMC < 25.0)
print ("Acima do peso?", 25.0 <= IMC < 30)
print ("Muito acima do peso?", 30 <= IMC > 30)
