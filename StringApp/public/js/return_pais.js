
var select_country=document.getElementsByName("country")[0]
var   lista=[]

fetch(
  `https://restcountries.com/v3.1/all`
)
.then((request) => request.json())
.then((response) => {

        response.forEach(e=>{lista.push(e.name.common)})

  var lista_order=[...lista.sort()]

lista_order.forEach(evt=>{
    var option = document.createElement("option");
    option.text = evt;
    select_country.add(option);
})


  });