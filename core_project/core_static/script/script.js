let categories = document.querySelectorAll('.categories ul li')

for(let cate of categories){
    cate.addEventListener('click', () =>{
        categories.forEach((category) =>{
            // Remove the 'active_category' class from all categories
            category.classList.remove('active')
        })
         // Add the 'active_category' class to the clicked category
        cate.classList.add('active')
    })
}


// hot_items slider

const slider = document.querySelector(".items_slider")
const prevBtn = document.querySelector(".prev_item")
const nxtBtn = document.querySelector(".next_item")
const itemWidth = slider.querySelector(".items_card").offsetWidth;
const cards_len = slider.querySelectorAll(".items_card").length

let currIndex = 0

function updateArrows() {
    prevBtn.style.display = currIndex === 0 ? "none" : "block";
    nxtBtn.style.display =
      currIndex === cards_len - 1 ? "none" : "block";
  }

//event listener for prev_button
prevBtn.addEventListener('click', () =>{
    if(currIndex > 0){
        currIndex--;
        const translateX = -currIndex * itemWidth;
        slider.style.transform = `translateX(${translateX}px)`
    }
    updateArrows()
})


// next_button event listener

nxtBtn.addEventListener("click", function () {
    if (currIndex < cards_len - 1) {
      currIndex++;
      const translateX = -currIndex * itemWidth;
      slider.style.transform = `translateX(${translateX}px)`;
      updateArrows();
    } else{
        // If the last card is visible, do nothing when clicking the next button
    }
  });

  updateArrows()



//   Countdown timer for deal_timer.html page

const dealEnd = new Date('2023-12-12T23:59:59').getTime()

const updateCountdown = () =>{
    const currTime = new Date().getTime()
    const timeRemaining = dealEnd - currTime

    const days = Math.floor(timeRemaining / (1000 * 60 * 60 *24))
    const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) /(1000 * 60 * 60) )
    const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60))
    const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000)

    document.getElementById('days').innerText = days
    document.getElementById('hours').innerText = hours
    document.getElementById('minutes').innerText = minutes
    document.getElementById('seconds').innerText = seconds

    if(timeRemaining <= 0){
        document.getElementById('countdown').innerHTML = 'Deal has expired'
    }
}

setInterval(updateCountdown, 1000);
updateCountdown()