import React, { useRef } from "react";
import Headercom from "../components/Headercom";
import "./homepg.css";
import Bodycom from "../components/Bodycom";
import Filter from "../components/Filter";
import Todos from "../components/Todos";
import AddTask from "../components/AddTask";
import addTaskAtom from "../components/recoil/addTaskAtom";
import { useRecoilState } from "recoil";
import apiDataAtom from "../components/recoil/apiDataAtom";
import todoatom from "../components/recoil/todoatom";
import { useGSAP } from "@gsap/react";
import gsap from "gsap";
import { useEffect } from "react";
import Updatetask from "../components/Updatetask";
import updateTaskAtom from "../components/recoil/updateTaskAtom";
const Homepg = () => {
  //variable
  const [apiData, setApiData] = useRecoilState(apiDataAtom);
  const [todoApiData, setTodoApiData] = useRecoilState(todoatom);
  const [addTaskOverlayer, setAddTaskOverlayer] = useRecoilState(addTaskAtom);
  const createref = useRef();
  const [updateTaskOverLayer, setUpdateTaskOverLayer] =
    useRecoilState(updateTaskAtom);
  useEffect(() => {
    fetch("http://127.0.0.1:8000/inital_call", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        setApiData(data?.[0]?.stats);
        setTodoApiData(data?.[0]?.todo);
      })
      .catch((error) => alert(error));
  }, []);
  //gsap
  useGSAP(() => {
    const tl = gsap.timeline();
    const tl1 = gsap.timeline();
    tl.from(".c01", {
      y: -10,
      opacity: 0,
      duration: 0.3,
      delay: 0.2,
    });
    tl.from(".c03", {
      x: 10,
      opacity: 0,
      duration: 0.4,
      delay: 0.1,
      scale: 0,
    });
    tl.from(".c04", {
      y: -20,
      duration: 0.3,
      delay: 0.1,
      opacity: 0,
    });
    // animate create button safely (ensure ref is attached)
    if (createref.current) {
      tl.to(createref.current, {
        y: -20,
        opacity: 1,
        duration: 0.6,
      });
    }
    const c09Nodes = gsap.utils.toArray(".c09");
    if (c09Nodes.length) {
      tl1.from(c09Nodes, {
        x: 20,
        opacity: 0,
        delay: 0.2,
        duration: 0.3,
        stagger: 0.2,
      });
    }
    const c14Nodes = gsap.utils.toArray(".c14");
    if (c14Nodes.length) {
      tl1.from(c14Nodes, {
        y: 5,
        opacity: 0,
        duration: 0.2,
        stagger: 0.2,
      });
    }
  });
  return (
    <div className="relative">
      {/* {update task} */}
      {updateTaskOverLayer && (
        <div>
          {console.log("yes i am working")}
          <div
            className="over-layer"
            onClick={() => {
              setUpdateTaskOverLayer(null);
            }}
          ></div>
          <Updatetask />
        </div>
      )}
      {/* add task */}
      {addTaskOverlayer && (
        <div>
          <div
            className="over-layer"
            onClick={() => {
              setAddTaskOverlayer(null);
            }}
          ></div>
          <AddTask />
        </div>
      )}

      <Headercom />
      <div className="bodycontainer">
        <Bodycom />
        <Filter />
        <Todos />
      </div>
      <button
        className="c02"
        ref={createref}
        onClick={() => {
          if (addTaskOverlayer) {
            setAddTaskOverlayer(null);
          } else {
            setAddTaskOverlayer(true);
          }
        }}
      >
        Create Todo
      </button>
    </div>
  );
};

export default Homepg;
