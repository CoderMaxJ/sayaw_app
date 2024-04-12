
text="Welcome to Sayaw Beach Resort"
text2="We offers you a very wonderful experience"
var label=document.getElementById('text').style.color="whitesmoke";






function loop(){
    setTimeout(function(){
        document.getElementById('text').innerHTML=text
        
      
    },3000)

    setTimeout(function(){
        document.getElementById('text').innerHTML=text2
    },6000) 
}

loop()



