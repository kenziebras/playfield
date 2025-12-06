// --- CONFIGURATION ---
// Mengambil variabel dari "jembatan" data di main.html
const GET_PRODUCTS_URL = DJANGO_VARS.getProductsUrl;
const CREATE_PRODUCT_URL = DJANGO_VARS.createProductUrl;
const GET_PRODUCT_JSON_URL_BASE = DJANGO_VARS.getProductJsonUrlBase;
const EDIT_PRODUCT_URL_BASE = DJANGO_VARS.editProductUrlBase;
const DELETE_PRODUCT_URL_BASE = DJANGO_VARS.deleteProductUrlBase;
const CURRENT_USER_ID = DJANGO_VARS.currentUserId;
const CSRF_TOKEN = DJANGO_VARS.csrfToken;

// --- DOM ELEMENTS ---
const grid = document.getElementById('products-grid');
const gridContainer = document.getElementById('products-grid-container');
const loading = document.getElementById('loading-state');
const error = document.getElementById('error-state');
const emptyAjax = document.getElementById('empty-state-ajax'); // State kosong khusus untuk hasil fetch AJAX

// --- STATE MANAGEMENT ---
function showState(state) {
    loading.classList.toggle('hidden', state !== 'loading');
    error.classList.toggle('hidden', state !== 'error');
    emptyAjax.classList.toggle('hidden', state !== 'empty');
    grid.classList.toggle('hidden', state !== 'grid');
}

// --- TOAST NOTIFICATION ---
function showToast(message, type = 'success') {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const toast = document.createElement('div');
    const bgColor = type === 'success' ? 'bg-green-500' : 'bg-red-500';
    
    toast.className = `px-4 py-3 rounded-md text-white ${bgColor} shadow-lg transition-all duration-300 transform translate-x-full opacity-0`;
    toast.textContent = message;
    
    container.appendChild(toast);

    // Animate in
    setTimeout(() => {
        toast.classList.remove('translate-x-full', 'opacity-0');
    }, 100);

    // Animate out and remove
    setTimeout(() => {
        toast.classList.add('opacity-0');
        toast.addEventListener('transitionend', () => toast.remove());
    }, 3000);
}

// --- MODAL HANDLING ---
function showModal(modalId, mode = 'create', productId = null) {
    const modal = document.getElementById(modalId);
    if (!modal) return;
    
    if (modalId === 'form-product-modal') {
        const form = document.getElementById('product-form');
        const title = document.getElementById('modal-title');
        const button = document.getElementById('modal-submit-button');
        
        form.reset();
        const errorDiv = document.getElementById('form-errors');
        if(errorDiv) errorDiv.textContent = '';
        
        if (mode === 'create') {
            title.textContent = 'Add New Product';
            button.textContent = 'Add Product';
            form.onsubmit = handleCreateSubmit;
        } else if (mode === 'update' && productId) {
            title.textContent = 'Edit Product';
            button.textContent = 'Update Product';
            // Populate form with existing data by fetching it
            fetch(`${GET_PRODUCT_JSON_URL_BASE}${productId}/`)
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'error') throw new Error(data.message);
                    document.getElementById('product-id').value = productId;
                    document.getElementById('name').value = data.name;
                    document.getElementById('price').value = data.price;
                    document.getElementById('description').value = data.description;
                    document.getElementById('thumbnail').value = data.thumbnail || '';
                    document.getElementById('category').value = data.category;
                    document.getElementById('is_featured').checked = data.is_featured;
                }).catch(err => {
                    console.error("Error fetching product data for edit:", err);
                    showToast("Failed to load product data.", "error");
                });
            form.onsubmit = (e) => handleUpdateSubmit(e, productId);
        }
    } else if (modalId === 'delete-confirm-modal' && productId) {
        const confirmButton = document.getElementById('confirm-delete-button');
        confirmButton.onclick = () => handleDelete(productId);
    }
    
    modal.classList.remove('hidden');
}

function hideModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) modal.classList.add('hidden');
}

