package sniper_test

import (
	"fmt"
	"reflect"
	sniper "sniper/snipercmd"
	"strconv"
	"testing"

	"github.com/stretchr/testify/require"
)

func TestGetFields(t *testing.T) {
	//Teste da função
	Fields, err := sniper.GetAllFields(sniper.IP, sniper.TOKEN)
	require.NoError(t, err)
	require.NotEmpty(t, Fields)

	kind := reflect.ValueOf(Fields).Kind()
	fmt.Println(kind)

	//Teste de erro de conexão ou ip
	_, Ferr1 := sniper.GetAllFields("127.127.127:8000", sniper.TOKEN)
	require.Error(t, Ferr1)

	//Teste de erro de autenticação
	_, Ferr2 := sniper.GetAllFields(sniper.IP, "")
	require.Error(t, Ferr2)

}

func TestGetAssets(t *testing.T) {

	Assets, err1 := sniper.GetAssets(sniper.IP, sniper.TOKEN)
	require.NoError(t, err1)
	require.NotEmpty(t, Assets)

	limit := 3
	AssetsOnlyLimit, errOnlyLimit := sniper.GetAssets(sniper.IP, sniper.TOKEN, strconv.Itoa(limit))
	require.NoError(t, errOnlyLimit)
	require.NotEmpty(t, AssetsOnlyLimit)
	require.Equal(t, limit, len(AssetsOnlyLimit))

	AssetsSorted, errSorted := sniper.GetAssets(sniper.IP, sniper.TOKEN, strconv.Itoa(limit), "name")
	require.NoError(t, errSorted)
	require.NotEmpty(t, AssetsSorted)
	require.Equal(t, limit, len(AssetsSorted))
	require.NotEqual(t, AssetsSorted, AssetsOnlyLimit)

	/*
		fmt.Println(AssetsOnlyLimit)
		fmt.Println(AssetsSorted)
	*/

}

func TestGetAssetsErrors(t *testing.T) {

	_, fErrorIp := sniper.GetAssets("10.10.10:8000", sniper.TOKEN)
	require.Error(t, fErrorIp)

	_, fErrorToken := sniper.GetAssets(sniper.IP, "ajsjgaojfpaspfkaopkfpaskp")
	require.Error(t, fErrorToken)

	_, fErrorLimit := sniper.GetAssets(sniper.IP, sniper.TOKEN, strconv.Itoa(0))
	require.Error(t, fErrorLimit)

	//não há erro no caso de uma palavra invalida
	_, fErrorSort := sniper.GetAssets(sniper.IP, sniper.TOKEN, "null")
	require.Error(t, fErrorSort)

}

func TestToShortAndFields(t *testing.T) {
	var ListOfAssets []sniper.AssetT
	Assets, _ := sniper.GetAssets(sniper.IP, sniper.TOKEN, "5")
	for _, a := range Assets {

		ListOfAssets = append(ListOfAssets, a.ToShort())
	}

	require.NotEmpty(t, ListOfAssets)
	fmt.Println(ListOfAssets)

	FullFields := sniper.Fields(Assets[0], "")
	ShortFields := sniper.Fields(ListOfAssets[0], "json")
	require.NotEmpty(t, FullFields)
	require.NotEmpty(t, ShortFields)
	require.NotEqual(t, FullFields, ShortFields)

	fmt.Println(sniper.Fields(Assets[0], ""))
	fmt.Println(sniper.Fields(ListOfAssets[0], "json"))

}

func TestGetAssetById(t *testing.T) {

	Asset, err := sniper.GetAssetById(sniper.IP, sniper.TOKEN, 31)
	require.NoError(t, err)
	require.NotEmpty(t, Asset)
	fmt.Println(Asset)

	_, fError := sniper.GetAssetById(sniper.IP, sniper.TOKEN, 0)
	require.Error(t, fError)

}

func TestGetAssetByTag(t *testing.T) {

	Asset, err := sniper.GetAssetByTag(sniper.IP, sniper.TOKEN, "00047")
	require.NoError(t, err)
	require.NotEmpty(t, Asset)

	_, fError := sniper.GetAssetByTag(sniper.IP, sniper.TOKEN, "00000")
	require.Error(t, fError)

	v := reflect.ValueOf(Asset)

	values := make([]interface{}, v.NumField())

	for i := 0; i < v.NumField(); i++ {
		values[i] = v.Field(i).Interface()
		fmt.Println(v.Type().Field(i).Name)
	}

	for _, val := range values {
		fmt.Printf("%v is a %T\n", val, val)
	}
}

