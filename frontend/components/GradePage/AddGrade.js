import React from 'react';
import axios from 'axios';


class AddGrade extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      status: '',
      grade: '',
      lesson: props.homework.lesson,
      homework: props.homework.id,
      student: props.homework.student,
      teacher: props.teacherId
    };
  }
  handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post(`${process.env.basePath}/api/v1/education/grades/`, this.state,{
      headers: {
        authorization: `JWT ${this.props.token}`,
        'Content-Type': 'application/json'
      }
    });
    if (response.status === 201) {
      alert('Оценка сохранена!');
    }
  };
  render() {
    return <div className='group py-4'>
      <div className='container'>
        <h2>Домашнее задание от {this.props.homework.student_first_name} {this.props.homework.student_last_name}</h2>
        <hr/>
        <form className='form-horizontal form-profile' role='form' onSubmit={this.handleSubmit.bind(this)} >
          <div className='form-group row'>
            <label className='col-lg-2 control-label'>Ответ студента</label>
            <div className='col-lg-10'>
              <input type='text' className='form-control-plaintext' readOnly value={this.props.homework.student_homework} />
            </div>
          </div>
          <div className='form-group row'>
            <label htmlFor='grade_status' className='col-lg-2 control-label'>Статус проверки</label>
            <div className='col-lg-10'>
              <div className='ui-select'>
                <select id='grade_status' className='form-control' value={this.state.status}
                        onChange={e => this.setState({ status: e.target.value })} >
                  <option value='undone'>Не сдано</option>
                  <option value='check'>На проверке</option>
                  <option value='rework'>На доработке</option>
                  <option value='done'>Сдано</option>
                </select>
              </div>
            </div>
          </div>
          <div className='form-group row'>
            <label htmlFor='grade_textarea' className='col-lg-2 control-label'>Оценка</label>
            <textarea className='col-lg-10 form-control' rows='4' value={this.state.grade}
                      onChange={e => this.setState({ grade: e.target.value })}
                      id='grade_textarea' required />
          </div>
          <button className='btn btn-secondary btn-md float-right' type='submit'>Сохранить</button>
        </form>
      </div>
    </div>
  }
}

export default (AddGrade);
