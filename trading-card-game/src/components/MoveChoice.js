import React from "react";
import { connect } from "react-redux";
import { steal, stolen } from "../actions";

const amount = 10;

const MoveChoice = (props) => {
  return (
    <div className="menu-container">
      <button
        onClick={() => {
          props.stolen(amount);
          console.log(props.gold.yourGold);
        }}
      >
        Play card
      </button>
      <button></button>
      <button></button>
    </div>
  );
};

const mapStateToProps = (state) => {
  return { gold: state.steal };
};

export default connect(mapStateToProps, { steal, stolen })(MoveChoice);
