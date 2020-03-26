import React from 'react';
import StudentProfile from './StudentProfile';
import PartnerProfile from './PartnerProfile';
import TeacherProfile from './TeacherProfile';
import ProfileAvatar from './ProfileAvatar';
import axios from 'axios';


class MainProfileSection extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      email: props.user.email,
      first_name: props.user.first_name,
      last_name: props.user.last_name,
      phone_number: props.user.phone_number
    };
  }

  handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.patch(`${process.env.basePath}/api/v1/users/me/`, this.state,{
      headers: {
        authorization: `JWT ${this.props.token}`,
        'Content-Type': 'application/json'
      }
    });
    if (response.status === 200) {
      alert('Данные успешно обновлены!');
    }
  };
  render() {
    return <div className='profile py-4'>
      <div className='container'>
        <h2>Мой профиль</h2>
        <hr/>
        <div className='row'>
          <div className='col-md-3'>
            {this.props.user.student_profile ? <ProfileAvatar
              avatar={this.props.user.student_profile.avatar}
              token={this.props.token}
              url={this.props.user.student_profile.url} /> : ''}
            {this.props.user.teacher_profile ? <ProfileAvatar avatar={this.props.user.teacher_profile.avatar}/> : ''}
            {this.props.user.partner_profile ? <ProfileAvatar avatar={this.props.user.partner_profile.logo}/> : ''}
          </div>
          <div className='col-md-9 personal-info'>
            <h3 id='main-title'>Основновная информация</h3>
            <form className='form-horizontal form-profile' role='form' onSubmit={this.handleSubmit.bind(this)} >
              <div className='form-group row'>
                <label className='col-lg-2 control-label'>Имя *</label>
                <div className='col-lg-10'>
                  <input className='form-control' type='text' value={this.state.first_name}
                         onChange={e => this.setState({ first_name: e.target.value })}
                         name='first_name' required />
                </div>
              </div>
              <div className='form-group row'>
                <label className='col-lg-2 control-label'>Фамилия</label>
                <div className='col-lg-10'>
                  <input className='form-control' type='text' value={this.state.last_name}
                         onChange={e => this.setState({ last_name: e.target.value })}
                         name='last_name' />
                </div>
              </div>
              <div className='form-group row'>
                <label htmlFor='staticEmail' className='col-lg-2 control-label'>Email *</label>
                <div className='col-lg-10'>
                  <input type='text' readOnly className='form-control-plaintext' id='staticEmail'
                         value={this.state.email}
                         name='email' required />
                </div>
              </div>
              <div className='form-group row'>
                <label className='col-md-2 control-label'>Телефонный номер *</label>
                <div className='col-md-10'>
                  <input className='form-control' type='text' placeholder='+79250000000'
                         value={this.state.phone_number}
                         onChange={e => this.setState({ phone_number: e.target.value })}
                         name='phone_number' required />
                </div>
              </div>
              <button className='btn btn-secondary btn-md' type='submit'>Сохранить изменения</button>
              <button className='btn btn-secondary btn-md btn-email' type='changeEmail'>Изменить email</button>
              <button className='btn btn-secondary btn-md btn-password' type='changePassword'>Изменить пароль</button>
            </form>
            <hr />
            <h3>Дополнительная информация</h3>
            {this.props.user.student_profile ? <StudentProfile student={this.props.user.student_profile} token={this.props.token}/> : ''}
            {this.props.user.teacher_profile ? <TeacherProfile teacher={this.props.user.teacher_profile} token={this.props.token}/> : ''}
            {this.props.user.partner_profile ? <PartnerProfile partner={this.props.user.partner_profile} token={this.props.token}/> : ''}
          </div>
        </div>
      </div>
    </div>
  }
}

export default MainProfileSection;
