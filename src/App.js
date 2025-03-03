import { useState } from "react";
import "./App.css"; // Import CSS
import robotImage from "/Users/ysp/Desktop/Desktop Folders/Grammar Check/my-react-app/src/CB2-removebg-preview.png"; // Add a robot image in public folder or src

function App() {
  const [text, setText] = useState("");
  const [correctedText, setCorrectedText] = useState("");

  const checkGrammar = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/check_grammar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();
      setCorrectedText(data.corrected_text);
    } catch (error) {
      console.error("Error connecting to the backend:", error);
    }
  };

  return (
    <div className="app-container">
      <h1>Gram Check</h1>
      <div className="input-container">
        <img src={robotImage} alt="Robot" className="floating-robot" />
        <textarea 
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter your text"
        />
      </div>
      <button onClick={checkGrammar}>Check Grammar</button>
      <h2>Corrected Text:</h2>
      <p>{correctedText}</p>
    </div>
  );
}

export default App;
