document.addEventListener('DOMContentLoaded', () => {
    const search_btn = document.getElementById('search-btn');
    search_btn.addEventListener("click", getWeather);

    function getWeather(e) {
        const input = document.getElementById('field1');
        const inputVal = input.value;
        console.log(inputVal);
        fetch(`get_weather?field1=${inputVal}`)
            .then(response => response.json())
            .then(weather_json => {
                const container = document.getElementById('field2');
                console.log(weather_json)
                container.innerText = weather_json.main.temp;
            });
    }
});