import Link from 'next/link';
import React from 'react';


const LessonSection = props => (
  <div className='col-md-12'>
    {props.lessons.map(lesson => (
      <div key={lesson.id}>
        <div className='row'>
        <div className='col-md-6'>
          <div><strong>Урок {lesson.number}: {lesson.name}</strong></div>
          <div>Описание: {lesson.description}</div>
          <div>Дата проведения: {new Date(lesson.datetime).toString()}</div>
          <div>Ссылка на трансляцию: <a href={lesson.url_translation}>Перейти</a></div>
        </div>
        <div className='col-md-6'>
          <div><strong>Домашнее задание:</strong> {lesson.homework_title}</div>
          <div>Описание: {lesson.homework_description}</div>
          <div>Сдать до: {lesson.homework_date}</div>
          <div>Сдать: <Link href={`/homework?lesson=${lesson.id}&title=${lesson.homework_title}`}>
            <a>Приступить</a>
          </Link></div>
        </div>
        </div>
        <hr/>
      </div>
    ))}
  </div>
);

export default LessonSection;