func TestCompare(t *testing.T) {

	MyPCAsset, _ := sniper.GetAssetByTag(sniper.IP, sniper.TOKEN, "00047")
	require.NotEmpty(t, MyPCAsset)
	AnotherPc, _ := sniper.GetAssetByTag(sniper.IP, sniper.TOKEN, "00046")
	require.NotEmpty(t, AnotherPc)

	Req, err := MyPCAsset.Compare(AnotherPc)
	require.NoError(t, err)
	require.NotEmpty(t, Req)

	fmt.Println(Req)
}

func TestPut(t *testing.T) {
	MyPCAsset, _ := sniper.GetAssetByTag(sniper.IP, sniper.TOKEN, "00047")
	require.NotEmpty(t, MyPCAsset)
	AnotherPc, _ := sniper.GetAssetByTag(sniper.IP, sniper.TOKEN, "00046")
	require.NotEmpty(t, AnotherPc)

	Req, _ := MyPCAsset.Compare(AnotherPc)
	fmt.Println(Req)
	Result, err := sniper.Put(sniper.IP, sniper.TOKEN, MyPCAsset.ID, Req)
	require.NoError(t, err)
	require.NotEmpty(t, Result)

}

func TestPatch(t *testing.T) {

	MyPCAsset, _ := sniper.GetAssetByTag(sniper.IP, sniper.TOKEN, "00047")
	require.NotEmpty(t, MyPCAsset)
	AnotherPc, _ := sniper.GetAssetByTag(sniper.IP, sniper.TOKEN, "00047")
	require.NotEmpty(t, AnotherPc)

	Req, Patchable := MyPCAsset.CompareAsset(AnotherPc)
	fmt.Printf("PATCH: %v\tREQUEST: %#v\n", Patchable, Req)
	if Patchable {
		Result, err := sniper.Patch(sniper.IP, sniper.TOKEN, MyPCAsset.ID, Req)
		require.NoError(t, err)
		require.NotEmpty(t, Result)
	}

	_, errIp := sniper.Patch("127.127.127:8000", sniper.TOKEN, MyPCAsset.ID, Req)
	require.Error(t, errIp)

	_, errTOKEN := sniper.Patch(sniper.IP, "dajdsapodpoasdpao", MyPCAsset.ID, Req)
	require.Error(t, errTOKEN)

	_, errID := sniper.Patch(sniper.IP, sniper.TOKEN, -1, Req)
	require.Error(t, errID)

	_, errREQ := sniper.Patch(sniper.IP, sniper.TOKEN, MyPCAsset.ID, "adopafapokspof")
	require.Error(t, errREQ)

}

func TestDelete(t *testing.T) {

	DeletableAsset, _ := sniper.GetAssetByTag(sniper.IP, sniper.TOKEN, "000404")
	fmt.Println(DeletableAsset)
	require.Equal(t, "TESTE", DeletableAsset.Name)

	_, errIp := sniper.Delete("127.127.127:8000", sniper.TOKEN, DeletableAsset.ID)
	require.Error(t, errIp)

	_, errTOKEN := sniper.Delete(sniper.IP, "dajdsapodpoasdpao", DeletableAsset.ID)
	require.Error(t, errTOKEN)

	_, errID := sniper.Delete(sniper.IP, sniper.TOKEN, -1)
	require.Error(t, errID)

	DelResp, errDel := sniper.Delete(sniper.IP, sniper.TOKEN, DeletableAsset.ID)
	require.NoError(t, errDel)
	require.NotEmpty(t, DelResp)

}

func TestPost(t *testing.T) {

	Asset := sniper.AssetT{
		Name:     "postTest",
		AssetTag: "00404",
		StatusID: "5",
		ModelID:  "10",
		SO:       "Linux - Ubuntu",
		Hostname: "DNZ-JVA",
	}

	fmt.Printf("%#v\n", Asset)

	err := sniper.Post(sniper.IP, sniper.TOKEN, Asset)
	require.NoError(t, err)
}
