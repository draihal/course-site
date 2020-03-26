import React from 'react';
import Link from 'next/link';


const StudentsHomework = props => (
  <div className='row'>
    <div className='col-md-12 table-responsive-md'>
      <table className='table'>
        <thead>
        <tr>
          <th scope='col'>Студент</th>
          <th scope='col'>Статус проверки</th>
          <th scope='col'>Оценка</th>
          <th scope='col'>Проверил</th>
          <th scope='col'>Домашняя работа</th>
        </tr>
        </thead>
        <tbody>
        {props.homework.map(homework => (
          <tr key={homework.id}>
            <th>{homework.student_first_name} {homework.student_last_name}</th>
            <th>{homework.grade ? homework.grade.status : ''}</th>
            <th>{homework.grade ? homework.grade.grade : ''}</th>
            <th>{homework.grade ? homework.grade.teacher_last_name : ''}</th>
            <th>
              <Link href={`/grade?homework=${homework.id}`}>
                <a>Проверить</a>
              </Link>
            </th>
          </tr>
        ))}
        </tbody>
      </table>
    </div>
  </div>
);

export default StudentsHomework;
