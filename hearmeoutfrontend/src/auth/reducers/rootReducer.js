import { combineReducers } from "redux";

// session
import {sessionreducer} from "redux-react-session"

const rootReducer = combineReducers({
    session: sessionreducer
});

export default rootReducer;
