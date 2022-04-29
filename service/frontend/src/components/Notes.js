import React from 'react'
import {Link} from "react-router-dom";


const NoteItem = ({note, createNote, deleteNote}) => {
   return (
       <tr>
           <td>{note.text}</td>
           <td>{note.project}</td>
           <td><button onClick={()=>createNote(note.project)} type='button'>Create</button></td>
           <td><button onClick={()=>deleteNote(note.project)} type='button'>Delete</button></td>
       </tr>
   )
}


const NoteList = ({notes, createNote, deleteNote}) => {
   return (
       <div>
           <table>
               <tr>
                   <th>Text</th>
                   <th>Project</th>
                   <th></th>
               </tr>
               {notes.map((note) => <NoteItem note={note} />)}
           </table>
           <link to='/notes/create'>Create</link>
           <link to='/notes/delete'>Delete</link>
       </div>
   )
}


export default NoteList;
