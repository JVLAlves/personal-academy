package sniper

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"net/http"
	"strconv"
	"strings"

	"github.com/rodaine/table"
)

//Modelo para coleta e envio de dados do computador.
type AssetT struct {
	ModelID   string `json:"model_id"`
	StatusID  string `json:"status_id"`
	AssetTag  string `json:"asset_tag"`
	Name      string `json:"name"`
	SO        string `json:"_snipeit_so_3"`
	Model     string `json:"_snipeit_modelo_7"`
	Hostname  string `json:"_snipeit_hostname_5"`
	HD        string `json:"_snipeit_hd_4"`
	CPU       string `json:"_snipeit_cpu_6"`
	Memory    string `json:"_snipeit_memoria_2"`
	Installed string `json:"_snipeit_programas_instalados_10"`
	Office    string `json:"_snipeit_office_9"`
}

//Modelo geral de RESPONSE
type GlobalResponseT struct {
	Status   string `json:"status"`
	Messages string `json:"messages"`
	Payload  struct {
		ModelID        int    `json:"model_id"`
		Name           string `json:"name"`
		Serial         string `json:"serial"`
		CompanyID      int    `json:"company_id"`
		OrderNumber    string `json:"order_number"`
		Notes          string `json:"notes"`
		AssetTag       string `json:"asset_tag"`
		UserID         int    `json:"user_id"`
		Archived       string `json:"archived"`
		Physical       string `json:"physical"`
		Depreciate     string `json:"depreciate"`
		StatusID       int    `json:"status_id"`
		WarrantyMonths string `json:"warranty_months"`
		PurchaseCost   string `json:"purchase_cost"`
		PurchaseDate   string `json:"purchase_date"`
		AssignedTo     string `json:"assigned_to"`
		SupplierID     string `json:"supplier_id"`
		Requestable    int    `json:"requestable"`
		RtdLocationID  string `json:"rtd_location_id"`
		UpdatedAt      string `json:"updated_at"`
		CreatedAt      string `json:"created_at"`
		ID             int    `json:"id"`
		Model          struct {
			ID                     int    `json:"id"`
			Name                   string `json:"name"`
			ModelNumber            string `json:"model_number"`
			ManufacturerID         int    `json:"manufacturer_id"`
			CategoryID             int    `json:"category_id"`
			CreatedAt              string `json:"created_at"`
			UpdatedAt              string `json:"updated_at"`
			DepreciationID         int    `json:"depreciation_id"`
			Eol                    int    `json:"eol"`
			Image                  string `json:"image"`
			DeprecatedAtivoAddress int    `json:"deprecated_Ativo_address"`
			FieldsetID             int    `json:"fieldset_id"`
			Notes                  string `json:"notes"`
			Requestable            int    `json:"requestable"`
		} `json:"model"`
	} `json:"payload"`
}

//Modelo de respose do m??todo PATCH
type PatchResponseT struct {
	Status   string `json:"status"`
	Messages string `json:"messages"`
	Payload  struct {
		ID                   int    `json:"id"`
		Name                 string `json:"name"`
		AssetTag             string `json:"asset_tag"`
		ModelID              int    `json:"model_id"`
		Serial               string `json:"serial"`
		PurchaseDate         string `json:"purchase_date"`
		PurchaseCost         string `json:"purchase_cost"`
		OrderNumber          string `json:"order_number"`
		AssignedTo           string `json:"assigned_to"`
		Notes                string `json:"notes"`
		Image                string `json:"image"`
		UserID               int    `json:"user_id"`
		CreatedAt            string `json:"created_at"`
		UpdatedAt            string `json:"updated_at"`
		Physical             int    `json:"physical"`
		DeletedAt            string `json:"deleted_at"`
		StatusID             int    `json:"status_id"`
		Archived             int    `json:"archived"`
		WarrantyMonths       string `json:"warranty_months"`
		Depreciate           int    `json:"depreciate"`
		SupplierID           int    `json:"supplier_id"`
		Requestable          bool   `json:"requestable"`
		RtdLocationID        int    `json:"rtd_location_id"`
		Accepted             string `json:"accepted"`
		LastCheckout         string `json:"last_checkout"`
		ExpectedCheckin      string `json:"expected_checkin"`
		CompanyID            int    `json:"company_id"`
		AssignedType         string `json:"assigned_type"`
		LastAuditDate        string `json:"last_audit_date"`
		NextAuditDate        string `json:"next_audit_date"`
		LocationID           int    `json:"location_id"`
		CheckinCounter       int    `json:"checkin_counter"`
		CheckoutCounter      int    `json:"checkout_counter"`
		RequestsCounter      int    `json:"requests_counter"`
		SnipeitImei1         string `json:"_snipeit_imei_1"`
		SnipeitPhoneNumber2  string `json:"_snipeit_phone_number_2"`
		SnipeitRAM3          string `json:"_snipeit_ram_3"`
		SnipeitCPU4          string `json:"_snipeit_cpu_4"`
		SnipeitAtivoAddress5 string `json:"_snipeit_Ativo_address_5"`
	} `json:"payload"`
}

