import React, { useState } from "react";
import Accordion from "./components/Accordion";
import Search from "./components/Search";
import Dropdown from "./components/Dropdown";
import Translate from "./components/Translate";
import Route from "./components/Route";
import Header from "./components/Header";

const items = [
  {
    title: "What is React?",
    content: "React is a javascript framework",
  },
  {
    title: "Why use React?",
    content: "its good",
  },
  { title: "how to use react?", content: "with components" },
];
const options = [
  {
    label: "the Color Red",
    value: "red",
  },
  {
    label: "the Color green",
    value: "green",
  },
  {
    label: "the Color blue",
    value: "blue",
  },
];

function App() {
  const [selected, setSelected] = useState(options[0]);
  // const [showDropdown, setShowDropdown] = useState(true);
  return (
    //   <button onClick={() => setShowDropdown(!showDropdown)}>
    //     Toggle Dropdwon
    //   </button>
    //   {showDropdown ? (
    //     <Dropdown
    //       selected={selected}
    //       options={options}
    //       onSelectedChange={setSelected}
    //     />
    //   ) : null}
    // </div>
    <div>
      <Header />
      <Route path="/">
        <Accordion items={items} />
      </Route>
      <Route path="/list">
        <Search />
      </Route>
      <Route path="/dropdown">
        <Dropdown
          label="Select a color"
          options={options}
          selected={selected}
          onSelectedChange={setSelected}
        />
      </Route>
      <Route path="/translate">
        <Translate />
      </Route>
    </div>
  );
}

export default App;
