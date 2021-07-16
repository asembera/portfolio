import React from "react";
import StripeCheckout from "react-stripe-checkout";
import { connect } from "react-redux";
import * as actions from "../actions";

const Payments = (props) => {
  return (
    <div>
      <StripeCheckout
        name="Emailer"
        description="$5 for 5 survey credits"
        amount={500}
        token={(token) => props.handleToken(token)}
        stripeKey={process.env.REACT_APP_STRIPE_KEY}
      >
        <button
          onClick={() =>
            alert(
              "NOTE: Do not put in real information. Use 4242 4242 4242 4242, any date in the future, and any security code to test the payment system out."
            )
          }
          className="btn"
        >
          Add Credits
        </button>
      </StripeCheckout>
    </div>
  );
};

export default connect(null, actions)(Payments);