//Modelo de response do m??todo GET
type GlobalGetT struct {
	ID       int    `json:"id"`
	Name     string `json:"name"`
	AssetTag string `json:"asset_tag"`
	Serial   string `json:"serial"`
	Model    struct {
		ID   int    `json:"id"`
		Name string `json:"name"`
	} `json:"model"`
	ModelNumber string `json:"model_number"`
	Eol         string `json:"eol"`
	StatusLabel struct {
		ID         int    `json:"id"`
		Name       string `json:"name"`
		StatusType string `json:"status_type"`
		StatusMeta string `json:"status_meta"`
	} `json:"status_label"`
	Category struct {
		ID   int    `json:"id"`
		Name string `json:"name"`
	} `json:"category"`
	Manufacturer struct {
		ID   int    `json:"id"`
		Name string `json:"name"`
	} `json:"manufacturer"`
	Supplier    string `json:"supplier"`
	Notes       string `json:"notes"`
	OrderNumber string `json:"order_number"`
	Company     struct {
		ID   int    `json:"id"`
		Name string `json:"name"`
	} `json:"company"`
	Location struct {
		ID   int    `json:"id"`
		Name string `json:"name"`
	} `json:"location"`
	RtdLocation struct {
		ID   int    `json:"id"`
		Name string `json:"name"`
	} `json:"rtd_location"`
	Image           string `json:"image"`
	AssignedTo      string `json:"assigned_to"`
	WarrantyMonths  string `json:"warranty_months"`
	WarrantyExpires string `json:"warranty_expires"`
	CreatedAt       struct {
		Datetime  string `json:"datetime"`
		Formatted string `json:"formatted"`
	} `json:"created_at"`
	UpdatedAt struct {
		Datetime  string `json:"datetime"`
		Formatted string `json:"formatted"`
	} `json:"updated_at"`
	LastAuditDate string `json:"last_audit_date"`
	NextAuditDate string `json:"next_audit_date"`
	DeletedAt     string `json:"deleted_at"`
	PurchaseDate  string `json:"purchase_date"`
	LastCheckout  struct {
		Datetime  string `json:"datetime"`
		Formatted string `json:"formatted"`
	} `json:"last_checkout"`
	ExpectedCheckin string `json:"expected_checkin"`
	PurchaseCost    string `json:"purchase_cost"`
	CheckinCounter  int    `json:"checkin_counter"`
	CheckoutCounter int    `json:"checkout_counter"`
	RequestsCounter int    `json:"requests_counter"`
	UserCanCheckout bool   `json:"user_can_checkout"`
	CustomFields    struct {
		Modelo struct {
			Field       string `json:"field"`
			Value       string `json:"value"`
			FieldFormat string `json:"field_format"`
		} `json:"Modelo"`
		Hostname struct {
			Field       string `json:"field"`
			Value       string `json:"value"`
			FieldFormat string `json:"field_format"`
		} `json:"Hostname"`
		Hd struct {
			Field       string `json:"field"`
			Value       string `json:"value"`
			FieldFormat string `json:"field_format"`
		} `json:"HD"`
		CPU struct {
			Field       string `json:"field"`
			Value       string `json:"value"`
			FieldFormat string `json:"field_format"`
		} `json:"CPU"`
		MemRia struct {
			Field       string `json:"field"`
			Value       string `json:"value"`
			FieldFormat string `json:"field_format"`
		} `json:"Memoria"`
		SO struct {
			Field       string `json:"field"`
			Value       string `json:"value"`
			FieldFormat string `json:"field_format"`
		} `json:"S.O."`
		Office struct {
			Field       string `json:"field"`
			Value       string `json:"value"`
			FieldFormat string `json:"field_format"`
		} `json:"Office"`
		Setor struct {
			Field       string `json:"field"`
			Value       string `json:"value"`
			FieldFormat string `json:"field_format"`
		} `json:"Setor"`
		ProgramasInstalados struct {
			Field       string `json:"field"`
			Value       string `json:"value"`
			FieldFormat string `json:"field_format"`
		} `json:"Programas Instalados"`
	} `json:"custom_fields"`
	AvailableActions struct {
		Checkout bool `json:"checkout"`
		Checkin  bool `json:"checkin"`
		Clone    bool `json:"clone"`
		Restore  bool `json:"restore"`
		Update   bool `json:"update"`
		Delete   bool `json:"delete"`
	} `json:"available_actions"`
}

