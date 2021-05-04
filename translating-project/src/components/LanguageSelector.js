import React, { useState, useContext } from "react";
import LanguageContext from "../contexts/LanguageContext";

const LanguageSelector = () => {
  const context = useContext(LanguageContext);

  return (
    <div>
      Select a language:
      <i onClick={() => context.setLanguage("english")} className="flag us" />
      <i onClick={() => context.setLanguage("dutch")} className="flag nl" />
    </div>
  );
};

export default LanguageSelector;
