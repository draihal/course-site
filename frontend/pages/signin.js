import React from 'react';
import Link from 'next/link';
import { connect } from 'react-redux';
import actions from '../redux/actions';
import Layout from '../components/Layout';

class Signin extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      email: '',
      password: ''
    };
  }
  handleSubmit(e) {
    e.preventDefault();
    this.props.authenticate(
        { email: this.state.email, password: this.state.password },
        'login'
    );
  }
  render() {
    return <Layout>
      <form className='form-signin' onSubmit={this.handleSubmit.bind(this)}>
        <h1 className='h3 mb-3 font-weight-normal text-center'>Вход</h1>
        {/*{error ? <p className='text-center'>{error}</p> : null}*/}
        <label htmlFor='inputEmail' className='sr-only'>Email</label>
        <input type='email'
               id='inputEmail'
               name='email'
               className='form-control'
               placeholder='Email'
               value={this.state.email}
               onChange={e => this.setState({ email: e.target.value })}
               required autoFocus />
        <label htmlFor='inputPassword' className='sr-only'>Пароль</label>
        <input type='password'
               id='inputPassword'
               name='password'
               className='form-control'
               placeholder='Пароль'
               value={this.state.password}
               onChange={e => this.setState({ password: e.target.value })}
               required />
        <button className='btn btn-lg btn-secondary btn-block' type='submit'>Войти</button>
        <p className='mt-5 mb-3 text-muted text-center'>Еще не зарегистрированы?</p>
        <Link href='/signup'><button className='btn btn-lg btn-secondary btn-block' type='registration'>Регистрация</button></Link>
      </form>
      <style global jsx>{`
      .main{
        padding-top: 12rem;
      }
      html {
        min-height: 100%;
        position: relative;
      }
      body {
        /* Margin bottom by footer height */
        margin-bottom: 60px;
      }
      #footer {
        position: absolute;
        bottom: 0;
        width: 100%;
        /* Set the fixed height of the footer here */
        height: 80px;
        background-color: #f5f5f5;
      }
      .form-signin {
        width: 100%;
        max-width: 350px;
        padding: 15px;
        margin: auto;
      }
      .form-signin .checkbox {
        font-weight: 400;
      }
      .form-signin .form-control {
        position: relative;
        box-sizing: border-box;
        height: auto;
        padding: 10px;
        font-size: 16px;
      }
      .form-signin .form-control:focus {
        z-index: 2;
      }
      .form-signin input{
        border-radius: 0;
      }
      .form-signin input[type='email'] {
        margin-bottom: -1px;
      }
      .form-signin input[type='password'] {
        margin-bottom: 10px;
      }
      .form-signin .btn-secondary {
        padding: .6rem 1.2rem;
        margin: 0;
      }
    `}</style>
    </Layout>;
  }
}

export default connect(
    state => state,
    actions
)(Signin);
