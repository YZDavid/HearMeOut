import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useHistory } from 'react-router-dom'; // Import the useHistory hook
import {
  StyledContainer,
  StyledTitle,
  StyledTextBox,
  StyledButton,
  StyledDisplayBox,
  StyledLogoutButton, // Assuming you have a custom styled component for the Logout button
  ErrorMsg,
  StyledConversionHistory,
  StyledConversionItem,
  StyledDropdown,
  StyledSelectedConversion
} from '../components/Styles1';

function Dashboard() {
  const history = useHistory(); // Initialize the useHistory hook
  const [text, setText] = useState('');
  const [convertedText, setConvertedText] = useState('');
  const [error, setError] = useState('');
  const [conversionHistory, setConversionHistory] = useState([]);
  const [selectedConversion, setSelectedConversion] = useState(null);

  useEffect(() => {
    fetchConversionHistory();
  }, []);

  const fetchConversionHistory = async () => {
    try {
      const response = await axios.get('/conversions');
      const history = response.data;
      setConversionHistory(history);
    } catch (error) {
      console.error(error);
    }
  };

  const handleLogout = () => {
    // Perform logout operation, such as redirecting to the login page or clearing user session
    // Add your logout logic here

    // Redirect the user to the /Home page upon logout
    history.push('/Home');
  };

  const handleConvert = async () => {
    if (text.trim() === '') {
      // Handle empty input
      return;
    }

    try {
      const response = await axios.post('/conversions', { input: text });
      const { output } = response.data; // Update the field name to match the backend response
      setConvertedText(output);
      fetchConversionHistory(); // Fetch the updated conversion history
    } catch (error) {
      setError('Conversion failed.');
      console.error(error);
    }
  };

  const handleConversionSelect = async (event) => {
    const selectedId = parseInt(event.target.value);
    const selectedConversion = conversionHistory.find((conversion) => conversion.id === selectedId);
    setSelectedConversion(selectedConversion);

    // Fetch the selected conversion by ID from the backend
    try {
      const response = await axios.get(`/conversions/${selectedId}`);
      const { input, output } = response.data;
      setSelectedConversion({ id: selectedId, input, output });
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <StyledContainer>
      <div>
        <StyledTitle>Welcome to HearMeOut </StyledTitle>
      </div>
      <div>
        <div style={{ display: 'flex' }}>
          <div style={{ flex: '1' }}>
            <StyledTextBox
              value={text}
              onChange={(e) => setText(e.target.value)}
              placeholder="Paste or type your text here..."
            />
            <div></div>
            {error && <ErrorMsg>{error}</ErrorMsg>}
            <div>
              <StyledButton onClick={handleConvert}>Convert</StyledButton>
            </div>
            <StyledDisplayBox
              value={convertedText}
              readOnly
              placeholder="Converted text will appear here"
            />
          </div>
          <div style={{ flex: '1', marginLeft: '1rem' }}>
            <StyledConversionHistory>
              <StyledDropdown onChange={handleConversionSelect}>
                <option value="">Select your Conversion History </option>
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
      </div>
      <StyledLogoutButton onClick={handleLogout}>Logout</StyledLogoutButton>
    </StyledContainer>
  );
}

export default Dashboard;
