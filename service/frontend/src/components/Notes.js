import React from 'react'


const NoteItem = ({note}) => {
   return (
       <tr>
           <td>{note.name}</td>
           <td>{note.link_repo}</td>
           <td>{note.lastname}</td>
       </tr>
   )
}

const NoteList = ({notes}) => {
   return (
       <table>
           <th>User name</th>
           <th>First name</th>
           <th>Last name</th>
           <th>email</th>
           {notes.map((note) => <NoteItem note={note} />)}
       </table>
   )
}


export default NoteList;