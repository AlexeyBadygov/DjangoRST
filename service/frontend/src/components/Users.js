import React from 'react'


const UsersItem = ({user}) => {
   return (
       <tr>
           <td>
               {User.username}
           </td>
           <td>
               {User.firstname}
           </td>
           <td>
               {User.lastname}
           </td>
           <td>
               {User.email}
           </td>


       </tr>
   )
}

const UserList = ({users}) => {
   return (
       <table>
           <th>
               User name
           </th>
           <th>
               First name
           </th>
           <th>
               Last name
           </th>
           <th>
               email
           </th>
           {users.map((user) => <UserItem user={user} />)}
       </table>
   )
}


export default UserList