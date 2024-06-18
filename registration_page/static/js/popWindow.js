let button = document.querySelector('.send-button')


button.addEventListener(
    'click', (event) =>{
        event.preventDefault()
        document.querySelector('.popup-window').style.display = 'flex'
        document.querySelector('.main-form').submit()
    }
)