//Modelo de reponse de ERRO
type ErrorT struct {
	Status   string `json:"status"`
	Messages string `json:"messages"`
	Payload  string `json:"payload"`
}

//Modelo exclusivo para ID
type IDT struct {
	ID int `json:"id"`
}

/* GET

Busca o ID do Ativo Existente.*/
func Getidbytag(assettag string, IP string) (ID int) {
	logs.InitLogger()
	Slogger := logs.Slogger
	funcname := "Getidbytag()"

	//Define URL (link da API com IP do servidor + Assettag para localiza????o do Ativo)
	url := "http://" + IP + "/api/v1/hardware/bytag/" + assettag
	//C??digo de autentica????o
	var bearer = "Bearer " + globals.SNIPEIT_AUTHENTIFICATION_TOKEN
	//REQUEST do GET
	req, _ := http.NewRequest("GET", url, nil)

	//HEADERs
	req.Header.Add("Accept", "application/json")
	req.Header.Add("Authorization", bearer)

	//Comunica????o HTTP com o invent??rio
	res, err := http.DefaultClient.Do(req)
	if err != nil {
		Slogger.Fatalw("Falha de conex??o com o Host Snipeit.",
			"funcname", funcname,
			"error", err,
		)
	}

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)

	//Caso a constante de desenvolvimento seja verdadeira, escre nos logs o JSON de response dessa fun????o.
	if globals.DEVSHOWJSON {

		//Ao escrever, indicar?? o tipo de JSON (reponse), a fun????o que o recebeu (Getidbytag()), e o struct o qual ser?? populado com as informa????es (IDT{})
		log.Printf("\n\nJSON (response, getidbytag(), IDT{}):\n %v\n\n", string(body))
	}

	if err != nil {
		log.Println("Error on parsing response.\n[ERROR] -", err)
	}

	// Unmarshal do resultado do response
	response := IDT{}
	err = json.Unmarshal(body, &response)
	if err != nil {
		log.Printf("Reading body failed: %s", err)
	}

	//Recebimento do ID
	Id := response.ID

	return Id

}

