import os
from pynput import keyboard

a = 0

class bcolors:
    OKBLUE = '\033[94m'
    ENDC = '\033[0m'
    BLUE_WHITE_INICIO = '\033[0;37;44m'
    BLUE_WHITE_FIM = '\033[0m 0;37;44m'
    BLACK_WHITE_INICIO = '\033[0;37;48m'
    BLACK_WHITE_FIM = '\033[0m 0;37;48m'

def on_press(key):
	pass
		
def limparTela():
	os.system('clear') or None

def criaMenu(Opcoes, i):
	def print_espaco(n):
		while n > 0:
			print(" ", end = "")
			n -= 1
			
	limparTela()
	
	global a
	a = i
	
	Elementos = len(Opcoes) - 1
	
	maior = 0
	for Opcao in Opcoes:
		if len(Opcao) > maior:
			maior = len(Opcao)
	
	for indice, Opcao in enumerate(Opcoes):
		if i == indice:
			print(bcolors.OKBLUE + bcolors.BLUE_WHITE_INICIO  + " " + Opcao + " ", end = "")
			print_espaco((maior - len(Opcao)))
			print(bcolors.ENDC + bcolors.OKBLUE + bcolors.ENDC)
		else:
			print(bcolors.OKBLUE + bcolors.BLACK_WHITE_INICIO + " " + Opcao + " " + bcolors.ENDC + bcolors.OKBLUE + bcolors.ENDC)
	
	def on_release(key):
		global a
		if key == keyboard.Key.esc:
			return False
		if key == keyboard.Key.down:
			if a >= 0 and a < Elementos:
				a += 1
		if key == keyboard.Key.up:
			if a <= Elementos and a > 0:
				a -= 1
		criaMenu(Opcoes, a)
		
	with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
		listener.join()
		
li = ['Sim, concordo com as regras', 'Não, discordo das regras', 'Sair']
criaMenu(li, 0)
