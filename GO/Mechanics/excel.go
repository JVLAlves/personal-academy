package excel

import (
	"fmt"
	"log"
	"strings"

	"github.com/360EntSecGroup-Skylar/excelize"
)

func main() {

	f, err := Open("Excelest.xlsx")
	if err != nil {
		log.Println(err)
	}
	cell := f.GetCellValue("PLAN", "A1")
	fmt.Println("A1: ", cell)
	rows := f.GetRows("PLAN")

	for _, row := range rows {

		for _, colCell := range row {
			fmt.Print(colCell, "\t")
		}
		fmt.Println()
	}

}

func Open(filename string) (*excelize.File, error) {
	fileparts := strings.Split(filename, ".")
	if len(fileparts) == 0 || (len(fileparts) == 2 && fileparts[1] == "") {
		return nil, fmt.Errorf("invalid file")
	}

	f, err := excelize.OpenFile(filename)
	if err != nil {
		return nil, err
	}

	return f, nil
}
