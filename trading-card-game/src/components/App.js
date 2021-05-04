import React from "react";
import Card from "./game-mechanics/Card";
import DrawCard from "./game-mechanics/DrawCard";
import MoveChoice from "./MoveChoice";

function App() {
  return (
    ///
    <div>
      <MoveChoice />
      <DrawCard />
      {/* <Card
        icon1="air"
        icon2="light"
        description="second card"
        position="hand-two"
      />
      <Card
        icon1="air"
        icon2="light"
        description="second card"
        position="hand-three"
      />
      <Card
        icon1="air"
        icon2="light"
        description="second card"
        position="hand-four"
      />
      <Card
        icon1="air"
        icon2="light"
        description="second card"
        position="hand-five"
      /> */}
    </div>
  );
}

export default App;
