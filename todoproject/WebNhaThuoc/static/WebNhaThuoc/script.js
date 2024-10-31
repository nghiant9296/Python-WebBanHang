

// Hàm tìm kiếm thuốc
function searchMedicines() {
    const input = document.getElementById('searchInput');
    const filter = input.value.toLowerCase();
    const medicineList = document.getElementById('medicineList');
    const items = medicineList.getElementsByTagName('li');

    for (let i = 0; i < items.length; i++) {
        const item = items[i].textContent || items[i].innerText;
        if (item.toLowerCase().indexOf(filter) > -1) {
            items[i].style.display = "";
        } else {
            items[i].style.display = "none";
        }
    }
}

// Giỏ hàng
let cart = [];
let totalPrice = 0;

function addToCart(productName, productPrice) {
    cart.push({ name: productName, price: productPrice });
    totalPrice += productPrice;
    updateCart();
}

function updateCart() {
    const cartItems = document.getElementById('cart-items');
    cartItems.innerHTML = ""; // Xóa nội dung cũ

    cart.forEach(item => {
        const li = document.createElement('li');
        li.className = "list-group-item";
        li.textContent = `${item.name} - ${item.price} VND`;
        cartItems.appendChild(li);
    });

    document.getElementById('total-price').textContent = totalPrice;
}



// function toggleDropdown() {
//     const dropdownMenu = document.getElementById('category-menu');
//     const isVisible = dropdownMenu.style.display === 'block';
    
//     dropdownMenu.style.display = isVisible ? 'none' : 'block'; // Đảo ngược hiển thị
// }
function toggleDropdown() {
    const menu = document.getElementById('category-menu');
    menu.style.display = menu.style.display === 'none' ? 'block' : 'none';
}


// Đóng dropdown khi nhấp ra ngoài
document.addEventListener('click', function(event) {
    const dropdownMenu = document.getElementById('category-menu');
    const button = document.querySelector('.group button');

    // Nếu nhấp ra ngoài nút và menu, ẩn dropdown
    if (!button.contains(event.target) && !dropdownMenu.contains(event.target)) {
        dropdownMenu.style.display = 'none';
    }
});
