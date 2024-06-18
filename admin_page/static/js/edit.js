let listButtonImage = document.querySelectorAll(".edit-img-btn")

for (let count = 0; count < listButtonImage.length; count++) {
    let button = listButtonImage[count]
    button.addEventListener(
        type = "click",
        listener = (event) => {
            document.querySelector(".modal-window").style.display = "flex"

            let inputData = document.querySelector(".input-data")
            inputData.type = "file" 
            inputData.accept = "image/*"
            inputData.name = "image"
            document.querySelector(".modal-label").textContent= "CHANGE IMAGE:"
            document.querySelector('.change-btn').value = `image-${button.id}`
        }
    )
}

let listButtonName = document.querySelectorAll(".edit-name")

for (let count = 0; count < listButtonName.length; count++) {
    let button = listButtonName[count]
    button.addEventListener(
        type = "click",
        listener = (event) => {
            document.querySelector(".modal-window").style.display = "flex"
            let inputData = document.querySelector(".input-data")
            inputData.type = "text"
            inputData.name = "name"
            document.querySelector(".modal-label").textContent= "CHANGE TEXT:"
            document.querySelector('.change-btn').value = `name-${button.id}`
        }
    )
}

let listButtonPrice = document.querySelectorAll(".edit-price")

for (let count = 0; count < listButtonPrice.length; count++) {
    let button = listButtonPrice[count]

    button.addEventListener(
        type = "click",
        listener = (event) => {
            document.querySelector(".modal-window").style.display = "flex"

            let inputData = document.querySelector(".input-data")
            inputData.type = "number"
            inputData.name = "price"
            document.querySelector(".modal-label").textContent= "CHANGE PRICE:"
            document.querySelector('.change-btn').value = `price-${button.id}`
        }
    )
}

let listButtonDiscount = document.querySelectorAll(".edit-discount")

for (let count = 0; count < listButtonDiscount.length; count++) {
    let button = listButtonDiscount[count]

    button.addEventListener(
        type = "click",
        listener = (event) => {
            document.querySelector(".modal-window").style.display = "flex"

            let inputData = document.querySelector(".input-data")
            inputData.type = "number"
            inputData.name = "discount"
            document.querySelector(".modal-label").textContent= "CHANGE DISCOUNT:"
            document.querySelector('.change-btn').value = `discount-${button.id}`
        }
    )
}

document.querySelector('.new-product').addEventListener(
    'click', (event) => {
        event.preventDefault()
        document.querySelector('.new-product-div').style.display = 'flex'
    }
)


