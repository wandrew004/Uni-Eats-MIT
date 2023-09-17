import React from 'react';
import './App.css';  // 
import Header from './header';  // 
import CaloriesInput from './CaloriesInput';
import BodySection from './bodysection';

function App() {
    return (
      <div className="App container space-y-large">  
        <Header />
        <div className="App-container">
          <CaloriesInput />
          <BodySection />
        </div>
      </div>
    );
}

export default App;
