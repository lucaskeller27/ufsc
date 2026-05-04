from limite import AnimalLimite

class AnimalControle:
    def __init__(self):
        self._boundary = AnimalLimite()
    
    def criar_cachorro(self):
        return self._boundary.criar_cachorro()
    
    def criar_gato(self):
        return self._boundary.criar_gato()
    
    def criar_canarinho(self, tamanho_passo, altura_voo):
        return self._boundary.criar_canarinho(tamanho_passo, altura_voo)
    
    def mover_animal(self, animal):
        return self._boundary.mover_animal(animal)
    
    def produzir_som_animal(self, animal):
        return self._boundary.produzir_som_animal(animal)
    
    def fazer_cachorro_latir(self):
        return self._boundary.cachorro_latir()
    
    def fazer_gato_miar(self):
        return self._boundary.gato_miar()
    
    def fazer_canarinho_cantar(self):
        return self._boundary.canarinho_cantar()
    
    def get_cachorro(self):
        return self._boundary.get_cachorro()
    
    def get_gato(self):
        return self._boundary.get_gato()
    
    def get_canarinho(self):
        return self._boundary.get_canarinho()
    
    def demonstrar_animais(self):
        resultados = []
        
        # Criar animais
        cachorro = self.criar_cachorro()
        gato = self.criar_gato()
        canarinho = self.criar_canarinho(5, 10)
        
        # Teste 3: Animais caminhando
        resultados.append("=== TESTE 3: Animais Caminhando ===")
        resultados.append(self.mover_animal(cachorro))
        resultados.append(self.mover_animal(gato))
        resultados.append(self.mover_animal(canarinho))
        
        # Teste 4: Animais produzindo sons
        resultados.append("\n=== TESTE 4: Animais Produzindo Sons ===")
        resultados.append(self.produzir_som_animal(cachorro))
        resultados.append(self.produzir_som_animal(gato))
        resultados.append(self.produzir_som_animal(canarinho))
        
        # Métodos específicos
        resultados.append("\n=== MÉTODOS ESPECÍFICOS ===")
        resultados.append(f"Cachorro latindo: {self.fazer_cachorro_latir()}")
        resultados.append(f"Gato miando: {self.fazer_gato_miar()}")
        resultados.append(f"Canarinho cantando: {self.fazer_canarinho_cantar()}")
        
        # Teste 5: Teste da herança (Mamifero.produzir_som base)
        resultados.append("\n=== TESTE 5: Teste da Herança ===")
        resultados.append("Nota: Mamifero é classe abstrata, não pode ser instanciada")
        resultados.append("O método produzir_som da classe Mamifero retornaria:")
        resultados.append('"MAMIFERO: PRODUZ SOM: X" (onde X é o volume)')
        
        return resultados
    
    def executar_menu_animais(self):
        """
        Método interativo para demonstrar os animais
        """
        print("=" * 50)
        print("SISTEMA DE ANIMAIS")
        print("=" * 50)
        
        # Criar animais
        cachorro = self.criar_cachorro()
        gato = self.criar_gato()
        
        print("\n--- CACHORRO ---")
        print(f"Tamanho do passo: {cachorro.tamanho_passo}")
        print(f"Volume do som: {cachorro.volume_som}")
        print(f"Ação: {self.mover_animal(cachorro)}")
        print(f"Som: {self.produzir_som_animal(cachorro)}")
        
        print("\n--- GATO ---")
        print(f"Tamanho do passo: {gato.tamanho_passo}")
        print(f"Volume do som: {gato.volume_som}")
        print(f"Ação: {self.mover_animal(gato)}")
        print(f"Som: {self.produzir_som_animal(gato)}")
        
        print("\n--- CANARINHO ---")
        tamanho_passo = int(input("Digite o tamanho do passo do canarinho: "))
        altura_voo = int(input("Digite a altura de voo do canarinho: "))
        
        canarinho = self.criar_canarinho(tamanho_passo, altura_voo)
        print(f"Tamanho do passo: {canarinho.tamanho_passo}")
        print(f"Altura de voo: {canarinho.altura_voo}")
        print(f"Ação: {self.mover_animal(canarinho)}")
        print(f"Som: {self.produzir_som_animal(canarinho)}")
        
        print("\n" + "=" * 50)