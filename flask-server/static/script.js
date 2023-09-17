const searchBox = document.getElementById('calories');

searchBox.addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        const query = searchBox.value;
        fetchAPI(query);
    }
});

function fetchAPI(query) {
    fetch(`http://localhost:5000/api/data`, {
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
    })
    .catch(error => {
        console.error("There was an error fetching data:", error);
    });
}
