programa
{
	inclua biblioteca Util
	inclua biblioteca Matematica --> mat
	
	funcao inicio()
	{
//Definindo variáveis
		real peso, altura, imc, aimc,  
		somaIdadeHJ=0.0,  somaIdadeHA=0.0,  somaIdadeHE=0.0,
		somaPesoHJ=0.0,   somaPesoHA=0.0,   somaPesoHE=0.0,
		somaAlturaHJ=0.0, somaAlturaHA=0.0, somaAlturaHE=0.0,
		somaImcHJ=0.0,    somaImcHA=0.0,    somaImcHE=0.0,
		
		somaIdadeMJ=0.0,  somaIdadeMA=0.0,  somaIdadeME=0.0,
		somaPesoMJ=0.0,   somaPesoMA=0.0,   somaPesoME=0.0,
		somaAlturaMJ=0.0, somaAlturaMA=0.0, somaAlturaME=0.0,
		somaImcMJ=0.0,    somaImcMA=0.0,    somaImcME=0.0,
		
		totalImc=0.0,     totalImcH=0.0,    totalImcM=0.0,
		
		mIdadeHJ=0.0,     mIdadeHA=0.0,     mIdadeHE=0.0,
		mPesoHJ=0.0,      mPesoHA=0.0,      mPesoHE=0.0,
		mAlturaHJ=0.0,    mAlturaHA=0.0,    mAlturaHE=0.0,
		mImcHJ=0.0,       mImcHA=0.0,       mImcHE=0.0,
		
		mIdadeMJ=0.0,     mIdadeMA=0.0,     mIdadeME=0.0,
		mPesoMJ=0.0,      mPesoMA=0.0,      mPesoME=0.0,
		mAlturaMJ=0.0,    mAlturaMA=0.0,    mAlturaME=0.0,
		mImcMJ=0.0,       mImcMA=0.0, 	 mImcME=0.0,	
							
		mImcTotal=0.0,    mImcMulher=0.0, 	 mImcHomem=0.0,
		
		amIdadeHJ=0.0,    amIdadeHA=0.0, 	 amIdadeHE=0.0,
		amPesoHJ=0.0,     amPesoHA=0.0, 	 amPesoHE=0.0,
		amAlturaHJ=0.0,   amAlturaHA=0.0, 	 amAlturaHE=0.0,
		amImcHJ=0.0,      amImcHA=0.0, 	 amImcHE=0.0,
		
		amIdadeMJ=0.0,    amIdadeMA=0.0, 	 amIdadeME=0.0,
		amPesoMJ=0.0,     amPesoMA=0.0, 	 amPesoME=0.0,
		amAlturaMJ=0.0,   amAlturaMA=0.0, 	 amAlturaME=0.0,
		amImcMJ=0.0,      amImcMA=0.0, 	 amImcME=0.0, 
		
		amImcTotal=0.0,   amImcMulher=0.0,	 amImcHomem=0.0
		
		cadeia nome

		inteiro idade, sexo, grupo=0, totalEntrev=0, totalEntrevM=0, totalEntrevH=0,
		contJovemH=0, contAdultoH=0, contExpertH=0, contJovemM=0, contAdultoM=0, contExpertM=0

		caracter f, s='s', S='S', n='n', N='N', cento=s
		
	    
//montando a calculadora
faca
{
	escreva("\nCalcule seu IMC para saber sua condição de peso!")
	escreva("\n=================================================\n")
	escreva("\nQual seu nome: ")
	leia(nome)
	limpa()
		
	faca
		{
	    	   escreva("\nQual sua idade (anos): ")
	    	   leia(idade)
	    	   limpa()
	    	   escreva("\nVocê precisa ter mais de 18 anos para responder esta pesquisa!\n")
	   	   			  
	    	se (idade > 99)
			{
				limpa()
				escreva("Você tem ",idade," anos? (s/n): ")					
				leia(cento)

	        		se (cento == s ou cento == S)
	        		limpa()
	     	   		
				se (cento == n ou cento == N)
				{
				escreva("\nQual sua idade (anos): ")
	        		leia(idade)
	        		limpa()
	        		}
	        	}
		}
	     enquanto (idade >= 0 e idade < 18)
	     limpa()

	faca
		{
	    	   escreva("\nQual seu peso (kg): ")
	    	   leia(peso)
	    	   limpa()
	    	   escreva("\nVocê precisa ter mais de 25 quilos para responder esta pesquisa!\n")
		  
	    	se (peso > 150)
			{
				limpa()
				escreva("Você tem ",peso," quilos? (s/n): ")					
				leia(cento)

	        		se (cento == s ou cento == S)
	        		limpa()
	        		
				se (cento == n ou cento == N)
				{
					escreva("\nQual seu peso (kg): ")
	        			leia(peso)
	     	   		limpa()
	     	   	}
	     	}
		}
	enquanto (peso >= 0 e peso < 25)
	     limpa()

	faca
		{
			escreva("\nQual sua altura (cm): ")
			leia(altura)
			limpa()
	    		escreva("\nVocê precisa ter mais de 1 metro (100 cm) para responder esta pesquisa!\n")
			  
	     	se (altura > 200)
				{
					limpa()
					escreva("Você tem ",altura / 100," metros? (s/n): ")					
					leia(cento)

	     	   		se (cento == s ou cento == S)
	     	   		limpa()
	     	   		
					se (cento == n ou cento == N)
					{
					escreva("\nQual seu altura (cm): ")
	     	   		leia(altura)
	     	   		limpa()}
	     	   	}
		}
	enquanto (altura >= 0 e altura < 100)
	limpa()

	faca
		{
			escreva("\nPara Mulher digite \"1\", para Homem digite \"2\": ")
	     	leia(sexo)
	         	Util.aguarde(1000)
	         	limpa()
	         	escreva("Digite apenas 1 ou 2")
		}
	enquanto (sexo != 1 e sexo != 2)
	limpa()

//Calculando IMC

imc = (peso/(altura*altura))*10000
aimc = mat.arredondar(imc, 2)


escreva(nome, ", seu IMC é: ",aimc)
escreva("\n|")
escreva("\n|")

	se (imc >= 18.5 e imc <= 24.9)
	{
		escreva("\n===>>> IMC 18,5 a 24,9   :     PESO IDEAL")
		escreva("\n       IMC abaixo de 18,5: ABAIXO DO PESO")
		escreva("\n       IMC acima de 24,9 :  ACIMA DO PESO")
		escreva("\n")
		escreva("\n=========================================")
	}   
	
	senao se (imc < 18.5)
	{
		escreva("\n|      IMC 18,5 a 24,9   :     PESO IDEAL")
		escreva("\n===>>> IMC abaixo de 18,5: ABAIXO DO PESO")
		escreva("\n       IMC acima de 24,9 :  ACIMA DO PESO")
		escreva("\n")
		escreva("\n=========================================")
	}   	                
	senao se (imc > 24.9)
	{
		escreva("\n|      IMC 18,5 a 24,9   :     PESO IDEAL")
		escreva("\n|      IMC abaixo de 18,5: ABAIXO DO PESO")
		escreva("\n===>>> IMC acima de 24,9 :  ACIMA DO PESO")
		escreva("\n")
		escreva("\n=========================================")
	}
	     
escreva("\n\nDeseja continuar a pesquisa? (s/n)")
leia(f)
limpa()

//Definindo Grupos
				
	se (sexo == 1)
	{
		se (idade >= 18 e idade <= 32)
		{
			grupo = 1
			contJovemM = contJovemM + 1
			somaIdadeMJ = somaIdadeMJ + (idade)
			somaPesoMJ = somaPesoMJ + (peso)
			somaAlturaMJ = somaAlturaMJ + (altura)
			somaImcMJ = somaImcMJ + (imc)
		}
	
		se (idade >= 33 e idade <= 60)
		{
			grupo = 2
			contAdultoM = contAdultoM + 1
			somaIdadeMA = somaIdadeMA + (idade)
			somaPesoMA = somaPesoMA + (peso)
			somaAlturaMA = somaAlturaMA + (altura)
			somaImcMA = somaImcMA + (imc)
		}
	
		se (idade >= 61)
		{
			grupo = 3
			contExpertM = contExpertM + 1
			somaIdadeME = somaIdadeME + (idade)
			somaPesoME = somaPesoME + (peso)
			somaAlturaME = somaAlturaME + (altura)
			somaImcME = somaImcME + (imc)
		}
	}

	se (sexo == 2)
	{
		se (idade >= 18 e idade <= 32)
		{
			grupo = 4
			contJovemH = contJovemH + 1
			somaIdadeHJ = somaIdadeHJ + (idade)
			somaPesoHJ = somaPesoHJ + (peso)
			somaAlturaHJ = somaAlturaHJ + (altura)
			somaImcHJ = somaImcHJ + (imc)
		}

		se (idade >= 33 e idade <= 60)
		{
			grupo = 5
			contAdultoH = contAdultoH + 1
			somaIdadeHA = somaIdadeHA + (idade)
			somaPesoHA = somaPesoHA + (peso)
			somaAlturaHA = somaAlturaHA + (altura)
			somaImcHA = somaImcHA + (imc)
		}

		se (idade >= 61)
		{
			grupo = 6
			contExpertH = contExpertH + 1
			somaIdadeHE = somaIdadeHE + (idade)
			somaPesoHE = somaPesoHE + (peso)
			somaAlturaHE = somaAlturaHE + (altura)
			somaImcHE = somaImcHE + (imc)
		}
	}
}
enquanto (f != n e f != N)

//Calculando totais de Entrevistados e IMCs

totalEntrevM = contJovemM + contAdultoM + contExpertM
totalEntrevH = contJovemH + contAdultoH + contExpertH
totalEntrev = totalEntrevM + totalEntrevH

totalImcM = somaImcMJ + somaImcMA + somaImcME
totalImcH = somaImcHJ + somaImcHA + somaImcHE
totalImc = totalImcM + totalImcH


//Calculando Médias

//	escolha (grupo)
//		{
//		caso 1:
	se (contJovemM > 0)
		{
			mIdadeMJ = somaIdadeMJ / contJovemM
			mPesoMJ = somaPesoMJ / contJovemM
			mAlturaMJ = (somaAlturaMJ / contJovemM)/100
			mImcMJ = somaImcMJ / contJovemM
			amIdadeMJ = mat.arredondar(mIdadeMJ, 2)
			amPesoMJ = mat.arredondar(mPesoMJ, 2)
			amAlturaMJ = mat.arredondar(mAlturaMJ, 2)
			amImcMJ = mat.arredondar(mImcMJ, 2)
		}
//		pare

//		caso 2:
	se (contAdultoM > 0)
		{
			mIdadeMA = somaIdadeMA / contAdultoM
			mPesoMA = somaPesoMA / contAdultoM
			mAlturaMA = (somaAlturaMA / contAdultoM)/100
			mImcMA = somaImcMA / contAdultoM
			amIdadeMA = mat.arredondar(mIdadeMA, 2)
			amPesoMA = mat.arredondar(mPesoMA, 2)
			amAlturaMA = mat.arredondar(mAlturaMA, 2)
			amImcMA = mat.arredondar(mImcMA, 2)
		}
//		pare

//		caso 3:
	se (contExpertM > 0)
		{
			mIdadeME = somaIdadeME / contExpertM
			mPesoME = somaPesoME / contExpertM
			mAlturaME = (somaAlturaME / contExpertM)/100
			mImcME = somaImcME / contExpertM
			amIdadeME = mat.arredondar(mIdadeME, 2)
			amPesoME = mat.arredondar(mPesoME, 2)
			amAlturaME = mat.arredondar(mAlturaME, 2)
			amImcME = mat.arredondar(mImcME, 2)
		}
//		pare

//		caso 4:
	se (contJovemH > 0)
		{
			mIdadeHJ = somaIdadeHJ / contJovemH
			mPesoHJ = somaPesoHJ / contJovemH
			mAlturaHJ = (somaAlturaHJ / contJovemH)/100
			mImcHJ = somaImcHJ / contJovemH
			amIdadeHJ = mat.arredondar(mIdadeHJ, 2)
			amPesoHJ = mat.arredondar(mPesoHJ, 2)
			amAlturaHJ = mat.arredondar(mAlturaHJ, 2)
			amImcHJ = mat.arredondar(mImcHJ, 2)
		}
//		pare

//		caso 5:
	se (contAdultoH > 0)
		{
			mIdadeHA = somaIdadeHA / contAdultoH
			mPesoHA = somaPesoHA / contAdultoH
			mAlturaHA = (somaAlturaHA / contAdultoH)/100
			mImcHA = somaImcHA / contAdultoH
			amIdadeHA = mat.arredondar(mIdadeHA, 2)
			amPesoHA = mat.arredondar(mPesoHA, 2)
			amAlturaHA = mat.arredondar(mAlturaHA, 2)
			amImcHA = mat.arredondar(mImcHA, 2)
		}
//		pare

//		caso 6:
	se (contExpertH > 0)
		{
			mIdadeHE = somaIdadeHE / contExpertH
			mPesoHE = somaPesoHE / contExpertH
			mAlturaHE = (somaAlturaHE / contExpertH)/100
			mImcHE = somaImcHE / contExpertH
			amIdadeHE = mat.arredondar(mIdadeHE, 2)
			amPesoHE = mat.arredondar(mPesoHE, 2)
			amAlturaHE = mat.arredondar(mAlturaHE, 2)
			amImcHE = mat.arredondar(mImcHE, 2)
		}
//		pare
//		}


mImcMulher = (somaImcMJ + somaImcMA + somaImcME) / totalEntrevM
amImcMulher = mat.arredondar(mImcMulher, 2)
	
mImcHomem = (somaImcHJ + somaImcHA + somaImcHE) / totalEntrevH
amImcHomem = mat.arredondar(mImcHomem, 2)
	
mImcTotal = (somaImcMJ + somaImcMA + somaImcME + somaImcHJ + somaImcHA + somaImcHE) / totalEntrev
amImcTotal = mat.arredondar(mImcTotal, 2)

// Montando Relatórios
Util.aguarde(1866) //rsrsrs
escreva("Total de Entrevistados: ",totalEntrev," - (Média de IMC: ",amImcTotal,")")
Util.aguarde(500)
			
se (totalEntrevH > 0)
	{
	escreva("\n\nTotal de Homens Entrevistados: ",totalEntrevH," - (Média de IMC: ",amImcHomem,")")
	Util.aguarde(500)
	}
			
se (totalEntrevM > 0)
	{
	escreva("\n\nTotal de Mulheres Entrevistadas: ",totalEntrevM," - (Média de IMC: ",amImcMulher,")")
	Util.aguarde(500)
	}
	
se (contJovemH > 0)
	{
	escreva("\n\nTotal de Homens entre 18 e 32 anos: ",contJovemH)
	Util.aguarde(500)
	escreva("\nMédia de Idade:                     ",amIdadeHJ," anos")
	Util.aguarde(500)
	escreva("\nMédia de Peso:                      ",amPesoHJ," Kg")
	Util.aguarde(500)
	escreva("\nMédia de Altura:                    ",amAlturaHJ," M")
	Util.aguarde(500)
	escreva("\nMédia de IMC:                       ",amImcHJ)
	Util.aguarde(500)
	}

se (contJovemM > 0)
	{
	escreva("\n\nTotal de Mulheres entre 18 e 32 anos: ",contJovemM)
	Util.aguarde(500)
	escreva("\nMédia de Idade:                       ",amIdadeMJ," anos")
	Util.aguarde(500)
	escreva("\nMédia de Peso:                        ",amPesoMJ," Kg")
	Util.aguarde(500)
	escreva("\nMédia de Altura:                      ",amAlturaMJ," M")
	Util.aguarde(500)
	escreva("\nMédia de IMC:                         ",amImcMJ)
	Util.aguarde(500)
	}

se (contAdultoH > 0)
	{
	escreva("\n\nTotal de Homens entre 33 e 60 anos: ",contAdultoH)
	Util.aguarde(500)
	escreva("\nMédia de Idade:                     ",amIdadeHA," anos")
	Util.aguarde(500)
	escreva("\nMédia de Peso:                      ",amPesoHA," Kg")
	Util.aguarde(500)
	escreva("\nMédia de Altura:                    ",amAlturaHA," M")
	Util.aguarde(500)
	escreva("\nMédia de IMC:                       ",amImcHA)
	Util.aguarde(500)
	}

se (contAdultoM > 0)
	{
	escreva("\n\nTotal de Mulheres entre 33 e 60 anos: ",contAdultoM)
	Util.aguarde(500)
	escreva("\nMédia de Idade:                       ",amIdadeMA," anos")
	Util.aguarde(500)
	escreva("\nMédia de Peso:                        ",amPesoMA," Kg")
	Util.aguarde(500)
	escreva("\nMédia de Altura:                      ",amAlturaMA," M")
	Util.aguarde(500)
	escreva("\nMédia de IMC:                         ",amImcMA)
	Util.aguarde(500)
	}

se (contExpertH > 0)
	{
	escreva("\n\nTotal de Homens acima de 60 anos: ",contExpertH)
	Util.aguarde(500)
	escreva("\nMédia de Idade:                   ",amIdadeHE," anos")
	Util.aguarde(500)
	escreva("\nMédia de Peso:                    ",amPesoHE," Kg")
	Util.aguarde(500)
	escreva("\nMédia de Altura:                  ",amAlturaHE," M")
	Util.aguarde(500)
	escreva("\nMédia de IMC:                     ",amImcHE)
	Util.aguarde(500)
	}
	

se (contExpertM > 0)
	{
	escreva("\n\nTotal de Mulheres acima de 60 anos: ",contExpertM)
	Util.aguarde(500)
	escreva("\nMédia de Idade:                     ",amIdadeME," anos")
	Util.aguarde(500)
	escreva("\nMédia de Peso:                      ",amPesoME," Kg")
	Util.aguarde(500)
	escreva("\nMédia de Altura:                    ",amAlturaME," M")
	Util.aguarde(500)
	escreva("\nMédia de IMC:                       ",amImcME)
	Util.aguarde(500)
	}
			
escreva("\n\n")

	}
//Fim do algoritmo
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 9232; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */