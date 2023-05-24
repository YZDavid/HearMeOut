import App from "../src/App";
import { StyledTitle, StyledSubTitle, Avatar, StyledButton, ButtomGroup } from "../src/Components/Styles";
import logo from './HearMeOut-1.png';

import { Link } from "react-router-dom";

const Home = () => { 
    return (
        <div>
            <div style={{
                position: "absolute",
                top: 0,
                left: 0,
                backgroundColor: "transparent",
                width: "100%",
                padding: "15px",
                display: "flex",
                justifyContent: "flex-start",  
            }}>
                <Avatar image={Logo} /> 
            </div>
            <StyledTitle size={65}>
                Welcome to HMO
            </StyledTitle>
            <StyledSubTitle size={27}> 
                Let The Magic Happen Now
            </StyledSubTitle>

            <ButtonGroup><StyledButton> to="/Login"  Login </StyledButton>
            <StyledButton> to="/Signup" Signup </StyledButton></ButtonGroup>
        </div>
    );
};

export default Home; 