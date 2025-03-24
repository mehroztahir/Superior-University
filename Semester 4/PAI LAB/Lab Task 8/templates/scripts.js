document.getElementById('weatherForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const city = document.getElementById('city').value;

    fetch('/get_weather', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `city=${encodeURIComponent(city)}`
    })
    .then(response => response.json())
    .then(data => {
        const weatherResult = document.getElementById('weatherResult');
        if (data.error) {
            weatherResult.innerHTML = `<p class="error">${data.error}</p>`;
        } else {
            weatherResult.innerHTML = `
                <h2>${data.city}</h2>
                <p>Temperature: ${data.temperature}°C</p>
                <p>Description: ${data.description}</p>
                <img src="http://openweathermap.org/img/wn/${data.icon}.png" alt="${data.description}">
            `;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});