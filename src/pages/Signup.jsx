import React, { useRef } from "react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import ".//signup.css";

const Logincom = () => {
  //global variable
  const navigate = useNavigate();
  //local vaiables
  const usernameref = useRef(null);
  const passwordref = useRef(null);
  const checkpasswordref = useRef(null);
  //functions
  const reset_input = (e) => {
    e.preventDefault();
    usernameref.current.value = "";
    passwordref.current.value = "";
    checkpasswordref.current.value = "";
  };
  const onSubmit = (event) => {
    event.preventDefault();
  };
  return (
    <div className="page_container">
      <h1 className="main_heading">TODO X</h1>
      <div className="container">
        <form action="#" onSubmit={onSubmit}>
          <h3 className="login_heading">Sign up Page</h3>
          <div className="input_field">
            <label htmlFor="username" className="label">
              Username :{" "}
            </label>
            <input
              className="input"
              type="text"
              name="username"
              ref={usernameref}
              autoComplete="new-password"
              required
            />
            <br />
            <br />
            <label htmlFor="password" className="label">
              Password :{" "}
            </label>
            <input
              className="input"
              type="password"
              name="password"
              ref={passwordref}
              autoComplete="off"
              required
            />
            <br />
            <br />
            <label htmlFor="password" className="label">
              Password :{" "}
            </label>
            <input
              className="input"
              type="password"
              name="password"
              ref={checkpasswordref}
              autoComplete="off"
              required
            />
            <br />
            <br />
            <button type="submit" className="submit_btn">
              Sign up
            </button>
            <button className="reset" onClick={reset_input}>
              Reset
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Logincom;
