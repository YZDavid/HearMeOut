
import { StyledTitle, StyledSubTitle, Avatar,
StyledButton, ButtonGroup } from "./../components/Styles";

import React from 'react';

//Logo
import Logo from "./../assets/HearMeOutLogo.png"

const Home = () => {
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
        <StyledTitle size={65}>
            Welcome to HearMeOut
        </StyledTitle>
        <StyledSubTitle size={27}>
           Ready to start hearing111 ?
        </StyledSubTitle>

        <ButtonGroup>
        <StyledButton to="/login"> Login </StyledButton>

        <StyledButton to="/dashboard"> Guest Login </StyledButton>

        <StyledButton to="/signup"> Signup </StyledButton>
        </ButtonGroup>
      </div>
    )
}

export default Home; 
