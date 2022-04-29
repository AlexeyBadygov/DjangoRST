import React from 'react'
import {Link} from "react-router-dom";



const ProjectItem = ({project, createProject, deleteProject}) => {
    return (
        <tr>
            <td>{project.name}</td>
            <td>{project.link_repo}</td>
            <td>{project.user}</td>
            <td><button onClick={()=>createProject(project.name)} type='button'>Create</button></td>
            <td><button onClick={()=>deleteProject(project.name)} type='button'>Delete</button></td>
        </tr>
    )
}


const ProjectList = ({projects, createProject, deleteProject}) => {
    return (
        <div>
            <table>
                <tr>
                    <td>Name</td>
                    <td>Link_repo</td>
                    <td>User</td>
                </tr>
                {projects.map((project) => <ProjectItem project={project} />)}
            </table>
            <Link to='/projects/create'>Create</Link>
            <Link to='/projects/delete'>Create</Link>
        </div>
    )
}

export default ProjectList;
