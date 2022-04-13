package sniper

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"reflect"
	help "sniper/snipercmd/helpers"
	"strconv"
	"strings"

	"github.com/rodaine/table"
)

const (
	IP = "10.20.1.67:8000"
	//Token de autenticação com Snipe it.
	TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMTFjN2U4NzA5MmMxNWVlNjBkYWI0Y2NjNzI1Y2U5YjBjYWM5NDgzYTZmZWYyOGQ3ODFmYzkzNjczNzliMzM2ZDE2YWMxNzIyYWVkZTQ4ZWUiLCJpYXQiOjE2NDMyOTE0NzQsIm5iZiI6MTY0MzI5MTQ3NCwiZXhwIjoyMTE2Njc3MDc0LCJzdWIiOiI0MCIsInNjb3BlcyI6W119.KPi_GZWymX7TbHfn35SYYLVTaTZk_og5MSrkKjt5oMGFXwG6PIol3TcfMJLEQ7be4gwKv04jS_CP3UD6fy5lQkD34BOb8KkL7wWX95EPrxp5o_4RsMJmBc2bBht_h5Cndg0uLe3oQUMxjStAc2lT7r7IHo_MPeKd3cykyuhgrmblMjzSR1bKQGidnvC6xWOfetJzU-bSjo6AiEBtB6V8TIE191_FMFrPDsU8AcOPnbSxf0bGZb1Jz1uHy0oOMXZFIMm3gubmWpl0M179u9D2bLRoNTOvYlXASGESEsdmROufvaZfgGF2ld_1E_0CP5Ys3YMmkxnmU45meqZu_WZtQkJbKCdeAFgPMBLaK2buRt-eub9puTlTRngDhCFCHnaDafL8hD7PBQYEgMGI0bCsaUD8QvcIDUhknFg7CwavTqEYD440aiunUurkqjPWPqPm2yLz8W36myWReZXJXNy-YH9fdjAMWAPFTq2bfi9MCUuoCeAOg5HYcUoJ6I20i5rInV6bPfidr3RGsLYOTxeJ_d2-INOyAIy-hc7MSskqWIBkGVCBh8T0p5RcRopk1F2rqF0Qj2bOyAh_NxiF-kR-WveLbMStsDzdr6HjU3BJ_aeBGjLSk91v9QCLt-gzNd25hgp4leGt54X4ODIAiQFVbI4IpwR_8UjPaoxroHrK4no"
)

type FieldsT struct {
	Total int `json:"total"`
	Rows  []struct {
		ID               int       `json:"id"`
		Name             string    `json:"name"`
		DbColumnName     string    `json:"db_column_name"`
		Format           string    `json:"format"`
		FieldValues      string    `json:"field_values"`
		FieldValuesArray []string  `json:"field_values_array"`
		Type             string    `json:"type"`
		Required         bool      `json:"required"`
		CreatedAt        DatetimeT `json:"created_at"`
		UpdatedAt        DatetimeT `json:"updated_at"`
	} `json:"rows"`
}

type FieldT struct {
	ID               int      `json:"id"`
	Name             string   `json:"name"`
	DbColumnName     string   `json:"db_column_name"`
	Format           string   `json:"format"`
	FieldValues      string   `json:"field_values"`
	FieldValuesArray []string `json:"field_values_array"`
	Type             string   `json:"type"`
}

type ErrorT struct {
	Msg string `json:"error"`
}

func GetAllFields(ip, token string) ([]FieldT, error) {
	var AllFields []FieldT

	url := "http://" + ip + "/api/v1/fields"

	req, errReq := http.NewRequest("GET", url, nil)

	if errReq != nil {
		return nil, errReq
	}

	req.Header.Add("Accept", "application/json")
	req.Header.Add("Authorization", "Bearer "+token)

	res, errRes := http.DefaultClient.Do(req)
	if errRes != nil {
		return nil, fmt.Errorf("falha de conexão com o host Snipeit. %v", errRes)
	}
	body, _ := ioutil.ReadAll(res.Body)
	Error := ErrorT{}
	NoErr := json.Unmarshal(body, &Error)

	if NoErr == nil && Error.Msg != "" {
		return nil, fmt.Errorf(Error.Msg)
	}

	defer res.Body.Close()

	fields := FieldsT{}
	errUnmarsh := json.Unmarshal(body, &fields)

	if errUnmarsh != nil {
		return nil, errUnmarsh
	}

	for _, f := range fields.Rows {
		var Field FieldT
		byts, _ := json.Marshal(f)
		json.Unmarshal(byts, &Field)
		AllFields = append(AllFields, Field)
	}
	return AllFields, nil
}

