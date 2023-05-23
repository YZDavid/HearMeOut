import React, { useEffect, useState } from "react"; 

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
                <label htmlFor="email">Email 📧</label>
                <input value={email} onChange={(e) => setEmail(e.target.value)} type="email" placeholder="user@hearmeout.com" id="email" name="email"/>
                <label for="password">Password 🔐</label>
                <input value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="*******" id="password" name="password"/>
                <button type="submit">Log Me In!</button>
            </form>
            <button className="link-btn" onClick={() => props.onFormSwitch('register')}> Don't have an account? Register here.</button>
        </div>
    )
}