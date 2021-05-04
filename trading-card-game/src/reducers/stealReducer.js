const INITIAL_STATE = {
  enemyGold: 100,
  yourGold: 100,
};

const stealReducer = (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case "STOLEN_FROM":
      return {
        ...state,
        yourGold: state.yourGold - action.payload,
        enemyGold: state.enemyGold + action.payload,
      };

    case "STEAL":
      return {
        ...state,
        yourGold: state.yourGold + action.payload,
        enemyGold: state.enemyGold - action.payload,
      };
    default:
      return state;
  }
};

export default stealReducer;
