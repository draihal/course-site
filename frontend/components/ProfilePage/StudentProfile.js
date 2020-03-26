import Link from 'next/link';
import React from 'react';
import axios from 'axios';


class StudentProfile extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      first_name_lat: props.student.first_name_lat,
      last_name_lat: props.student.last_name_lat,
      username: props.student.username,
      birth_date: props.student.birth_date,
      sex: props.student.sex,
      country: props.student.country,
      city: props.student.city,
      can_relocate: props.student.can_relocate,
      can_full_time: props.student.can_full_time,
      can_part_time: props.student.can_part_time,
      can_remote: props.student.can_remote,
      company: props.student.company,
      position: props.student.position
    };
  }
  handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.patch(`${process.env.basePath}/api/v1/profile/student/${this.props.student.id}/`, this.state,{
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
    return <form className='form-horizontal form-profile' role='form' onSubmit={this.handleSubmit.bind(this)} >
      <div className='form-group row'>
        <label className='col-lg-2 control-label'>Имя (Латиницей)</label>
        <div className='col-lg-10'>
          <input className='form-control' type='text' value={this.state.first_name_lat}
                 onChange={e => this.setState({ first_name_lat: e.target.value })} />
        </div>
      </div>
      <div className='form-group row'>
        <label className='col-lg-2 control-label'>Фамилия (Латиницей)</label>
        <div className='col-lg-10'>
          <input className='form-control' type='text' value={this.state.last_name_lat}
                 onChange={e => this.setState({ last_name_lat: e.target.value })} />
        </div>
      </div>
      <div className='form-group row'>
        <label className='col-lg-2 control-label'>Юзернейм</label>
        <div className='col-lg-10'>
          <input className='form-control' type='text' value={this.state.username}
                 onChange={e => this.setState({ username: e.target.value })} />
        </div>
      </div>
      <div className='form-group row'>
        <label className='col-lg-2 control-label'>Дата рождения</label>
        <div className='col-lg-10'>
          <input className='form-control' type='text' placeholder='1999-01-25' value={this.state.birth_date}
                 onChange={e => this.setState({ birth_date: e.target.value })} />
        </div>
      </div>
      <div className='form-group row'>
        <label className='col-lg-2 control-label'>Пол *</label>
        <div className='col-lg-10'>
          <div className='ui-select'>
            <select id='user_country' className='form-control' value={this.state.sex}
                    onChange={e => this.setState({ sex: e.target.value })} >
              <option value='0'>Не указано</option>
              <option value='m'>Мужской</option>
              <option value='f'>Женский</option>
            </select>
          </div>
        </div>
      </div>
      <div className='form-group row'>
        <label className='col-lg-2 control-label'>Страна *</label>
        <div className='col-lg-10'>
          <div className='ui-select'>
            <select id='user_country' className='form-control' value={this.state.country}
                    onChange={e => this.setState({ country: e.target.value })} >
              <option value='NA'>Не указано</option>
              <option value='RU'>Россия</option>
              <option value='BY'>Беларусь</option>
              <option value='UA'>Украина</option>
              <option value='KZ'>Казахстан</option>
            </select>
          </div>
        </div>
      </div>
      <div className='form-group row'>
        <label className='col-md-2 control-label'>Город *</label>
        <div className='col-md-10'>
          <input className='form-control' type='text' required value={this.state.city}
                 onChange={e => this.setState({ city: e.target.value })} />
        </div>
      </div>
      <div className='form-group row'>
        <label className='col-md-2 control-label'>Компания</label>
        <div className='col-md-10'>
          <input className='form-control' type='text' value={this.state.company}
                 onChange={e => this.setState({ company: e.target.value })} />
        </div>
      </div>
      <div className='form-group row'>
        <label className='col-md-2 control-label'>Позиция</label>
        <div className='col-md-10'>
          <input className='form-control' type='text' value={this.state.position}
                 onChange={e => this.setState({ position: e.target.value })} />
        </div>
      </div>
      <div className='form-group row'>
        <div className='col-md-2'>Формат работы</div>
        <div className='ccol-md-10'>
          <div className='form-check'>
            <input className='form-check-input' type='checkbox' id='gridCheck1' defaultChecked={this.state.can_full_time}
                   onChange={() => this.setState({ can_full_time: !this.state.can_full_time })} />
            <label className='form-check-label' htmlFor='gridCheck1' >
              Полный рабочий день
            </label>
          </div>
          <div className='form-check'>
            <input className='form-check-input' type='checkbox' id='gridCheck1' defaultChecked={this.state.can_part_time}
                   onChange={() => this.setState({ can_part_time: !this.state.can_part_time })} />
            <label className='form-check-label' htmlFor='gridCheck1' >
              Неполный рабочий день
            </label>
          </div>
          <div className='form-check'>
            <input className='form-check-input' type='checkbox' id='gridCheck1' defaultChecked={this.state.can_remote}
                   onChange={() => this.setState({ can_remote: !this.state.can_remote })} />
            <label className='form-check-label' htmlFor='gridCheck1' >
              Удаленно
            </label>
          </div>
          <div className='form-check'>
            <input className='form-check-input' type='checkbox' id='gridCheck1' defaultChecked={this.state.can_relocate}
                   onChange={() => this.setState({ can_relocate: !this.state.can_relocate })} />
            <label className='form-check-label' htmlFor='gridCheck1' >
              Готов к переезду
            </label>
          </div>
        </div>
      </div>
      <button className='btn btn-secondary btn-md' type='submit'>Сохранить изменения</button>
    </form>
  }
}

export default StudentProfile;
