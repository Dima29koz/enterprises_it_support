document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('field1');
    input.addEventListener('keyup', getMatches);

    function getMatches(elem) {
        const inputVal = elem.currentTarget.value;
        fetch(`./index4?field1=${inputVal}`)
            .then(response => response.json())
            .then(matches_json => {
                const container = document.getElementById('field2');
                container.innerText = matches_json.matches;
            });
    }
});