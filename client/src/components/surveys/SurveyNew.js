import React, { useState } from "react";
import SurveyForm from "./SurveyForm";
import { reduxForm } from "redux-form";
import SurveyFormReview from "./SurveyFormReview";

const SurveyNew = () => {
  const [showReview, setShowReview] = useState(false);

  function renderContent() {
    if (showReview) {
      return <SurveyFormReview onCancel={() => setShowReview(false)} />;
    }

    return <SurveyForm onSurveySubmit={() => setShowReview(true)} />;
  }

  return <div>{renderContent()}</div>;
};

export default reduxForm({
  form: "surveyForm",
})(SurveyNew);