/*GET

Busca as informa????es do Ativo existente no invent??rio Snipe it e compara com o Ativo criado ao executar o programa.
Ele recebe o Asset Tag ??nico do Ativo existente e a vari??vel que cont??m o tipo populado com as informa????es do Ativo criado.
Ao comparar ambos A. Existente e A. Criado ele destaca as disparidades e as retorna  em uma string Patchrequest, assim como um bool Needpatching que afirma se ?? necess??rio um PATCH ou n??o.

OBS: Patchrequest ?? um JSON padronizado especificamente para o envio atrav??s do m??todo PATCH.*/
func GetAssetbytag(IP string, assettag string) *AssetT {

	logs.InitLogger()
	Slogger := logs.Slogger
	funcname := "Getbytag()"

	//Define URL (link da API com IP do servidor + Assettag para localiza????o do Ativo)
	url := "http://" + IP + "/api/v1/hardware/bytag/" + assettag
	//C??digo de autentica????o
	var bearer = "Bearer " + globals.SNIPEIT_AUTHENTIFICATION_TOKEN

	//REQUEST do GET
	req, _ := http.NewRequest("GET", url, nil)

	//HEADERs
	req.Header.Add("Accept", "application/json")
	req.Header.Add("Authorization", bearer)

	//Comunica????o HTTP com o invent??rio
	res, err := http.DefaultClient.Do(req)
	if err != nil {
		Slogger.Fatalw("Falha de conex??o com o Host Snipeit.",
			"funcname", funcname,
			"error", err,
		)
	}

	defer res.Body.Close()

	body, _ := ioutil.ReadAll(res.Body)

	//Caso a constante de desenvolvimento seja verdadeira, escre nos logs o JSON de response dessa fun????o.
	if globals.DEVSHOWJSON {

		//Ao escrever, indicar?? o tipo de JSON, a fun????o que o recebeu, e o struct o qual ser?? populado com as informa????es.
		log.Printf("\n\nJSON (response, Getbytag(), GlobalGetT{}):\n %v\n\n", string(body))
	}

	io.MultiReader()
	if err != nil {
		log.Println("Error on parsing response.\n[ERROR] -", err)
	}

	//Variavel que cont??m os dados do Ativo Existente
	var responsevar GlobalGetT

	// Unmarshal do resultado do response
	err = json.Unmarshal(body, &responsevar) //<-- GlobalGetT Needs to be remade.
	if err != nil {
		log.Printf("Reading body failed: %s", err)
	}

	//Vari??vel Struct utilizada para a an??lise de disparidades entre Ativo Existente no invent??rio e Ativo Criado pela execu????o do programa
	var ExistentAsset AssetT

	//Armazena as informa????es selecioandas do Response na vari??vel Struct de an??lise
	ExistentAsset.Name = responsevar.Name
	ExistentAsset.AssetTag = responsevar.AssetTag
	ExistentAsset.ModelID = strconv.Itoa(responsevar.Model.ID)
	ExistentAsset.StatusID = strconv.Itoa(responsevar.StatusLabel.ID)
	ExistentAsset.Memory = responsevar.CustomFields.MemRia.Value
	ExistentAsset.SO = responsevar.CustomFields.SO.Value
	ExistentAsset.HD = responsevar.CustomFields.Hd.Value
	ExistentAsset.Hostname = responsevar.CustomFields.Hostname.Value
	ExistentAsset.CPU = responsevar.CustomFields.CPU.Value
	ExistentAsset.Model = responsevar.CustomFields.Modelo.Value
	ExistentAsset.Installed = responsevar.CustomFields.ProgramasInstalados.Value
	ExistentAsset.Office = responsevar.CustomFields.Office.Value
	return &ExistentAsset

}

func (Asset *AssetT) ComparePrograms(f io.Writer, ExistentAsset *AssetT) (PatchrequestSlice string) {

	var IsDifferent bool = false

	ExistentAssetPrograms := strings.Split(ExistentAsset.Installed, " | ")
	AssetPrograms := strings.Split(Asset.Installed, " | ")

	tbl := table.New("STATUS", "PROGRAMA")

	//Implementa????o da formata????o
	tbl.WithWriter(f)

	for in, v := range AssetPrograms {

		if v != ExistentAssetPrograms[in] {
			IsDifferent = true
			break
		}
	}

	if IsDifferent {

		var PatchrequestSlice string = ", \"_snipeit_programas_instalados_10\":\""

		fmt.Fprintln(f, "Programa(s) desconhecido(s) encontrado(s). Refazendo lista de programas instalados.")

		for in, v := range AssetPrograms {

			if v == ExistentAssetPrograms[in] {

				tbl.AddRow("Novo!", v)

			}

			tbl.AddRow("Existente", v)
		}

		PatchrequestSlice += strings.Join(AssetPrograms, " | ")

		return PatchrequestSlice

	} else {

		fmt.Fprintln(f, "N??o h?? novos programas instalados.")

		for _, v := range AssetPrograms {

			tbl.AddRow("Existente", v)

		}

		return
	}
}

