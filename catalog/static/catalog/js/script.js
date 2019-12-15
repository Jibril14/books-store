
const open_menu = document.querySelector('.menu')
const nav_container = document.querySelector('.nav-container')
  
const mobile_logo = document.querySelector('.logo') 

open_menu.addEventListener('click', () =>{
 nav_container.classList.toggle('active')
 mobile_logo.classList.toggle('active')
 
})



const counters = document.querySelectorAll(".counter")
console.log("c",counters)
counters.forEach(count=>{
    count.innerText = '0' 
    const updateCounter = () => {
      const target = Number(count.getAttribute('data-target'))
      const c = Number(count.innerText)
      const increment = target / 1000
      
      if (c < target){
        count.innerText = `${Math.ceil(c + increment)}`
        setTimeout(updateCounter, 100 )
      }else{
        count.innerText = target
      }
      
    }
    
   
    updateCounter()
})


const profile = document.querySelector('.profile-card')
const card_content = document.querySelector('.card-content')

window.addEventListener("scroll", showProfile)

function showProfile(){
  const triggerPoint = window.innerHeight * 0.8
  console.log("TriggerPoint",triggerPoint)

        const profileTop = profile.getBoundingClientRect().top
        console.log("ProfileTop",profileTop)
        if(profileTop < triggerPoint){
            profile.classList.add('show')
            card_content.classList.add('show')
        } else{
            profile.classList.remove('show')
            card_content.classList.remove('show')
        }
  
}