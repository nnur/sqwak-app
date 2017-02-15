import React, {Component} from 'react';
import Tooltip from 'rc-tooltip';
import 'rc-tooltip/assets/bootstrap.css';
import optionsImg from './../../assets/images/icons/options.svg';


class ClassCard extends Component {

    constructor(props) {
        super(props);
        this.state = { dropdownOpen: false };
    }

    onClick() {
        this.dropDownButton.blur();
        this.props.onClick(this.props.mlClass.id);
    }

    onEditClick(event) {
        event.stopPropagation();
        this.dropDownButton.blur();
        console.log(this.props.mlClass)
        this.props.onEditClick(this.props.mlClass.id);
    }

    onDeleteClick(event) {
        event.stopPropagation();
        this.dropDownButton.blur();
        this.props.onDeleteClick(this.props.mlClass.id);
    }

    renderIndicator() {
        let classList = ["sq-class-card--status-indicator"];
        !this.props.mlClass.inModel && classList.push("hidden");
        !this.props.mlClass.isEdited && classList.push("published");
        return ( <div className={classList.join(" ")}></div> )
    }

    dropDownButtonClicked() {
        console.log('OKOKOKOKOKO')
    }

    render () {
        let {imgName} = this.props.mlClass;
        imgName = imgName || "blue-cube";
        const imgIcon = require(`./../../assets/images/class-icons/${imgName}.svg`);
        let addRemoveText = this.props.mlClass.inModel ? "Remove" : "Add";

        return (
            <div className="sq-class-card">
                <div className="sq-class-card--header">
                    <Tooltip
                        overlayClassName={"sq-tooltip-overlay" + (this.props.mlClass.isEdited ? "" : " trained")}
                        placement="top"
                        mouseEnterDelay={0}
                        mouseLeaveDelay={0.1}
                        overlay={
                            <div
                                className={"sq-class-card--status-tooltip" + (this.props.mlClass.isEdited ? "" : " trained")}>
                                {this.props.mlClass.isEdited ? "untrained samples" : "all trained"}
                            </div>}
                        align={{ offset: [0, 0] }}
                        >
                        {this.renderIndicator()}
                    </Tooltip>
                    <button
                        ref={(e)=>{this.dropDownButton = e;}}
                        className="sq-class-card--edit sq-text__sm__pale"
                        onClick={this.dropDownButtonClicked.bind(this)}>
                        <img src={optionsImg} role="presentation"/>
                        <div className="sq-class-card--dropdown-menu">
                            <div className="sq-class-card--dropdown-menu-item" onClick={this.onEditClick.bind(this)}>Edit</div>
                            <div className="sq-class-card--dropdown-menu-item" onClick={this.onClick.bind(this)}>{addRemoveText}</div>
                            <div className="sq-class-card--dropdown-menu-item" onClick={this.onDeleteClick.bind(this)}>Delete</div>
                        </div>
                    </button>
                </div>
                <div className="sq-class-card--icon">
                    <img src={imgIcon} role="presentation"/>
                </div>
                <div className="sq-class-card--label sq-text__sm">
                    {this.props.mlClass.className}
                </div>
            </div>
        )
    }
}

export default ClassCard