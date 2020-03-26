// import axios, { AxiosRequestConfig } from 'axios';
import Cookies from 'js-cookie';
import Router from 'next/router';
// import { LoginInputs } from '../pages/signin';
import { catchAxiosError } from './error';
import { post } from './rest_service';

export const COOKIES = {
  authToken: 'courseSite.token'
};

export async function login(inputs) {
  const data = new URLSearchParams(inputs);
  const res = await post('/api/v1/jwt/create/', data).catch(catchAxiosError);
  if (res.error) {
    return res.error;
  } else if (!res.data || !res.data.access) {
    return 'Wrong password or username!';
  }
  const token = res.data.access;
  const refreshToken = res.data.refresh;

  // store the token into cookies
  Cookies.set(COOKIES.authToken, token, {
    expires: 1,
    // https://github.com/js-cookie/js-cookie/wiki/Frequently-Asked-Questions#im-using-httponly-true-wheres-my-cookie
    // httpOnly: true,
    // secure: true,
    // sameSite: true,
  });
  await Router.push('/profile');
}

