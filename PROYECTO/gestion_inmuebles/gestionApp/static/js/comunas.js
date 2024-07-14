document.addEventListener("DOMContentLoaded", function() {
    const regionSelect = document.querySelector('.region-select select');
    const comunaSelect = document.querySelector('.comuna-select select');

    regionSelect.addEventListener('change', function() {
        const regionId = regionSelect.value;

        if (regionId) {
            fetch(`/load-comunas/?region_id=${regionId}`)
                .then(response => response.json())
                .then(data => {
                    comunaSelect.innerHTML = '<option value="">--- Seleccione Comuna ---</option>';
                    data.forEach(function(comuna) {
                        const option = document.createElement('option');
                        option.value = comuna.id;
                        option.textContent = comuna.nombre;
                        comunaSelect.appendChild(option);
                    });
                });
        } else {
            comunaSelect.innerHTML = '<option value="">--- Seleccione Comuna ---</option>';
        }
    });
});
