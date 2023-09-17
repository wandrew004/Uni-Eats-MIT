const searchBox = document.getElementById('calories');
const regenerateButton = document.getElementById('regenerate');
var value = 0

searchBox.addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        const query = searchBox.value;
        value = query
        fetchAPI(query);
    }
});

regenerateButton.addEventListener('click', function() {
    fetchAPI(value)
});

function fetchAPI(query) {
    fetch(`http://127.0.0.1:5000/api/data`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            userInput: query
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        document.getElementById("foods").innerText = data
    
    })
    .catch(error => {
        console.error("There was an error fetching data:", error);
    });
}
