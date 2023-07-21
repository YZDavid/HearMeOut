// Dashboard.js

import React, { useState, useEffect } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";
import {
  StyledContainer,
  StyledTitle,
  StyledTextBox,
  StyledButton,
  StyledDisplayBox,
  StyledLogoutButton,
  ErrorMsg,
  StyledConversionHistory,
  StyledConversionItem,
  StyledDropdown,
  StyledSelectedConversion,
  StyledAudioLink,
  StyledAudioPlayer,
} from "../components/Styles1";

function Dashboard() {
  const history = useHistory();
  const [text, setText] = useState("");
  const [convertedText, setConvertedText] = useState("");
  const [error, setError] = useState("");
  const [conversionHistory, setConversionHistory] = useState([]);
  const [selectedConversion, setSelectedConversion] = useState(null);

  useEffect(() => {
    fetchConversionHistory();
  }, []);

  const fetchConversionHistory = async () => {
    try {
      const response = await axios.get("/conversions");
      const history = response.data;
      setConversionHistory(history);
    } catch (error) {
      console.error(error);
    }
  };

  const handleLogout = () => {
    history.push("/Home");
  };

  const handleConvert = async (audio = false) => {
    if (text.trim() === "") {
      setError("Please enter some text to convert.");
      return;
    }

    try {
      setError("");
      const response = await axios.post("/conversions", { input: text, audio });
      const { output } = response.data;
      setConvertedText(output);
      fetchConversionHistory();
    } catch (error) {
      setError("Conversion failed.");
      console.error(error);
    }
  };

  const handleConversionSelect = async (event) => {
    const selectedId = parseInt(event.target.value);
    const selectedConversion = conversionHistory.find(
      (conversion) => conversion.id === selectedId
    );
    setSelectedConversion(selectedConversion);

    try {
      const response = await axios.get(`/conversions/${selectedId}`);
      const { input, output, audio_filename } = response.data;
      setSelectedConversion({ id: selectedId, input, output, audio_filename });
    } catch (error) {
      console.error(error);
    }
  };

  const [showInputOutput, setShowInputOutput] = useState(false);

  const handleAudioConvert = async () => {
    if (text.trim() === "") {
      setError("Please enter some text to convert.");
      return;
    }

    try {
      setError("");
      const response = await axios.post("/conversions", { input: text, audio: true });
      const { output, audio_filename } = response.data;
      setConvertedText(output);
      setSelectedConversion({ input: text, output, audio_filename });
      setShowInputOutput(false); // Hide the input and output sections
    } catch (error) {
      setError("Conversion failed.");
      console.error(error);
    }
  };

  return (
    <StyledContainer>
      <div>
        <StyledTitle>Welcome to HearMeOut</StyledTitle>
      </div>
      <div style={{ display: "flex" }}>
        <div style={{ flex: "1" }}>
          <StyledTextBox
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Paste or type your text here..."
          />
          <div></div>
          {error && <ErrorMsg>{error}</ErrorMsg>}
          <div style={{ display: "flex" }}> {/* Separate the buttons */}
            <div>
              <StyledButton onClick={() => handleConvert()}>Convert</StyledButton>
            </div>
            <div style={{ marginLeft: "1rem" }}>
              <StyledButton onClick={handleAudioConvert}>Audio</StyledButton> {/* Add the "Audio" button */}
            </div>
          </div>
          <StyledDisplayBox
            value={convertedText}
            readOnly
            placeholder="Converted text will appear here"
          />
          {selectedConversion && selectedConversion.audio_filename && (
            <div style={{ marginTop: "1rem" }}>
              <StyledAudioLink href={`/audio/${selectedConversion.audio_filename}`} download>
                Download Audio
              </StyledAudioLink>
              <StyledAudioPlayer controls>
                <source src={`/audio/${selectedConversion.audio_filename}`} type="audio/mp3" />
                Your browser does not support the audio element.
              </StyledAudioPlayer>
            </div>
          )}
        </div>
        <div style={{ flex: "1", marginLeft: "1rem" }}>
          <StyledConversionHistory>
            <StyledDropdown onChange={handleConversionSelect}>
              {/* Show the selected conversion if available */}
              {selectedConversion ? (
                <option value={selectedConversion.id}>Conversion {selectedConversion.id}</option>
              ) : (
                <option value="">Select your Conversion History</option>
              )}
              {conversionHistory.map((conversion) => (
                <option key={conversion.id} value={conversion.id}>
                  Conversion {conversion.id}
                </option>
              ))}
            </StyledDropdown>
            {selectedConversion && (
              <StyledSelectedConversion>
                <p>Input: {selectedConversion.input}</p>
                <p>Output: {selectedConversion.output}</p>
              </StyledSelectedConversion>
            )}
          </StyledConversionHistory>
        </div>
      </div>
      <StyledLogoutButton onClick={handleLogout}>Logout</StyledLogoutButton>
    </StyledContainer>
  );
}

export default Dashboard;