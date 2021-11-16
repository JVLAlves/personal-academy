let num = document.querySelector('input#number')
let lista = document.querySelector('select#listbox')
let res = document.querySelector('div#return')
let valores = []

function isNumero(n){
    if (Number(n) >= 1 && Number(n) <= 100){
        return true
    } else {return false}
}

function inLista(n, l){
    if (l.indexOf(Number(n)) != -1 ){
        return true
    } else {return false}


}

function add(){
    if (isNumero(num.value) && !inLista(num.value, valores)){
        valores.push(Number(num.value))
        let item = document.createElement('option')
        item.text = `Valor ${Number(num.value)} adicionado.`
        lista.appendChild(item)
        res.innerHTML=""
    }else {window.alert('valor inválido ou já encontrado na lista.')}
    num.value = ''
    num.focus()
}

function send(){
    if (valores.length == 0){
        window.alert('adicione valores antes de finalizar!')
    }else{
        let tot = valores.length
        let maior = valores[0]
        let menor = valores[0]
        let soma = 0
        let media = 0
        for (let pos in valores){
            soma += valores[pos]

            if (valores[pos] > maior){
                maior = valores[pos]
            }
            if (valores[pos] < menor){
                menor = valores[pos]
            }
        }
        media = soma/tot
        res.innerHTML=""
        res.innerHTML += `<p> Ao todo, temos ${tot} números cadastrados.</p>`
        res.innerHTML += `<p> O maior valor informado foi ${maior}.</p>`
        res.innerHTML += `<p> O menor valor informado foi ${menor}.</p>`
        res.innerHTML += `<p> Somando todos os valores, temos ${soma}.</p>`
        res.innerHTML += `<p> A média dos valores digitados é ${media}.</p>`

    }
}