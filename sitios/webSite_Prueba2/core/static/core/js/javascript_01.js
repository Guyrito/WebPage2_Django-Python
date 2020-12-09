function fechaHora()
{
    var fecha = new Date();
    document.getElementById("fechaHora").innerHTML="la fecha de hoy es: "+fecha;
    var tiempo = setTimeout(function(){fechaHora()},1000);
}

$(document).ready(function() 
{
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open ('GET','https://mindicador.cl/api',true);
    xmlhttp.send();

    var dolar = 0;

    xmlhttp.onreadystatechange = function() 
    {
        if (this.readyState == 4 && this.status == 200)
        {
            var data = JSON.parse(this.responseText);
            dolar = data.dolar.valor;
        }
        document.getElementById("valorDolar").innerHTML = "Valor actual del Dólar: " + new Intl.NumberFormat('es-CL',{style:'currency',currency:'CLP',maximumFractionDigits:2}).format(dolar);
    }   
});

function usdToClp(valNum)
{
    parseFloat(document.getElementById("inputCLP").value=valNum*749).toFixed(2);
}
function clpToUsd(valNum)
{
    parseFloat(document.getElementById("inputUSD").value=valNum*0.0013).toFixed(2);
}
