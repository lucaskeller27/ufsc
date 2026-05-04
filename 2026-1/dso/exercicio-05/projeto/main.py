from controle import AnimalControle

def main():
    controle = AnimalControle()
    
    # Executa a demonstração completa
    resultados = controle.demonstrar_animais()
    
    for resultado in resultados:
        print(resultado)
    
    # controle.executar_menu_animais()

if __name__ == "__main__":
    main()