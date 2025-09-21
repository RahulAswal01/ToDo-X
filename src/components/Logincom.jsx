import React, { useRef } from "react";
import { useState } from "react";
import { useRecoilState } from "recoil";
import userInfoAtom from "./recoil/userInfo";

const Logincom = () => {
  //global variable
  const [userInfo, setUserInfo] = useRecoilState(userInfoAtom);

  //usestate
  // not working function
  // const reset = () => {
  //   const usernameref = useRef(null);
  //   const passwordref = useRef(null);
  // };
  //local vaiables
  const usernameref = useRef(null);
  const passwordref = useRef(null);
  //functions
  const onSubmit = (event) => {
    event.preventDefault();
    console.log("username is : ", usernameref?.current?.value);
    console.log("password is : ", passwordref?.current?.value);
    const usercred = {
      username: usernameref?.current?.value,
      password: passwordref?.current?.value,
    };
    fetch("http://127.0.0.1:8000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(usercred),
    })
      .then((res) => res.json())
      .then((res) => {
        console.log(res);
        if (res.message === "Successfully login") {
          localStorage.setItem("userStatus", true);
          setUserInfo(true);
        } else {
          localStorage.setItem("userStatus", false);
        }
      })
      .catch((error) => console.log(error));
  };
  return (
    <div className="page_container">
      <h1 className="main_heading">TODO X</h1>
      <div className="container">
        <form action="#" onSubmit={onSubmit}>
          <h3 className="login_heading">Login Page</h3>
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
            <button type="submit" className="submit_btn">
              Login
            </button>
            <button className="reset">Reset</button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Logincom;
