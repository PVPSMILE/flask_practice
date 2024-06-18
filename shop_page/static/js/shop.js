const listButtons = document.querySelectorAll('.button')

let basketLink = document.querySelector('.basket-link')
let tickCount = 0

let p = document.createElement('p')

// document.body.appendChild()

for (let count = 0; count < listButtons.length; count++) {
    let button = listButtons[count]
    button.addEventListener(
        type = 'click',
        listener = function (event) {
            console.log('added')

            let img = document.createElement("img")
            img.src = 'img/cart-tick.png'
            img.classList.add('cart-tick')
            basketLink.appendChild(img)

            tickCount++
            p.textContent = tickCount
            p.classList.add('cart-p')
            basketLink.appendChild(p)

            if(p.textContent > 9){
                p.style.fontSize = 10
                p.style.paddingTop = 12
            }

            if (document.cookie == ''){
                document.cookie = `products = ${button.id}; path = / `

            }else{
                product_id = document.cookie.split('=')[1]
                document.cookie = `products = ${product_id} ${button.id}; path = / `
            }
        }
    )
}




