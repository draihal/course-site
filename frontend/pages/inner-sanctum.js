import React from 'react';
import axios from 'axios';
import { connect } from 'react-redux';
import actions from '../redux/actions';
import Layout from '../components/Layout';
import StudentsHomework from '../components/InnerSanctum/StudentsHomework';


const InnerSanctum = ({ group }) => {
  return (
    <Layout title='Кабинет преподавателя'>
      {(group && (
        <div className='group py-4'>
          <div className='container'>
            <h2>Группа: {group.slug}</h2>
            <hr/>
            <div className='row'>
              <div className='col-md-6'>Дата начала обучения: {group.date_start}</div>
              <div className='col-md-6'>Дата окончания обучения: {group.date_end}</div>
              <div className='col-md-12'>
                {group.module.map(module => (
                  <div key={module.id}>
                    <h3>Модуль: {module.name}</h3>
                    <hr/>
                    <div className='col-md-12'>
                      {module.lessons.map(lesson => (
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
                              <div>Дата сдачи до: {lesson.homework_date}</div>
                            </div>
                          </div>
                          <StudentsHomework homework={lesson.homework} lesson={lesson.id}/>
                          <hr/>
                        </div>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      )) || 'Пожалуйста войдите!'}
      <style global jsx>
        {`
          .main{
            padding-top: 6rem;
          }
          html {
            min-height: 100%;
            position: relative;
          }
          body {
            /* Margin bottom by footer height */
            margin-bottom: 80px;
          }
          #footer {
            position: absolute;
            bottom: 0;
            width: 100%;
            /* Set the fixed height of the footer here */
            height: 80px;
            background-color: #f5f5f5;
          }
      `}
      </style>
    </Layout>
  );
};

InnerSanctum.getInitialProps = async (ctx) => {
  const { token } = ctx.store.getState().authentication;
  const slug = ctx.query.name;
  if (token) {
    const response = await axios.get(`${process.env.basePath}/api/v1/education/groups/${slug}/`, {
      headers: {
        authorization: `JWT ${token}`,
        'Content-Type': 'application/json'
      }
    });
    const group = response.data;
    return {
      group, token
    };
  }
};

export default connect(state => state, actions)(InnerSanctum);
