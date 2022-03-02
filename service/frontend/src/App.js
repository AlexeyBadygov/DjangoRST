import React from 'react';
import axios from 'axios'
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js';
import UsersList from './components/Users.js';
import Header from './components/Header.js';
import Footer from './components/Footer.js';


class App extends React.Component {
   constructor(props) {
       super(props)
       this.state = {
           'authors': [],
           'users': []
       }
   }

    componentDidMount() {
       axios.get('http://127.0.0.1:8000/api/authors')
           .then(response => {
               const authors = response.data
                   this.setState(
                   {
                        'authors': authors
                   }
               )
           }).catch(error => console.log(error))
    }


    componentDidMount() {
       axios.get('http://127.0.0.1:8000/users/users')
           .then(response => {
               const users = response.data
                   this.setState(
                   {
                        'users': users
                   }
               )
           }).catch(error => console.log(error))
    }


    render () {
        return (
            <div>
                <Header />
                <UsersList users={this.state.users} />
                <AuthorList authors={this.state.authors} />
                <Footer />
            </div>
        );
    }
}

export default App;
