
const open_menu = document.querySelector('.menu')
const nav_container = document.querySelector('.nav-container')
  
const mobile_logo =document.querySelector('.logo') 

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

