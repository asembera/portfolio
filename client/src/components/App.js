import React, { useEffect } from "react";
import { BrowserRouter, Route } from "react-router-dom";
import { connect } from "react-redux";
import * as actions from "../actions";

import Header from "./Header";
import Landing from "./Landing";

const Dashboard = () => <h2>Dashboard</h2>;
const SurveyNew = () => <h2>SurveyNew</h2>;

const App = (props) => {
  useEffect(() => {
    props.fetchUser();
  }, []);

  return (
    //
    <div className="container">
      <BrowserRouter>
        <div>
          <Header />
          <Route exact path="/surveys" component={Dashboard}></Route>
          <Route exact path="/surveys/new" component={SurveyNew}></Route>
          <Route exact path="/" component={Landing}></Route>
        </div>
      </BrowserRouter>
    </div>
  );
};

export default connect(null, actions)(App);
