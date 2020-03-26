import Router from 'next/router';
import axios from 'axios';
import { AUTHENTICATE, DEAUTHENTICATE, USER } from '../types';
import { setCookie, removeCookie } from '../../services/cookie';


// TODO: add rest_service with catch error
// TODO: add refresh token


// register user
const register = ({ email, first_name, last_name, password, phone_number, is_partner, is_student, is_teacher }, type) => {
  if (type !== 'register') {
    throw new Error('Wrong API call!');
  }
  return (dispatch) => {
    axios.post(`${process.env.basePath}/api/v1/users/`, {email, first_name, last_name, password, phone_number, is_partner, is_student, is_teacher })
        .then((response) => {
          Router.push('/signin');
        })
        .catch((error) => {
          switch (error.response.status) {
            case 422:
              alert(error.response.data[Object.keys(error.response.data)[0]]);
              break;
            case 401:
              alert(error.response.data[Object.keys(error.response.data)[0]]);
              break;
            case 500:
              alert('Interval server error! Try again!');
              break;
            default:
              alert(error.response.data[Object.keys(error.response.data)[0]]);
              break;
          }
        });
  };
};

// gets token from the api and stores it in the redux store and in cookie
const authenticate = ({ email, password }, type) => {
  if (type !== 'login') {
    throw new Error('Wrong API call!');
  }
  return (dispatch) => {
    axios.post(`${process.env.basePath}/api/v1/jwt/create/`, { email, password })
        .then((response) => {
          setCookie('token', response.data.access);
          Router.push('/profile');
          dispatch({type: AUTHENTICATE, payload: response.data.access});
        })
        .catch((error) => {
          if (error.response) {
            switch (error.response.status) {
              case 422:
                alert(error.response.data[Object.keys(error.response.data)[0]]);
                break;
              case 401:
                alert(error.response.data[Object.keys(error.response.data)[0]]);
                break;
              case 500:
                alert('Interval server error! Try again!');
                break;
              default:
                alert(error.response.data[Object.keys(error.response.data)[0]]);
                break;
            }
          }
        });
  };
};

// gets the token from the cookie and saves it in the store
const reauthenticate = (token) => {
  return (dispatch) => {
    dispatch({type: AUTHENTICATE, payload: token});
  };
};

// removing the token
const deauthenticate = () => {
  return (dispatch) => {
    removeCookie('token');
    Router.push('/signin');
    dispatch({type: DEAUTHENTICATE});
  };
};

const getUser = ({ token }, type) => {
  console.log(token);
  return (dispatch) => {
    axios.get(`${process.env.basePath}/api/v1/users/me/`,{headers: {
        'Authorization' : 'JWT ' + token
      }
    })
        .then((response) => {
          dispatch({ type: USER, payload: response.data.first_name });
        })
        .catch((error) => {
          switch (error.response.status) {
            case 401:
              Router.push('/signin');
              break;
            case 422:
              alert(error.response.data[Object.keys(error.response.data)[0]]);
              break;
            case 500:
              alert('Interval server error! Try again!');
              break;
            case 503:
              alert(error.response.data[Object.keys(error.response.data)[0]]);
              Router.push('/');
              break;
            default:
              alert(error.response.data[Object.keys(error.response.data)[0]]);
              break;
          }
        });
  };
};


export default {
  register,
  authenticate,
  reauthenticate,
  deauthenticate,
  getUser,
};

