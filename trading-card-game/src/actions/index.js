export const steal = (amount) => {
  return {
    type: "STEAL",
    payload: amount,
  };
};

export const stolen = (amount) => {
  return {
    type: "STOLEN_FROM",
    payload: amount,
  };
};
