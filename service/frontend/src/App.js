import React from 'react';
import axios from 'axios'
import './App.css';
import AuthorList from './components/Author.js';
import UsersList from './components/Users.js';
import Header from './components/Header.js';
import Footer from './components/Footer.js';
import {BrowserRouter, Link, Route, Switch} from 'react-router-dom'
import BookList from "./components/Book";
import NoteList from "./components/Notes";
import LoginForm from "./components/Auth";
import NoteForm from "./components/NoteForm";
import ProjectList from "./components/Project";
import ProjectForm from "./components/ProjectForm";


const NotFound404 = ({ location }) => {
    return (
        <div>
            <h1>Страница или адресс'{location.pathname}' не найдены</h1>
        </div>
    )
}

class App extends React.Component {
   constructor(props) {
       super(props)
       this.state = {
           'authors': [],
           'users': [],
           'books':[],
           'token': ''
       }
   }

   set_token(token) {
       // const cookies = new Cookies()
       localStorage.setItem('token', token)
       this.setState({'token': token}, ()=>this.load_data())
   }

   is_authenticated() {
       return this.state.token != ''
   }

   logout() {
       this.set_token('')
   }

   get_token_from_storage() {
       // const cookies = new Cookies()
       const token = localStorage.setItem('token')
       this.setState({'token': token}, ()=>this.load_data())
   }

   get_token(username, password) {
       axios.post('http://127.0.0.1:8000/api-token-auth', {username: username, password: password})
           .then(response => {
               this.set_token(response.data['token'])
           }).catch(error => alert('login or password is not correct'))

   }
    get_headers() {
       let headers = {
           'Content-Type': 'application/json'
       }
    if (this.is_authenticated())
        {
            headers['Authorization'] = 'Token' + this.state.token
        }
        return headers
    }


    load_data() {

       const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/authors/', {headers})
            .then(response => {
                this.setState({authors: response.data})
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/books', {headers})
            .then(response => {
                this.setState({books: response.data})
            }).catch(error => {
                console.log(error)
            this.setState({books: []})
        })

        axios.get('http://127.0.0.1:8000/api/biography', {headers})
            .then(response => {
                this.setState({biography: response.data})
            }).catch(error => {
                console.log(error)
            this.setState({biography: []})
        })

        axios.get('http://127.0.0.1:8000/api/articles', {headers})
            .then(response => {
                this.setState({articles: response.data})
            }).catch(error => {
                console.log(error)
            this.setState({articles: []})
        })
    }


    createProject(name, user) {
        const headers = this.get_headers()
        const data = {name: name}
        axios.post('http://127.0.0.1:8000/api/projects/', data, {headers})
            .then(response => {
                let newProject = response.data
                const user = this.state.users.filter(item) => item.id === newProject.user)[0]
                newProject.user = user
                this.setState({projects:[... this.state.projects, newProject]})
            })
        }

    deleteProject(name, user) {
       const header = this.get_headers()
        axios.delete('http://127.0.0.1:8000/api/projects/${id}', {headers})
            .then(response => {
                this.setState({projects: this.state.projects.filter((item)=>item.id != id)})
            }).catch(error => {
                console.log(error)
        })
    }


    deleteNote(project) {
       const header = this.get_headers()
        axios.delete('http://127.0.0.1:8000/api/notes/${id}', {headers})
            .then(response => {
                this.setState({notes: this.state.notes.filter((item)=>item.project != project)})
            }).catch(error => {
                console.log(error)
        })
    }

    componentDidMount() {
        this.get_token_from_storage()
    }

    render () {
        return (
            <div className='App'>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Authors</Link>
                            </li>
                            <li>
                                <Link to='/books'>Books</Link>
                            </li>
                            <li>
                                {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    {/*<Switch>*/}
                    <Header />
                        <Route exact path='/authors' component={() => <AuthorList authors={this.state.authors} />} />
                        <Route exact path='/books' component={() => <BookList books={this.state.books} />} />
                        <Route exact path='/notes' component={() => <NoteList notes={this.state.notes} />} />
                        <Route exact path='/notes/create' component={() => <NoteForm notes={this.state.notes} createNote={(project) => this.createNote(project)}/>} />
                        <Route exact path='/notes/delete' component={() => <NoteForm notes={this.state.notes} deleteNote={(project) => this.deleteNote(project)}/>} />
                        <Route exact path='/project/' component={() => <ProjectList projects={this.state.projects} />} />
                        <Route exact path='/project/create' component={() => <ProjectForm projects={this.state.projects} createProject={(name) => this.createProject(name)}/>} />
                        <Route exact path='/project/delete' component={() => <ProjectForm projects={this.state.projects} deleteProject={(name) => this.deleteProject(name)}/>} />
                        <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
                        <Route component={NotFound404} />
                    {/*</Switch>*/}
                    <Footer />
                </BrowserRouter>
            </div>
        );
    }
}

export default App;