func (Asset *AssetT) CompareAsset(f io.Writer, ExistentAsset *AssetT) (Patchrequest string, Needpatching bool) {

	var IsDifferent bool = false
	//Vari??vel Array com as informa????es do Struct de an??lise
	var ExistentAssetIndex = []string{ExistentAsset.Name, ExistentAsset.AssetTag, ExistentAsset.ModelID, ExistentAsset.StatusID, ExistentAsset.Memory, ExistentAsset.SO, ExistentAsset.HD, ExistentAsset.Hostname, ExistentAsset.CPU, ExistentAsset.Model}

	//Vari??vel Array com as informa????es do Struct do Ativo Criado
	var AssetIndex = []string{Asset.Name, Asset.AssetTag, Asset.ModelID, Asset.StatusID, Asset.Memory, Asset.SO, Asset.HD, Asset.Hostname, Asset.CPU, Asset.Model}

	//Variav??l Array que cont??m as altera????es pendentes
	var Pending []string

	//Vari??vel String que cont??m o pr??ncipio do Patchrequest
	var Patchresquest string = "{\"requestable\":false,\"archived\":false"

	//Verifica as disparidades, destacando-as e criando o Patchrequest.
	for in, v := range AssetIndex {

		if v != ExistentAssetIndex[in] {
			IsDifferent = true
			break
		}

	}
	if IsDifferent {

		//Cria tabela com os Cabe??alhos "Ativo Existente", "Ativo Criado"
		tbl := table.New("Fieldname", "Ativo Existente", "Ativo Criado")

		//Implementa????o da formata????o
		tbl.WithWriter(f)
		fmt.Fprintln(f, "Disparidades encontradas.")

		//Analise de disparidades
		for i := 0; i < len(ExistentAssetIndex); i++ {
			if ExistentAssetIndex[i] != AssetIndex[i] {
				var Fieldname string
				switch i {
				case 0:
					//Caso a disparidade seja encontrada no Index [0] do Array, ?? necess??rio PATCH no campo NAME
					Patchresquest += ",\"name\":\"" + AssetIndex[i] + "\""
					Fieldname = "NAME"
				case 1:
					//Caso a disparidade seja encontrada no Index [1] do Array, ?? necess??rio PATCH no campo ASSET TAG
					Patchresquest += ",\"asset_tag\":\"" + AssetIndex[i] + "\""
					Fieldname = "ASSET TAG"
				case 2:
					//Caso a disparidade seja encontrada no Index [2] do Array, ?? necess??rio PATCH no campo MODEL ID
					Patchresquest += ",\"model_id\":\"" + AssetIndex[i] + "\""
					Fieldname = "MODEL ID"
				case 3:
					//Caso a disparidade seja encontrada no Index [3] do Array, ?? necess??rio PATCH no campo STATUS ID
					Patchresquest += ",\"status_id\":\"" + AssetIndex[i] + "\""
					Fieldname = "STATUS ID"
				case 4:
					//Caso a disparidade seja encontrada no Index [4] do Array, ?? necess??rio PATCH no campo MEM??RIA
					Patchresquest += ",\"_snipeit_memoria_2\":\"" + AssetIndex[i] + "\""
					Fieldname = "MEM??RIA"
				case 5:
					//Caso a disparidade seja encontrada no Index [5] do Array, ?? necess??rio PATCH no campo SISTEMA OPERACIONAL
					Patchresquest += ",\"_snipeit_so_3\":\"" + AssetIndex[i] + "\""
					Fieldname = "SISTEMA OPERACIONAL"
				case 6:
					//Caso a disparidade seja encontrada no Index [6] do Array, ?? necess??rio PATCH no campo HD
					Patchresquest += ",\"_snipeit_hd_4\":\"" + AssetIndex[i] + "\""
					Fieldname = "HD"
				case 7:
					//Caso a disparidade seja encontrada no Index [7] do Array, ?? necess??rio PATCH no campo HOSTNAME
					Patchresquest += ",\"_snipeit_hostname_5\":\"" + AssetIndex[i] + "\""
					Fieldname = "HOSTNAME"
				case 8:
					//Caso a disparidade seja encontrada no Index [8] do Array, ?? necess??rio PATCH no campo CPU
					Patchresquest += ",\"_snipeit_cpu_6\":\"" + AssetIndex[i] + "\""
					Fieldname = "CPU"
				case 9:
					//Caso a disparidade seja encontrada no Index [9] do Array, ?? necess??rio PATCH no campo MODELO
					Patchresquest += ",\"_snipeit_modelo_7\":\"" + AssetIndex[i] + "\""
					Fieldname = "MODEL"
				case 10:
					//Caso a disparidade seja encontrada no Index [10] do Array, ?? necess??rio PATCH no campo OFFICE
					Patchresquest += ",\"_snipeit_office_9\":\"" + AssetIndex[i] + "\""
					Fieldname = "OFFICE"
				case 11:
					//Caso a disparidade seja encontrada no Index [11] do Array, ?? necess??rio PATCH no campo PROGRAMAS INSTALADOS
					Patchresquest += ",\"_snipeit_programas_instalados_10\":\"" + AssetIndex[i] + "\""
					Fieldname = "PROGRAMAS INSTALADOS"
				}

				//Acrescenta informa????es a tabela
				tbl.AddRow(Fieldname, ExistentAssetIndex[i], AssetIndex[i])

				//Acrescenta altera????es a uma lista de pend??ncias para expor visualmente depois
				Pending = append(Pending, AssetIndex[i])
			} else {
				//Se n??o h?? disparidades, continue a an??lise
				continue
			}
		}

		ProgramsRequest := Asset.ComparePrograms(f, ExistentAsset)
		//Fechamento do Patchresquest
		Patchresquest += ProgramsRequest + "}"
		fmt.Printf("\nAltera????es pendentes:\n%v\n", Pending)
		//Caso haja altera????es,printe a tabela retorna true
		tbl.Print()
		return Patchresquest, true
	} else {
		//Caso n??o.. retorna false
		_, _ = fmt.Fprintf(f, "Nenhuma disparidade foi encontrada no Ativo...\n\n")
		_, _ = fmt.Fprintf(f, "")

		//Cria tabela com os Cabe??alhos "Fieldname" e "Ativo Existente"
		tbl := table.New("Fieldname", "Ativo Existente")

		//Implementa????o da formata????o
		tbl.WithWriter(f)

		for i := 0; i < len(ExistentAssetIndex); i++ {

			var Fieldname string
			switch i {
			case 0:
				Fieldname = "NAME"
			case 1:

				Fieldname = "ASSET TAG"
			case 2:

				Fieldname = "MODEL ID"
			case 3:

				Fieldname = "STATUS ID"
			case 4:

				Fieldname = "MEM??RIA"
			case 5:

				Fieldname = "SISTEMA OPERACIONAL"
			case 6:

				Fieldname = "HD"
			case 7:

				Fieldname = "HOSTNAME"
			case 8:

				Fieldname = "CPU"
			case 9:

				Fieldname = "MODEL"
			case 10:

				Fieldname = "OFFICE"
			case 11:

				Fieldname = "PROGRAMAS INSTALADOS"
			}

			//Acrescenta informa????es a tabela
			tbl.AddRow(Fieldname, ExistentAssetIndex[i])

		}

		//Exp??e tabela do Ativo Existente
		tbl.Print()

		return Patchresquest, false
	}
}

