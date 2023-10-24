const API_URL = 'http://127.0.0.1:5000';
const vehicleDropdown = document.getElementById('vehicleDropdown');
const vehicleForm = document.getElementById('vehicleForm');

// Charge la liste des véhicules dans le menu déroulant
fetch(API_URL + '/get_vehicules')
    .then(response => response.json())
    .then(data => {
        data.forEach(vehicle => {
            const option = document.createElement('option');
            option.value = vehicle.id;
            option.textContent = vehicle.desc;
            vehicleDropdown.appendChild(option);
        });
    })
    .catch(error => console.error("Erreur lors de la récupération des véhicules:", error));

// Gère la soumission du formulaire
vehicleForm.addEventListener('submit', function (event) {
    event.preventDefault();

    const selectedVehicleId = vehicleDropdown.value;
    fetch(`${API_URL}/get_summary/${selectedVehicleId}`)
        .then(response => response.text())
        .then(filename => {
            const downloadBox = document.getElementById('downloadBox');
            const linkElement = document.getElementById('downloadLink');
            linkElement.href = `${API_URL}${filename}`;
            downloadBox.style.display = 'block';    
        })
        .catch(error => console.error('Erreur lors de la soumission:', error));
});