type FullAssetT struct {
	ID               int               `json:"id"`
	Name             string            `json:"name"`
	AssetTag         string            `json:"asset_tag"`
	Serial           string            `json:"serial"`
	Model            IDnameInfoT       `json:"model"`
	ModelNumber      string            `json:"model_number"`
	Eol              string            `json:"eol"`
	StatusLabel      StatusLabelT      `json:"status_label"`
	Category         IDnameInfoT       `json:"category"`
	Manufacturer     IDnameInfoT       `json:"manufacturer"`
	Supplier         string            `json:"supplier"`
	Notes            string            `json:"notes"`
	OrderNumber      string            `json:"order_number"`
	Company          IDnameInfoT       `json:"company"`
	Location         IDnameInfoT       `json:"location"`
	RtdLocation      IDnameInfoT       `json:"rtd_location"`
	Image            string            `json:"image"`
	AssignedTo       interface{}       `json:"assigned_to"`
	WarrantyMonths   string            `json:"warranty_months"`
	WarrantyExpires  string            `json:"warranty_expires"`
	CreatedAt        DatetimeT         `json:"created_at"`
	UpdatedAt        DatetimeT         `json:"updated_at"`
	LastAuditDate    string            `json:"last_audit_date"`
	NextAuditDate    string            `json:"next_audit_date"`
	DeletedAt        string            `json:"deleted_at"`
	PurchaseDate     string            `json:"purchase_date"`
	LastCheckout     DatetimeT         `json:"last_checkout"`
	ExpectedCheckin  string            `json:"expected_checkin"`
	PurchaseCost     string            `json:"purchase_cost"`
	CheckinCounter   int               `json:"checkin_counter"`
	CheckoutCounter  int               `json:"checkout_counter"`
	RequestsCounter  int               `json:"requests_counter"`
	UserCanCheckout  bool              `json:"user_can_checkout"`
	CustomFields     CustomFieldsT     `json:"custom_fields"`
	AvailableActions AvailableActionsT `json:"available_actions"`
}

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

type AllAssetsT struct {
	Total int `json:"total"`
	Rows  []struct {
		ID               int               `json:"id"`
		Name             string            `json:"name"`
		AssetTag         string            `json:"asset_tag"`
		Serial           string            `json:"serial"`
		Model            IDnameInfoT       `json:"model"`
		ModelNumber      string            `json:"model_number"`
		Eol              string            `json:"eol"`
		StatusLabel      StatusLabelT      `json:"status_label"`
		Category         IDnameInfoT       `json:"category"`
		Manufacturer     IDnameInfoT       `json:"manufacturer"`
		Supplier         string            `json:"supplier"`
		Notes            string            `json:"notes"`
		OrderNumber      string            `json:"order_number"`
		Company          IDnameInfoT       `json:"company"`
		Location         IDnameInfoT       `json:"location"`
		RtdLocation      IDnameInfoT       `json:"rtd_location"`
		Image            string            `json:"image"`
		AssignedTo       interface{}       `json:"assigned_to"`
		WarrantyMonths   string            `json:"warranty_months"`
		WarrantyExpires  string            `json:"warranty_expires"`
		CreatedAt        DatetimeT         `json:"created_at"`
		UpdatedAt        DatetimeT         `json:"updated_at"`
		LastAuditDate    string            `json:"last_audit_date"`
		NextAuditDate    string            `json:"next_audit_date"`
		DeletedAt        string            `json:"deleted_at"`
		PurchaseDate     string            `json:"purchase_date"`
		LastCheckout     DatetimeT         `json:"last_checkout"`
		ExpectedCheckin  string            `json:"expected_checkin"`
		PurchaseCost     string            `json:"purchase_cost"`
		CheckinCounter   int               `json:"checkin_counter"`
		CheckoutCounter  int               `json:"checkout_counter"`
		RequestsCounter  int               `json:"requests_counter"`
		UserCanCheckout  bool              `json:"user_can_checkout"`
		CustomFields     CustomFieldsT     `json:"custom_fields"`
		AvailableActions AvailableActionsT `json:"available_actions"`
	} `json:"rows"`
}

