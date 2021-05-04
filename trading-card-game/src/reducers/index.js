import { combineReducers } from "redux";
import stealReducer from "./stealReducer";

export default combineReducers({
  steal: stealReducer,
});
