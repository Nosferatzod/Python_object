from modelos.carro import Carro  

def main():
    carro1 = Carro(marca="BMW", modelo="M5", cor="preto")
    carro2 = Carro(marca="Toyota", modelo="Supra", cor="amarelo")
    carro3 = Carro(marca="Honda", modelo="Civic", cor="prata")
    
    carros = [carro1, carro2, carro3]
    
    for carro in carros:
        carro.ligar()

if __name__ == "__main__":
    main()
