import React, { useState } from "react";
import CalorieDisplay from './CalorieDisplay';



export default function BodySection() {
const [entree, setEntree] = useState("");
const [appetizer, setAppetizer] = useState("");
const [dessert, setDessert] = useState("");



const generateRandomValues = () => {

const randomEntree = "Random Entree"; 
const randomAppetizer = "Random Appetizer"; 
const randomDessert = "Random Dessert";



setEntree(randomEntree);
setAppetizer(randomAppetizer);
setDessert(randomDessert);


};


return (

<div className="bodysection-list">

<button onClick={generateRandomValues}>Regenerate</button>

<div className="foodsection-list">

<h2>Entree: {entree}</h2>
<h2>Appetizer: {appetizer}</h2>
<h2>Dessert: {dessert}</h2>
<h2> <CalorieDisplay /> </h2>



</div>

</div>
);
}