/*PATCH

Envia altera????es feitas no ativo existente no invent??rio atrav??s de seu ID.*/
func Patchbyid(id int, IP string, Patchresquest string) {

	logs.InitLogger()
	Slogger := logs.Slogger
	funcname := "Patchbyid()"

	//Converte ID de string para int
	StringID := strconv.Itoa(id)
	//Define URL (link da API com IP do servidor + Assettag para localiza????o do Ativo)
	url := "http://" + IP + "/api/v1/hardware/" + StringID

	payload := strings.NewReader(Patchresquest)
	//REQUEST do GET
	req, err := http.NewRequest("PATCH", url, payload)
	if err != nil {
		log.Fatalf("Request Error")
	}

	//C??digo de autentica????o
	var bearer = "Bearer " + globals.SNIPEIT_AUTHENTIFICATION_TOKEN

	//HEADERs
	req.Header.Add("Accept", "application/json")
	req.Header.Add("Authorization", bearer)
	req.Header.Add("Content-Type", "application/json")

	//Comunica????o HTTP com o invent??rio
	res, err := http.DefaultClient.Do(req)
	if err != nil {
		Slogger.Fatalw("Falha de conex??o com o Host Snipeit.",
			"funcname", funcname,
			"error", err,
		)
	}

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)
	//Se DEVVIEW for verdadeiro, mostra nos logs o JSON de response
	if globals.DEVVIEW {
		log.Printf("\nJSON de Response (-patchbyid()-):\n %v\n", string(body))
	}

	//Caso a constante de desenvolvimento seja verdadeira, escre nos logs o JSON de response dessa fun????o.
	if globals.DEVSHOWJSON {

		//Ao escrever, indicar?? o tipo de JSON, a fun????o que o recebeu, e o struct o qual ser?? populado com as informa????es.
		log.Printf("\n\nJSON (response, Patchbyid(), PatchResponseT{}):\n %v\n\n", string(body))
	}

	// Unmarshal do resultado do response
	response := PatchResponseT{}
	err = json.Unmarshal(body, &response)
	if err != nil {
		log.Printf("Reading body failed: %s", err)
	}

}

