import Link from 'next/link';
import urlFor from '../../services/urlFor';


const TeacherSection = props => (
    <div id='teachers' className='offset'>
        <div className='fixed-background'>
            <div className='row dark'>
                <div className='container'>
                    <div className='narrow text-center'>
                        <div className='col-12'>
                            <h3 className='heading'>Преподаватели</h3>
                            <div className='heading-underline'> </div>
                        </div>
                    </div>
                    <div className='row text-center'>
                        {props.teachers.map(teacher => (
                            <div className='col-md-4 teachers' key={teacher.teacher_id}>
                                <h3>{teacher.teacher_first_name} {teacher.teacher_last_name}</h3>
                                <div className='feature'>
                                    {teacher.avatar ? <img src={urlFor(teacher.avatar)} /> : <img src='static/default_user.jpg' />}
                                    <p className='lead'>{teacher.position}</p>
                                </div>
                            </div>
                        ))}
                    </div>
                    <div className='text-center'>
                        <div className='col-12'>
                            <a className='btn btn-outline-light btn-lg' href='#'>Все преподаватели</a>
                        </div>
                    </div>
                </div>
            </div>
            <div className='fixed-wrap'>
                <div className='fixed'>
                </div>
            </div>
        </div>
    </div>
);

export default TeacherSection;
