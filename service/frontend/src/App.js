import React from 'react';
import axios from 'axios'
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js';
import UsersList from './components/Users.js';
import Header from './components/Header.js';
import Footer from './components/Footer.js';
import {BrowserRouter, HashRouter, Route, Link} from 'react-router-dom'
import BookList from "./components/Book";
import NoteList from "./components/Notes";

class App extends React.Component {
   constructor(props) {
       super(props)
       this.state = {
           'authors': [],
           'users': [],
           'books':[]
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

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/books')
           .then(response => {
               const books = response.data
                   this.setState(
                   {
                        'books': books
                   }
               )
           }).catch(error => console.log(error))
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/notes/project')
            .then(response => {
                const note = response.data
                    this.setState(
                    {
                        'note': note
                    }
                )
            }).catch(error => console.log(error))
    }

    render () {
        return (
            <div className='App'>
                <BrowserRouter>
                    <Header />
                        <Route exact path='/users' component={() => <UsersList users={this.state.users} />} />
                        <Route exact path='/authors' component={() => <AuthorList authors={this.state.authors} />} />
                        <Route exact path='/books' component={() => <BookList books={this.state.books} />} />
                        <Route exact path='/notes' component={() => <NoteList notes={this.state.notes} />} />
                    <Footer />
                </BrowserRouter>
            </div>
        );
    }
}

export default App;