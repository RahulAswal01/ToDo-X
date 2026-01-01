import React from "react";
import SearchRoundedIcon from "@mui/icons-material/SearchRounded";
//recoil
import { useRecoilState } from "recoil";
import addTaskAtom from "./recoil/addTaskAtom";
import searchInput from "./recoil/searchInput";
const Bodycom = () => {
  const [text, setText] = useRecoilState(searchInput);
  return (
    <div>
      <div className="c04">
        <input
          type="text"
          onChange={(e) => {
            setText(e.target.value);
            console.log(e.target.value);
          }}
          placeholder="Search task here with title ... "
          className="c05"
          autoComplete="off"
        />
        <SearchRoundedIcon className="c06" style={{ fontSize: 28 }} />
      </div>
    </div>
  );
};

export default Bodycom;
