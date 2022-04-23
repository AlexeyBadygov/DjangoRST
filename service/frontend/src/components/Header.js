import React from 'react';
import {BrowserRouter, Link} from "react-router-dom";





const Header = ({Header}) => {
    return (
        <div>
            <BrowserRouter>
                <ul id="navbar">
                    <li><a href="/users">Пользователи</a></li>
                    <li><a href="/note">Проекты</a></li>
                    <li><a href="#">Контакты</a>
                        <ul>
                            <li><a href="#">Адрес</a></li>
                            <li><a href="#">Телефон</a></li>
                            <li><a href="#">Email</a></li>
                        </ul>
                  </li>
                  <li><a href="#">Вход</a></li>
                  </ul>
            </BrowserRouter>
        </div>
    );
}

export default Header;



// import {HashRouter, Route, Link} from 'react-router-dom'
// class App extends React.Component {
// ...
// render() {
// return (
// <div className="App">
// <HashRouter>
// <nav>
// <ul>
// <li>
// <Link to='/'>Authors</Link>
// </li>
// <li>
// <Link to='/books'>Books</Link>
// </li>
// </ul>
// </nav>
// <Route exact path='/' component={() => <AuthorList
// items={this.state.authors} />} />
// <Route exact path='/books' component={() => <BookList
// items={this.state.books} />} />
// </HashRouter>
// </div>
// )
// }
// }
// export default App;