const button=document.getElementById('button');
const modal=document.getElementById('container');
const record_box=document.getElementById('record-container')
const label_property=document.getElementById('label-div')
const value_property=document.getElementById('value-div')

var message_box=document.getElementById('toggle-div')
var text=document.getElementById("message")
var button_ok=document.getElementById("btn-ok")

button.addEventListener('click',function(){
    // button.innerHTML="X";
    // button.style.backgroundColor="red";
    // button.style.width="50px";
    // button.style.paddingLeft="5px";
    // button.style.paddingRight="5px";
   
    modal.style.display = (modal.style.display === "none" || modal.style.display === "") ? "flex" : "none";
    hide();
})

function hide(){
    if(modal.style.display=="block"){
        label_property.style.display="none";
        value_property.style.display="none";
        modal.style.display="block";
        modal.style.marginLeft="20%";
    }
    else{
        label_property.style.display="block";
        value_property.style.display="block";
    }
}

hide();

message_box.addEventListener('click',function(){
    if (text.style.display=="none"){
        text.style.display="block";
        button_ok.style.display="block";
 
    }
    else if (message_box.style.display=="block"){
        message_box.style.display="none";
      
    }
})

button_ok.addEventListener('click',function(){
    message_box.style.display="none";
    text.style.display="none";
    button_ok.style.display="none";
})