// --- DYNAMIC CARD BUILDER ---
// Fungsi ini membuat HTML untuk satu kartu produk dari data JSON
// --- DYNAMIC CARD BUILDER ---
// Fungsi ini membuat HTML untuk satu kartu produk dari data JSON
function buildProductCard(product) {
    const fields = product.fields;
    const pk = product.pk;
    const isOwner = CURRENT_USER_ID && Number(CURRENT_USER_ID) === Number(fields.user);
    
    // Logika tombol: Tampilkan Edit/Delete hanya jika pengguna adalah pemilik
    let buttonsHtml = `
      <div class="pt-4 border-t border-gray-700">
        <a href="/product/${pk}/" class="text-gray-300 hover:text-gray-100 font-medium text-sm transition-colors">
          Detail →
        </a>
      </div>`;

    if (isOwner) {
        buttonsHtml = `
          <div class="flex items-center justify-between pt-4 border-t border-gray-700">
            <a href="/product/${pk}/" class="text-gray-300 hover:text-gray-100 font-medium text-sm transition-colors">
              Detail
            </a>
            <div class="flex space-x-2">
              <button onclick="showModal('form-product-modal', 'update', '${pk}')" class="text-gray-400 hover:text-gray-200 text-sm transition-colors">
                Edit
              </button>
              <button onclick="showModal('delete-confirm-modal', 'delete', '${pk}')" class="text-red-500 hover:text-red-400 text-sm transition-colors">
                Delete
              </button>
            </div>
          </div>`;
    }

    // Ganti tag <article> ini untuk menambahkan ID unik
    return `
        <article id="product-card-${pk}" class="bg-gray-800 border border-gray-700 rounded-lg overflow-hidden hover:shadow-2xl hover:shadow-gray-600/50 transition-shadow duration-300">
          <div class="p-5">
            <div class="flex items-center text-sm text-gray-400 mb-3">
              <time>${new Date(fields.created_at).toLocaleDateString("en-US", { day: 'numeric', month: 'short', year: 'numeric' })}</time>
              <span class="mx-2">•</span>
              <span>Views: ${fields.product_views}</span>
            </div>
            <h3 class="text-lg font-semibold text-gray-200 mb-3 line-clamp-2 leading-tight">
              <a href="/product/${pk}/" class="hover:text-gray-300 transition-colors">${fields.name}</a>
            </h3>
            <p class="text-gray-400 text-sm leading-relaxed line-clamp-3 mb-4">${fields.description.substring(0, 100)}...</p>
            <p class="text-gray-200 font-medium mb-4">Price: Rp ${fields.price}</p>
            ${buttonsHtml}
          </div>
        </article>`;
}
// --- AJAX FETCH & RENDER ---
async function fetchProducts() {
    showState('loading');
    try {
        const response = await fetch(GET_PRODUCTS_URL);
        if (!response.ok) throw new Error('Network response was not ok');
        const products = await response.json();
        
        // Sembunyikan state kosong bawaan Django jika ada
        const emptyStateServer = document.getElementById('empty-state');
        if(emptyStateServer) emptyStateServer.classList.add('hidden');

        grid.innerHTML = ''; // Kosongkan grid sebelum diisi ulang
        if (products.length === 0) {
            showState('empty');
        } else {
            products.forEach(product => {
                grid.innerHTML += buildProductCard(product);
            });
            showState('grid');
        }
    } catch (e) {
        console.error("Fetch error:", e);
        showState('error');
    }
}

// --- AJAX CRUD HANDLERS ---
async function handleCreateSubmit(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);

    const response = await fetch(CREATE_PRODUCT_URL, {
        method: 'POST',
        body: formData,
        headers: { "X-CSRFToken": CSRF_TOKEN } // Diperlukan untuk keamanan
    });
    
    const data = await response.json();
    if (response.ok) {
        hideModal('form-product-modal');
        showToast(data.message, 'success');
        fetchProducts(); // Refresh daftar produk
    } else {
        const errorDiv = document.getElementById('form-errors');
        if(errorDiv) errorDiv.textContent = "Please correct the errors.";
        console.error("Form errors:", data.errors);
    }
}

async function handleUpdateSubmit(event, productId) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);

    const response = await fetch(`${EDIT_PRODUCT_URL_BASE}${productId}/`, {
        method: 'POST',
        body: formData,
        headers: { "X-CSRFToken": CSRF_TOKEN }
    });

    const data = await response.json();
    if (response.ok) {
        hideModal('form-product-modal');
        showToast(data.message, 'success');
        fetchProducts();
    } else {
        const errorDiv = document.getElementById('form-errors');
        if(errorDiv) errorDiv.textContent = "Failed to update product.";
    }
}

async function handleDelete(productId) {
    // 1. Kirim request POST ke Django
    const response = await fetch(`${DELETE_PRODUCT_URL_BASE}${productId}/`, {
        method: 'POST',
        headers: { "X-CSRFToken": CSRF_TOKEN }
    });

    const data = await response.json();
    
    if (response.ok) {
        hideModal('delete-confirm-modal');
        showToast(data.message, 'success');
        
        // 2. HAPUS KARTU LANGSUNG DARI DOM UNTUK PENGALAMAN AJAX YANG CEPAT
        const cardElement = document.getElementById(`product-card-${productId}`);
        if(cardElement) {
            cardElement.remove();
        }
        
        // Cek jika setelah dihapus grid menjadi kosong
        // Lakukan pemanggilan fetchProducts() HANYA jika list menjadi kosong
        if(grid.childElementCount === 0) {
            fetchProducts();
        }

    } else {
        showToast('Failed to delete product: ' + (data.message || 'Server error.'), 'error');
    }
}

// --- EVENT LISTENERS & INITIALIZATION ---
// Menjalankan kode setelah seluruh halaman (DOM) selesai dimuat
document.addEventListener('DOMContentLoaded', () => {
    // Tombol refresh
    const refreshButton = document.getElementById('refresh-button');
    if(refreshButton) {
        refreshButton.addEventListener('click', fetchProducts);
    }
});

window.showModal = showModal;
window.hideModal = hideModal;
window.fetchProducts = fetchProducts;
window.deleteProduct = handleDelete; // Opsional jika Anda memanggilnya langsung