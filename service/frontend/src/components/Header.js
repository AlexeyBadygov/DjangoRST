import React from 'react';

const Header = ({Header}) => {
    return (
        <div>
            <ul id="navbar">
              <li><a href="#">Главная</a></li>
              <li><a href="#">Новости</a></li>
              <li><a href="#">Контакты</a>
                <ul>
                  <li><a href="#">Адрес</a></li>
                  <li><a href="#">Телефон</a></li>
                  <li><a href="#">Email</a></li>
                </ul>
              </li>
              <li><a href="#">Вход</a></li>
              </ul>
        </div>
    );
}

export default Header;