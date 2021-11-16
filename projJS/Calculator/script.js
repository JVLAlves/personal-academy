const divRes = window.document.getElementById("response")
const n1 = window.document.getElementById("n1");
const n2 = window.document.getElementById("n2");

function options(){
    let divOpt = window.document.getElementById("options");
    divOpt.innerHTML = ""
    let form = document.createElement("form");
    CreateRadioInput(form, "sum", "+")
    CreateRadioInput(form, "sub", "-")
    CreateRadioInput(form, "times", "*")
    CreateRadioInput(form, "divide","/")
    let submit = document.createElement("input");
    submit.setAttribute("type", "submit")
    submit.setAttribute("onclick", "alterInputs()")
    form.appendChild(submit)
    divOpt.appendChild(form)
}

function alterInputs(){
    let opt;
    let radio = document.getElementsByName("operator");
    for (let i = 0; i < radio.length; i++){
             if (radio[i].checked){
                opt = radio[i].value
             }
         }
    let p = window.document.getElementById("operatorSignal");
    let btnres = document.getElementById("btnres");
    switch (opt){

        case "+":
            btnres.setAttribute("onclick","sum()")
            break
        case "-":
            btnres.setAttribute("onclick","sub()")
            break
        case "*":
            btnres.setAttribute("onclick","times()")
            break
        case "/":
            btnres.setAttribute("onclick","divide()")
            break
        default:
            alert("Resposta inválida.")
    }
    p.innerText = opt
    let divOpt = document.getElementById("options");
    divOpt.innerHTML = ""
        }


function CreateRadioInput(parent, id, value){

    let Input = document.createElement("input");
    Input.setAttribute("type", "radio")
    Input.setAttribute("name", "operator")
    Input.setAttribute("id", id)
    Input.setAttribute("value", (value))

    const label = document.createElement("label");
    label.setAttribute("for", id)
    label.innerText = value

    const brk = document.createElement("br");

    parent.appendChild(Input)
    parent.appendChild(label)
    parent.appendChild(brk)


}

function sum(){
    historyClear()

    const s = Number(n1.value) + Number(n2.value);
    const newP = window.document.createElement("p");
    newP.setAttribute("name", "history")
    newP.innerText = `${Number(n1.value)} + ${Number(n2.value)} = ${s}`
    divRes.appendChild(newP)
}

function sub(){
   historyClear()
    const s = Number(n1.value) - Number(n2.value);
    const newP = window.document.createElement("p");
    newP.setAttribute("name", "history")
    newP.innerText = `${Number(n1.value)} - ${Number(n2.value)} = ${s}`
    divRes.appendChild(newP)
}

function times(){
   historyClear()
    const s = Number(n1.value) * Number(n2.value);
    const newP = document.createElement("p");
    newP.setAttribute("name", "history")
    newP.innerText = `${Number(n1.value)} * ${Number(n2.value)} = ${s}`
    divRes.appendChild(newP)
}

function divide(){
    historyClear()
    const s = Number(n1.value) / Number(n2.value);
    const newP = window.document.createElement("p");
    newP.setAttribute("name", "history")
    newP.innerText = `${Number(n1.value)} / ${Number(n2.value)} = ${s}`
    divRes.appendChild(newP)
}

function historyClear(){
    const elemToClear = document.getElementsByName("history");
    let i = 4
    if (elemToClear.length > 4) {
        while (elemToClear.length > 0){
            divRes.removeChild(elemToClear[i])
            i--
        }
    }

}