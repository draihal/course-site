import React from 'react';
import axios from 'axios';
import { connect } from 'react-redux';
import actions from '../redux/actions';
import Layout from '../components/Layout';
import ModuleSection from '../components/GroupPage/ModuleSection';


const Group = ({ group }) => {
  return (
    <Layout>
      {(group && (
        <div className='group py-4'>
          <div className='container'>
            <h2>Группа: {group.slug}</h2>
            <hr/>
            <div className='row'>
              <div className='col-md-6'>Дата начала обучения: {group.date_start}</div>
              <div className='col-md-6'>Дата окончания обучения: {group.date_end}</div>
              <ModuleSection modules={group.module}/>
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

Group.getInitialProps = async (ctx) => {
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

export default connect(state => state, actions)(Group);
