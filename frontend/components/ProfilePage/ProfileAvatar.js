import Link from 'next/link';
import React from 'react';
import axios from 'axios';


class ProfileAvatar extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      avatar: props.avatar
    };
  }
  handleSubmit = async (e) => {
    e.preventDefault();
    let form_data = new FormData();
    form_data.append('avatar', this.state.avatar);
    const response = await axios.patch(`${this.props.url}`, form_data,{
      headers: {
        authorization: `JWT ${this.props.token}`,
        'Content-Type': 'multipart/form-data'
      }
    });
    if (response.status === 200) {
      alert('Фотография успешно обновлена!');
    }
  };
  render() {
    return <div className='text-center'>
      {this.props.avatar ? <img src={this.props.avatar} alt='avatar' /> : <img src='static/default_user.jpg' alt='avatar' />}
      <hr />
      <form onSubmit={this.handleSubmit.bind(this)} >
        <input type='file'
               id='image'
               accept='image/png, image/jpeg'
               className='form-control'
               onChange={e => this.setState({ avatar: e.target.files[0] })}
               required/>
        <button className='btn btn-secondary btn-md' type='submit'>Изменить</button>
      </form>
    </div>
  }
}

export default ProfileAvatar;
