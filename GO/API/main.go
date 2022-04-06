package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"strconv"
	"strings"
)

type Book struct {
	ID     int    `json:"id"`
	Title  string `json:"title"`
	Author string `json:"author"`
}

var Books []Book = []Book{
	{ID: 1, Title: "O Guarani", Author: "José de Alencar"},
	{ID: 2, Title: "Cazuza", Author: "Viriato Correia"},
	{ID: 3, Title: "Dom Casmurro", Author: "Machado de Assis"},
}

func MainRoute(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "hello, world")
}

func ListBooks(w http.ResponseWriter, r *http.Request) {
	if r.Method != "GET" {
		return
	}
	w.Header().Set("Content-Type", "application/json")
	encoder := json.NewEncoder(w)
	encoder.Encode(Books)
}

func PostBooks(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)

	slcbyt, err := ioutil.ReadAll(r.Body)
	if err != nil {
		log.Fatal(err)
	}
	var NewBook Book
	json.Unmarshal(slcbyt, &NewBook)
	if NewBook.ID == 0 {
		NewBook.ID = len(Books) + 1
	}

	Books = append(Books, NewBook)
	encoder := json.NewEncoder(w)
	encoder.Encode(NewBook)

}

func DeleteBook(w http.ResponseWriter, r *http.Request) {

	parts := strings.Split(r.URL.Path, "/")
	id, err := strconv.Atoi(parts[2])
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		return
	}

	BookIndex := -1

	for in, b := range Books {
		if b.ID == id {
			BookIndex = in
			break
		}
	}

	if BookIndex < 0 {
		w.WriteHeader(http.StatusNotFound)
		return
	}

	Left := Books[0:BookIndex]
	Right := Books[BookIndex+1:]
	Books = append(Left, Right...)

	w.WriteHeader(http.StatusNoContent)

}

func UpdateBook(w http.ResponseWriter, r *http.Request) {

	parts := strings.Split(r.URL.Path, "/")
	id, errID := strconv.Atoi(parts[2])

	if errID != nil {

		w.WriteHeader(http.StatusBadRequest)
		return

	}

	body, errRead := ioutil.ReadAll(r.Body)

	if errRead != nil {

		w.WriteHeader(http.StatusInternalServerError)
		return

	}

	var UpdatedBook Book

	errJson := json.Unmarshal(body, &UpdatedBook)
	UpdatedBook.ID = id

	if errJson != nil {

		w.WriteHeader(http.StatusBadRequest)
		return

	}

	BookIndex := -1
	for in, b := range Books {

		if b.ID == id {
			BookIndex = in
			break
		}

	}

	if BookIndex < 0 {
		w.WriteHeader(http.StatusNotFound)
		return
	}

	Books[BookIndex] = UpdatedBook

	json.NewEncoder(w).Encode(UpdatedBook)

}

func RouteBooks(w http.ResponseWriter, r *http.Request) {
	fmt.Println(r.Method)
	fmt.Println(r.URL.Path)
	parts := strings.Split(r.URL.Path, "/")
	if r.Method == "GET" {
		fmt.Println(parts)
		if len(parts) == 2 || len(parts) == 3 && parts[2] == "" {
			ListBooks(w, r)
		} else if len(parts) == 3 || len(parts) == 4 && parts[3] == "" {
			fmt.Println(parts)
			SearchBooks(w, r)
		} else {
			w.WriteHeader(http.StatusBadRequest)
		}
	} else if r.Method == "POST" {
		PostBooks(w, r)
	} else if r.Method == "DELETE" {
		DeleteBook(w, r)
	} else if r.Method == "PUT" {

		UpdateBook(w, r)

	} else {
		w.WriteHeader(http.StatusNotFound)
	}

}

func SearchBooks(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	parts := strings.Split(r.URL.Path, "/")

	id, err := strconv.Atoi(parts[2])
	if err != nil {
		w.WriteHeader(http.StatusNotFound)
		return
	}

	for _, b := range Books {
		if b.ID == id {
			json.NewEncoder(w).Encode(b)
			return
		}
	}

	w.WriteHeader(http.StatusNotFound)

}

func ConfigRoutes() {
	http.HandleFunc("/", MainRoute)
	http.HandleFunc("/books/", RouteBooks)
}
func ConfigServer() {

	ConfigRoutes()
	fmt.Println("Servidor rodando na porta 1337")
	log.Fatal(http.ListenAndServe(":1337", nil))
}

func main() {

	ConfigServer()

}
