import React, { useState } from "react";
import Card from "./Card";

const DrawCard = () => {
  const [position, setPosition] = useState("deck flip");
  const [position2, setPosition2] = useState("deck flip");
  const [position3, setPosition3] = useState("deck flip");

  ////// COME BACK TO ANIMATION LATER//////
  // const deckCard = document.querySelector(".deck");
  // deckCard.style.animation = "draw 1s ease-in";

  ////tentative: Should probably transfer the state here to Redux
  const onDraw = () => {
    setPosition("hand two");
  };

  const onPlay = () => {
    setPosition("played-card");
  };

  const onDiscard = () => {
    setPosition("discard-pile");
  };

  const moveHandler = () => {
    if (position.includes("deck flip")) {
      onDraw();
    } else if (position.includes("hand")) {
      onPlay();
    } else if (position.includes("played-card")) {
      onDiscard();
    }
  };

  return (
    <div>
      <Card
        onClick={() => {
          moveHandler();
        }}
        icon1="stars"
        icon2="stars"
        description="Description of card"
        position={position}
      />
      <Card
        onClick={() => {
          moveHandler();
        }}
        icon1="stars"
        icon2="stars"
        description="Description of card"
        position={position2}
      />
      <Card
        onClick={() => {
          moveHandler();
        }}
        icon1="air"
        icon2="light"
        description="second card"
        position={position3}
      />
    </div>
  );
};

export default DrawCard;
