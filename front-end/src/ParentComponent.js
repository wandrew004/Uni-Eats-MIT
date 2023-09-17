import React, { useState } from 'react';
import CaloriesInput from './CaloriesInput';
import CalorieDisplay from './CalorieDisplay';

function ParentComponent() {
    const [calories, setCalories] = useState('');

    return (
        <div>
            <CaloriesInput calories={calories} setCalories={setCalories} />
            <CalorieDisplay calories={calories} />
        </div>
    );
}

export default ParentComponent;
