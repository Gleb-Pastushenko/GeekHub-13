const handleAddToCart = e => {
    if (e.target.dataset.type === 'add-to-cart-btn') {
        e.preventDefault()
        fetch(`/cart/add/${e.target.dataset.product_id}`)
    }
}

document.addEventListener('click', (e) => { handleAddToCart(e) })
