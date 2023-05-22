import React, { useState } from "react"; 

export const Login = (props) => {
    const [email, setEmail] = useState('');
    const [pass, setPass] = useState(''); 

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(email);
    }
    
    return (
        <div className="auth-form-container">
            <form className="login-form" onSubmit={handleSubmit}>
                <label htmlFor="email">email</label>
                <input value={email} onChange={(e) => setEmail(e.target.value)} type="email" placeholder="myemail@gmail.com" id="email" name="email"/>
                <label for="password">password</label>
                <input value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="*******" id="password" name="password"/>
                <button type="submit">Log In</button>
            </form>
            <button className="link-btn" onClicck={() => props.onFormSwitch('register')}> Don't have an account? Register here.</button>
        </div>
    )
}