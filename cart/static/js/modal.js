let currentForm;
    

function showModal() {
    currentForm = event.target;
    document.getElementById('modal-message').innerText = `Your personal data, ready to buy?`;
    document.getElementById('modal').style.display = 'block';
    return false;
}

function submitForm() {
    currentForm.submit();
}

function closeModal() {
    document.getElementById('modal').style.display = 'none';
}