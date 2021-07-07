import React from "react";
import { connect } from "react-redux";
import formFields from "./formFields";
import * as actions from "../../actions";
import { withRouter } from "react-router";

const SurveyFormReview = ({ onCancel, formValues, submitSurvey, history }) => {
  const reviewFields = formFields.map(({ name, label }) => {
    return (
      <div key={name}>
        <label>{label}</label>
        <div>{formValues[name]} </div>
      </div>
    );
  });

  return (
    <div>
      <h5>Please confirm entries</h5>
      {reviewFields}
      <button className="teal  btn" onClick={onCancel}>
        <i className="material-icons"> edit</i>
      </button>
      <button
        onClick={() => submitSurvey(formValues, history)}
        className="teal btn right"
      >
        Send Survey<i className="material-icons right">email</i>
      </button>
    </div>
  );
};

function mapStateToProps(state) {
  return { formValues: state.form.surveyForm.values };
}

export default connect(mapStateToProps, actions)(withRouter(SurveyFormReview));
