import React from 'react';

function Header() {
    const school = {
        name: "Boston University",
        location: "Boston, MA"
    };

    return (
        <div>
            <header className="app-header">
                <h1>UniEats</h1>
            </header>
            <section className="school-section">
                <h2>School: {school.name}</h2>
                <p>Location: {school.location}</p>
            </section>
        </div>
    );
}

export default Header;
