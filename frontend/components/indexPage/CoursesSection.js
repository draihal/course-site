import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUserGraduate, faUser, faUserFriends } from '@fortawesome/free-solid-svg-icons'
import Link from 'next/link';

const CoursesSection = props => (
    <div id='courses' className='offset'>
        <div className='container'>
            <div className='col-12 narrow text-center'>
                <h1>Курсы</h1>
                <p className='lead'>{props.description}</p>
                <Link href='/'><a className='btn btn-secondary btn-md'>Выбрать</a></Link>
            </div></div>
        {/* <!--- Start Jumbotron --> */}
        <div id='features'>
            <div className='jumbotron'>
                <div className='container'>
                    <div className='narrow text-center'>
                        <div className='col-12'>
                            <h3 className='heading'>Наша статистика</h3>
                            <div className='heading-underline'> </div>
                        </div>
                        <div className='row text-center'>
                            <div className='col-md-4'>
                                <div className='feature'>
                                    <FontAwesomeIcon icon={faUserGraduate} size='4x' transform='shrink-3 up-5' />
                                    <h3>{props.number_of_students} студентов</h3>
                                    <p>Некоторый текст!</p>
                                </div>
                            </div>
                            <div className='col-md-4'>
                                <div className='feature'>
                                    <FontAwesomeIcon icon={faUser} size='4x' transform='shrink-3 up-5' />
                                    <h3>{props.number_of_groups} групп</h3>
                                    <p>Еще какой-то текст!</p>
                                </div>
                            </div>
                            <div className='col-md-4'>
                                <div className='feature'>
                                    <FontAwesomeIcon icon={faUserFriends} size='4x' transform='shrink-3 up-5' />
                                    <h3>{props.number_of_teachers} преподавателей</h3>
                                    <p>И еще текст!</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        {/* <!--- End Jumbotron --> */}
    </div>
);

export default CoursesSection;
