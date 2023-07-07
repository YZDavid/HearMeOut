import React, { useState } from 'react';
import axios from 'axios';
import {
  StyledContainer,
  StyledTitle,
  StyledTextBox,
  StyledButton,
  StyledDisplayBox,
  StyledLogoutButton,
  ErrorMsg
} from '../components/Styles1';

function Dashboard() {
  const [text, setText] = useState('');
  const [convertedText, setConvertedText] = useState('');
  const [error, setError] = useState('');

  const handleLogout = () => {
    // Perform logout operation, such as redirecting to the login page or clearing user session
    // Add your logout logic here
  };

  const handleConvert = async () => {
    if (text.trim() === '') {
      // Handle empty input
      return;
    }

    try {
      const response = await axios.post('/convert', { text });
      const { convertedText } = response.data;
      setConvertedText(convertedText);
    } catch (error) {
      setError('Conversion failed.');
      console.error(error);
    }
  };

  return (
    <StyledContainer>
      <div>
        <StyledTitle>Welcome to HearMeOut</StyledTitle>
      </div>
      <div>
        <StyledTextBox
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Paste or type your text here..."
        />
        <div>
        </div>
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
      <StyledLogoutButton onClick={handleLogout}>Logout</StyledLogoutButton>
    </StyledContainer>
  );
}

export default Dashboard;
