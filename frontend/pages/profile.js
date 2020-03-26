import React from 'react';
import axios from 'axios';
import { connect } from 'react-redux';
import actions from '../redux/actions';
import Layout from '../components/Layout';
import MainProfileSection from '../components/ProfilePage/MainProfileSection';


const Profile = ({ user, token, error }) => (
  <Layout title='Мой профиль'>
    {(user && (
      <div>
        {error ? <p className='text-center'>{error}</p> : null}
        <MainProfileSection user={user} token={token}/>
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
          .form-control {
            border-radius: 0;
          }
          // [class*='col-'] {
          //   padding: 0.5rem;
          // }
          .form-group {
             margin-bottom: 0;
          }
          .btn-email {
            background-color: #20815D;
            border-color: #20815D;
          }
          .btn-email:hover {
              background-color: #BF5730	;
              border-color: #BF5730	;
          }
          .btn-password {
            background-color: #20815D;
            border-color: #20815D;
          }
          .btn-password:hover {
              background-color: #BF5730;
              border-color: #BF5730;
          }
          .form-check-input {
            position: relative;
            // margin-top: .3rem;
            margin-left: 0rem;
            margin-right: 1rem;
          }
          .profile img {
            width: 200px;
            height: 200px;
            border-radius: 50%;
           }
      `}
    </style>
  </Layout>
);

Profile.getInitialProps = async ctx => {
  const { token } = ctx.store.getState().authentication;
  if (token) {
    const response = await axios.get(`${process.env.basePath}/api/v1/users/`, {
      headers: {
        authorization: `JWT ${token}`,
        'Content-Type': 'application/json'
      }
    });
    const user = response.data.results[0];
    return {
      user, token
    };
  }
};

export default connect(state => state, actions)(Profile);
