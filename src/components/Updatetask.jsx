import React, { useRef, useState } from "react";
import updateTaskAtom from "./recoil/updateTaskAtom";
import { useRecoilState } from "recoil";
import btn_manager from "./recoil/btn_manager";
import todoatom from "./recoil/todoatom";
import apiDataAtom from "./recoil/apiDataAtom";
import updateIdTracker from "./recoil/updateIdTracker";

const Updatetask = () => {
  const [updateTask, setUpdateTask] = useRecoilState(updateTaskAtom);
  const updatetitleref = useRef(null);
  const updatedescref = useRef(null);
  const [status, setStatus] = useState("");
  const [btnTracker, setBtnTracker] = useRecoilState(btn_manager);
  const [todoApiData, setTodoApiData] = useRecoilState(todoatom);
  const [apiData, setApiData] = useRecoilState(apiDataAtom);
  const [IdTracker, setIdTracker] = useRecoilState(updateIdTracker);
  // const [UpdateTaskOverLayer, setUpdateTaskOverLayer] =
  //   useRecoilState(updateTaskAtom);

  const updateTaskHandler = (e) => {
    e.preventDefault();
    if (btnTracker == "all") {
      const updatecred = {
        id: IdTracker,
        title: updatetitleref.current.value,
        desc: updatedescref.current.value,
        status: status,
      };
      fetch("http://127.0.0.1:8000/update_task_all", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(updatecred),
      })
        .then((res) => res.json())
        .then((data) => {
          setApiData(data?.[0]?.stats);
          setTodoApiData(data?.[0]?.todo);
        })
        .catch((error) => alert(error));
    } else if (btnTracker == "completed") {
      const updatecred = {
        id: IdTracker,
        title: updatetitleref.current.value,
        desc: updatedescref.current.value,
      };
      fetch("http://127.0.0.1:8000/update_task_completed", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(updatecred),
      })
        .then((res) => res.json())
        .then((data) => {
          setApiData(data?.[0]?.stats);
          setTodoApiData(data?.[0]?.todo);
        })
        .catch((error) => alert(error));
    } else if (btnTracker == "in progress") {
      const updatecred = {
        id: IdTracker,
        title: updatetitleref.current.value,
        desc: updatedescref.current.value,
      };
      fetch("http://127.0.0.1:8000/update_task_in_progress", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(updatecred),
      })
        .then((res) => res.json())
        .then((data) => {
          setApiData(data?.[0]?.stats);
          setTodoApiData(data?.[0]?.todo);
        })
        .catch((error) => alert(error));
    } else if (btnTracker == "archived") {
      const updatecred = {
        id: IdTracker,
        title: updatetitleref.current.value,
        desc: updatedescref.current.value,
      };
      fetch("http://127.0.0.1:8000/update_task_archived", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(updatecred),
      })
        .then((res) => res.json())
        .then((data) => {
          setApiData(data?.[0]?.stats);
          setTodoApiData(data?.[0]?.todo);
        })
        .catch((error) => alert(error));
    } else {
      console.log("not found any value in btn tracker");
    }
    setUpdateTask(null); // Move this here after update logic
  };

  return (
    <div className="outer-container">
      <div className="innerContainer">
        <h1 className="heading">Update Task</h1>
        <form action="#" onSubmit={updateTaskHandler}>
          <label htmlFor="tile" className="titdesc">
            Title :{" "}
          </label>
          <input
            type="text"
            className="title-text"
            name="title"
            ref={updatetitleref}
            required
            autoComplete="off"
          />
          <input type="hidden" name="id" value={updateTask?.id} />
          <br />
          <br />
          <label htmlFor="desc" className="titdesc">
            description
          </label>
          <br />
          <textarea
            name="desc"
            className="desc-text"
            cols={60}
            rows={5}
            id=""
            required
            autoComplete="off"
            ref={updatedescref}
          ></textarea>
          <br />
          <br />
          <fieldset className="radio-cont">
            <legend>Task status</legend>
            <div className="radio-btn">
              <div>
                <input
                  className="radio-input"
                  type="radio"
                  onClick={(e) => {
                    setStatus(e.target.value);
                  }}
                  value="completed"
                  name="status"
                  required
                />
                <label htmlFor="completed">completed</label>
              </div>

              <div>
                <input
                  className="radio-input"
                  type="radio"
                  onClick={(e) => {
                    setStatus(e.target.value);
                  }}
                  value="in progress"
                  name="status"
                />
                <label htmlFor="in progress">in progress</label>
              </div>

              <div>
                <input
                  className="radio-input"
                  type="radio"
                  name="status"
                  onClick={(e) => {
                    setStatus(e.target.value);
                  }}
                  value="archived"
                />
                <label htmlFor="archived">archived</label>
              </div>
            </div>
          </fieldset>
          <br />
          <br />
          <button type="submit" className="update-form-submit">
            Update Todo
          </button>
        </form>
      </div>
    </div>
  );
};

export default Updatetask;