type CustomFieldsT struct {
	Modelo struct {
		Field       string "json:\"field\""
		Value       string "json:\"value\""
		FieldFormat string "json:\"field_format\""
	} "json:\"Modelo\""
	Hostname struct {
		Field       string "json:\"field\""
		Value       string "json:\"value\""
		FieldFormat string "json:\"field_format\""
	} "json:\"Hostname\""
	Hd struct {
		Field       string "json:\"field\""
		Value       string "json:\"value\""
		FieldFormat string "json:\"field_format\""
	} "json:\"HD\""
	CPU struct {
		Field       string "json:\"field\""
		Value       string "json:\"value\""
		FieldFormat string "json:\"field_format\""
	} "json:\"CPU\""
	MemRia struct {
		Field       string "json:\"field\""
		Value       string "json:\"value\""
		FieldFormat string "json:\"field_format\""
	} "json:\"Memoria\""
	SO struct {
		Field       string "json:\"field\""
		Value       string "json:\"value\""
		FieldFormat string "json:\"field_format\""
	} "json:\"S.O.\""
	Office struct {
		Field       string "json:\"field\""
		Value       string "json:\"value\""
		FieldFormat string "json:\"field_format\""
	} "json:\"Office\""
	Setor struct {
		Field       string "json:\"field\""
		Value       string "json:\"value\""
		FieldFormat string "json:\"field_format\""
	} "json:\"Setor\""
	ProgramasInstalados struct {
		Field       string "json:\"field\""
		Value       string "json:\"value\""
		FieldFormat string "json:\"field_format\""
	} "json:\"Programas Instalados\""
}

type AvailableActionsT struct {
	Checkout bool "json:\"checkout\""
	Checkin  bool "json:\"checkin\""
	Clone    bool "json:\"clone\""
	Restore  bool "json:\"restore\""
	Update   bool "json:\"update\""
	Delete   bool "json:\"delete\""
}

type DatetimeT struct {
	Datetime  string "json:\"datetime\""
	Formatted string "json:\"formatted\""
}

type IDnameInfoT struct {
	ID   int    "json:\"id\""
	Name string "json:\"name\""
}

type StatusLabelT struct {
	ID         int    "json:\"id\""
	Name       string "json:\"name\""
	StatusType string "json:\"status_type\""
	StatusMeta string "json:\"status_meta\""
}

var sortableColumns = []string{"id", "name", "asset_tag", "serial", "model", "model_number", "last_checkout", "category", "notes", "manufacturer", "expected_checkin", "order_number", "companyName", "location", "image", "status_label", "assigned_to", "created_at", "purchase_date", "purchase_cost"}

func GetAssets(ip, token string, params ...string) ([]FullAssetT, error) {

	var (
		limit = "2"
		sort  = "created_at"
	)

	if len(params) > 3 {
		return nil, fmt.Errorf("invalid params")
	} else if len(params) > 0 {

		for _, v := range params {
			if v != "" {
				switch {

				case help.IsNumeric(v):
					TrueValue, _ := strconv.Atoi(v)
					if TrueValue > 0 {
						limit = v
					} else {
						return nil, fmt.Errorf("invalid limit number")
					}

				default:
					var sortable bool = false
				sortLoop:
					for _, sc := range sortableColumns {

						if sc == v {
							sortable = true
							break sortLoop
						}
					}
					if sortable {
						sort = v
					} else {
						return nil, fmt.Errorf("invalid sortable column")
					}
				}
			}
		}

	}

	url := "http://" + ip + "/api/v1/hardware?limit=" + limit + "&offset=0&sort=" + sort + "&order=desc"

	req, errReq := http.NewRequest("GET", url, nil)

	if errReq != nil {
		return nil, errReq
	}

	req.Header.Add("Accept", "application/json")
	req.Header.Add("Authorization", "Bearer "+token)

	res, errRes := http.DefaultClient.Do(req)
	if errRes != nil {
		return nil, fmt.Errorf("falha de conexão com o host Snipeit. %v", errRes)
	}
	body, _ := ioutil.ReadAll(res.Body)
	Error := ErrorT{}
	NoErr := json.Unmarshal(body, &Error)

	defer res.Body.Close()

	if NoErr == nil && Error.Msg != "" {
		return nil, fmt.Errorf(Error.Msg)
	}

	allAssets := AllAssetsT{}
	log.Println(string(body))
	errJson := json.Unmarshal(body, &allAssets)
	if errJson != nil {
		return nil, errJson
	}

	var FullAssetList []FullAssetT
	for _, asset := range allAssets.Rows {
		fAsset := FullAssetT{}
		byts, _ := json.Marshal(asset)
		json.Unmarshal(byts, &fAsset)
		FullAssetList = append(FullAssetList, fAsset)

	}

	if len(FullAssetList) == 0 {
		return nil, fmt.Errorf("the full asset list is empty")
	}

	return FullAssetList, nil

}

