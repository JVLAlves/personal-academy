package svgident

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func SearchImg(filename string) (bool, error) {
	f, err := os.Open(filename)

	if err != nil {
		return false, err
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		if strings.Contains(scanner.Text(), "<image") {
			return true, nil
		}
	}

	return false, nil
}

func GetValidFiles(files []string) ([]string, []error) {

	var errorlist []error
	var ValidFileList []string
	for _, f := range files {

		isImage, err := SearchImg(f)
		if err != nil {
			errorlist = append(errorlist, err)
			continue
		}

		if !isImage {
			ValidFileList = append(ValidFileList, f)
		} else {
			errorlist = append(errorlist, fmt.Errorf("the file %v contains an image", f))
		}
	}

	if len(ValidFileList) == len(files) {
		return ValidFileList, nil
	} else if len(ValidFileList) == 0 {
		return nil, errorlist
	} else {
		return ValidFileList, errorlist
	}

}

func GetImage(filename string) ([]string, error) {
	f, err := os.Open(filename)

	if err != nil {
		return nil, err
	}

	defer f.Close()
	var imgList []string
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		if strings.Contains(scanner.Text(), "<image") {
			imgList = append(imgList, strings.TrimSpace(scanner.Text()))
		}
	}

	if len(imgList) != 0 {
		return imgList, nil
	} else {
		return nil, fmt.Errorf("no images in file %v", filename)
	}

}

func NoImageFile(filename string) error {

	f, err := os.Open(filename)
	if err != nil {
		return err
	}
	defer f.Close()

	var lines []string
	var ImageExists int
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		fmt.Println(scanner.Text())
		if !strings.Contains(scanner.Text(), "<image") {
			lines = append(lines, scanner.Text())
		} else {
			ImageExists++
		}
	}

	if ImageExists == 0 {
		return fmt.Errorf("this file does not contains images")
	}

	if len(lines) == 0 || (len(lines) == 1 && lines[0] == "") {
		return fmt.Errorf("empty line array")
	}

	NoImageFile, err2 := os.OpenFile("NoImage"+filename, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)

	if err2 != nil {
		return err2
	}

	defer NoImageFile.Close()

	writer := bufio.NewWriter(NoImageFile)

	iter := 0
	for _, data := range lines {
		_, errW := writer.WriteString(data + "\n")

		if errW != nil {
			return fmt.Errorf("error writing file in line %v of content %v\t ERROR: %v", iter, data, errW)
		}
		iter++
	}

	writer.Flush()
	return nil
}
