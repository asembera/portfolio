import React, { useState } from "react";
import UserCreate from "./UserCreate";
import Context, { LanguageStore } from "../contexts/LanguageContext";
import ColorContext from "../contexts/ColorContexts";
import LanguageSelector from "./LanguageSelector";

function App() {
  return (
    //
    <div className="ui container">
      <LanguageStore>
        <LanguageSelector />

        <ColorContext.Provider value="red">
          <UserCreate />
        </ColorContext.Provider>
      </LanguageStore>
    </div>
  );
}

export default App;
