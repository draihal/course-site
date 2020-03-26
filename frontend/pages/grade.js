import React from 'react';
import axios from 'axios';
import { connect } from 'react-redux';
import actions from '../redux/actions';
import Layout from '../components/Layout';
import GradeSection from '../components/GradePage/GradeSection';


const Grade = ({ userId, homework, token, error }) => (
  <Layout>
    {(userId && (
      <div>
        {error ? <p className='text-center'>{error}</p> : null}
        <GradeSection homework={homework} teacherId={userId} token={token} />
      </div>
    )) ||
    'Пожалуйста войдите!'}
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

Grade.getInitialProps = async (ctx) => {
  const { token } = ctx.store.getState().authentication;
  const homeworkId = ctx.query.homework;
  if (token) {
    const response = await axios.get(`${process.env.basePath}/api/v1/education/homework/${homeworkId}/`, {
      headers: {
        authorization: `JWT ${token}`,
        'Content-Type': 'application/json'
      }
    });
    const homework = response.data;
    const responseUser = await await axios.get(`${process.env.basePath}/api/v1/users/me/`, {
      headers: {
        authorization: `JWT ${token}`,
        'Content-Type': 'application/json'
      }
    });
    const userId = responseUser.data.id;
    return {
      userId, homework, token
    };
  }
};

export default connect(state => state, actions)(Grade);