func GetAssetById(ip, token string, id int) (FullAssetT, error) {
	EmptyAsset := FullAssetT{}
	FullAsset := FullAssetT{}

	url := "http://" + ip + "/api/v1/hardware/" + strconv.Itoa(id)

	req, errReq := http.NewRequest("GET", url, nil)

	if errReq != nil {
		return EmptyAsset, errReq
	}

	req.Header.Add("Accept", "application/json")
	req.Header.Add("Authorization", "Bearer "+token)

	res, errRes := http.DefaultClient.Do(req)
	if errRes != nil {
		return EmptyAsset, fmt.Errorf("falha de conexão com o host Snipeit. %v", errRes)
	}
	body, _ := ioutil.ReadAll(res.Body)
	Error := ErrorT{}
	NoErr := json.Unmarshal(body, &Error)

	defer res.Body.Close()

	if NoErr == nil && Error.Msg != "" {
		return EmptyAsset, fmt.Errorf(Error.Msg)
	}

	errJson := json.Unmarshal(body, &FullAsset)

	if errJson != nil {

		return EmptyAsset, errJson
	}

	if FullAsset == EmptyAsset {
		return EmptyAsset, fmt.Errorf("empty asset")
	}
	return FullAsset, nil
}

func GetAssetByTag(ip, token, tag string) (FullAssetT, error) {
	EmptyAsset := FullAssetT{}
	FullAsset := FullAssetT{}

	url := "http://" + ip + "/api/v1/hardware/bytag/" + tag

	req, errReq := http.NewRequest("GET", url, nil)

	if errReq != nil {
		return EmptyAsset, errReq
	}

	req.Header.Add("Accept", "application/json")
	req.Header.Add("Authorization", "Bearer "+token)

	res, errRes := http.DefaultClient.Do(req)
	if errRes != nil {
		return EmptyAsset, fmt.Errorf("falha de conexão com o host Snipeit. %v", errRes)
	}
	body, _ := ioutil.ReadAll(res.Body)
	Error := ErrorT{}
	NoErr := json.Unmarshal(body, &Error)

	defer res.Body.Close()

	if NoErr == nil && Error.Msg != "" {
		return EmptyAsset, fmt.Errorf(Error.Msg)
	}

	errJson := json.Unmarshal(body, &FullAsset)

	if errJson != nil {

		return EmptyAsset, errJson
	}

	if FullAsset == EmptyAsset {
		return EmptyAsset, fmt.Errorf("empty asset")
	}

	return FullAsset, nil
}

func (fa FullAssetT) ToShort() AssetT {

	var asset AssetT

	asset.Name = fa.Name
	asset.AssetTag = fa.AssetTag
	asset.ModelID = strconv.Itoa(fa.Model.ID)
	asset.StatusID = strconv.Itoa(fa.StatusLabel.ID)
	asset.Memory = fa.CustomFields.MemRia.Value
	asset.SO = fa.CustomFields.SO.Value
	asset.HD = fa.CustomFields.Hd.Value
	asset.Hostname = fa.CustomFields.Hostname.Value
	asset.CPU = fa.CustomFields.CPU.Value
	asset.Model = fa.CustomFields.Modelo.Value
	asset.Installed = fa.CustomFields.ProgramasInstalados.Value
	asset.Office = fa.CustomFields.Office.Value

	return asset
}

func (fa FullAssetT) fieldnames(tag string) []string {
	var Fields []string
	v := reflect.ValueOf(fa)

	for i := 0; i < v.NumField(); i++ {
		var FieldName string
		if strings.ToLower(tag) == "json" {
			FieldName = v.Type().Field(i).Tag.Get("json")

		} else {
			FieldName = v.Type().Field(i).Name
		}

		Fields = append(Fields, FieldName)
	}

	return Fields
}

func (a AssetT) fieldnames(tag string) []string {
	var Fields []string
	v := reflect.ValueOf(a)

	for i := 0; i < v.NumField(); i++ {
		var FieldName string
		if strings.ToLower(tag) == "json" {
			FieldName = v.Type().Field(i).Tag.Get("json")

		} else {
			FieldName = v.Type().Field(i).Name
		}

		Fields = append(Fields, FieldName)
	}

	return Fields
}

func (a CustomFieldsT) fieldnames(tag string) []string {
	var Fields []string
	v := reflect.ValueOf(a)

	for i := 0; i < v.NumField(); i++ {
		var FieldName string
		if strings.ToLower(tag) == "json" {
			FieldName = v.Type().Field(i).Tag.Get("json")

		} else {
			FieldName = v.Type().Field(i).Name
		}

		Fields = append(Fields, FieldName)
	}

	return Fields
}

