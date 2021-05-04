import React from "react";
import "../../styling/App.css";

// ${props.animation} come back to animation later
const Card = (props) => {
  return (
    <div className={`card-body ${props.position} `}>
      <div className={`card-back `}>
        <div className="back-content"></div>
      </div>
      <div className={`card-front`}>
        <div className="card-art"></div>
        <div className="card-attributes">
          <i className="material-icons md-18">{props.icon2}</i>
          <i className="material-icons md-18">{props.icon1}</i>
        </div>
        <p className="card-description">{props.description}</p>
      </div>
    </div>
  );
};

export default Card;
