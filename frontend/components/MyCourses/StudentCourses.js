import Link from 'next/link';
import React from 'react';


const StudentCourses = props => (
  <div className='container'>
    <h2>Мои курсы</h2>
    <hr/>
    <div className='row'>
      {props.groups.map(group => (
        <div className='col-sm-4' key={group.id}>
          <div className='card'>
            <div className='card-body'>
              <h5 className='card-title'>{group.name}</h5>
              <p className='card-text'>Some text.</p>
              <Link href={`/group?name=${group.slug}`}>
                <a className='btn btn-secondary btn-md float-right'>Перейти</a>
              </Link>
            </div>
          </div>
        </div>
      ))}
    </div>
  </div>
);

export default StudentCourses;