func (a IDnameInfoT) fieldnames(tag string) []string {
	var Fields []string
	v := reflect.ValueOf(a)

	for i := 0; i < v.NumField(); i++ {
		var FieldName string
		if strings.ToLower(tag) == "json" {
			FieldName = v.Type().Field(i).Tag.Get("json")

		} else {
			FieldName = v.Type().Field(i).Name
		}

		Fields = append(Fields, FieldName)
	}

	return Fields
}

func (a StatusLabelT) fieldnames(tag string) []string {
	var Fields []string
	v := reflect.ValueOf(a)

	for i := 0; i < v.NumField(); i++ {
		var FieldName string
		if strings.ToLower(tag) == "json" {
			FieldName = v.Type().Field(i).Tag.Get("json")

		} else {
			FieldName = v.Type().Field(i).Name
		}

		Fields = append(Fields, FieldName)
	}

	return Fields
}

func (a AvailableActionsT) fieldnames(tag string) []string {
	var Fields []string
	v := reflect.ValueOf(a)

	for i := 0; i < v.NumField(); i++ {
		var FieldName string
		if strings.ToLower(tag) == "json" {
			FieldName = v.Type().Field(i).Tag.Get("json")

		} else {
			FieldName = v.Type().Field(i).Name
		}

		Fields = append(Fields, FieldName)
	}

	return Fields
}

func (a DatetimeT) fieldnames(tag string) []string {
	var Fields []string
	v := reflect.ValueOf(a)

	for i := 0; i < v.NumField(); i++ {
		var FieldName string
		if strings.ToLower(tag) == "json" {
			FieldName = v.Type().Field(i).Tag.Get("json")

		} else {
			FieldName = v.Type().Field(i).Name
		}

		Fields = append(Fields, FieldName)
	}

	return Fields
}

type Asset interface {
	fieldnames(string) []string
}

func Fields(a Asset, tag string) []string {

	return a.fieldnames(tag)
}

var SniperTypes = []string{"sniper.IDnameInfoT", "sniper.StatusLabelT", "sniper.DatetimeT", "sniper.CustomFieldsT", "sniper.AvailableActionsT"}

func (old FullAssetT) Compare(new FullAssetT) (string, error) {

	StructFields := Fields(old, "")
	JsonField := Fields(old, "json")
	reflectOld := reflect.ValueOf(old)
	reflectNew := reflect.ValueOf(new)
	var PutRequest string = "{"
	for in, field := range StructFields {
		OldVal := reflectOld.FieldByName(field)
		sOldVal := fmt.Sprint(OldVal)
		NewVal := reflectNew.FieldByName(field)
		sNewVal := fmt.Sprint(NewVal)
		fmt.Println(OldVal, NewVal)

		if sNewVal == sOldVal || (field == "StatusLabel" || field == "Model") {
			if NewVal == reflect.Zero(reflect.TypeOf(new)) || field == "AssetTag" || field == "ID" {
				continue
			}

			var isStruct bool = false
			NewValType := fmt.Sprint(reflect.TypeOf(new).Field(in).Type)

		TypeAnalysisLoop:
			for _, t := range SniperTypes {

				if NewValType == t {
					isStruct = true
					break TypeAnalysisLoop
				}
			}

			if isStruct {

				for i := 0; i < NewVal.NumField(); i++ {

					json := NewVal.Type().Field(i).Tag.Get("json")
					value := NewVal.Field(i)

					if value == reflect.Zero(reflect.TypeOf(value)) {
						continue
					}
					resquest := fmt.Sprintf("\"%v_%v\":\"%v\",", JsonField[in], json, value)
					PutRequest += resquest

				}

				continue

			}

			resquest := fmt.Sprintf("\"%v\":\"%v\",", JsonField[in], NewVal)
			PutRequest += resquest

		} else {
			continue
		}
	}

	if PutRequest == "{" {
		return "", fmt.Errorf("there is nothing new")

	}

	PutRequest = strings.TrimRight(PutRequest, ",") + "}"

	return PutRequest, nil
}

