package Hydro


type Velocidade struct {
	value float64
	unit  string

}

type Diametro struct {
	value float64
	unit string
}

func (D Diametro)Raio()float64{
	return D.value/2
}
