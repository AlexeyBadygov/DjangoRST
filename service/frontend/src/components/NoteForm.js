import React from 'react'


class NoteForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {project: ''}
    }

    handleChange(event)
    {
        this.setState(
        {
                [event.target.project]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        console.log(this.state.project)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className="form-group">
                <label for="login">project</label>
                    <input type="text" className="form-control" project="project" value={this.state.project} onChange={(event)=>this.handleChange(event)} />
                </div>
            <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        );
    }
}

export default NoteForm