type Success struct {
	Status   string  `json:"status"`
	Messages string  `json:"messages"`
	Payload  Payload `json:"payload"`
}
type Model struct {
	ID                   int         `json:"id"`
	Name                 string      `json:"name"`
	ModelNumber          interface{} `json:"model_number"`
	ManufacturerID       int         `json:"manufacturer_id"`
	CategoryID           int         `json:"category_id"`
	CreatedAt            string      `json:"created_at"`
	UpdatedAt            string      `json:"updated_at"`
	DepreciationID       interface{} `json:"depreciation_id"`
	Eol                  int         `json:"eol"`
	Image                interface{} `json:"image"`
	DeprecatedMacAddress int         `json:"deprecated_mac_address"`
	FieldsetID           int         `json:"fieldset_id"`
	Notes                interface{} `json:"notes"`
	Requestable          int         `json:"requestable"`
}
type Payload struct {
	ID                           int         `json:"id"`
	Name                         string      `json:"name"`
	AssetTag                     string      `json:"asset_tag"`
	ModelID                      int         `json:"model_id"`
	Serial                       string      `json:"serial"`
	PurchaseDate                 interface{} `json:"purchase_date"`
	PurchaseCost                 interface{} `json:"purchase_cost"`
	OrderNumber                  interface{} `json:"order_number"`
	AssignedTo                   string      `json:"assigned_to"`
	Notes                        interface{} `json:"notes"`
	Image                        interface{} `json:"image"`
	UserID                       int         `json:"user_id"`
	CreatedAt                    string      `json:"created_at"`
	UpdatedAt                    string      `json:"updated_at"`
	Physical                     int         `json:"physical"`
	DeletedAt                    interface{} `json:"deleted_at"`
	StatusID                     int         `json:"status_id"`
	Archived                     int         `json:"archived"`
	WarrantyMonths               interface{} `json:"warranty_months"`
	Depreciate                   int         `json:"depreciate"`
	SupplierID                   interface{} `json:"supplier_id"`
	Requestable                  int         `json:"requestable"`
	RtdLocationID                string      `json:"rtd_location_id"`
	Accepted                     interface{} `json:"accepted"`
	LastCheckout                 string      `json:"last_checkout"`
	ExpectedCheckin              interface{} `json:"expected_checkin"`
	CompanyID                    int         `json:"company_id"`
	AssignedType                 interface{} `json:"assigned_type"`
	LastAuditDate                interface{} `json:"last_audit_date"`
	NextAuditDate                interface{} `json:"next_audit_date"`
	LocationID                   int         `json:"location_id"`
	CheckinCounter               int         `json:"checkin_counter"`
	CheckoutCounter              int         `json:"checkout_counter"`
	RequestsCounter              int         `json:"requests_counter"`
	SnipeitMemoria2              string      `json:"_snipeit_memoria_2"`
	SnipeitSo3                   string      `json:"_snipeit_so_3"`
	SnipeitHd4                   string      `json:"_snipeit_hd_4"`
	SnipeitHostname5             string      `json:"_snipeit_hostname_5"`
	SnipeitCPU6                  string      `json:"_snipeit_cpu_6"`
	SnipeitModelo7               string      `json:"_snipeit_modelo_7"`
	SnipeitSetor8                string      `json:"_snipeit_setor_8"`
	SnipeitOffice9               string      `json:"_snipeit_office_9"`
	SnipeitProgramasInstalados10 interface{} `json:"_snipeit_programas_instalados_10"`
	Model                        Model       `json:"model"`
}

func Put(ip, token string, id int, PutRequest string) (Success, error) {
	EmptyRespose := Success{}
	url := "http://" + ip + "/api/v1/hardware/" + strconv.Itoa(id)
	log.Println(url)
	payload := strings.NewReader(PutRequest)

	req, err := http.NewRequest("PUT", url, payload)

	if err != nil {
		return EmptyRespose, err
	}

	req.Header.Add("Accept", "application/json")
	req.Header.Add("Authorization", "Bearer "+token)
	req.Header.Add("Content-Type", "application/json")

	res, errRes := http.DefaultClient.Do(req)
	if errRes != nil {
		return EmptyRespose, fmt.Errorf("falha de conexão com o host Snipeit. %v", errRes)
	}

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)
	log.Println(string(body))
	Success := Success{}
	json.Unmarshal(body, &Success)

	return Success, nil
}

