import React, { useContext } from "react";
import LanguageContext from "../contexts/LanguageContext";
import ColorContext from "../contexts/ColorContexts";

const Button = () => {
  // const context = useContext(LanguageContext);

  // const text = context === "english" ? "Submit" : "Voorleggen";

  return (
    <ColorContext.Consumer>
      {(color) => (
        <button className={`ui button ${color}`}>
          <LanguageContext.Consumer>
            {({ language }) =>
              language === "english" ? "Submit" : "Voorleggen"
            }
          </LanguageContext.Consumer>
        </button>
      )}
    </ColorContext.Consumer>
  );
};

export default Button;