/*GET

Verifica se ativo existe procurando-o (GET) no invent??rio atrav??s do seu Asset Tag ??nico.*/
func Verifybytag(assettag string, IP string) bool {

	logs.InitLogger()
	Slogger := logs.Slogger
	funcname := "Verifybytag()"

	//Define URL (link da API com IP do servidor + Assettag para localiza????o do Ativo)
	url := "http://" + IP + "/api/v1/hardware/bytag/" + assettag

	//C??digo de autentica????o
	var bearer = "Bearer " + globals.SNIPEIT_AUTHENTIFICATION_TOKEN

	//REQUEST do GET
	req, _ := http.NewRequest("GET", url, nil)

	//HEADERs
	req.Header.Add("Accept", "application/json")
	req.Header.Add("Authorization", bearer)

	//Comunica????o HTTP com o invent??rio
	res, err := http.DefaultClient.Do(req)
	if err != nil {
		Slogger.Fatalw("Falha de conex??o com o Host Snipeit.",
			"funcname", funcname,
			"error", err,
		)
	}

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)

	//Caso a constante de desenvolvimento seja verdadeira, escre nos logs o JSON de response dessa fun????o.
	if globals.DEVSHOWJSON {

		//Ao escrever, indicar?? o tipo de JSON, a fun????o que o recebeu, e o struct o qual ser?? populado com as informa????es.
		log.Printf("\n\nJSON (response, Verifybytag(), ErrorT{}):\n %v\n\n", string(body))
	}

	// Unmarshal do resultado do response
	response := ErrorT{}
	err = json.Unmarshal(body, &response)
	if err != nil {
		log.Printf("Reading body failed: %s", err)
	}

	//tipo vazio para a compara????o. (Se a Reponse for igual a ele, isto ??, vazio, ent??o ele retorna um false significando que n??o h?? erro)
	blankspace := ErrorT{}
	//Printando o Response
	if response == blankspace {
		return false

	} else {
		return true
	}
}