func (old FullAssetT) CompareAsset(new FullAssetT) (string, bool) {

	ExistentAsset := old.ToShort()
	Asset := new.ToShort()

	var IsDifferent bool = false
	//Variável Array com as informações do Struct de análise
	var ExistentAssetIndex = []string{ExistentAsset.Name, ExistentAsset.AssetTag, ExistentAsset.ModelID, ExistentAsset.StatusID, ExistentAsset.Memory, ExistentAsset.SO, ExistentAsset.HD, ExistentAsset.Hostname, ExistentAsset.CPU, ExistentAsset.Model}

	//Variável Array com as informações do Struct do Ativo Criado
	var AssetIndex = []string{Asset.Name, Asset.AssetTag, Asset.ModelID, Asset.StatusID, Asset.Memory, Asset.SO, Asset.HD, Asset.Hostname, Asset.CPU, Asset.Model}

	//Variavél Array que contém as alterações pendentes
	var Pending []string

	//Variável String que contém o príncipio do Patchrequest
	var Patchresquest string = "{\"requestable\":false,\"archived\":false"

	//Verifica as disparidades, destacando-as e criando o Patchrequest.
	for in, v := range AssetIndex {

		if v != ExistentAssetIndex[in] && in != 1 {
			IsDifferent = true
			break
		}

	}
	if IsDifferent {

		//Cria tabela com os Cabeçalhos "Ativo Existente", "Ativo Criado"
		tbl := table.New("Fieldname", "Ativo Existente", "Ativo Criado")

		log.Println("Disparidades encontradas.")

		//Analise de disparidades
		for i := 0; i < len(ExistentAssetIndex); i++ {
			if ExistentAssetIndex[i] != AssetIndex[i] {
				var Fieldname string
				switch i {
				case 0:
					//Caso a disparidade seja encontrada no Index [0] do Array, é necessário PATCH no campo NAME
					Patchresquest += ",\"name\":\"" + AssetIndex[i] + "\""
					Fieldname = "NAME"
				case 2:
					//Caso a disparidade seja encontrada no Index [2] do Array, é necessário PATCH no campo MODEL ID
					Patchresquest += ",\"model_id\":\"" + AssetIndex[i] + "\""
					Fieldname = "MODEL ID"
				case 3:
					//Caso a disparidade seja encontrada no Index [3] do Array, é necessário PATCH no campo STATUS ID
					Patchresquest += ",\"status_id\":\"" + AssetIndex[i] + "\""
					Fieldname = "STATUS ID"
				case 4:
					//Caso a disparidade seja encontrada no Index [4] do Array, é necessário PATCH no campo MEMÓRIA
					Patchresquest += ",\"_snipeit_memoria_2\":\"" + AssetIndex[i] + "\""
					Fieldname = "MEMÓRIA"
				case 5:
					//Caso a disparidade seja encontrada no Index [5] do Array, é necessário PATCH no campo SISTEMA OPERACIONAL
					Patchresquest += ",\"_snipeit_so_3\":\"" + AssetIndex[i] + "\""
					Fieldname = "SISTEMA OPERACIONAL"
				case 6:
					//Caso a disparidade seja encontrada no Index [6] do Array, é necessário PATCH no campo HD
					Patchresquest += ",\"_snipeit_hd_4\":\"" + AssetIndex[i] + "\""
					Fieldname = "HD"
				case 7:
					//Caso a disparidade seja encontrada no Index [7] do Array, é necessário PATCH no campo HOSTNAME
					Patchresquest += ",\"_snipeit_hostname_5\":\"" + AssetIndex[i] + "\""
					Fieldname = "HOSTNAME"
				case 8:
					//Caso a disparidade seja encontrada no Index [8] do Array, é necessário PATCH no campo CPU
					Patchresquest += ",\"_snipeit_cpu_6\":\"" + AssetIndex[i] + "\""
					Fieldname = "CPU"
				case 9:
					//Caso a disparidade seja encontrada no Index [9] do Array, é necessário PATCH no campo MODELO
					Patchresquest += ",\"_snipeit_modelo_7\":\"" + AssetIndex[i] + "\""
					Fieldname = "MODEL"
				case 10:
					//Caso a disparidade seja encontrada no Index [10] do Array, é necessário PATCH no campo OFFICE
					Patchresquest += ",\"_snipeit_office_9\":\"" + AssetIndex[i] + "\""
					Fieldname = "OFFICE"
				case 11:
					//Caso a disparidade seja encontrada no Index [11] do Array, é necessário PATCH no campo PROGRAMAS INSTALADOS
					Patchresquest += ",\"_snipeit_programas_instalados_10\":\"" + AssetIndex[i] + "\""
					Fieldname = "PROGRAMAS INSTALADOS"
				}

				//Acrescenta informações a tabela
				tbl.AddRow(Fieldname, ExistentAssetIndex[i], AssetIndex[i])

				//Acrescenta alterações a uma lista de pendências para expor visualmente depois
				Pending = append(Pending, AssetIndex[i])
			} else {
				//Se não há disparidades, continue a análise
				continue
			}
		}

		ProgramsRequest := Asset.ComparePrograms(ExistentAsset)
		//Fechamento do Patchresquest
		Patchresquest += ProgramsRequest + "}"
		log.Printf("\nAlterações pendentes:\n%v\n", Pending)
		//Caso haja alterações,printe a tabela retorna true
		tbl.Print()
		return Patchresquest, true
	} else {
		//Caso não.. retorna false
		log.Println("Nenhuma disparidade foi encontrada no Ativo...")

		//Cria tabela com os Cabeçalhos "Fieldname" e "Ativo Existente"
		tbl := table.New("Fieldname", "Ativo Existente")

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

				Fieldname = "MEMÓRIA"
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

			//Acrescenta informações a tabela
			tbl.AddRow(Fieldname, ExistentAssetIndex[i])

		}

		//Expõe tabela do Ativo Existente
		tbl.Print()

		return Patchresquest, false
	}
}

