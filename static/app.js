function fetchWeather() {
    const city = document.getElementById('cityInput').value;
    const resultDiv = document.getElementById('result');

    if (city.trim() === '') {
        alert('Please enter a city name.');
        return;
    }

    fetch(`/weather?city=${city}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                resultDiv.innerHTML = `<p style="color: red;">${data.error}</p>`;
            } else {
                const weatherInfo = `
                    <p><strong>City:</strong> ${data.city}</p>
                    <p><strong>Country:</strong> ${data.country}</p>
                    <p><strong>Temperature:</strong> ${data.temperature}°C</p>
                    <p><strong>Description:</strong> ${data.description}</p>
                `;
                resultDiv.innerHTML = weatherInfo;
            }
        })
        .catch(error => {
            console.error("Error fetching weather:", error);
            resultDiv.innerHTML = `<p style="color: red;">Failed to fetch weather data.</p>`;
        });
}
