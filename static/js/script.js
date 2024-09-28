document.addEventListener('DOMContentLoaded', () => {
    const itemForm = document.getElementById('item-form');
    const itemsTable = document.getElementById('items-table');
    let items = [];

    // Function to render items into the table
    function renderItems() {
        itemsTable.innerHTML = '';
        items.forEach((item, index) => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${index + 1}</td>
                <td>${item.name}</td>
                <td>${item.quantity}</td>
                <td>$${item.price}</td>
                <td><button onclick="deleteItem(${index})">Delete</button></td>
            `;
            itemsTable.appendChild(row);
        });
    }

    // Handle form submission to add a new item
    itemForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const name = document.getElementById('item-name').value;
        const quantity = document.getElementById('item-quantity').value;
        const price = document.getElementById('item-price').value;

        // Add new item to the list
        items.push({ name, quantity, price });

        // Render updated items list
        renderItems();

        // Clear the form
        itemForm.reset();
    });

    // Function to delete an item
    window.deleteItem = (index) => {
        items.splice(index, 1);
        renderItems();
    };
});
