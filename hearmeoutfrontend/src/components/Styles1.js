

import styled from "styled-components";

// background
import background from "./../assets/HMOBG.png";

// React router
import { Link } from "react-router-dom";


export const colors = {
  primary: "#fff",
  theme: "#BE185D",
  light1: "#F3F4F6",
  light2: "#E5E7EB",
  dark1: "#1F2937",
  dark2: "#4B5563",
  dark3: "#9CA3AF",
  red: "#DC2626",
};

export const StyledContainer = styled.div`
  margin: 0;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: linear-gradient(
      0deg,
      rgba(0, 0, 0, 0.6),
      rgba(0, 0, 0, 0.6)
    ),
    url(${background});
  background-size: cover;
  background-attachment: fixed;
`;

export const StyledTitle = styled.h2`
  font-size: ${(props) => props.size}px;
  text-align: center;
  color: ${(props) => (props.color ? props.color : colors.primary)};
  padding: 5px;
  margin-bottom: 20px;
`;

export const StyledTextBox = styled.textarea`
  width: 400px;
  height: 150px;
  padding: 10px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  background-color: ${colors.light2};
  color: ${colors.dark1};
  resize: vertical;
  margin-bottom: 20px;
`;

export const StyledButton = styled.button`
  padding: 10px 20px;
  font-size: 16px;
  background-color: ${colors.theme};
  color: ${colors.primary};
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-bottom: 20px;
`;

export const StyledDisplayBox = styled.textarea`
  width: 400px;
  height: 200px;
  padding: 10px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  background-color: ${colors.light2};
  color: ${colors.dark1};
  resize: vertical;
`;

export const StyledLogoutButton = styled.button`
  padding: 15px 30px;
  font-size: 20px;
  background-color: ${colors.primary};
  color: ${colors.theme};
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 20px;
`;

export const ErrorMsg = styled.div`
  font-size: 14px;
  color: red;
  margin-top: 5px;
  text-align: center;
`;
