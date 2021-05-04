

//declaring all constant variables used in code
const dropDown = document.querySelector('[data-drop-down')
const body = document.querySelector('body')
const playerOne = document.querySelector('[data-player-one]')
const playerTwo = document.querySelector('[data-player-two]')
const btn = document.querySelector('[data-btn]')


const playerTwoHealthBar = document.querySelector('.health-one.player-two')
const playerOneHealthBar = document.querySelector('.health-one.player-one')
const shootArrow = document.querySelector('[data-btn-bow]')
const arrow = document.querySelector('.arrow')


function player() {
    this.playerHealth= 80
}

var player1 = new player()
var player2 = new player()


playerTwo.addEventListener('click', e=>{
    body.classList.add("attack")
    
})

//toggles drop down menu when "Choose Move is selected"
btn.addEventListener('click', e=>{    
    dropDown.classList.toggle("show")
})


//when choice "Bow" is clicked, arrow is shot
//will either hit or miss in this case there is 80% chance of hit
shootArrow.addEventListener('click', e=>{
    bowShot()
   
})

function bowShot(){
    arrow.style.display = "initial"
    arrow.style.animation = "shoot 250ms ease-out forwards"
    setTimeout(function(){arrow.style.display = "none"}, 350)
    if (hitChance(80)==true){
        player2.playerHealth -= 10
        
        playerTwoHealthBar.style.width = player2.playerHealth +"px"
        if (player2.playerHealth <= 0){
            playerDeath()
            
        }
    }
}

//when choice "Saber" is clicked, saber is slashed
//will either hit or miss in this case there is 95% chance of hit
//since it is up close however, there is a chance that you will also get hit
const swingSword = document.querySelector('[data-btn-saber]')
const saber = document.querySelector('.saber')
swingSword.addEventListener('click', e=>{
    slash()

})

function slash(){
    saber.style.display = "initial"
    saber.style.animation = "slash 250ms ease-out forwards"
    setTimeout(function(){saber.style.display = "none"}, 350)
    if (hitChance(95)==true){
        player2.playerHealth -= 20
        if(player2.playerHealth < 0){
            player2.playerHealth = 0
        }
        playerTwoHealthBar.style.width = player2.playerHealth +"px"
        if (player2.playerHealth <= 0){
            playerDeath()
        }

        if (hitChance(50)==true){
            player1.playerHealth -= 20
        
        }
        playerOneHealthBar.style.width = player1.playerHealth +"px"
        if (player1.playerHealth  <= 0){
            playerDeath()
        }  
      
    }

}


//calculates whether or not attack was a hit
//based off percentaged passed as argument
function hitChance(accuracy){
    let hit = null
    let random = Math.floor((Math.random()*100))
    if (random <= accuracy){
        hit = true
    }
    else{
        hit = false
    }
    return hit
}

const healButton = document.querySelector(['data-btn-heal'])
healButton.addEventListener('click', e=>{
    heal(player1.playerHealth)
     

})

function heal(health){
    health += 5
    playerOneHealthBar.style.width = player1.playerHealth +"px"
}


//will happen when you die
const everyDiv = document.querySelectorAll('div')
console.log(everyDiv)

function playerDeath(){
    everyDiv.forEach(function(content){
        content.style.backgroundColor = "black" 
    })

}

