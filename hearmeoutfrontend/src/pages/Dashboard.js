import { StyledTitle, StyledSubTitle, Avatar,
    StyledButton, ButtonGroup,
    StyledFormArea, colors } from "./../components/Styles";
    
    import React, { useState } from 'react';
    
    //Logo
    import Logo from "./../assets/HearMeOutLogo.png"

    
    const Dashboard = () => {
        const [inputText, setInputText] = useState('');
        const [convertedText, setConvertedText] = useState('');

        const handleInputChange = (e) => {
            setInputText(e.target.value);
  };

  const handleConvertClick = () => {
    // Perform your conversion logic here
    const converted = inputText.toUpperCase();
    setConvertedText(converted);
  };

        return (
          <div>
            <div styles={{
                position: "absolute",
                top: 0,
                left: 0,
                backgroundColor: "transparent",
                width: "100%",
                display: "flex",
                justifyContent: "flex-start",
            }} >
                <Avatar image={Logo} /> 
            </div>
            <StyledFormArea bg={colors.dark2}>
                <StyledTitle size={12}>
                <h1> Let HMO do the talking </h1>
                <input type="etext"/> 

        <ButtonGroup>
        <StyledButton to="/Convert"> Convert </StyledButton>
        </ButtonGroup>

                </StyledTitle>
                <ButtonGroup>
                    <StyledButton to="/Home" >Logout</StyledButton>
                </ButtonGroup>
            </StyledFormArea>
          </div>
        )
    }
    
    export default Dashboard; 
    