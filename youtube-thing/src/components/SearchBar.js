import React from "react";

class SearchBar extends React.Component {
  state = { term: "" };

  onInputChange = (e) => {
    this.setState({ term: e.target.value });
  };

  onFormSubmit = (e) => {
    e.preventDefault();

    this.props.onFormSubmit(this.state.term);

    //todo make sure call callback from parent component
  };

  render() {
    return (
      <div className="myStyle">
        <div className="search-bar ui segment">
          <form onSubmit={this.onFormSubmit} className="ui form">
            <div className="field">
              <label>Video search</label>
              <input
                type="text"
                value={this.state.term}
                onChange={this.onInputChange}
              />
            </div>
          </form>
        </div>
      </div>
    );
  }
}

export default SearchBar;