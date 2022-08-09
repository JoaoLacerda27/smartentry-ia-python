import reconhecimento_placa as rp
import reconhecimento_caracter as rc
import conexao

if __name__ == "__main__":

    rp.reconhecePlaca()
    reconhece_caracter = rc.Reconhece()
    reconhece_caracter.validaPlaca()