func (ExistentAsset AssetT) ComparePrograms(Asset AssetT) string {

	var IsDifferent bool = false

	ExistentAssetPrograms := strings.Split(ExistentAsset.Installed, " | ")
	AssetPrograms := strings.Split(Asset.Installed, " | ")

	tbl := table.New("STATUS", "PROGRAMA")

	for in, v := range AssetPrograms {

		if v != ExistentAssetPrograms[in] {
			IsDifferent = true
			break
		}
	}

	if IsDifferent {

		var PatchrequestSlice string = ", \"_snipeit_programas_instalados_10\":\""

		log.Println("Programa(s) desconhecido(s) encontrado(s). Refazendo lista de programas instalados.")

		for in, v := range AssetPrograms {

			if v == ExistentAssetPrograms[in] {

				tbl.AddRow("Novo!", v)

			}

			tbl.AddRow("Existente", v)
		}

		PatchrequestSlice += strings.Join(AssetPrograms, " | ")

		return PatchrequestSlice

	} else {

		log.Println("Não há novos programas instalados.")

		for _, v := range AssetPrograms {

			tbl.AddRow("Existente", v)

		}

		return ""
	}
}

func Patch(ip, token string, id int, PutRequest string) (Success, error) {

	EmptyRespose := Success{}

	if id < 2 {
		return EmptyRespose, fmt.Errorf("invalid id")
	}

	url := "http://" + ip + "/api/v1/hardware/" + strconv.Itoa(id)

	if !strings.ContainsAny(PutRequest, "{\"}") {
		return EmptyRespose, fmt.Errorf("invalid put request")
	}

	payload := strings.NewReader(PutRequest)

	req, err := http.NewRequest("PUT", url, payload)

	if err != nil {
		return EmptyRespose, err
	}

	req.Header.Add("Accept", "application/json")
	req.Header.Add("Authorization", "Bearer "+token)
	req.Header.Add("Content-Type", "application/json")

	res, errRes := http.DefaultClient.Do(req)
	if errRes != nil {
		return EmptyRespose, fmt.Errorf("falha de conexão com o host Snipeit. %v", errRes)
	}

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)
	SuccessPatch := Success{}
	json.Unmarshal(body, &SuccessPatch)
	if EmptyRespose == SuccessPatch {
		return EmptyRespose, fmt.Errorf(string(body))
	}
	return SuccessPatch, nil

}

type messagesT struct {
	Status   string `json:"status"`
	Messages string `json:"messages"`
}

func Delete(ip, token string, id int) (messagesT, error) {
	EmptyRespose := messagesT{}
	if id < 3 {
		return EmptyRespose, fmt.Errorf("invalid id")
	}

	url := "http://" + ip + "/api/v1/hardware/" + strconv.Itoa(id)

	req, errReq := http.NewRequest("DELETE", url, nil)
	if errReq != nil {
		return EmptyRespose, errReq
	}
	req.Header.Add("Accept", "text/plain")
	req.Header.Add("Authorization", "Bearer "+token)

	res, errRes := http.DefaultClient.Do(req)

	if errRes != nil {
		return EmptyRespose, fmt.Errorf("falha de conexão com o host Snipeit. %v", errRes)
	}

	defer res.Body.Close()

	msgT := messagesT{}
	body, _ := ioutil.ReadAll(res.Body)
	json.Unmarshal(body, &msgT)

	if msgT.Status == "error" {
		return EmptyRespose, fmt.Errorf(msgT.Messages)
	} else if msgT == EmptyRespose {
		return EmptyRespose, fmt.Errorf("error getting response")
	}

	return msgT, nil

}

func Post(ip, token string, asset AssetT) error {
	json, err := json.Marshal(asset)

	if err != nil {
		return err
	}

	url := "http://" + ip + "/api/v1/hardware/"

	req, errReq := http.NewRequest("POST", url, bytes.NewBuffer(json))

	if errReq != nil {
		return errReq
	}

	req.Header.Add("Accept", "application/json")
	req.Header.Add("Authorization", "Bearer "+ token)
	req.Header.Add("Content-Type", "application/json")

	res, errRes := http.DefaultClient.Do(req)

	if errRes != nil {
		return fmt.Errorf("falha de conexão com o host Snipeit. %v", errRes)
	}

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)
	fmt.Println(string(body))

	return nil
}
