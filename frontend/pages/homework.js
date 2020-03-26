import React from 'react';
import axios from 'axios';
import { connect } from 'react-redux';
import actions from '../redux/actions';
import Layout from '../components/Layout';


class Homework extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      student_homework: '',
      lesson: props.lesson,
      student: props.user
    };
  }
  handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post(`${process.env.basePath}/api/v1/education/homework/`, this.state,{
      headers: {
        authorization: `JWT ${this.props.token}`,
        'Content-Type': 'application/json'
      }
    });
    if (response.status === 201) {
      alert('Задание успешно отправлено!');
    }
  };
  render() {
    return <Layout>
      {(this.props.user && (
        <div className='group py-4'>
          <div className='container'>
            <h2>Домашнее задание: {this.props.title}</h2>
            <hr/>
            <form className='form-horizontal form-profile' role='form' onSubmit={this.handleSubmit.bind(this)} >
              <div className='form-group row'>
                <label className='control-label'>Решение:</label>
                  <textarea className='form-control' rows='4' value={this.state.student_homework}
                         onChange={e => this.setState({ student_homework: e.target.value })} required />
              </div>
              <button className='btn btn-secondary btn-md float-right' type='submit'>Отправить</button>
            </form>
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
  }
}

Homework.getInitialProps = async (ctx) => {
  const { token } = ctx.store.getState().authentication;
  const lesson = ctx.query.lesson;
  const title = ctx.query.title;
  if (token) {
    const response = await axios.get(`${process.env.basePath}/api/v1/users/`, {
      headers: {
        authorization: `JWT ${token}`,
        'Content-Type': 'application/json'
      }
    });
    const user = response.data.results[0].id;
    return {
      user, lesson, title, token
    };
  }
};

export default connect(state => state, actions)(Homework);
