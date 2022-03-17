
def TeordeUmidade_peso(peso_dos_solidos, peso_da_agua,  peso_total=None):
    if peso_da_agua is None and peso_total is not None:
        return ((peso_total - peso_dos_solidos)/peso_dos_solidos)*100
    else:
        return (peso_da_agua/peso_dos_solidos)*100

def TeordeUmidade_massa(massa_dos_solidos, massa_da_agua,  massa_total=None):
    if massa_da_agua is None and massa_total is not None:
        return ((massa_total - massa_dos_solidos)/massa_dos_solidos)*100
    else:
        return (massa_da_agua/massa_dos_solidos)*100

def IndicedeVazios(volume_de_vazios, volume_dos_solidos):
    return volume_de_vazios/volume_dos_solidos

def Porosidade(volume_de_vazios, volume_total):
    return volume_de_vazios/volume_total

def GraudeSaturacao(volume_de_agua, volume_de_vazios):
    return (volume_de_agua, volume_de_vazios)*100

def PesoEspecifico(peso, volume):
    return peso/volume

def PesoEspecificodosSolidos(peso_dos_solidos, volume_dos_solidos):
    return peso_dos_solidos/volume_dos_solidos




