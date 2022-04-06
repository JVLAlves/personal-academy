package svgident

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/require"
)

func TestSearches(t *testing.T) {
	//Arquivo com duas imagens em base64
	f := "imgs.svg"

	//Chamada da função que verifica a existencia de imagens em um SVG
	isImage, err := SearchImg(f)
	require.NoError(t, err)      //Não pode haver nenhum erro em execução normal
	require.NotEmpty(t, isImage) //Não pode retornar uma resposta vazia ou "zerada" (0, "", nil etc.)
	fmt.Println("Is there any image? ", isImage)

	//No caso de haver alguma imagem, procurar quais são as tags que as apresentam
	if isImage {
		//Chamada da função que busca pela tag image
		imgs, errimgs := GetImage(f)
		require.NoError(t, errimgs)               //Não pode haver nenhum erro em execução normal
		require.NotEmpty(t, imgs)                 //Não pode retornar uma resposta vazia ou "zerada" (0, "", nil etc.)
		fmt.Printf("list of images:\n%v\n", imgs) //Lista de tags image
	}

	//Teste de erro para arquivos inexistentes
	_, Ferr := SearchImg("foo.svg")
	require.Error(t, Ferr)
	fmt.Println(Ferr)

	//Teste de arquivos que não contém imagens
	isImageF, _ := SearchImg("wns-14.svg")
	require.NotEqual(t, isImageF, isImage)
	fmt.Println("Is there any image? ", isImageF)

}

func TestFilter(t *testing.T) {

	//lista de arquivos svg
	var filelist = []string{"icon.svg", "imgs.svg", "wns-14.svg"}

	//chamada da função que busca quais arquivos não contém imagens
	vList, eList := GetValidFiles(filelist)
	require.NotEqual(t, vList, eList) //Lista de valrores não pode ser igual a lista de erros
	require.NotEmpty(t, vList)        //Não pode retornar uma resposta vazia ou "zerada" (0, "", nil etc.)
	require.NotEmpty(t, eList)        //Não pode retornar uma resposta vazia ou "zerada" (0, "", nil etc.)
	fmt.Println(vList, eList)

	//Lista de arquivos que não contém imagens
	sFileList := []string{"wns-14.svg"}
	v2list, errs := GetValidFiles(sFileList)
	require.NotEmpty(t, v2list)                   //Não pode retornar uma resposta vazia ou "zerada" (0, "", nil etc.)
	require.Equal(t, len(v2list), len(sFileList)) //Tamanho da lista de resposta precisa ser identico ao tamanho da lista de entrada
	require.Nil(t, errs)                          //Não pode haver nenhum erro em execução normal

	//Lista de arquivos que possuem imagens
	tFileList := []string{"icon.svg", "imgs.svg"}
	_, errList := GetValidFiles(tFileList)
	require.NotNil(t, errList)                     //è necessário que haja um erro intencional (existencia de imagens no arquivo svg)
	require.Equal(t, len(errList), len(tFileList)) //Tamanho da lista de resposta precisa ser identico ao tamanho da lista de entrada

	//Lista de  arquivos inexistentes
	_, errListT := GetValidFiles([]string{"foo.svg", "bar.svg"})
	require.NotEmpty(t, errListT) //Teste de erro
}

func TestGetimgs(t *testing.T) {

	var filewith string = "icon.svg"      //Arquivo com imagem
	var filewithout string = "wns-14.svg" //Arquivo sem imagem

	//Chamada da função que busca as imagens em um svg
	imgs, noerr := GetImage(filewith)
	require.NoError(t, noerr) //Não pode haver nenhum erro em execução normal
	require.NotEmpty(t, imgs) //Não pode retornar uma resposta vazia ou "zerada" (0, "", nil etc.)

	noimgs, err := GetImage(filewithout)

	require.Error(t, err)    //Precisa apresentar erro sob a condição do arquivo não conter imagens
	require.Empty(t, noimgs) //Precisa ser vazio, uma vez que não há nada a retornar

	//teste de erro para arquivos inexistentes
	_, Ferr := GetImage("foo.svg")
	require.Error(t, Ferr)

}

func TestNoImage(t *testing.T) {

	nErr := NoImageFile("imgs.svg")
	require.NoError(t, nErr)

	yErr := NoImageFile("wns-14.svg")
	require.Error(t, yErr)

	yErr2 := NoImageFile("foo.svg")
	require.Error(t, yErr2)

}
