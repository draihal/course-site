import React from 'react';
import Link from 'next/link';
import { connect } from 'react-redux';
import actions from '../redux/actions';
import Layout from '../components/Layout';


class Signup extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      email:'',
      first_name:'',
      last_name:'',
      password:'',
      phone_number: '',
      is_partner: false,
      is_student: false,
      is_teacher: false
    };
  }

  handleSubmit(e) {
    e.preventDefault();
    this.props.register(
        { email: this.state.email,
          first_name: this.state.first_name,
          last_name: this.state.last_name,
          password:this.state.password,
          phone_number: this.state.phone_number,
          is_partner: this.state.is_partner,
          is_student: this.state.is_student,
          is_teacher: this.state.is_teacher,
        },
        'register'
    );
  }
  render() {
    return <Layout>
      <form className='form-registration' onSubmit={this.handleSubmit.bind(this)}>
        <h1 className='h3 mb-3 font-weight-normal text-center'>Регистрация</h1>
        {/*{error ? <p className='text-center'>{error}</p> : null}*/}
        <label htmlFor='inputName' className='sr-only'>Имя</label>
        <input type='text'
               id='inputName'
               name='first_name'
               className='form-control'
               placeholder='Имя'
               value={this.state.first_name}
               onChange={e => this.setState({ first_name: e.target.value })}
               required autoFocus />
        <label htmlFor='inputSurname' className='sr-only'>Фамилия</label>
        <input type='text'
               id='inputSurname'
               name='last_name'
               className='form-control'
               placeholder='Фамилия'
               value={this.state.last_name}
               onChange={e => this.setState({ last_name: e.target.value })}
        />
        <label htmlFor='inputEmail' className='sr-only'>Email</label>
        <input type='email'
               id='inputEmail'
               name='email'
               className='form-control'
               placeholder='Email'
               value={this.state.email}
               onChange={e => this.setState({ email: e.target.value })}
               required />
        <label htmlFor='inputPassword' className='sr-only'>Пароль</label>
        <input type='password'
               id='inputPassword'
               name='password'
               className='form-control'
               placeholder='Пароль'
               value={this.state.password}
               onChange={e => this.setState({ password: e.target.value })}
               required />
        <label htmlFor='inputPhone' className='sr-only'>Телефонный номер</label>
        <input type='tel'
               id='inputPhone'
               name='phone_number'
               className='form-control'
               placeholder='Телефонный номер'
               value={this.state.phone_number}
               onChange={e => this.setState({ phone_number: e.target.value })}
               required />
        <div className='btn-group btn-group-toggle' data-toggle='buttons'>
          <label className='btn btn-outline-secondary active'>
            <input type='radio'
                   name='is_student'
                   id='option1'
                   autoComplete='off'
                   defaultChecked={this.state.is_student}
                   onClick={e => this.setState({
                     is_student: true,
                     is_teacher: false,
                     is_partner: false })}
            /> Студент
          </label>
          <label className='btn btn-outline-secondary'>
            <input type='radio'
                   name='is_teacher'
                   id='option2'
                   autoComplete='off'
                   defaultChecked={this.state.is_teacher}
                   onClick={e => this.setState({
                     is_teacher: true,
                     is_student: false,
                     is_partner: false })}
            /> Преподаватель
          </label>
          <label className='btn btn-outline-secondary'>
            <input type='radio'
                   name='is_partner'
                   id='option3'
                   autoComplete='off'
                   defaultChecked={this.state.is_partner}
                   onClick={e => this.setState({
                     is_partner: true,
                     is_student: false,
                     is_teacher: false })}
            /> Партнер
          </label>
        </div>
        <button className='btn btn-lg btn-secondary btn-block' type='submit'>Зарегистрироваться</button>
        <p className='mt-5 mb-3 text-muted text-center'>Уже зарегистрированы?</p>
        <Link href='/signin'><button className='btn btn-lg btn-secondary btn-block' type='login'>Войти</button></Link>
      </form>
      <style global jsx>{`
        .main{
          padding-top: 9rem;
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
        .form-registration {
          width: 100%;
          max-width: 350px;
          padding: 15px;
          margin: auto;
        }
        .form-registration .checkbox {
          font-weight: 400;
        }
        .form-registration .form-control {
          position: relative;
          box-sizing: border-box;
          height: auto;
          padding: 10px;
          font-size: 16px;
        }
        .form-registration .form-control:focus {
          z-index: 2;
        }
        .form-registration input{
          border-radius: 0;
        }
        .form-registration input[type='name'] {
          margin-bottom: -1px;
        }
        .form-registration input[type='phone'] {
          margin-bottom: 10px;
        }
        .form-registration button[type='submit'] {
          margin-top: 10px;
        }
        .form-registration .btn-group {
          margin-top: 10px;
        }
        .form-registration .btn-outline-secondary {
          border-radius: 0;
        }
        .form-registration .btn-secondary {
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
)(Signup);


