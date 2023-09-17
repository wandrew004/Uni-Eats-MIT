import React, { useState } from 'react';


function CaloriesInput() {
    const [calories, setCalories] = useState(''); // Initializing state to store calorie input
    
    // React.useEffect(() => {
    //     // Using fetch to fetch the api from
    //     // flask server it will be redirected to proxy
    //     fetch("/data").then((res) =>
    //         res.json().then((data) => {
    //             // Setting a data from api
    //             console.log(data.Name);
    //         })
    //     );
    // }, []);
    

    const handleChange = (event) => {
        setCalories(event.target.value); // Update calorie amount with user input
    };

    const handleKeyDown = (event) => {
        if (event.key === 'Enter') {
            saveCalories();
            console.log(calories);
        }
    };

    const saveCalories = () => {
        fetch("/api/data", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({userInput: calories})
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log(data.message);
        })
        .catch(error => {
            console.error("Error:", error);
        });
    };
    

    return (
        <section className="calories-section">
            <label htmlFor="calorie-input">Enter Calorie Amount: </label>
            <input
                type="number"
                id="calorie-input"
                value={calories}
                onChange={handleChange}
                onKeyDown={handleKeyDown} // Add onKeyDown event here
                placeholder="e.g., 2000"
            />
            <p>You've entered {calories} calories.</p>
        </section>
    );
}

export default CaloriesInput;
