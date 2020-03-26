import Router from 'next/router';
import actions from '../redux/actions';
import { getCookie } from '../services/cookie';
import { AuthToken } from '../services/auth_token';


// checks if the page is being loaded on the server, and if so, get auth token from the cookie:
export default function(ctx) {

  if(ctx.isServer) {
    if(ctx.req.headers.cookie) {
      const token = getCookie('token', ctx.req);
      if (token){
        ctx.store.dispatch(actions.reauthenticate(token));
      }
    }
  } else {
    const token = ctx.store.getState().authentication.token;
    // checks if the token is being expired, and if so, deauthenticate user:
    const auth = new AuthToken(token);
    if (token && auth.isExpired) {
      ctx.store.dispatch(actions.deauthenticate());
    }
    if(token && (ctx.pathname === '/signin' || ctx.pathname === '/signup')) {
      setTimeout(function() {
        Router.push('/');
      }, 0);
    }
  }

}
