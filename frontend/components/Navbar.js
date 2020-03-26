import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSignInAlt, faSignOutAlt, faUserAlt, faGraduationCap } from '@fortawesome/free-solid-svg-icons';
import { faBell } from '@fortawesome/free-regular-svg-icons';
import Link from 'next/link';


const Navbar = (props) => (
  <div>
      <nav className='navbar navbar-expand-lg navbar-dark black fixed-top'>
          <div className='container'>
              <Link href='/'>
                  <a className='navbar-brand'>Онлайн курсы</a>
              </Link>
              <button className='navbar-toggler' type='button' data-toggle='collapse'
                      data-target='#navbarResponsive'>
                  <span className='navbar-toggler-icon'> </span>
              </button>
              <div className='collapse navbar-collapse' id='navbarResponsive'>
                  <ul className='navbar-nav ml-auto'>
                      <li className='nav-item'>
                          <Link href='/#home'>
                              <a className='nav-link'>Главная</a>
                          </Link>
                      </li>
                      <li className='nav-item dropdown'>
                          <a className='nav-link dropdown-toggle' href='index.html#courses'  id='navbarDropdown' role='button'
                             data-toggle='dropdown' aria-haspopup='true' aria-expanded='false'>Курсы</a>
                          <div className='dropdown-menu' aria-labelledby='navbarDropdown'>
                              <a className='dropdown-item' href='#'>Категория курса</a>
                              <a className='dropdown-item' href='#'>Другая категория</a>
                              <a className='dropdown-item' href='#'>Еще одна</a>
                              <a className='dropdown-item' href='#'>И еще</a>
                          </div>
                      </li>
                      <li className='nav-item'>
                          <Link href='/#teachers'><a className='nav-link'>Преподаватели</a></Link>
                      </li>
                      <li className='nav-item'>
                          <Link href='/#partners'><a className='nav-link'>Работа в компаниях</a></Link>
                      </li>
                      <li className='nav-item'>
                          <Link href='/#reviews'><a className='nav-link'>Отзывы</a></Link>
                      </li>
                      {!props.isAuthenticated && (<li className='nav-item'>
                          <Link href='/signin'>
                              <a className='nav-link' id='login-icon' data-testid='signin-link'>
                                  <FontAwesomeIcon icon={faSignInAlt} size='2x' />
                              </a>
                          </Link>
                      </li>)}
                      {props.isAuthenticated && (<li className='nav-item'>
                          <Link href='/profile'>
                              <a className='nav-link' id='user-icon' data-testid='profile-link'>
                                  <FontAwesomeIcon icon={faUserAlt} size='2x' />
                              </a>
                          </Link>
                      </li>)}
                      {props.isAuthenticated && (<li className='nav-item'>
                          <Link href='/my-courses'>
                          <a className='nav-link' id='bell-icon' data-testid='my-courses-link'>
                              <FontAwesomeIcon icon={faGraduationCap} size='2x' />
                          </a>
                          </Link>
                      </li>)}
                      {/*{props.isAuthenticated && (<li className='nav-item'>*/}
                          {/*<a className='nav-link' id='bell-icon' data-testid='bell-link'>*/}
                              {/*<FontAwesomeIcon icon={faBell} size='2x' />*/}
                          {/*</a>*/}
                      {/*</li>)}*/}
                      {props.isAuthenticated && (<li onClick={props.deauthenticate} className='nav-item'>
                          <a className='nav-link' id='logout-icon' data-testid='deauthenticate-link'>
                              <FontAwesomeIcon icon={faSignOutAlt} size='2x' />
                          </a>
                      </li>)}
                  </ul>
              </div>
          </div>
      </nav>
  </div>
);

export default Navbar;