/* POST

Envia os dados do computador para o invent??rio no Snipeit. (Essa fun????o recebe a variavel que recebe o tipo struct criado com os dados do computador)*/
func Shoot(Asset *AssetT, IP string, f io.Writer) {
	logs.InitLogger()
	Slogger := logs.Slogger
	funcname := "Verifybytag()"

	var AssetIndex = []string{Asset.Name, Asset.AssetTag, Asset.ModelID, Asset.StatusID, Asset.Memory, Asset.SO, Asset.HD, Asset.Hostname, Asset.CPU, Asset.Model}

	//URL da API SnipeIt
	url := "http://" + IP + "/api/v1/hardware"

	// Token de autentiuca????o
	var bearer = "Bearer " + globals.SNIPEIT_AUTHENTIFICATION_TOKEN

	//transformando em bytes a vari??vel hw
	hardwarePostJSON, err := json.Marshal(Asset)
	//Tratando o ocasoional erro transforma????o da vari??vel em byte
	if err != nil {
		panic(err)
	}

	//POST REQUEST
	req, err := http.NewRequest("POST", url, bytes.NewBuffer(hardwarePostJSON))

	//Tratando o ocasoional erro do POST/REQUEST
	if err != nil {
		panic(err)
	}

	//adicionando os headers a autoriza????o
	req.Header.Add("Authorization", bearer)
	//definindo a formata????o do REQUEST
	req.Header.Add("Content-type", "application/json")

	// Send req using http Client
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		Slogger.Fatalw("Error on request.",
			"funcname", funcname,
			"error", err,
		)

	}

	//fechando o Response ap??s a conclus??o do c??digo
	defer resp.Body.Close()

	//lendo o RESQUEST
	body, err := ioutil.ReadAll(resp.Body)
	//Caso a constante de desenvolvimento seja verdadeira, escre nos logs o JSON de response dessa fun????o.
	if globals.DEVSHOWJSON {

		//Ao escrever, indicar?? o tipo de JSON, a fun????o que o recebeu, e o struct o qual ser?? populado com as informa????es.
		log.Printf("\n\nJSON (response, PostSnipe(), SnipeitResponse{}):\n %v\n\n", string(body))
	}
	//Tratando o ocasoional erro do request
	if err != nil {
		log.Println("Error on parsing response.\n[ERROR] -", err)
	}

	// Unmarshal do resultado do response
	response := GlobalResponseT{}

	err = json.Unmarshal(body, &response)
	if err != nil {
		log.Printf("Reading body failed: %s", err)
		return
	} else {
		log.Println(response.Status, response.Messages)
	}

	//Cria tabela com os Cabe??alhos "Fieldname" e "Ativo Existente"
	tbl := table.New("Fieldname", "Novo Ativo")
	tblProgs := table.New("Programas Instalados")
	//Implementa????o da formata????o
	tbl.WithWriter(f)
	tblProgs.WithWriter(f)

	for i := 0; i < len(AssetIndex); i++ {

		var Fieldname string
		switch i {
		case 0:
			Fieldname = "NAME"
		case 1:

			Fieldname = "ASSET TAG"
		case 2:

			Fieldname = "MODEL ID"
		case 3:

			Fieldname = "STATUS ID"
		case 4:

			Fieldname = "MEM??RIA"
		case 5:

			Fieldname = "SISTEMA OPERACIONAL"
		case 6:

			Fieldname = "HD"
		case 7:

			Fieldname = "HOSTNAME"
		case 8:

			Fieldname = "CPU"
		case 9:

			Fieldname = "MODEL"
		}

		//Acrescenta informa????es a tabela
		tbl.AddRow(Fieldname, AssetIndex[i])

	}

	for _, v := range Asset.Installed {

		tblProgs.AddRow(v)

	}

	//Exp??e tabela do Ativo Existente
	tbl.Print()
	tblProgs.Print()

	//Printando o Response
	fmt.Println("Response do POST:", response)
}

func NewAsset() *AssetT {
	return &AssetT{}
}
func NewSnipeitGetResponse() GlobalResponseT {
	return GlobalResponseT{}
}
func NewSnipeitPatchResponse() *PatchResponseT { return &PatchResponseT{} }
