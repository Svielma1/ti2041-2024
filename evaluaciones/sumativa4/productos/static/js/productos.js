const token = "{{ token }}";

async function eliminarProducto(code) {
    try {
        const response = await fetch(`/api/productos/${code}`, {
            method: 'DELETE',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Error al eliminar el producto');
        }

        alert('Producto eliminado exitosamente');
        window.location.reload();
    } catch (error) {
        console.error('Error:', error);
        alert('Error: ' + error.message);
    }
}

document.querySelectorAll('.delete-button').forEach(button => {
    button.addEventListener('click', () => {
        const code = button.dataset.code;
        eliminarProducto(code);
    });
});