const handleCartEdit = async e => {
    if (e.target.dataset.type === 'cart-edit-btn') {
        e.preventDefault()
        const response = await fetch(`/cart/${e.target.dataset.action}/${e.target.dataset.product_id || ""}`)
        const htmlString = await response.text()

        const parser = new DOMParser()
        const htmlDocument = parser.parseFromString(htmlString, 'text/html')
        const productsTableUpdated = htmlDocument.querySelector('#products_table')

        products_table.replaceWith(productsTableUpdated)
    }
}

document.addEventListener('click', (e) => { handleCartEdit(e) })
