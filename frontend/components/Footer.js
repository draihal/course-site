import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faFacebookSquare } from '@fortawesome/free-brands-svg-icons'
import { faTelegram } from '@fortawesome/free-brands-svg-icons'
import { faInstagram } from '@fortawesome/free-brands-svg-icons'
import { faVk } from '@fortawesome/free-brands-svg-icons'

import Link from 'next/link';


const Footer = () => (
    <div id='footer'>
        <footer>
            <div className='container' id='sticky-footer'>
                <div className='row footer-columns justify-content-center'>
                    <div className='footer-column col-md-2'>
                        <ul className='list-unstyled'>
                            <li><a href='#' target='_blank'>
                                <FontAwesomeIcon icon={faFacebookSquare} size='2x' />
                            </a></li>
                            <li><a href='#' target='_blank'>
                                <FontAwesomeIcon icon={faTelegram} size='2x' />
                            </a></li>
                            <li><a href='#' target='_blank'>
                                <FontAwesomeIcon icon={faInstagram} size='2x' />
                            </a></li>
                            <li><a href='#' target='_blank'>
                                <FontAwesomeIcon icon={faVk} size='2x' />
                            </a></li>
                        </ul>
                    </div>
                    <div className='footer-column col-md-2'>
                        <ul className='list-unstyled'>
                            <li><Link href='/about'><a>О нас</a></Link></li>
                            <li><a href='#'>СМИ о нас</a></li>
                            <li><a href='#'>Отзывы</a></li>
                            <li><a href='#'>Контакты</a></li>
                            <li><a href='#'>FAQ</a></li>
                        </ul>
                    </div>
                    <div className='footer-column col-md-2'>
                        <ul className='list-unstyled'>
                            <li><a href='#'>Мероприятия</a></li>
                            <li><a href='#'>Каталог курсов</a></li>
                            <li><a href='#'>Наши партнеры</a></li>
                            <li><a href='#'>Блог</a></li>
                            <li><a href='#'>Программы лояльности</a></li>
                        </ul>
                    </div>
                    <div className='footer-column col-md-3'>
                        <a href='tel:+79259999999' title='+7 925 999 99 99'>+7 925 999 99 99</a>
                        <p>По всем вопросам пишите на
                            <a href='mailto:help@test.com' target='_blank' title='help@test.com'> help@test.com</a>
                        </p>
                    </div>
                </div>
            </div>
            <div className='row justify-content-center'>
                <div className='col-md-5 text-center socket-div'>
                    <hr className='socket' />
                        © 2019-{new Date().getFullYear()} Course Site
                </div>
            </div>
        </footer>
    </div>
);

export default Footer;
