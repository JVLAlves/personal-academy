
function carregar() {
var msg = window.document.getElementById('msg')
var img = window.document.getElementById('image')
var date = new Date() 
var hour = date.getHours()
msg.innerHTML= `Agora são ${hour} horas.`

if (hour >= 0 && hour < 12) {
//BOM DIA - COLOR #F8B892
img.src = "Morning.png"
document.body.style.background = "#F8B892"

}else if (hour >= 12 && hour <18){
//BOA TARDE - COLOR #00BAAD
img.src = "Noon.png"
document.body.style.background = "#00BAAD"

}else {
//BOA NOITE - COLOR #0D343C
img.src = "Night.png"
document.body.style.background = "#0D343C"


}
}