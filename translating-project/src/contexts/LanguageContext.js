import React, { useState } from "react";

const Context = React.createContext("english");

export const LanguageStore = (props) => {
  const [language, setLanguage] = useState("english");

  return (
    <Context.Provider value={{ language, setLanguage: setLanguage }}>
      {props.children}
    </Context.Provider>
  );
};

export default Context;
