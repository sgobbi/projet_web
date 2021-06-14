

window.addEventListener("DOMContentLoaded", (event) => {
    var socket = io.connect("http://" + document.domain + ":" + location.port );

    document.onkeydown = function(e){
        switch(e.keyCode){
            case 37:
                socket.emit("move", {dx:-1, dy:0});
                break;
            case 38:
                socket.emit("move", {dx:0, dy:-1});
                break;
            case 39:
                socket.emit("move", {dx:1, dy:0});
                break;
            case 40:
                socket.emit("move", {dx:0, dy:1});
                break;
        }


    };
    
    var btn_n = document.getElementById("go_n");
    btn_n.onclick = function(e) {
        console.log("Clicked on button north");
        socket.emit("move", {dx:0, dy:-1});
    };

    var btn_s = document.getElementById("go_s");
    btn_s.onclick = function(e) {
        console.log("Clicked on button south");
        socket.emit("move", {dx:0, dy:1});
    };

    var btn_w = document.getElementById("go_w");
    btn_w.onclick = function(e) {
        console.log("Clicked on button w");
        socket.emit("move", {dx:-1, dy:0});
    };

    var btn_e = document.getElementById("go_e");
    btn_e.onclick = function(e) {
        console.log("Clicked on button e");
        socket.emit("move", {dx:1, dy:0});
    };


    socket.on("response", function(Data){
        console.log(Data);
        var data = Data[0];   
        var lifes = Data[1];
        var coins = Data[2];
        var swords = Data[3];


        for( var i=0; i<2; i++){
            var cell_id = "cell " + data[i].i + "-" + data[i].j;
            var span_to_modif = document.getElementById(cell_id);
            span_to_modif.textContent = data[i].content;
        } 

        var doc = document.getElementById("life");
        doc.innerText = lifes ;

        /*for( var i=0; i<data.length; i++){
            var cell_id = "cell " + data[i].i + "-" + data[i].j;
            var span_to_modif = document.getElementById(cell_id);
            span_to_modif.className = data[i].content;
        }
        
        for(var j=0;j<accessoire.length;j++)
        {
            var life = document.getElementById("life" + (j+1).toString());
            life.innerHTML = "Vies Joueur" + (j+1).toString() + " ; " + accessoire[j];
            if(j==1)
            {
                life.style.visibility = "visible";
            }
        }  */
        
    });

});