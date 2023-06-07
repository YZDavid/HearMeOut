import { StyledTitle, StyledSubTitle, Avatar,
    StyledButton, ButtonGroup,
    StyledFormArea, colors } from "./../components/Styles";
    
    import React from 'react';
    
    //Logo
    import Logo from "./../assets/HearMeOutLogo.png"
    
    const Dashboard = () => {
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
                <StyledTitle size={65}>
                    Welcome, User
                </StyledTitle>

                <ButtonGroup>
                    <StyledButton to="#" >Logout</StyledButton>
                </ButtonGroup>
            </StyledFormArea>
            
          </div>
        )
    }
    
    export default Dashboard; 
    