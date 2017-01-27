import React, {Component} from 'react'
import PlushButton from './../../shared/PlushButton';


class NewAppForm extends Component {

    constructor(props) {
        super(props);
        this.state = {
            formIsValid: false,
            newAppName: props.initialAppName || ""
        };
    }

    componentDidMount() {
        this.nameInput.focus();
    }

    userDidType(event) {
        this.setState({newAppName: event.target.value});
    }

    handleSubmit() {
        if(this.props.onSumbit) {
            this.props.onSumbit({newAppName: this.state.newAppName});
        }
    }

    render () {
        return (
            <div className="sq-new-app-form">
                <div className="sq-new-app-form--container">
                    <div className="sq-new-app-form--title">Create app</div>
                    <input 
                        value={this.state.newAppName}
                        ref={(el)=> {this.nameInput = el;}}
                        type="text"
                        className="sq-basic-input"
                        placeholder="app name"
                        onChange={this.userDidType.bind(this)} />
                    <div className="sq-new-app-form--button-wrapper">
                        <PlushButton buttonText="New app" disabled={this.state.newAppName === ""} onClick={this.handleSubmit.bind(this)}/>
                    </div>
                </div>
            </div>
        )
    }
}

export default NewAppForm