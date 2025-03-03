import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css'; // Optional: Your global styles
import App from './App'; // Import the App component
import reportWebVitals from './reportWebVitals'; // Optional: For measuring performance

const root = ReactDOM.createRoot(document.getElementById('root')); // Create a root for rendering
root.render(
  <React.StrictMode>
    <App /> {/* Render the App component */}
  </React.StrictMode>
);

// Optional: For measuring performance
reportWebVitals();