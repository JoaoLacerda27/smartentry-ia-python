import reconhecimento_placa as rp
import reconhecimento_caracter as rc

if __name__ == "__main__":
    rp.reconhecePlaca()
    rc.Reconhece().reconheceCaracter()

    if(rc.Reconhece().validaPlaca()):
        print("Placa permitida! ")
    else:
        print("Placa Negada! ")